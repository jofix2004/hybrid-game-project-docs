Project Code: HYBRID
Version: 0.6 (Draft)
Author: null
Date: 14/01/2026

# 02_CONTENT_MAP

Tài liệu này định nghĩa các nhóm nội dung mà bộ câu hỏi phải bao phủ.

## Ma trận nội dung

| Nhóm nội dung | Bắt đầu hỏi từ cấp độ | Đi sâu nhất ở cấp độ | Đầu ra chính |
| :--- | :--- | :--- | :--- |
| Định danh game | 0 | 2 | Mô tả game ngắn, rõ |
| Người chơi mục tiêu | 1 | 3 | Chân dung người chơi và nhu cầu |
| Fantasy và cảm xúc | 1 | 3 | Cảm giác cốt lõi khi chơi |
| Game pillars | 1 | 2 | Các trụ cột không được phá vỡ |
| Core gameplay loop | 2 | 4 | Vòng lặp hành động - phần thưởng |
| Session structure | 2 | 4 | Nhịp phiên ngắn và dài |
| Hệ thống người chơi | 3 | 8 | Stats, skill, inventory, control |
| Combat | 3 | 8 | Rule chiến đấu, công thức, counterplay |
| Survival | 3 | 7 | Áp lực sinh tồn và cách khắc phục |
| Building và crafting | 3 | 8 | Luồng tạo vật phẩm và phát triển căn cứ |
| Tài nguyên và economy | 4 | 8 | Resource flow, sink, scarcity |
| World và biome | 4 | 7 | Khung nội dung thế giới |
| Dungeon hoặc mission structure | 4 | 8 | Cấu trúc thử thách chính |
| Enemy và boss content | 5 | 8 | Vai trò, độ khó, tiến triển |
| Progression | 4 | 8 | Mở khóa, tăng sức mạnh, mục tiêu dài hạn |
| Multiplayer hoặc social | 5 | 7 | Hợp tác, cạnh tranh, chia sẻ, revive |
| Technical constraints | 6 | 8 | Networking, save, tools, pipeline |
| UI/UX và accessibility | 5 | 8 | Dòng thông tin, thao tác, hỗ trợ người chơi |
| Balance và data | 6 | 8 | Bảng số liệu, công thức, tuning |
| Scope và production reality | 6 | 7 | Mức độ khả thi và ưu tiên làm |

## Nhóm nội dung bắt buộc phải có trước khi viết GDD sâu

- Định danh game
- Fantasy và cảm xúc
- Game pillars
- Core gameplay loop
- Hệ thống người chơi
- Tài nguyên và economy
- Progression
- Scope và production reality

## Nhóm nội dung có thể đi sau nhưng không được bỏ qua

- UI/UX và accessibility
- Multiplayer hoặc social
- Balance và data
- Technical constraints

## Cách đọc ma trận này

- Nếu một nhóm nội dung bắt đầu quá sớm, bộ câu hỏi sẽ bị nặng chi tiết khi nền chưa chắc.
- Nếu một nhóm nội dung đi quá muộn, khung game dễ bị lệch hoặc phải sửa lớn.
- Mỗi nhóm nội dung nên được hỏi lại nhiều vòng, nhưng với độ sâu tăng dần.

## Trục đào sâu cho mỗi nhóm nội dung

Mỗi nhóm nội dung sau này nên được hỏi theo cùng một trục:

1. Nó tồn tại để phục vụ mục tiêu gì.
2. Người chơi tương tác với nó khi nào.
3. Nó ảnh hưởng tới loop nào.
4. Nó thưởng gì và phạt gì.
5. Nó liên kết với hệ thống nào khác.
6. Nó có bao nhiêu biến thể nội dung.
7. Nó có chỉ số hoặc công thức nào.
8. Nó có edge case hoặc failure case nào.
