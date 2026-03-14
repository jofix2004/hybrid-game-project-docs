from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.parse import quote, unquote


DOC_ROOT = Path(__file__).resolve().parent
OUTPUT_FILE = DOC_ROOT / "snapshot_reader.html"

ROOT_FILE_ORDER = {
    "README.md": 0,
    "MUC_LUC.md": 1,
    "GDD_EXECUTION_PLAN.md": 2,
    "GDD_DOC_BACKLOG.md": 3,
}

DIR_ORDER = {
    "00_GAME_VISION": 0,
    "01_GAMEPLAY_LOOP": 1,
    "02_CORE_SYSTEMS": 2,
    "03_PLAYER_SYSTEMS": 3,
    "04_WORLD_SYSTEMS": 4,
    "05_DUNGEON_SYSTEM": 5,
    "06_ECONOMY_SYSTEM": 6,
    "07_PROGRESSION_SYSTEM": 7,
    "08_CONTENT_DATABASE": 8,
    "09_MULTIPLAYER": 9,
    "10_TECHNICAL_DESIGN": 10,
    "11_BALANCE_DATA": 11,
    "12_QUESTION_FRAMEWORK": 12,
}


def natural_part(value: str):
    return [int(piece) if piece.isdigit() else piece.lower() for piece in re.split(r"(\d+)", value)]


def sort_key(path: Path):
    rel = path.relative_to(DOC_ROOT)
    parts = rel.parts
    if len(parts) == 1:
        return (0, ROOT_FILE_ORDER.get(parts[0], 100), natural_part(parts[0]))
    head = parts[0]
    tail = [natural_part(piece) for piece in parts[1:]]
    return (1, DIR_ORDER.get(head, 100), natural_part(head), tail)


def collect_markdown_files() -> list[Path]:
    files = []
    for path in DOC_ROOT.rglob("*.md"):
        if path.name.startswith("."):
            continue
        files.append(path)
    files.sort(key=sort_key)
    return files


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-") or "section"


def make_internal_href(target: str, current_rel: str, heading_map: dict[str, str]) -> str | None:
    target = target.strip()
    if not target:
        return None

    if target.startswith("#"):
        anchor = target[1:]
        if anchor in heading_map:
            return f"#{quote(current_rel)}::{quote(heading_map[anchor])}"
        return None

    normalized = target.replace("\\", "/")
    normalized = unquote(html.unescape(normalized))

    lower = normalized.lower()
    if lower.startswith("http://") or lower.startswith("https://"):
        return None

    doc_root_prefix = "/d:/trinhlagiv2/document/game_project_docs/"
    if lower.startswith(doc_root_prefix):
        normalized = normalized[len(doc_root_prefix):]
    elif lower.startswith("d:/trinhlagiv2/document/game_project_docs/"):
        normalized = normalized[len("d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/"):]
    elif lower.startswith("./") or lower.startswith("../"):
        current_abs = (DOC_ROOT / current_rel).resolve()
        target_abs = (current_abs.parent / normalized).resolve()
        try:
            normalized = str(target_abs.relative_to(DOC_ROOT.resolve())).replace("\\", "/")
        except ValueError:
            return None

    if normalized.endswith(".md"):
        return f"#{quote(normalized)}"

    return None


def convert_inline(text: str, current_rel: str, heading_map: dict[str, str]) -> str:
    placeholders: list[str] = []

    def stash(fragment: str) -> str:
        placeholders.append(fragment)
        return f"@@PLACEHOLDER_{len(placeholders) - 1}@@"

    escaped = html.escape(text, quote=False)

    escaped = re.sub(
        r"`([^`]+)`",
        lambda match: stash(f"<code>{html.escape(html.unescape(match.group(1)), quote=False)}</code>"),
        escaped,
    )

    def replace_link(match: re.Match[str]) -> str:
        label = convert_inline(html.unescape(match.group(1)), current_rel, heading_map)
        href_raw = html.unescape(match.group(2)).strip()
        internal_href = make_internal_href(href_raw, current_rel, heading_map)
        if internal_href is not None:
            return stash(f'<a href="{html.escape(internal_href, quote=True)}">{label}</a>')
        if href_raw.startswith("http://") or href_raw.startswith("https://"):
            safe_href = html.escape(href_raw, quote=True)
            return stash(f'<a href="{safe_href}" target="_blank" rel="noreferrer noopener">{label}</a>')
        return stash(label)

    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_link, escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", escaped)

    for index, fragment in enumerate(placeholders):
        escaped = escaped.replace(f"@@PLACEHOLDER_{index}@@", fragment)

    return escaped


def build_heading_map(lines: list[str]) -> dict[str, str]:
    heading_map: dict[str, str] = {}
    seen: dict[str, int] = {}
    for raw in lines:
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", raw)
        if not match:
            continue
        heading_text = match.group(2).strip()
        slug = slugify(heading_text)
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        if count:
            slug = f"{slug}-{count + 1}"
        heading_map[heading_text] = slug
    return heading_map


def markdown_to_html(text: str, current_rel: str) -> tuple[str, list[dict[str, str]]]:
    lines = text.splitlines()
    heading_map = build_heading_map(lines)
    toc: list[dict[str, str]] = []
    output: list[str] = []
    paragraph: list[str] = []
    list_stack: list[str] = []
    in_code = False
    code_lang = ""
    code_lines: list[str] = []

    def flush_paragraph():
        nonlocal paragraph
        if not paragraph:
            return
        joined = " ".join(part.strip() for part in paragraph if part.strip())
        output.append(f"<p>{convert_inline(joined, current_rel, heading_map)}</p>")
        paragraph = []

    def close_lists(target_indent: int = -1):
        while list_stack and int(list_stack[-1].split(":", 1)[1]) >= target_indent:
            tag, _indent = list_stack.pop().split(":", 1)
            output.append(f"</{tag}>")

    def flush_code():
        nonlocal in_code, code_lang, code_lines
        if not in_code:
            return
        code_class = f' class="language-{html.escape(code_lang, quote=True)}"' if code_lang else ""
        code_text = html.escape("\n".join(code_lines))
        output.append(f"<pre><code{code_class}>{code_text}</code></pre>")
        in_code = False
        code_lang = ""
        code_lines = []

    for raw_line in lines:
        line = raw_line.rstrip("\n")

        code_match = re.match(r"^```(\w+)?\s*$", line)
        if code_match:
            flush_paragraph()
            close_lists()
            if in_code:
                flush_code()
            else:
                in_code = True
                code_lang = code_match.group(1) or ""
                code_lines = []
            continue

        if in_code:
            code_lines.append(raw_line)
            continue

        heading_match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading_match:
            flush_paragraph()
            close_lists()
            level = len(heading_match.group(1))
            heading_text = heading_match.group(2).strip()
            anchor = heading_map.get(heading_text, slugify(heading_text))
            output.append(
                f'<h{level} id="{html.escape(anchor, quote=True)}">{convert_inline(heading_text, current_rel, heading_map)}</h{level}>'
            )
            if level in (2, 3):
                toc.append({"level": str(level), "title": heading_text, "anchor": anchor})
            continue

        if not line.strip():
            flush_paragraph()
            close_lists()
            continue

        list_match = re.match(r"^(\s*)([-*]|\d+\.)\s+(.+)$", line)
        if list_match:
            flush_paragraph()
            indent = len(list_match.group(1))
            marker = list_match.group(2)
            content = list_match.group(3)
            list_tag = "ol" if marker.endswith(".") and marker[:-1].isdigit() else "ul"

            while list_stack and int(list_stack[-1].split(":", 1)[1]) > indent:
                tag, _indent = list_stack.pop().split(":", 1)
                output.append(f"</{tag}>")

            if not list_stack or int(list_stack[-1].split(":", 1)[1]) < indent or list_stack[-1].split(":", 1)[0] != list_tag:
                output.append(f"<{list_tag}>")
                list_stack.append(f"{list_tag}:{indent}")

            output.append(f"<li>{convert_inline(content.strip(), current_rel, heading_map)}</li>")
            continue

        paragraph.append(line)

    flush_paragraph()
    close_lists()
    flush_code()
    return "\n".join(output), toc


def build_docs_payload(paths: list[Path]) -> list[dict[str, object]]:
    payload = []
    for path in paths:
        rel = path.relative_to(DOC_ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        rendered, toc = markdown_to_html(text, rel)
        title_match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
        title = title_match.group(1).strip() if title_match else path.stem
        payload.append(
            {
                "id": rel,
                "title": title,
                "path": rel,
                "section": path.parent.name if path.parent != DOC_ROOT else "ROOT",
                "html": rendered,
                "toc": toc,
            }
        )
    return payload


def build_html(docs_payload: list[dict[str, object]]) -> str:
    docs_json = json.dumps(docs_payload, ensure_ascii=False)
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>GAME_PROJECT_DOCS</title>
  <style>
    :root {{
      --bg: #f6f0e8;
      --panel: #fffaf4;
      --panel-2: #efe4d4;
      --line: #d2c2ad;
      --text: #2b241d;
      --muted: #6f6255;
      --accent: #87643e;
      --accent-strong: #6f4f2e;
      --shadow: 0 18px 40px rgba(62, 44, 25, 0.12);
      --sidebar-w: 340px;
      --font-body: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
      --font-title: Georgia, "Times New Roman", serif;
    }}

    * {{
      box-sizing: border-box;
    }}

    html, body {{
      margin: 0;
      min-height: 100%;
      background:
        radial-gradient(circle at top left, rgba(255,255,255,0.65), transparent 40%),
        linear-gradient(180deg, #f8f3ec 0%, var(--bg) 100%);
      color: var(--text);
      font-family: var(--font-body);
    }}

    body {{
      display: grid;
      grid-template-columns: var(--sidebar-w) 1fr;
    }}

    .sidebar {{
      position: sticky;
      top: 0;
      height: 100vh;
      overflow: auto;
      padding: 24px 20px 32px;
      background: rgba(255, 250, 244, 0.92);
      border-right: 1px solid var(--line);
      box-shadow: inset -1px 0 0 rgba(255,255,255,0.5);
      backdrop-filter: blur(10px);
    }}

    .brand {{
      margin-bottom: 20px;
      padding-bottom: 18px;
      border-bottom: 1px solid var(--line);
    }}

    .brand h1 {{
      margin: 0 0 6px;
      font-family: var(--font-title);
      font-size: 1.7rem;
      line-height: 1.1;
    }}

    .brand p {{
      margin: 0;
      color: var(--muted);
      font-size: 0.95rem;
      line-height: 1.5;
    }}

    .search {{
      width: 100%;
      padding: 11px 14px;
      border: 1px solid var(--line);
      border-radius: 12px;
      background: #fff;
      color: var(--text);
      font: inherit;
      box-shadow: inset 0 1px 2px rgba(0,0,0,0.04);
    }}

    .nav {{
      margin-top: 18px;
      display: grid;
      gap: 14px;
    }}

    .nav-group {{
      border: 1px solid rgba(135, 100, 62, 0.15);
      border-radius: 14px;
      background: rgba(255,255,255,0.55);
      overflow: hidden;
    }}

    .nav-group h2 {{
      margin: 0;
      padding: 12px 14px 10px;
      background: rgba(239, 228, 212, 0.7);
      border-bottom: 1px solid rgba(135, 100, 62, 0.1);
      font-size: 0.78rem;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--accent-strong);
    }}

    .nav-group ul {{
      list-style: none;
      margin: 0;
      padding: 8px;
    }}

    .nav-group li + li {{
      margin-top: 4px;
    }}

    .nav-group a {{
      display: block;
      padding: 10px 12px;
      border-radius: 10px;
      color: var(--text);
      text-decoration: none;
      line-height: 1.35;
      transition: background 0.16s ease, color 0.16s ease, transform 0.16s ease;
    }}

    .nav-group a:hover {{
      background: rgba(135, 100, 62, 0.09);
      transform: translateX(2px);
    }}

    .nav-group a.is-active {{
      background: var(--accent);
      color: #fffaf4;
      box-shadow: 0 10px 20px rgba(111, 79, 46, 0.22);
    }}

    .content {{
      min-width: 0;
      padding: 28px 32px 80px;
    }}

    .hero {{
      margin-bottom: 22px;
      padding: 22px 24px;
      border: 1px solid rgba(135, 100, 62, 0.16);
      border-radius: 22px;
      background:
        linear-gradient(135deg, rgba(255,255,255,0.78), rgba(255,250,244,0.9)),
        linear-gradient(135deg, rgba(135, 100, 62, 0.08), transparent 40%);
      box-shadow: var(--shadow);
    }}

    .hero small {{
      display: inline-block;
      margin-bottom: 8px;
      color: var(--accent-strong);
      letter-spacing: 0.08em;
      text-transform: uppercase;
      font-weight: 600;
    }}

    .hero h2 {{
      margin: 0 0 10px;
      font-family: var(--font-title);
      font-size: clamp(1.8rem, 2vw, 2.5rem);
    }}

    .hero p {{
      margin: 0;
      color: var(--muted);
      max-width: 70ch;
      line-height: 1.65;
    }}

    .doc-shell {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) 260px;
      gap: 24px;
      align-items: start;
    }}

    .doc-card {{
      min-width: 0;
      padding: 32px;
      border-radius: 24px;
      border: 1px solid rgba(135, 100, 62, 0.14);
      background: var(--panel);
      box-shadow: var(--shadow);
    }}

    .doc-meta {{
      margin-bottom: 24px;
      padding-bottom: 18px;
      border-bottom: 1px solid var(--line);
    }}

    .doc-meta .path {{
      margin: 0 0 10px;
      color: var(--muted);
      font-size: 0.92rem;
      word-break: break-all;
    }}

    .doc-meta h1 {{
      margin: 0;
      font-family: var(--font-title);
      font-size: clamp(2rem, 2.2vw, 2.9rem);
      line-height: 1.08;
    }}

    .doc-body {{
      font-size: 1rem;
      line-height: 1.75;
    }}

    .doc-body h1,
    .doc-body h2,
    .doc-body h3,
    .doc-body h4,
    .doc-body h5,
    .doc-body h6 {{
      margin-top: 1.75em;
      margin-bottom: 0.45em;
      font-family: var(--font-title);
      line-height: 1.2;
      scroll-margin-top: 24px;
    }}

    .doc-body h1 {{ font-size: 2rem; }}
    .doc-body h2 {{ font-size: 1.5rem; }}
    .doc-body h3 {{ font-size: 1.22rem; }}

    .doc-body p,
    .doc-body li {{
      color: var(--text);
    }}

    .doc-body ul,
    .doc-body ol {{
      padding-left: 1.5em;
    }}

    .doc-body li + li {{
      margin-top: 0.25em;
    }}

    .doc-body a {{
      color: var(--accent-strong);
      text-decoration-thickness: 1px;
      text-underline-offset: 0.18em;
    }}

    .doc-body code {{
      padding: 0.16em 0.4em;
      border-radius: 0.45em;
      background: var(--panel-2);
      font-family: Consolas, "Courier New", monospace;
      font-size: 0.94em;
    }}

    .doc-body pre {{
      overflow: auto;
      padding: 16px 18px;
      border-radius: 16px;
      background: #2c241d;
      color: #f9f3ea;
      box-shadow: inset 0 0 0 1px rgba(255,255,255,0.06);
    }}

    .doc-body pre code {{
      padding: 0;
      background: transparent;
      color: inherit;
    }}

    .toc {{
      position: sticky;
      top: 28px;
      padding: 20px 18px;
      border-radius: 20px;
      border: 1px solid rgba(135, 100, 62, 0.14);
      background: rgba(255, 250, 244, 0.96);
      box-shadow: var(--shadow);
    }}

    .toc h3 {{
      margin: 0 0 12px;
      font-size: 0.84rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--accent-strong);
    }}

    .toc ul {{
      list-style: none;
      margin: 0;
      padding: 0;
    }}

    .toc li + li {{
      margin-top: 8px;
    }}

    .toc a {{
      color: var(--muted);
      text-decoration: none;
      line-height: 1.35;
      display: block;
    }}

    .toc a[data-level="3"] {{
      padding-left: 12px;
      font-size: 0.94rem;
    }}

    .toc a:hover {{
      color: var(--accent-strong);
    }}

    .empty-search {{
      display: none;
      margin-top: 12px;
      color: var(--muted);
      font-size: 0.92rem;
    }}

    @media (max-width: 1080px) {{
      body {{
        grid-template-columns: 1fr;
      }}

      .sidebar {{
        position: static;
        height: auto;
        border-right: 0;
        border-bottom: 1px solid var(--line);
      }}

      .doc-shell {{
        grid-template-columns: 1fr;
      }}

      .toc {{
        position: static;
        order: -1;
      }}
    }}

    @media (max-width: 720px) {{
      .content {{
        padding: 20px 14px 48px;
      }}

      .doc-card {{
        padding: 22px 18px;
      }}

      .hero {{
        padding: 18px 18px;
      }}
    }}
  </style>
</head>
<body>
  <aside class="sidebar">
    <div class="brand">
      <h1>GAME_PROJECT_DOCS</h1>
      <p>Trang đọc tài liệu GDD tĩnh, gom toàn bộ thư mục thành một giao diện dễ chia sẻ và dễ theo dõi.</p>
    </div>
    <input id="search" class="search" type="search" placeholder="Tìm tài liệu theo tên hoặc đường dẫn">
    <div id="empty-search" class="empty-search">Không có tài liệu khớp bộ lọc.</div>
    <nav id="nav" class="nav" aria-label="Danh sách tài liệu"></nav>
  </aside>

  <main class="content">
    <section class="hero">
      <small>GDD Reader</small>
      <h2>Đọc toàn bộ thư mục như một trang web</h2>
      <p>Mỗi tài liệu được render sẵn từ Markdown, có điều hướng theo module và liên kết nội bộ để chia sẻ cho người đọc bình thường mà không cần IDE.</p>
    </section>

    <section class="doc-shell">
      <article class="doc-card">
        <div class="doc-meta">
          <p id="doc-path" class="path"></p>
          <h1 id="doc-title"></h1>
        </div>
        <div id="doc-body" class="doc-body"></div>
      </article>
      <aside class="toc">
        <h3>Mục trong tài liệu</h3>
        <ul id="toc"></ul>
      </aside>
    </section>
  </main>

  <script>
    const DOCS = {docs_json};
    const DEFAULT_DOC = "MUC_LUC.md";
    const docMap = new Map(DOCS.map((doc) => [doc.id, doc]));

    const navRoot = document.getElementById("nav");
    const searchInput = document.getElementById("search");
    const emptySearch = document.getElementById("empty-search");
    const docPath = document.getElementById("doc-path");
    const docTitle = document.getElementById("doc-title");
    const docBody = document.getElementById("doc-body");
    const tocRoot = document.getElementById("toc");

    const sectionOrder = [
      "ROOT",
      "00_GAME_VISION",
      "01_GAMEPLAY_LOOP",
      "02_CORE_SYSTEMS",
      "03_PLAYER_SYSTEMS",
      "04_WORLD_SYSTEMS",
      "05_DUNGEON_SYSTEM",
      "06_ECONOMY_SYSTEM",
      "07_PROGRESSION_SYSTEM",
      "08_CONTENT_DATABASE",
      "09_MULTIPLAYER",
      "10_TECHNICAL_DESIGN",
      "11_BALANCE_DATA",
      "12_QUESTION_FRAMEWORK",
    ];

    function buildNav(filterText = "") {{
      const normalized = filterText.trim().toLowerCase();
      navRoot.innerHTML = "";
      let visibleCount = 0;

      sectionOrder.forEach((section) => {{
        const docs = DOCS.filter((doc) => doc.section === section).filter((doc) => {{
          if (!normalized) return true;
          return doc.title.toLowerCase().includes(normalized) || doc.path.toLowerCase().includes(normalized);
        }});

        if (!docs.length) return;
        visibleCount += docs.length;

        const group = document.createElement("section");
        group.className = "nav-group";
        const title = document.createElement("h2");
        title.textContent = section === "ROOT" ? "Tài liệu gốc" : section;
        group.appendChild(title);

        const list = document.createElement("ul");
        docs.forEach((doc) => {{
          const item = document.createElement("li");
          const link = document.createElement("a");
          link.href = `#${{encodeURIComponent(doc.id)}}`;
          link.dataset.docId = doc.id;
          link.textContent = doc.title;
          item.appendChild(link);
          list.appendChild(item);
        }});
        group.appendChild(list);
        navRoot.appendChild(group);
      }});

      emptySearch.style.display = visibleCount ? "none" : "block";
      syncActiveLink();
    }}

    function parseHash() {{
      const raw = window.location.hash.replace(/^#/, "");
      if (!raw) return {{ docId: DEFAULT_DOC, anchor: "" }};
      const [docPart, anchorPart] = raw.split("::");
      const docId = decodeURIComponent(docPart || DEFAULT_DOC);
      const anchor = anchorPart ? decodeURIComponent(anchorPart) : "";
      return {{ docId, anchor }};
    }}

    function renderDoc(docId, anchor = "") {{
      const doc = docMap.get(docId) || docMap.get(DEFAULT_DOC) || DOCS[0];
      if (!doc) return;

      docPath.textContent = doc.path;
      docTitle.textContent = doc.title;
      docBody.innerHTML = doc.html;
      buildToc(doc.toc || [], doc.id);
      syncActiveLink(doc.id);

      if (anchor) {{
        requestAnimationFrame(() => {{
          const target = document.getElementById(anchor);
          if (target) target.scrollIntoView({{ behavior: "smooth", block: "start" }});
        }});
      }} else {{
        window.scrollTo({{ top: 0, behavior: "auto" }});
      }}
    }}

    function buildToc(items, docId) {{
      tocRoot.innerHTML = "";
      if (!items.length) {{
        const li = document.createElement("li");
        li.textContent = "Tài liệu này chưa có mục con đủ lớn để tạo mục lục nhanh.";
        tocRoot.appendChild(li);
        return;
      }}

      items.forEach((item) => {{
        const li = document.createElement("li");
        const link = document.createElement("a");
        link.href = `#${{encodeURIComponent(docId)}}::${{encodeURIComponent(item.anchor)}}`;
        link.dataset.level = item.level;
        link.textContent = item.title;
        li.appendChild(link);
        tocRoot.appendChild(li);
      }});
    }}

    function syncActiveLink(activeDocId = parseHash().docId) {{
      document.querySelectorAll(".nav-group a").forEach((link) => {{
        link.classList.toggle("is-active", link.dataset.docId === activeDocId);
      }});
    }}

    window.addEventListener("hashchange", () => {{
      const {{ docId, anchor }} = parseHash();
      renderDoc(docId, anchor);
    }});

    searchInput.addEventListener("input", (event) => {{
      buildNav(event.target.value);
    }});

    buildNav();
    const {{ docId, anchor }} = parseHash();
    renderDoc(docId, anchor);
  </script>
</body>
</html>
"""


def main():
    docs = build_docs_payload(collect_markdown_files())
    OUTPUT_FILE.write_text(build_html(docs), encoding="utf-8")
    print(f"Built {OUTPUT_FILE} with {len(docs)} markdown documents.")


if __name__ == "__main__":
    main()
