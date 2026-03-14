Project Code: HYBRID
Version: 0.6 (Draft)
Author: null
Date: 15/01/2026

# 03_USAGE_ROADMAP

Tài liệu này mô tả cách dùng khung cấp độ và ma trận nội dung để tạo bộ câu hỏi thật ở bước tiếp theo.

## Chặng 1: Khóa định hướng

- Phạm vi: cấp độ 0 đến 2.
- Mục tiêu: trả lời được game là gì, dành cho ai, cảm giác cốt lõi là gì.
- Đầu ra: game vision ngắn, player fantasy, pillars, target experience.
- Không làm lúc này: hỏi công thức, data table, balance chi tiết.

## Chặng 2: Dựng bộ khung gameplay

- Phạm vi: cấp độ 3 đến 4.
- Mục tiêu: dựng được core loop, session loop và các hệ thống chính.
- Đầu ra: sơ đồ loop, danh sách hệ thống, vai trò từng hệ thống.
- Dấu hiệu hoàn tất: có thể giải thích game trong một phiên chơi mẫu.

## Chặng 3: Dựng nội dung và tiến trình

- Phạm vi: cấp độ 5 đến 6.
- Mục tiêu: biết game có gì để chơi, chơi vì sao tiếp tục và tốn tài nguyên gì.
- Đầu ra: khung world, dungeon, enemy, resource, progression, economy.
- Dấu hiệu hoàn tất: người chơi có đường tiến lên rõ ràng và game có đủ nội dung để nuôi loop.

## Chặng 4: Kiểm tra tính khả thi

- Phạm vi: cấp độ 7.
- Mục tiêu: đối chiếu ý tưởng với technical constraints, đội ngũ và phạm vi sản xuất.
- Đầu ra: danh sách giả định kỹ thuật, rủi ro, giới hạn scope, hạng mục ưu tiên.
- Dấu hiệu hoàn tất: biết cái gì làm trước, cái gì cắt, cái gì để bản sau.

## Chặng 5: Đặc tả sẵn sàng triển khai

- Phạm vi: cấp độ 8.
- Mục tiêu: chuyển từ khái niệm sang tài liệu có thể giao việc.
- Đầu ra: thông số, quy tắc, bảng dữ liệu, edge case, flow hoàn chỉnh.
- Dấu hiệu hoàn tất: từng bộ phận có thể bắt tay vào việc mà không phải đoán ý quá nhiều.

## Quy tắc khi viết bộ câu hỏi thật

- Mỗi câu hỏi chỉ nên đào vào một biến số chính.
- Đi từ mở đến đóng: hỏi khám phá trước, hỏi chốt sau.
- Hỏi theo mạch người chơi trước, mạch hệ thống sau.
- Luôn có câu hỏi kiểm tra mâu thuẫn giữa các câu trả lời.
- Khi đã có quyết định, chuyển nó thành phát biểu thiết kế thay vì hỏi lại nhiều lần.

## Thứ tự ưu tiên khi triển khai bộ câu hỏi thật

1. Viết bộ câu hỏi cho cấp 0 đến cấp 2.
2. Viết bộ câu hỏi cho loop và hệ thống chính ở cấp 3 đến cấp 4.
3. Viết bộ câu hỏi cho world, content, progression và economy.
4. Viết bộ câu hỏi cho technical, multiplayer, balance và data.

## Cách chia bộ câu hỏi thành nhiều đợt

- Đợt 1: 15 đến 25 câu để khóa tầm nhìn.
- Đợt 2: 25 đến 40 câu để dựng loop và hệ thống chính.
- Đợt 3: 30 đến 50 câu để phủ world, content, progression và economy.
- Đợt 4: 20 đến 40 câu để xử lý technical, scope, balance và production.

## Kết quả mong đợi của bước hiện tại

Sau tài liệu này, bước tiếp theo nên là tạo bộ câu hỏi thật cho từng cấp độ, bắt đầu từ cấp 0 đến cấp 2 trước, thay vì cố viết toàn bộ một lần.
