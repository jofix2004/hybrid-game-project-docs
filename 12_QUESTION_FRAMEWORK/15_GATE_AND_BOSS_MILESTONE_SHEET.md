Project Code: HYBRID
Version: 0.9 (Draft)
Author: null
Date: 22/02/2026

# 15_GATE_AND_BOSS_MILESTONE_SHEET

Sheet này chốt cụm rule quanh `boss mốc`, `sửa gate`, `dịch chuyển ổn định` và vòng farm lại boss.

## Mục tiêu

- Tách riêng các rule milestone quan trọng khỏi ghi chú rải trong level 8.
- Chốt rõ:
  - boss giữ gate làm gì
  - gate mở ra bằng cách nào
  - dùng gate tốn gì
  - farm boss lại thì được gì và mất gì

## 1. Vai trò của Gate

- Gate không phải chỉ là cánh cổng mở khóa tuyến tính.
- Gate là:
  - mốc sửa chữa
  - tuyến đi lại ổn định
  - phần thưởng logistics dài hạn
- Khi chưa ổn định:
  - người chơi vẫn có thể lách đi sâu bằng lối phụ nguy hiểm hơn
- Khi đã ổn định:
  - chiều sâu đó trở thành tuyến đi lại có thể khai thác lâu dài hơn

## 2. Vai trò của Boss Gatekeeper

- Boss đứng ở khu gate để:
  - cản người chơi
  - đánh người chơi
  - phá tiến độ sửa gate
- Boss không chỉ là “ổ khóa sống”, mà là áp lực thật lên hành vi sửa gate

## 3. Behavior Priority of Gatekeeper Boss

- Thứ tự ưu tiên:
  1. `Đánh người chơi`
  2. `Phá gate định kỳ`
  3. `Đi loanh quanh`

### Ghi chú

- Hành vi phá gate có cooldown.
- Hành vi aggro và chi tiết AI có thể thay đổi theo từng boss.
- Có boss ngu, có boss xảo quyệt, có boss lừa người chơi, thậm chí có thực thể đặc biệt không thuần combat.

## 4. Gate Repair Flow

### Khi boss còn sống

- Người chơi vẫn có thể sửa gate từng phần.
- Nhưng boss có thể:
  - đánh người chơi
  - phá module đang sửa
  - làm mất một phần tài nguyên vừa nhét vào

### Khi boss chết

- Người chơi có cửa sổ an toàn hơn để sửa gate.
- Sửa xong thì gate trở thành tuyến ổn định.

## 5. Gate Damage Model

- Boss phá gate theo `module`, không phải chỉ trừ một thanh tiến độ trừu tượng.
- Nếu người chơi vừa nạp tài nguyên vào một module:
  - boss có thể phá và làm mất một phần tài nguyên đó

## 6. Stable Gate State

- Khi gate được sửa ổn định:
  - gate mở vĩnh viễn
- Nhưng:
  - mỗi lần dùng vẫn tốn năng lượng

## 7. Gate Energy Rules

### Nguồn ưu tiên

- `Network mana`
- `Năng lượng sẵn có của gate`
- `Mana cá nhân` chỉ bù khi thiếu

### Ý đồ thiết kế

- Gate được chuẩn bị sẵn sẽ dùng ổn định và rẻ hơn
- Gate cạn năng lượng tạo áp lực thật lên những chuyến đi chưa chuẩn bị logistics

## 8. Gate Fuel Rules

- Gate được nạp bằng:
  - vật phẩm nhiên liệu
- Nhiên liệu gate dùng chung họ với:
  - `pin`
  - `bình`
  - `lõi mana`

## 9. Cost Per Use

- Chi phí dùng gate tính theo:
  - `khoảng cách`
  - `tầng`
  - `số lần dùng`

## 10. Undercharged Gate Rules

- Gate thiếu năng lượng vẫn dùng được
- Nhưng:
  - rất đắt
  - có tỷ lệ lỗi
  - có thể làm mất mana vô ích

### Gate Failure

- Khi lỗi:
  - không dịch chuyển
  - nhưng vẫn mất năng lượng

## 11. Gate and Personal Mana Interaction

- Nếu tới hoặc qua một gate đang thiếu năng lượng:
  - gate có thể trừ mạnh hơn vào mana của cả party đứng gần cổng
- Vì vậy:
  - người chơi được khuyến khích nạp sẵn gate
  - thay vì chỉ dựa vào mana cá nhân

## 12. Boss Reset and Persistence

- Mất aggro:
  - tùy loại boss
  - có con quay lại gate
  - có con hồi máu
  - có con không hồi máu
- Nếu người chơi rời khỏi hầm ngục hoặc tầng:
  - boss reset phase hoặc reset hẳn
- Máu boss trong cùng một lần thám hiểm:
  - tùy loại boss

## 13. Boss Respawn Rules

- Boss gatekeeper chỉ hồi lại nếu:
  - người chơi chưa sửa gate xong

### Chủ động gọi lại boss

- Người chơi có thể phá gate để gọi boss lại
- Mục đích:
  - farm thêm vật liệu
- Khi phá gate:
  - gate chỉ hỏng một phần
  - sửa lại tương đối dễ

## 14. Refarm Reward Rules

- Boss gọi lại để farm:
  - chỉ rơi vật liệu farm
  - không rơi lại milestone

### Vật liệu farm tùy loại boss

- Boss thiên chiến đấu:
  - rơi vật liệu combat
- Boss dạng pháp sư hoặc ma thú:
  - rơi vật liệu phép, mana hoặc utility liên quan
- Boss dạng máy móc hoặc vật cổ:
  - rơi vật liệu chế tạo, công nghệ hoặc cấu phần đặc thù

## 15. Milestone Summary

- `Milestone thật` của boss gatekeeper là:
  - tạo khoảng an toàn để sửa gate
  - và giúp biến mốc sâu thành tuyến đi lại bền vững
- `Milestone` không nên farm lại vô hạn
- `Farm loop` chỉ nên cho vật liệu phụ trợ, không làm vỡ tiến trình chính

## 16. Cần tinh chỉnh sau

- Số module của từng loại gate
- Tốc độ boss phá gate
- Tỷ lệ mất tài nguyên khi module bị phá
- Mức tiêu hao năng lượng theo từng khoảng cách và tầng
- Tỷ lệ lỗi của gate khi thiếu năng lượng
- Số vật liệu farm và loot table chi tiết cho từng họ boss

## 17. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 1

- `Sửa gate`
  - sửa từng module độc lập hoàn toàn
- `Boss phá gate`
  - phá ngẫu nhiên một module đang có
- `Tài nguyên nhét vào gate`
  - đi vào các ô nhét item của module
  - đủ điều kiện hoặc đủ item thì module mới hoàn thành / kích hoạt được
  - có giai đoạn đang lắp nên có thể bị ngắt trước khi hoàn tất
- `Người chơi đang sửa gate mà bị hit`
  - hủy thao tác sửa ngay
- `Gate đã ổn định nhưng đói năng lượng lâu`
  - không xuống cấp vật lý
  - chủ yếu là không dùng được hoặc lỗi nhiều hơn
- `Chi phí dùng gate`
  - tính theo `khoảng cách dịch chuyển`
- `Mana cá nhân bù cho gate`
  - tự hút nếu người chơi bấm dùng gate
- `Boss gatekeeper chết rồi mà gate chưa sửa xong`
  - biến mất ngay để clear khu vực
  - bắt đầu bộ đếm hồi sinh
- `Gọi lại boss`
  - dùng công cụ đập phá công trình để phá gate
- `Loot farm từ boss gọi lại`
  - để `tùy loại boss`

## 18. Ghi chú chốt tạm thêm: vòng hỏi chi tiết 2

- `Số ô nhét item của gate`
  - tùy loại gate hoặc tùy tầng
- `Module gate đủ item`
  - tự hoàn thành ngay
- `Nhét sai item vào ô gate`
  - cho nhét nhưng không có tác dụng
- `Boss hồi sinh lại`
  - hồi đủ máu như mới
- `Bộ đếm hồi sinh boss`
  - chạy theo thời gian thực
- `Phá gate để gọi lại boss`
  - đi theo logic gần giống boss phá gate
  - làm rơi một vài nguyên liệu ở khe sửa chữa
  - khiến gate ngừng hoạt động
- `Gate lỗi khi đói năng lượng`
  - chỉ mất năng lượng mà không dịch chuyển
- `Mana cá nhân bù cho gate`
  - có thể hút từ cả party đứng gần cổng
- `Loot boss gọi lại`
  - tùy boss
- `Gate ổn định`
  - lưu trạng thái chung cho cả world vĩnh viễn
