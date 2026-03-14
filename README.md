Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 15/03/2026

# GAME_PROJECT_DOCS

Bộ tài liệu thiết kế game được chuẩn hóa lại cho dự án `HYBRID`.

## Mục lục

- [Tổng quan game](./GAME_OVERVIEW.md)
- [Bắt đầu đọc từ đây](./START_HERE.md)
- [Mở mục lục trung tâm](./MUC_LUC.md)
- [GDD Execution Plan](./GDD_EXECUTION_PLAN.md)
- [GDD Doc Backlog](./GDD_DOC_BACKLOG.md)
- [Kế hoạch ứng dụng Visual Cues Tutorial](./VISUAL_CUES_TUTORIAL_APPLICATION_PLAN.md)

## Mục tiêu

- Dùng một cấu trúc cố định cho game design, technical design và balance.
- Giữ nguyên các file `.txt` cũ trong `document/` để đối chiếu lịch sử.
- Đặt các tài liệu mới theo module để dễ mở rộng, review và phân công.

## Nguồn tổng hợp

- Dữ liệu cấu trúc do user cung cấp.
- Nội dung bổ sung từ các tài liệu cũ: `[GDD]`, `[TDD]`, `[NPS]`, `[WGS]`.

## Thư mục chuẩn

- `00_GAME_VISION`: Tầm nhìn, fantasy, điểm bán độc đáo.
- `01_GAMEPLAY_LOOP`: Vòng lặp gameplay ngắn, dài hạn và co-op.
- `02_CORE_SYSTEMS`: Luật chơi cốt lõi.
- `03_PLAYER_SYSTEMS`: Hệ thống nhân vật người chơi.
- `04_WORLD_SYSTEMS`: Sinh thái, thời tiết, world generation.
- `05_DUNGEON_SYSTEM`: Cấu trúc hầm ngục và boss.
- `06_ECONOMY_SYSTEM`: Tài nguyên, phân bổ, kinh tế crafting.
- `07_PROGRESSION_SYSTEM`: Công nghệ, level, điều kiện mở khóa.
- `08_CONTENT_DATABASE`: Định nghĩa bảng dữ liệu.
- `09_MULTIPLAYER`: Co-op, revive, chia sẻ tài nguyên, sync.
- `10_TECHNICAL_DESIGN`: Logic kỹ thuật cần cho gameplay.
- `11_BALANCE_DATA`: Khung cân bằng số liệu.

## Thư mục hỗ trợ

- `12_QUESTION_FRAMEWORK`: Khung xây dựng bộ câu hỏi từ siêu cơ bản đến cực chi tiết.

## Nguyên tắc cập nhật

- Mỗi thay đổi gameplay phải cập nhật ít nhất `01`, `02`, `07` và `11` nếu có ảnh hưởng số liệu.
- Mỗi thay đổi networking hoặc multiplayer phải cập nhật `09` và `10`.
- Bảng data chỉ lưu schema mẫu trong repo; data số lượng lớn nên quản lý thêm bằng spreadsheet hoặc tool nội bộ.

## Xuất bản web

- Reader chính nằm ở [index.html](./index.html)
