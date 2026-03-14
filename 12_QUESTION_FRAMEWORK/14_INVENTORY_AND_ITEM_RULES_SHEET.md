Project Code: HYBRID
Version: 0.9 (Draft)
Author: null
Date: 20/02/2026

# 14_INVENTORY_AND_ITEM_RULES_SHEET

Sheet này chốt luật mang đồ, nhặt đồ, stack, trang bị và độ bền vật phẩm.

## Mục tiêu

- Biến các quyết định về inventory và item từ level 8 thành rule rõ để code và UI bám theo.
- Tách rõ:
  - `bag logic`
  - `equipment logic`
  - `durability logic`
  - `repair and salvage logic`

## 1. Inventory Structure

- Mô hình hiện tại:
  - `Hotbar + Túi chính`
- Kiểu giới hạn:
  - theo `slot`
- Chưa dùng:
  - `weight system`

## 2. Hotbar Rules

### Vai trò

- Là khu đồ đang cầm hoặc dùng nhanh.
- Cho phép đổi trực tiếp mà không cần mở túi.
- Hiện tại có `8 ô`.

### Loại đồ hợp lệ

- `Item dùng nhanh`
- `Tool`
- `Weapon`
- `Consumable`
- `Utility cầm tay`

## 3. Main Bag Rules

### Vai trò

- Chứa phần lớn loot, nguyên liệu và đồ dự phòng.
- Đầu game có `24 ô`.
- Có thể tăng theo `tiến trình` hoặc `phụ kiện`.

### Auto-pickup Order

- Ưu tiên nhét vào `stack cũ trên hotbar`
- Sau đó nhét vào `stack cũ trong túi chính`
- Nếu chưa vào được stack:
  - ưu tiên `ô trống trên hotbar`
  - rồi mới tới `ô trống trong túi chính`
- Nếu full cả hai:
  - item ở lại đất

### Auto-sort

- Chưa có ở giai đoạn hiện tại.
- Để sau như một tính năng nâng cao.

## 4. Stack Rules

- `Tài nguyên`
  - có stack
  - số stack tùy item
- `Consumable`
  - có stack
  - số stack tùy item
- `Tool / Weapon / Equipment`
  - không stack

## 5. Equipment Slots

### Có slot riêng cho

- `Giáp`
- `Artifact`

### Artifact Rules

- Có khoảng `4 ô artifact`
- Artifact có thể:
  - cộng chỉ số thụ động
  - mở hiệu ứng đặc biệt
  - tăng mana hoặc utility
- Artifact là lớp loadout cơ học khá nặng theo lối chơi
- Có loại dùng mana
- Có loại có durability

### Armor Rules

- Giáp có thể:
  - giảm sát thương
  - kháng hiệu ứng
  - mang hiệu ứng riêng
- Có loại theo set bonus
- Có loại mạnh theo từng món riêng

## 6. Ground Loot Rules

- Đa số tài nguyên khi khai thác:
  - rơi ra đất
- Một số loại thu hoạch hoặc chiết xuất đặc biệt:
  - vào thẳng inventory
- Nếu inventory đầy:
  - loot vẫn rơi bình thường
- Ở mode thường:
  - loot rơi đất từ khai thác hoặc quái ai cũng có thể nhặt ngay

## 7. Item Durability Rules

### Tool

- Dùng để khai thác:
  - tốn thời gian
  - tốn durability
  - có thể tốn thêm mana nếu là tool hỗ trợ mana
- Khi `durability = 0`
  - gãy luôn hoặc biến mất

### Armor

- Hỏng dần và phải sửa
- Không vỡ thành phế liệu ngay
- Khi `durability = 0`
  - vẫn mang được
  - nhưng vô tác dụng

### Broken Item State

- Đồ hỏng vẫn:
  - mang được
  - chiếm slot
- Nhưng:
  - không còn hiệu lực gameplay tương ứng

## 8. Repair Rules

### Repair Kit

- Chủ yếu craft ở workstation
- Có thể mua nếu người chơi dư tiền hoặc thiếu loot
- Là công cụ dùng dã chiến
- Tạo một lần và dùng lâu dài
- Có `4 cấp`

### Repair Kit Limit

- Kit cấp thấp không sửa được đồ cao tier
- Sửa bằng kit:
  - đắt hơn base
  - hoặc hiệu quả thấp hơn base

### Base Repair Machine

- Có tier riêng
- Nhanh hơn
- Rẻ hơn
- Hồi full độ bền

## 9. Salvage Rules

- Tùy loại đồ mới có thể tháo rã
- Thu hồi luôn ít hơn chế mới
- Nếu đồ còn độ bền:
  - lượng thu hồi ổn định theo loại
- Nếu đồ đã `0 durability`
  - thu hồi ít hơn nữa

## 10. Item Rule Summary

- `Tool`
  - không stack
  - hỏng là gãy mất
- `Armor`
  - không stack
  - hỏng thì vẫn mang nhưng vô tác dụng
- `Artifact`
  - đi theo loadout
  - không phải loot stack đại trà
- `Loot thường`
  - ưu tiên rơi đất
  - người chơi phải quyết định mang gì về

## 12. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 1

- `Hotbar`
  - có `8 ô`
- `Túi chính`
  - đầu game có `24 ô`
  - có thể tăng theo `tiến trình` hoặc `phụ kiện`
- `Auto-sort`
  - chưa có
  - để sau như tính năng nâng cao
- `Ưu tiên nhặt đồ`
  - `stack cũ trên hotbar`
  - rồi tới `stack cũ trong túi`
  - rồi `ô trống trên hotbar`
  - rồi `ô trống trong túi chính`
- `Loot rơi đất ở mode thường`
  - ai cũng nhặt được ngay
- `Hotbar khi chết`
  - rơi thẳng xuống đất
  - rơi theo từng món như vật lý đơn giản
  - nếu đang stack thì rơi theo stack đó
- `Bia mộ và hotbar`
  - hotbar luôn rơi đất
  - không đưa vào bia mộ
- `Artifact loadout`
  - người chơi được đổi tự do ở mọi lúc
- `Giáp đang mặc bị hỏng`
  - vẫn nằm ở slot
  - nhưng vô tác dụng

## 13. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 2

- `Stack size`
  - `tài nguyên thường`: khoảng `20x - 40x`
  - `consumable`: khoảng `20x - 40x`
  - `mana fuel / pin / lõi`: không gộp stack
  - `đồ hiếm milestone`: khoảng `20x - 40x`
- `Nhặt item dùng nhanh khi hotbar đầy`
  - luôn đẩy vào túi nếu còn chỗ
- `Kéo item từ hotbar sang hotbar`
  - nếu cùng loại thì ưu tiên gộp stack trước
  - nếu không gộp được thì đổi vị trí
- `Kéo weapon / tool đang dùng ra khỏi hotbar`
  - cho phép bình thường
- `Đổi artifact giữa combat`
  - hiệu ứng áp dụng ngay
- `Thay giáp giữa combat`
  - cho thay tự do
- `Lấy đồ từ bia mộ khi túi không đủ chỗ`
  - lấy món nào ra thì món đó ra
  - không tự nhồi phần dư theo cơ chế khác
- `Repair kit dùng dã chiến`
  - là action channel lâu
- `Tháo rã đồ`
  - ở workstation thì nhanh hơn và hiệu suất cao hơn
  - ngoài hiện trường thì chậm hơn và hiệu suất kém hơn
  - dùng luôn repair kit như tool tháo rã dã chiến
- `Đồ 0 durability ở hotbar`
  - đa số là vỡ mất
  - các món đặc biệt có thể giữ nguyên icon nhưng bị làm xám

## 14. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 3

- `Đổi artifact giữa combat`
  - buff cũ mất ngay
  - buff mới vào ngay
- `Thay giáp giữa combat`
  - đổi món là áp giáp mới ngay
- `Channel repair kit`
  - nếu bị hit thì hủy repair
- `Repair kit sửa dã chiến`
  - sửa được cả giáp đang mặc
- `Tháo rã ngoài hiện trường`
  - thu hồi item trực tiếp vào túi
- `Bia mộ ở mode thường`
  - người khác có thể mở và lấy tự do
- `Loot all cho bia mộ`
  - tạm thời chưa cần
  - ưu tiên flow lấy từng món
- `Artifact`
  - tùy loại
  - loại dùng mana thì có thể vô hạn
  - loại khác có thể có độ bền
- `Pin / lõi mana`
  - có charge riêng
  - dùng như vật phẩm nạp mana cá nhân
  - dùng tới đâu trừ charge tới đó, không bỏ lượng thừa
  - ví dụ người chơi `8/10 mana`, bình `5/5`:
    dùng xong người chơi thành `10/10`, bình còn `3/5`
- `Item vỡ mất khỏi hotbar`
  - ô đó trống ngay

## 15. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 4

- `Đổi artifact làm giảm mana tối đa`
  - `mana hiện tại` bị clamp về trần mới
- `Thay giáp giữa combat`
  - chỉ áp stat mới ngay
  - không có delay hoặc chống abuse riêng ở giai đoạn này
- `Repair kit`
  - đổi hướng thành `công trình đặt xuống`
  - có thể thu hồi
  - người chơi nhét đồ vào slot của công trình để sửa hoặc tháo rã
- `Tool vỡ đúng hit cuối khai thác`
  - vẫn cho ra loot nếu hit cuối đã hợp lệ
- `Pin / lõi mana`
  - không dùng logic tiêu thụ theo thứ tự slot nữa
  - là vật phẩm nạp mana có charge riêng
  - cho phép nạp dở nhiều mức
- `Artifact có durability`
  - khi về `0` thì vỡ
- `Bia mộ`
  - chỉ cho lấy đồ ra
  - không cho nhét đồ vào
- `Tăng túi qua phụ kiện`
  - nếu tháo phụ kiện mà đang overflow thì đồ dư rơi hết ra ngoài theo logic xếp đồ thông thường
- `Loot thường ở mode thường`
  - chấp nhận tự do hoàn toàn

## 16. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 5

- `Repair kit khi thu hồi`
  - hoàn `100%`
- `Repair kit đặt xuống`
  - có `giới hạn số slot sửa`
- `Repair kit đang sửa dở mà bị nhặt lên hoặc bị phá`
  - hủy tiến trình
  - rơi đồ đang sửa ra đất
- `Artifact về 0 durability`
  - vỡ là mất luôn
- `Pin / lõi mana về 0 charge`
  - xử lý `tùy loại`
  - có loại giữ lại vỏ để sạc
  - có loại dùng hết rồi biến mất
- `Bia mộ`
  - chỉ click lấy từng món theo đúng thứ tự bên trong
  - không có flow sắp xếp lại bên trong
- `Thay giáp giữa combat`
  - mỗi lần thay từng món độc lập
- `Loot tự do ở mode thường`
  - áp dụng cùng một hướng tự do cho:
    `bia mộ`,
    `đồ rơi từ hotbar`,
    `loot quái / khai thác`
- `Tool / weapon vỡ khi đang dùng`
  - hủy action ngay
  - chuyển sang trạng thái đánh tay không
- `Tăng túi qua phụ kiện`
  - nếu tháo ra làm overflow thì đồ dư sẽ rơi hết ra ngoài

## 17. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 6

- `Repair kit`
  - chỉ có `1 slot` xử lý tại một thời điểm
- `Nguyên liệu sửa đồ trong repair kit`
  - lấy từ `inventory người chơi`
  - và `kho gần đó`
- `Tháo rã ngoài hiện trường`
  - ưu tiên trả đồ vào túi
  - nếu không đủ chỗ thì phần dư rơi ra đất
- `Artifact vỡ`
  - món vỡ mất thì coi như biến mất
- `Vỏ pin / lõi mana`
  - nếu là loại giữ lại vỏ thì `không stack`
- `Loot all cho bia mộ của người khác`
  - ở mode thường có thể cho lấy luôn nếu tính năng đó tồn tại
- `Thay giáp giữa combat`
  - là thao tác inventory trực tiếp
  - không cần thêm rule hủy action riêng ngoài flow đổi đồ
- `Đồ dư khi giảm sức chứa túi`
  - rơi ra ngoài theo logic xếp đồ thông thường
- `Mất phụ kiện tăng túi`
  - sức chứa giảm ngay

## 18. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 7

- `Repair kit có 1 slot`
  - nếu muốn lấy món sửa dở ra thì phải hủy tiến trình trước
  - nguyên liệu hoàn trả về túi
  - nếu thiếu chỗ thì phần dư rơi ra đất
- `Vị trí đặt repair kit`
  - đặt được ở bất kỳ chỗ nào cho phép xây dựng
- `Thu hồi repair kit khi bên trong còn đồ`
  - tự đẩy đồ ra đất
- `Pin / lõi mana`
  - cho phép gán vào hotbar để dùng nhanh
- `Pin / lõi mana còn charge dở`
  - cơ chế gộp hoặc nạp chéo để sau
- `Artifact có durability`
  - độ bền hao theo từng loại artifact
- `Giáp`
  - độ bền hao khác nhau giữa `hit vật lý`, `hit môi trường` và `ăn mòn đặc biệt`
- `Bia mộ`
  - UI hiển thị dạng `full lưới như rương`
- `Loot rơi đất`
  - có cơ chế tự hút vào người chơi trong bán kính gần
- `Đồ hiếm milestone`
  - stack tùy loại
  - có món có thể không stack

## 19. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 8

- `Loot tự hút`
  - có độ trễ ngắn rồi mới hút
  - áp dụng cho mọi item
- `Pin / lõi mana dùng từ hotbar`
  - nạp ngay
- `Pin / lõi mana đang còn charge`
  - hiển thị cả `thanh` và `số tuyệt đối`
- `Repair kit`
  - có độ bền riêng
- `Repair kit nếu bị phá`
  - rơi lại item kit
- `Giáp bị ăn mòn đặc biệt`
  - chỉ trừ durability
- `Artifact loại dùng mana vô hạn`
  - chỉ cần người chơi còn mana là chạy
- `Phụ kiện tăng túi`
  - nằm ở slot equipment riêng
- `Bia mộ`
  - hiển thị dạng full lưới như rương
  - giữ đúng layout từ túi người chết

## 20. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 9

- `Repair kit`
  - độ bền bị trừ theo mỗi lần `sửa / tháo`
  - ngoài ra bản thân công trình có thể có hệ hao mòn độ bền riêng để phục vụ dọn map
- `Repair kit khi bị phá`
  - nếu `thu hồi` thì rơi lại nguyên kit với độ bền còn lại
  - nếu `phá` thì rơi ra nguyên liệu chế tạo của nó, giống tháo công trình
- `Repair kit trong co-op`
  - cho người khác dùng chung
- `Artifact loại dùng mana`
  - khi người chơi hết mana thì tắt ngay
- `Artifact có durability`
  - không sửa được
- `Phụ kiện tăng túi`
  - nếu chết ở mode nặng thì rơi như item thường
- `Đồ dư khi tháo phụ kiện tăng túi`
  - rơi theo đúng thứ tự ô bị tràn
- `Loot tự hút`
  - áp dụng cả với đồ từ hotbar rơi khi chết
  - kể cả với người khác trong mode thường
- `Hotbar khi chết`
  - đã tách riêng khỏi bia mộ
  - không có layout hotbar bên trong bia mộ
- `Đồ milestone không stack`
  - nếu rơi đất nhiều món giống nhau thì hiển thị từng món riêng

## 11. Cần tinh chỉnh sau

- Số slot hotbar
- Số slot túi chính
- Stack size từng nhóm item
- Tier mapping giữa item và repair kit
- Cụ thể UI cho đồ hỏng, đồ không stack và artifact loadout
