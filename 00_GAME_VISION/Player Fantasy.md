Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 25/02/2026

# Player Fantasy

Tài liệu này chốt fantasy trung tâm của người chơi trong game: người chơi tin rằng mình đang trở thành ai, giỏi ở điều gì, và tại sao hành trình đó đáng để tiếp tục.

## Mục tiêu

- Chốt fantasy trung tâm để các hệ thống sau này không làm lệch vai trò người chơi.
- Làm rõ cảm giác làm chủ của người chơi qua từng giai đoạn.
- Tách rõ fantasy này khỏi các fantasy dễ gây lệch lõi game.

## Phạm vi

Tài liệu này tập trung vào:
- vai trò người chơi
- hành trình biến đổi của người chơi
- cảm giác “giỏi” mà game phải tạo ra
- quan hệ giữa fantasy này với co-op, survival, chiều sâu và mana

Tài liệu này không đi sâu vào:
- class system
- combat build chi tiết
- lore hoặc cốt truyện tuyến tính

## Source Coverage

### Nguồn bắt buộc

- [04_QUESTIONS_LEVEL_0.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/04_QUESTIONS_LEVEL_0.md)
  - chốt fantasy gốc: từ tay trắng thành nhóm sống sót lão luyện
  - chốt cảm giác “giỏi” là giỏi sống sót, giỏi đọc tình huống, giỏi phối hợp, giỏi mang tài nguyên về an toàn và giỏi đi sâu hơn
- [05_QUESTIONS_LEVEL_1.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/05_QUESTIONS_LEVEL_1.md)
  - chốt bản văn fantasy trung tâm
  - chốt người chơi không phải anh hùng được chọn sẵn
  - chốt khác biệt giữa đóng góp build và class cứng
- [06_QUESTIONS_LEVEL_2.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/06_QUESTIONS_LEVEL_2.md)
  - cung cấp hành trình cảm xúc thực tế khi chơi
  - chỉ ra vì sao người chơi muốn quay lại và tiếp tục đi sâu

### Nguồn bổ trợ

- [07_QUESTIONS_LEVEL_3.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/07_QUESTIONS_LEVEL_3.md)
  - dùng để kiểm tra fantasy này có thật sự bám vào loop hành động và loop tiến trình hay không

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - Fantasy trung tâm đã đủ rõ để dùng làm chuẩn cho progression, co-op, survival và itemization.
  - Nếu một hệ thống mới khiến người chơi cảm thấy mình đang trở thành “pháp sư combat thuần”, “anh hùng tuyến tính” hoặc “ông chủ sandbox rời rạc”, hệ đó đang đi lệch.

## Rule Summary

Fantasy trung tâm của game là:
- người chơi bắt đầu từ con số 0
- không phải anh hùng được định sẵn
- phải tự tạo cơ hội sống sót cho mình và cho nhóm
- dần trở thành những người thám hiểm thế giới ngầm lão luyện
- biết chuẩn bị, biết phối hợp, biết đọc nguy hiểm và biết mang chiến lợi phẩm về an toàn

Game không xây fantasy theo hướng:
- anh hùng cứu thế
- pháp sư thuần phép
- hoặc sandbox builder thuần xây dựng

## 1. Người Chơi Đang Là Ai

Người chơi không phải là một nhân vật “được chọn”.

Họ là:
- người sống sót
- bắt đầu tay trắng
- yếu, thiếu, và chưa có quyền kiểm soát thế giới

Điều quan trọng là:
- giá trị của người chơi không đến từ danh tính sẵn có
- mà đến từ những gì họ làm được cùng đồng đội, những gì họ sống sót qua, và những gì họ mang về được

## 2. Người Chơi Đang Trở Thành Ai

Fantasy đúng của game là một hành trình biến đổi:

### Giai đoạn đầu

Người chơi là:
- người mới chạm vào thế giới
- tò mò nhưng dè chừng
- sống bằng phản xạ cơ bản, nhặt nhạnh, thử sai và học luật chơi

### Giai đoạn giữa

Người chơi trở thành:
- người biết chuẩn bị
- biết chia việc
- biết đọc nguy hiểm
- biết đánh đổi rủi ro với phần thưởng

### Giai đoạn sâu hơn

Người chơi trở thành:
- thành viên của một nhóm thám hiểm thế giới ngầm lão luyện
- biết vận hành hậu cần
- biết tổ chức chuyến đi
- biết dùng các lớp công cụ, mana và công trình để đi xa hơn người mới rất nhiều

Nói ngắn gọn:
- từ `kẻ tay trắng`
- thành `người sống sót có kinh nghiệm`
- rồi thành `nhóm thám hiểm chiều sâu có tổ chức`

## 3. Cảm Giác “Giỏi” Mà Game Phải Tạo Ra

Game này không nên khiến người chơi cảm thấy mình “giỏi” vì:
- tung kỹ năng đẹp mắt
- combo phức tạp
- hoặc có class mạnh hơn người khác

Game này nên khiến người chơi cảm thấy mình “giỏi” vì:
- giỏi sống sót lâu
- giỏi đọc tình huống
- giỏi biết khi nào nên tham, khi nào nên rút
- giỏi chuẩn bị trước chuyến đi
- giỏi phối hợp với đồng đội
- giỏi mang thứ quý về an toàn
- giỏi đẩy được chuyến đi sâu hơn mỗi lần chơi

Đây là fantasy của:
- competence
- discipline
- và collective survival

không phải fantasy của power trip thuần túy.

## 4. Quan Hệ Giữa Fantasy Và Co-op

Co-op không phải phần cộng thêm cho fantasy này. Co-op là nơi fantasy đó đạt hình thái mạnh nhất.

Trong co-op, người chơi phải cảm thấy:
- mình có ích
- mình đang gánh một phần của chuyến đi
- thành công của nhóm có phần của mình trong đó

Fantasy chuẩn của game không phải:
- “mỗi người là một siêu anh hùng riêng”

mà là:
- “cả nhóm đang giỏi dần lên cùng nhau”

Điều này cho phép:
- vai trò tự nhiên nổi lên
- build khác nhau vẫn cùng tồn tại
- nhưng không cần khóa class cứng quá sớm

## 5. Quan Hệ Giữa Fantasy Và Sinh Tồn

Fantasy này chỉ hoạt động nếu sinh tồn có áp lực thật.

Nếu sống sót quá dễ:
- người chơi không còn cảm giác “mình đã khéo léo đưa được cả nhóm qua”

Nếu hình phạt quá nặng và vô lý:
- người chơi không còn cảm giác làm chủ
- mà chỉ còn cảm giác bị game bóp

Vì vậy fantasy đúng nằm ở giữa:
- đủ khắc nghiệt để thành tích có giá
- đủ công bằng để người chơi tin mình có thể giỏi lên thật

## 6. Quan Hệ Giữa Fantasy Và Chiều Sâu

Người chơi không chỉ sống sót để tồn tại.
Người chơi sống sót để:
- xuống sâu hơn
- thấy thứ mới
- mở mốc mới
- và chứng minh mình đã sẵn sàng cho lớp nguy hiểm tiếp theo

Fantasy vì thế gắn chặt với:
- hành trình chiều sâu
- không gian ngầm
- và lời hứa rằng bên dưới còn thứ đáng để liều hơn nữa

Nếu game mất động cơ đi sâu:
- fantasy này cũng mất trục chính

## 7. Quan Hệ Giữa Fantasy Và Mana

Mana là lớp làm fantasy này đặc biệt hơn, nhưng không được phép thay đổi bản chất của nó.

Người chơi không nên cảm thấy:
- “mình là pháp sư combat thuần”

Người chơi nên cảm thấy:
- “mình đang học cách sử dụng một lớp năng lượng nguy hiểm và quý giá để sống sót tốt hơn, vận hành tốt hơn, đi xa hơn”

Mana đúng nghĩa là:
- công cụ khuếch đại sinh tồn
- khuếch đại utility
- khuếch đại logistics
- khuếch đại khả năng đi sâu

không phải lớp nhận diện duy nhất của nhân vật.

## 8. Fantasy Không Được Là Gì

Để tránh lệch lõi, game không được đẩy người chơi vào các fantasy sau như fantasy trung tâm:

### 8.1. Anh hùng được chọn

Không nên có cảm giác:
- người chơi đặc biệt vì cốt truyện chọn sẵn

Fantasy đúng là:
- tự gây dựng năng lực từ tay trắng

### 8.2. Pháp sư thuần chiến đấu

Không nên có cảm giác:
- mana tồn tại chủ yếu để spam skill đẹp

Fantasy đúng là:
- mana là lớp năng lượng làm nhóm sống sót và đi sâu tốt hơn

### 8.3. Nhà xây dựng sandbox thuần túy

Không nên có cảm giác:
- thế giới chỉ là nơi để decor, build tự do và mở rộng vô hạn

Fantasy đúng là:
- mọi thứ xây dựng đều phục vụ cho hành trình sống sót và xuống sâu

### 8.4. Kẻ solo thống trị tuyệt đối

Solo phải chơi được, nhưng fantasy trung tâm không được viết xoay quanh:
- một cá nhân tự cân hết mọi thứ dễ dàng

Fantasy chuẩn vẫn nghiêng về:
- nhóm người sống sót học cách phối hợp

## 9. Dấu Hiệu Fantasy Đang Đúng

Fantasy được xem là đang vận hành đúng nếu người chơi thường nói hoặc cảm thấy các điều sau:

- “Nhóm mình hôm nay đi bài bản hơn”
- “Lần này mình biết lúc nào nên rút”
- “Mang được đống này về là quá lời”
- “Tầng dưới đúng là không còn như tầng trên”
- “Có chuẩn bị nên chuyến này nhẹ hơn hẳn”
- “Thiếu mình thì chuyến này khó hơn”

Nếu người chơi chủ yếu chỉ cảm thấy:
- “skill này mạnh quá”
- “build này đè số”
- “cứ lao tiếp thôi, chết cũng không sao”

thì fantasy trung tâm đang bị lệch.

## 10. Cách Dùng Fantasy Này Để Duyệt Feature

Khi đánh giá một hệ mới, phải hỏi:

1. Hệ này làm người chơi cảm thấy mình giỏi ở kiểu gì.
2. Kiểu “giỏi” đó có đúng với fantasy đã khóa không.
3. Hệ này làm co-op và chiều sâu mạnh hơn hay yếu đi.
4. Hệ này có đẩy người chơi sang fantasy sai như caster thuần, hero tuyến tính hoặc sandbox builder thuần không.

Nếu không trả lời được 4 câu này, chưa nên nhận feature đó vào core.

## Open Design Questions

- Hiện chưa có câu hỏi mở bắt buộc ở cấp fantasy.
- Nếu sau này xuất hiện system class, faction hoặc story campaign mạnh, phải rà lại doc này trước.

## Open Balance Variables

Ở cấp fantasy, chưa khóa số balance.

Các tài liệu sau cần hiện thực fantasy này bằng rule cụ thể:
- `Target Experience`
- `Core Gameplay Loop`
- `Player Stats`
- `Player Progression`
- `Survival System`
- `Player Revive`
