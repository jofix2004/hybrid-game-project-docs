Project Code: HYBRID
Version: 0.9 (Draft)
Author: null
Date: 18/02/2026

# 13_PLAYER_CORE_STATE_SHEET

Sheet này chốt luật vận hành lõi của người chơi ở mức gameplay.

## Mục tiêu

- Biến phần `Player Core State` trong level 8 thành rule có thể giao việc.
- Tách rõ `resource`, `state`, `fail state`, `recovery`.
- Giữ gọn MVP, chưa đưa các hệ survival nâng cao vào.

## Phạm vi hiện tại

- Có 3 thanh chính:
  - `Máu`
  - `Thức ăn`
  - `Mana`
- Chưa đưa vào lõi:
  - `Nước`
  - `Tinh thần`
  - `Bệnh tật`
  - `Stamina`

## 1. Core Resources

### Máu

- Vai trò:
  - thước đo sinh tồn trực tiếp
  - chạm `0` là vào fail flow
- Hồi phục tự nhiên:
  - hồi theo tốc độ cố định
  - chỉ hồi khi không bị đánh trong vài giây
  - chỉ hồi khi `Thức ăn` đang ở mức `No`

### Thức ăn

- Vai trò:
  - thanh duy trì sinh tồn nền
  - quyết định khả năng hồi máu tự nhiên
  - gây phạt khi đói

### Mana

- Vai trò:
  - tài nguyên vận hành cho tool, utility, trang bị và một phần skill
  - không dùng như thanh phép tự hồi vô hạn
- Tính chất:
  - không tự hồi
  - dung tích tăng theo tiến trình chung
  - có thêm phần cộng từ trang bị hoặc artifact

## 2. Hunger State Rules

### Các ngưỡng thức ăn

- `0 = Kiệt đói`
  - mất máu theo thời gian
  - nếu không có cách cứu thì có thể chết
- `1-30 = Đói`
  - giảm sát thương
  - không hồi máu tự nhiên
- `30-70 = Vừa`
  - trạng thái trung tính
- `70-100 = No`
  - có thể hồi máu tự nhiên nếu thỏa điều kiện không bị đánh

### Ý đồ thiết kế

- Thanh `Thức ăn` không chỉ là duy trì sự sống, mà còn ảnh hưởng trực tiếp tới hiệu suất chiến đấu.
- Người chơi đói vẫn chơi được, nhưng chất lượng chuyến đi giảm rõ.
- `Kiệt đói` là tín hiệu phải xử lý ngay, không phải chỉ là debuff nhẹ.

## 3. Mana Rules

### Khi Mana về 0

- Không dùng được hành động cần mana.
- Các thiết bị hoặc hiệu ứng duy trì bằng mana sẽ tắt nếu không có nguồn thay thế.

### Nguồn nạp mana cá nhân

- `Nguồn chính`
  - nạp ở base
  - bằng cách mang quặng mana về chiết xuất thành mana tích trữ
- `Nguồn cứu nguy`
  - bình chứa dự trữ
- `Nguồn cơ hội`
  - quặng tinh khiết
  - mana rơi từ sinh vật

### Quy tắc hiệu quả nguồn nạp

- Base là nơi nạp hiệu quả nhất.
- Bình chứa là công cụ cơ động để mang đi xa.
- Quặng tinh khiết có thể dùng tại chỗ nhưng hiệu quả kém.
- Mana rơi từ sinh vật là nguồn bổ sung, không thay vai trò của khai khoáng.

## 4. Death, Downed and Respawn

### Rule khi Máu = 0

- `Solo`
  - chết ngay
- `Co-op`
  - vào trạng thái `Downed`

### Downed State

- Người chơi nằm im.
- Không di chuyển.
- Không hành động.
- Thời gian mặc định:
  - `60 giây`
- Có thể scale theo mode hoặc độ khó.

### Revive Rule

- `Cứu cơ bản`
  - dùng máu của người cứu để đổi lấy lượt hồi sinh đồng đội
- `Cứu nâng cao`
  - vật phẩm hoặc kỹ năng giúp cứu nhanh hơn hoặc an toàn hơn
- Người được cứu dậy với:
  - `50% máu`
  - các chỉ số khác giữ như trước lúc chết hoặc downed

### Respawn Locations

- Căn cứ
- Điểm hồi sinh đã mở
- Công trình hồi sinh
- Khả năng hồi sinh từ đồng đội hoặc kỹ năng đặc biệt

## 5. Death Penalty by Mode

- `Nhẹ`
  - không rơi gì hoặc chỉ rơi một phần
- `Vừa`
  - rơi hết đồ mang theo
- `Nặng`
  - rơi đồ
  - không làm mất `điểm chỉ số`
  - chỉ có thể mất thêm một phần tích lũy phụ nếu mode đó bật luật này

## 6. Player State List for Implementation

- `Normal`
  - trạng thái thường
- `Hungry`
  - khi thức ăn trong ngưỡng đói
- `Starving`
  - khi thức ăn về 0
- `Mana Depleted`
  - khi mana về 0
- `Downed`
  - chỉ có ở co-op
- `Dead`
  - trạng thái thất bại trực tiếp

## 7. Transition Notes

- `No -> Vừa -> Đói -> Kiệt đói`
  - xảy ra khi không ăn trong quá trình chơi
- `Normal -> Mana Depleted`
  - khi dùng hết mana
- `Alive -> Downed`
  - chỉ trong co-op khi máu về 0
- `Alive -> Dead`
  - trong solo khi máu về 0
- `Downed -> Alive`
  - khi được cứu
- `Downed -> Dead`
  - khi hết thời gian hoặc không được cứu

## 8. Rule Summary

- `Máu` là fail bar trực tiếp.
- `Thức ăn` là thanh duy trì ảnh hưởng cả sinh tồn lẫn sức chiến đấu.
- `Mana` là tài nguyên vận hành, không tự hồi.
- `Solo` chết ngay, `co-op` có lớp `downed`.
- Recovery có thật, nhưng luôn gắn với chi phí hoặc rủi ro.

## 9. Cần tinh chỉnh sau

- Số cụ thể cho tốc độ hồi máu
- Tốc độ tụt thức ăn
- Tốc độ mất máu khi `Kiệt đói`
- Lượng máu người cứu phải trả khi hồi sinh đồng đội
- Tương tác giữa mode khó và death penalty

## 10. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 1

- `Máu tối đa`
  - tăng theo `tiến trình nhân vật`
  - phần tăng nền hiện đi qua `điểm chỉ số` nhận từ các mốc tiến trình
  - trang bị, giáp và artifact không phải nguồn tăng nền chính
  - nhưng vẫn là lớp `loadout cơ học` quan trọng, có thể ảnh hưởng mạnh tới cách chơi
- `Tăng chỉ số nền`
  - đi theo `mốc tiến trình`
  - và được người chơi tự phân bổ bằng `điểm chỉ số` tại `base / shrine`
- `Tốc độ tăng các thanh`
  - `Máu` và `Mana` có thể tăng ở các mốc khác nhau
  - `Thức ăn tối đa` tăng chậm hơn hoặc ít hơn
- `Thức ăn`
  - tụt đều theo thời gian
- `Đồ ăn`
  - mỗi loại có giá trị cố định riêng
  - có thể cho hiệu quả tức thì hoặc hiệu ứng hồi dần
- `Ăn uống`
  - có animation ngắn
  - cooldown chi tiết để theo từng item sau
- `Nhóm đồ ăn`
  - `đồ ăn rẻ`
  - `đồ ăn tốt`
  - `đồ ăn buff`
- `Đồ ăn buff`
  - chính là buff sinh tồn
  - buff combat ít hơn
  - buff utility hoặc môi trường là nhánh đặc thù hơn
- `Mana`
  - không tụt tự nhiên theo thời gian
  - không cần thêm ngưỡng cảnh báo gameplay riêng
  - người chơi tự theo dõi qua UI

## 11. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 2

- `Sau khi được cứu dậy`
  - có vài giây miễn nhiễm hoặc giảm sát thương
- `Downed hết thời gian`
  - chết thật ngay
- `Recovery khi chết`
  - có `recovery marker` rõ ở đúng nơi chết
  - item trên `hotbar` rơi thẳng xuống đất
  - item trong túi nằm trong `bia mộ`
- `Bia mộ`
  - hoạt động gần như một rương
  - biến mất khi bên trong rỗng
  - ở mode thường thì ai cũng mở được
  - nếu bật PvP mode thì chỉ chủ nhân hoặc đồng đội được mở
  - không thể phá hủy
  - không thể chạy mất
  - thời gian tồn tại tùy mode: có thể vô hạn hoặc rất dài
- `Respawn`
  - hồi trạng thái tùy điểm hồi sinh
- `Base respawn`
  - là spawn gốc hoặc giường
  - cho trạng thái hồi tốt nhất
- `Điểm hồi sinh mở`
  - là công trình chế tạo
  - dùng hữu hạn lần
  - tốn chi phí xây dựng
  - hiệu quả hồi kém hơn base
- `Đồng đội hoặc kỹ năng`
  - hồi sinh thường thì chậm và yếu hơn
  - bản chuyên kỹ năng hồi sinh sẽ tốt hơn
- `Respawn ở base`
  - chỉ hồi chỉ số
  - không kèm buff an toàn riêng
- `Kiệt đói`
  - có thể giết người chơi ngoài combat
  - nghĩa là `AFK = có thể chết`
  - tốc độ mất máu đi theo nhịp đều

## 12. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 3

- `Ăn khi đang đói`
  - cộng no ngay
  - rồi áp dụng lại rule mới theo ngưỡng hiện tại
- `Đồ ăn có hiệu ứng hồi dần`
  - vẫn cộng no ngay
  - còn hiệu ứng phụ hoặc phần hồi thêm chạy sau
- `Hồi máu tự nhiên`
  - bất kỳ hit nào cũng reset timer
  - nếu người chơi đủ no và đủ an toàn thì có thể hồi đầy
- `Mana refill item`
  - loại tức thì là chính
  - loại hồi dần để sau nếu cần
  - dùng với animation ngắn như ăn
  - nếu dùng khi gần đầy thì phần dư đa số bị mất
- `Mana cá nhân`
  - không vượt quá mức tối đa ở giai đoạn này
- `Hồi máu bằng item trực tiếp`
  - có tồn tại
  - nhưng hiếm và đắt
  - vai trò là cả hồi giữa chuyến đi lẫn cứu nguy
  - trong đó cứu nguy khẩn cấp là hướng chính

## 13. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 4

- `Tốc độ di chuyển`
  - không là trục tăng trưởng lớn
  - nếu có thì chỉ tăng rất ít theo mốc
- `Sát thương cơ bản`
  - có thể tăng ít theo tiến trình nền
  - nhưng không phải nguồn sức mạnh chính
- `Nguồn sát thương chính`
  - `vũ khí` là chính
  - `trang bị` là nguồn bổ trợ
  - `đồ ăn` là lớp buff phụ
- `Tiến trình chỉ số nền`
  - không dùng thanh EXP liên tục
  - thay bằng `điểm chỉ số`
- `Nguồn nhận điểm chỉ số`
  - chủ yếu từ `mở tầng`
  - `boss / milestone` là nguồn phụ
- `Điểm chỉ số` dùng để cộng vào:
  - `máu tối đa`
  - `ma lực tối đa`
  - `độ tụt thức ăn`
- `Điểm thức ăn`
  - làm tốc độ tụt đói chậm hơn
- `Phân bổ điểm chỉ số`
  - chỉ thực hiện tại `base / shrine / chỗ an toàn`

## 14. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 5

- `Điểm theo mốc`
  - `mốc thường` cho `1 điểm`
  - `mốc lớn` cho `nhiều điểm`
  - `boss` có thể cho `1 hoặc nhiều điểm` tùy vai trò
- `Giá điểm`
  - giai đoạn đầu để như nhau giữa các chỉ số
  - về sau nếu cần mới tách
- `Giới hạn đầu tư`
  - bỏ hướng `hard cap theo mốc`
  - người chơi thích cộng vào đâu thì cộng
  - cho phép `all in` vào một chỉ số nếu muốn
- `Respec`
  - được phép dùng để tránh khóa nhầm build
  - chỉ thực hiện ở `base / shrine`
  - hoàn lại `toàn bộ điểm`
  - cần một `item chuyên dụng`, ví dụ như thuốc trí nhớ
  - chi phí respec nên đắt để giữ trọng lượng quyết định
- `Điểm chỉ số khi chết`
  - không mất, kể cả ở mode nặng

## 15. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 6

- `All in build`
  - người chơi được tự do cộng lệch hoàn toàn
  - không có cảnh báo UI
  - chấp nhận khả năng trap người chơi mới
- `Điểm chỉ số`
  - áp dụng ngay khi cộng
- `Cộng máu tối đa`
  - tăng cả `máu hiện tại` tương ứng
  - xử lý theo `%`
- `Cộng mana tối đa`
  - chỉ tăng `trần mana`
  - không tăng `mana hiện tại`
- `Cộng vào độ tụt thức ăn`
  - giảm theo `%`
- `Item respec`
  - là vật phẩm dùng một lần rồi mất
- `Điểm được dùng cho`
  - `máu tối đa`
  - `ma lực tối đa`
  - `độ tụt thức ăn`
- `Respec`
  - chỉ cho ở `base` hoặc `shrine mốc lớn`
  - không mở ở mọi khu an toàn nhỏ

## 16. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 7

- `Resolve order` khi người chơi vừa ăn vừa đang ở trạng thái nguy hiểm:
  - cập nhật hành động `ăn` trước
  - tính lại ngưỡng `thức ăn`
  - rồi mới xử lý `mất máu / hồi máu`
- `Ăn và bị hit cùng lúc`
  - hit reset hồi máu ngay
- `Heal over time`
  - vẫn chạy dù người chơi đang đói
  - nếu đồng thời có `kiệt đói` thì hai vế triệt tiêu nhau theo số thực
- `Cứu sát giờ`
  - nếu action cứu hoàn tất trước khi timer về `0` thì cứu thành công
- `Nhiều nguồn hồi máu`
  - cộng dồn bình thường ở giai đoạn đầu
- `Nhiều nguồn mất máu`
  - cộng dồn bình thường
- `Respawn`
  - reset hiệu ứng theo `điểm hồi sinh`
- `Base respawn`
  - xóa sạch debuff ngắn
  - xóa đa số debuff thường
- `Điểm hồi sinh mở`
  - giữ lại nhiều debuff hơn base
- `Hồi sinh bởi đồng đội hoặc kỹ năng`
  - giữ gần như toàn bộ debuff hiện có

## 17. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 8

- `Base respawn`
  - `Máu đầy`
  - `Thức ăn` ở mức `vừa hoặc no`
  - `Mana` không nhất thiết đầy để vẫn giữ vai trò của trạm nạp
- `Điểm hồi sinh mở`
  - `Máu` ở mức khoảng nửa hoặc hơn
  - `Thức ăn` thấp hơn base
  - `Mana` thấp hoặc gần như không có
- `Hồi sinh bởi đồng đội / kỹ năng`
  - `Máu` thấp hay cao tùy kỹ năng, nhưng mặc định thấp hơn điểm hồi sinh mở
  - `Thức ăn` giữ nguyên
  - `Mana` giữ nguyên hoặc rất thấp

## 18. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 9

- `Điểm chỉ số chưa dùng`
  - giữ luôn trên nhân vật
- `Cộng điểm`
  - chỉ thực hiện khi đang ở `base / shrine mốc lớn`
- `Respec trong combat`
  - không cần cấm riêng
  - vì bản thân respec chỉ dùng được ở `base / shrine mốc lớn`
- `Respec giảm máu tối đa`
  - `máu hiện tại` co theo `%` như lúc cộng điểm
- `Respec giảm mana tối đa`
  - `mana hiện tại` bị clamp về trần mới
- `Cộng điểm vào độ tụt thức ăn`
  - chỉ ảnh hưởng các nhịp sau
  - không sửa ngay giá trị hiện tại của thanh đói
- `Ăn khi gần đầy`
  - phần no dư bị mất
  - buff phụ của món ăn vẫn kích hoạt nếu item cho phép
- `Item hồi máu trực tiếp`
  - vẫn dùng được khi đang `đói / kiệt đói`
- `Heal over time khi downed`
  - vẫn tiếp tục chạy
- `Kiểm tra chết trong một nhịp`
  - nếu chạm `0` ở bất kỳ bước nào thì chết ngay
