Project Code: HYBRID
Version: 0.6 (Draft)
Author: null
Date: 13/01/2026

# 01_LEVEL_LADDER

Tài liệu này định nghĩa các cấp độ của bộ câu hỏi, từ mức rất cơ bản đến mức cực chi tiết.

## Tổng quan thang cấp độ

| Cấp độ | Tên cấp độ | Mục tiêu chính | Đầu ra mong đợi |
| :--- | :--- | :--- | :--- |
| 0 | Hạt giống ý tưởng | Chốt game là gì trong một câu | Một mô tả 1 đến 3 câu |
| 1 | Khung bản sắc | Xác định fantasy, pillar, đối tượng người chơi | Một bản tóm tắt định hướng |
| 2 | Khung trải nghiệm | Làm rõ cảm xúc, nhịp chơi, trải nghiệm phiên chơi | Mô tả trải nghiệm đầu, giữa, cuối game |
| 3 | Khung gameplay cốt lõi | Chốt loop, hành động chính, rủi ro và phần thưởng | Loop rõ ràng và có thể mô phỏng |
| 4 | Khung hệ thống | Xác định các hệ thống chính và quan hệ giữa chúng | Danh sách hệ thống và vai trò |
| 5 | Khung nội dung thế giới | Xác định world, content, dungeon, enemy, resource | Bản đồ nội dung cấp cao |
| 6 | Khung tiến trình và kinh tế | Xác định progression, unlock, economy, balance hướng | Luồng phát triển dài hạn |
| 7 | Khung vận hành và kỹ thuật | Xác định co-op, technical, scope, pipeline, ràng buộc | Bộ điều kiện triển khai |
| 8 | Khung đặc tả chi tiết | Xác định công thức, bảng dữ liệu, edge case, quy tắc đầy đủ | Tài liệu sẵn sàng cho implementation |

## Mô tả từng cấp độ

### Cấp độ 0: Hạt giống ý tưởng

- Mục tiêu: biết chính xác game này là gì.
- Độ sâu: cực ngắn, cực rõ, không lan sang chi tiết hệ thống.
- Nên trả lời được: thể loại, fantasy chính, điểm hấp dẫn đầu tiên.
- Chưa nên hỏi: công thức sát thương, bảng dữ liệu, kiến trúc kỹ thuật.

### Cấp độ 1: Khung bản sắc

- Mục tiêu: xác định DNA của game.
- Độ sâu: đủ để phân biệt game với các game khác cùng thể loại.
- Nội dung cần có: pillars, player fantasy, target experience, inspirations, USP.
- Dấu hiệu hoàn tất: người khác đọc xong hiểu game này muốn trở thành gì.

### Cấp độ 2: Khung trải nghiệm

- Mục tiêu: mô tả cảm giác chơi chứ chưa đi quá sâu vào rule chi tiết.
- Nội dung cần có: nhịp nhanh hay chậm, áp lực ở đâu, khoảnh khắc đáng nhớ là gì.
- Dấu hiệu hoàn tất: có thể kể được hành trình cảm xúc của người chơi qua một phiên và qua nhiều giờ chơi.

### Cấp độ 3: Khung gameplay cốt lõi

- Mục tiêu: chốt người chơi làm gì lặp đi lặp lại.
- Nội dung cần có: core loop, short session loop, long progression loop, risk/reward loop.
- Dấu hiệu hoàn tất: có thể vẽ thành sơ đồ vòng lặp và tìm ra điểm nghẽn.

### Cấp độ 4: Khung hệ thống

- Mục tiêu: liệt kê và phân vai cho các hệ thống chính.
- Nội dung cần có: combat, survival, crafting, building, resource flow, control flow.
- Dấu hiệu hoàn tất: biết hệ thống nào là trục chính, hệ thống nào chỉ hỗ trợ.

### Cấp độ 5: Khung nội dung thế giới

- Mục tiêu: xác định game chứa những loại nội dung gì.
- Nội dung cần có: biome hang mở, lớp chiều sâu hang mở, POI hoặc công trình, room nội thất, enemy families, resource families, event types.
- Dấu hiệu hoàn tất: có thể hình dung game có đủ thứ để nuôi loop trong nhiều giờ.

### Cấp độ 6: Khung tiến trình và kinh tế

- Mục tiêu: làm rõ người chơi tiến lên bằng cách nào và tốn gì để tiến lên.
- Nội dung cần có: tech tree, unlock conditions, resource tiers, economy sinks, build variety.
- Dấu hiệu hoàn tất: có thể giải thích vì sao người chơi tiếp tục chơi thêm 10 giờ nữa.

### Cấp độ 7: Khung vận hành và kỹ thuật

- Mục tiêu: đảm bảo ý tưởng có thể sản xuất và vận hành.
- Nội dung cần có: multiplayer assumptions, networking level, save system, content pipeline, scope, tools.
- Dấu hiệu hoàn tất: đã thấy rõ các ràng buộc lớn và rủi ro sản xuất.

### Cấp độ 8: Khung đặc tả chi tiết

- Mục tiêu: đưa game từ “ý tưởng tốt” sang “tài liệu có thể làm”.
- Nội dung cần có: công thức, bảng dữ liệu, thông số, edge case, logic fail state, state transition.
- Dấu hiệu hoàn tất: có thể giao việc chi tiết cho design, code, art, content.

## Quy tắc chuyển cấp

- Chỉ chuyển cấp khi cấp hiện tại đã có câu trả lời ngắn gọn nhưng chắc chắn.
- Nếu cấp cao hơn làm lộ mâu thuẫn, quay lại cấp thấp hơn để sửa định hướng.
- Không để chi tiết kỹ thuật kéo ngược định hướng fantasy quá sớm.
- Từ cấp 4 trở đi, mỗi nhóm câu hỏi phải được soi lại bằng tiêu chí cố định của chính cấp đó, không được mặc định đúng chỉ vì các cấp trước đã nói tới.

## Gợi ý cách dùng sau này

- Cấp 0 đến 2 dùng để khóa tầm nhìn.
- Cấp 3 đến 5 dùng để dựng bộ khung game.
- Cấp 6 đến 8 dùng để chuẩn bị production và balancing.
