Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 24/02/2026

# Game Pillars

Tài liệu này chốt các trụ cột thiết kế cốt lõi của game. Đây là lớp định hướng dùng để kiểm tra xem một tính năng mới có đang nuôi đúng bản sắc game hay đang làm lệch lõi.

## Mục tiêu

- Chốt các pillar không được phép lệch trong suốt quá trình phát triển.
- Biến các câu trả lời ở `Question Framework` thành tiêu chí đánh giá feature thật.
- Làm rõ vì sao mỗi pillar tồn tại và nó phải xuất hiện trong gameplay như thế nào.

## Phạm vi

Tài liệu này chỉ chốt:
- các trụ cột thiết kế cấp vision
- ý nghĩa của từng trụ cột
- biểu hiện của trụ cột trong gameplay
- các giới hạn để không làm lệch pillar

Tài liệu này không đi sâu vào:
- công thức hệ thống
- schema data
- số liệu balance

## Source Coverage

### Nguồn bắt buộc

- [04_QUESTIONS_LEVEL_0.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/04_QUESTIONS_LEVEL_0.md)
  - khóa hạt giống của game, fantasy trung tâm, trục co-op survival và chiều sâu
- [05_QUESTIONS_LEVEL_1.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/05_QUESTIONS_LEVEL_1.md)
  - đã chốt sơ bộ `Game Pillars`, `Player Fantasy`, `USP` và các ranh giới bản sắc
- [06_QUESTIONS_LEVEL_2.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/06_QUESTIONS_LEVEL_2.md)
  - cung cấp lớp cảm xúc, nhịp trải nghiệm, risk/reward và lý do quay lại

### Nguồn bổ trợ

- [07_QUESTIONS_LEVEL_3.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/07_QUESTIONS_LEVEL_3.md)
  - dùng để kiểm tra pillar có thật sự nuôi được gameplay loop hay không

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - Các pillar dưới đây đã đủ chắc để dùng làm tiêu chí duyệt feature.
  - Nếu một hệ thống mới đi ngược một pillar, phải sửa hệ thống đó trước khi tiếp tục mở rộng.

## Rule Summary

Game này được xây trên 5 pillar:
1. `Co-op tạo giá trị thật`
2. `Sinh tồn có áp lực thật`
3. `Khám phá chiều sâu là động cơ chính`
4. `Tích lũy và chuẩn bị để đi xa hơn`
5. `Mana là lớp khuếch đại, không cướp lõi survival`

Nếu một ý tưởng mới không nuôi được ít nhất 1 pillar, và đặc biệt nếu nó làm yếu đi 1 pillar hiện có, thì không nên xem đó là core feature.

## Pillar 1: Co-op Tạo Giá Trị Thật

### Ý nghĩa

Co-op không chỉ là “cho nhiều người cùng vào một map”, mà là lõi trải nghiệm. Niềm vui lớn nhất của game phải đến từ việc:
- chia việc
- cứu nhau
- kéo nhau qua rủi ro
- và cùng mang chiến lợi phẩm về an toàn

### Biểu hiện trong gameplay

- Người chơi đi cùng nhau thì hiệu quả hơn, an toàn hơn và đáng nhớ hơn.
- Mỗi người có thể đóng góp khác nhau mà không cần khóa class cứng quá sớm.
- Các quyết định lớn như `đi tiếp hay rút`, `cứu người hay bỏ vị trí`, `chia đồ thế nào`, `mang gì về trước` đều có giá trị hơn khi có đồng đội.

### Dấu hiệu đúng

- Một chuyến đi co-op tạo ra nhiều câu chuyện hơn solo.
- Người chơi cảm thấy “mình có ích” cho cả nhóm.
- Thất bại trong co-op tạo ra drama và bài học, không chỉ là mất đồ đơn lẻ.

### Guardrail

Không được làm co-op thành:
- chỉ là solo nhưng nhiều người cùng farm
- chỉ là cộng thêm DPS
- hoặc chỉ là “cho vui” mà không tạo quyết định chung

## Pillar 2: Sinh Tồn Có Áp Lực Thật

### Ý nghĩa

Game phải luôn cho cảm giác người chơi đang đánh đổi giữa:
- an toàn
- phần thưởng
- và khả năng quay về

Sinh tồn không chỉ là thanh hiển thị, mà phải là thứ ảnh hưởng trực tiếp tới quyết định.

### Biểu hiện trong gameplay

- Đói, kiệt đói, hồi phục, thiếu mana, mất đồ, hỏng đồ và chi phí chuyến đi đều tạo áp lực thật.
- Người chơi có thể thất bại chỉ vì tham quá lâu ngoài field.
- Chuẩn bị trước chuyến đi quan trọng gần ngang với lúc đang đi.

### Dấu hiệu đúng

- Người chơi luôn phải cân nhắc `đi tiếp hay quay về`.
- Mất mát có ý nghĩa, nhưng chưa tới mức bóp chết động lực chơi tiếp.
- Một chuyến đi thành công phải đem lại cảm giác “thoát về được là thắng”.

### Guardrail

Không được làm sinh tồn thành:
- lớp trang trí chỉ để tăng icon trên UI
- một debuff nhẹ không đủ ảnh hưởng quyết định
- hoặc một hình phạt vô lý khiến game mất đường phục hồi

## Pillar 3: Khám Phá Chiều Sâu Là Động Cơ Chính

### Ý nghĩa

Điều hấp dẫn nhất của game không nằm ở độ rộng sandbox, mà nằm ở chiều sâu. Người chơi phải luôn cảm thấy:
- bên dưới còn thứ mới
- càng xuống sâu càng đáng giá
- và mỗi tầng mới là một nấc mở thật sự

### Biểu hiện trong gameplay

- Đi sâu hơn mở ra môi trường mới, tài nguyên mới, đe dọa mới, sinh vật mới và milestone mới.
- Boss, gate và các điểm mốc sâu không chỉ là chướng ngại, mà là bước chuyển trạng thái của thế giới chơi.
- Progression phải bám vào chiều sâu, không bị lệch thành farm vặt vô hướng.

### Dấu hiệu đúng

- Người chơi luôn có một lời hứa rõ ở phía trước.
- Mỗi lần xuống sâu hơn, phần thưởng và rủi ro đều tăng rõ.
- Tầng mới làm thay đổi cách chuẩn bị, không chỉ thay đổi số.

### Guardrail

Không được làm game thành:
- sandbox rộng nhưng không có động lực xuống sâu
- hệ mở khóa tuyến tính rời rạc với hầm ngục
- hoặc chiều sâu chỉ là “reskin map” mà không đổi giá trị gameplay

## Pillar 4: Tích Lũy Và Chuẩn Bị Để Đi Xa Hơn

### Ý nghĩa

Người chơi không ra ngoài chỉ để sống qua ngày, mà để mang thứ có giá trị về và biến nó thành năng lực cho chuyến đi sau.

Pillar này giữ cho loop có nhịp:
- chuẩn bị
- mạo hiểm
- trở về
- nâng cấp
- quay lại sâu hơn

### Biểu hiện trong gameplay

- Loot mang về phải đổi được thành công cụ tốt hơn, căn cứ tốt hơn, utility tốt hơn, tuyến đi ổn định hơn hoặc khả năng chịu rủi ro cao hơn.
- Một phiên ngắn vẫn phải có tiến bộ thật.
- Một phiên dài phải có cảm giác “hôm nay đã đẩy được cả hệ tiến lên”.

### Dấu hiệu đúng

- Người chơi thấy rõ mối liên hệ giữa `mang được gì về` và `lần sau đi sâu được bao nhiêu`.
- Chuẩn bị trước chuyến đi không bị cảm giác lãng phí thời gian.
- Base, tool, repair, fuel, item dự trữ và milestone đều gắn vào một đường dây tiến bộ chung.

### Guardrail

Không được làm progression thành:
- chỉ là tăng số vô nghĩa
- chỉ là unlock menu
- hoặc biến phần về base thành khoảng chết không có giá trị

## Pillar 5: Mana Là Lớp Khuếch Đại, Không Cướp Lõi Survival

### Ý nghĩa

Mana và ma thuật là điểm khác biệt quan trọng của game, nhưng nó không được phép nuốt mất lõi survival. Mana phải đóng vai trò:
- nguồn năng lượng
- lớp utility
- lớp khuếch đại khai thác, vận hành và logistic

chứ không biến game thành fantasy caster thuần túy.

### Biểu hiện trong gameplay

- Mana xuất hiện sớm như một lớp năng lượng quan trọng của thế giới.
- Mana hỗ trợ tool, utility, machine, network và gate.
- Mana cá nhân là nguồn cơ động nhỏ; mana base và infrastructure mới là nguồn lớn.
- Người chơi càng đi sâu càng thấy mana quan trọng hơn trong vận hành cả chuyến đi.

### Dấu hiệu đúng

- Mana làm game mới hơn, không làm game lệch khỏi survival co-op.
- Hệ mana mở ra khả năng chuẩn bị và hậu cần, không chỉ thêm nút skill.
- Gate, máy, pin, lõi và quặng mana nối được với loop chính.

### Guardrail

Không được làm mana thành:
- thanh phép tự hồi vô nghĩa
- lớp fantasy chiến đấu áp đảo mọi hệ còn lại
- hoặc một tài nguyên chỉ tồn tại để “cho có chất ma thuật”

## Quan Hệ Giữa Các Pillar

5 pillar này không tách rời nhau:

- `Co-op` làm cho `sinh tồn` nặng hơn về quyết định và giàu hơn về cảm xúc.
- `Sinh tồn` làm cho `khám phá chiều sâu` có giá.
- `Chiều sâu` làm cho `tích lũy và chuẩn bị` có ý nghĩa.
- `Mana` làm giàu thêm cho toàn bộ vòng lặp nhưng không được thay thế lõi cũ.

Nếu một thiết kế mới chỉ mạnh ở 1 pillar nhưng làm yếu 2 pillar còn lại, nó không phù hợp với hướng game.

## Cách Dùng Pillars Để Duyệt Feature

Khi đánh giá một feature mới, phải trả lời 4 câu:

1. Feature này nuôi pillar nào là chính.
2. Feature này có làm yếu pillar nào đang có không.
3. Feature này xuất hiện được trong gameplay thật hay chỉ đẹp trên giấy.
4. Feature này có làm game rộng hơn nhưng nông hơn không.

Nếu không trả lời được 4 câu trên, feature chưa nên vào core scope.

## Những Điều Không Được Làm

- Không biến game thành sandbox ôm quá nhiều thứ rời rạc.
- Không để các hệ phụ làm loãng trục survival co-op và khám phá chiều sâu.
- Không đẩy game thành combat fantasy thuần phép.
- Không để co-op chỉ còn vai trò “chơi cùng cho đông”.
- Không biến progression thành mở khóa menu mà không gắn với chuyến đi thật.

## Open Design Questions

- Chưa có câu hỏi mở bắt buộc ở cấp pillar hiện tại.
- Nếu sau này xuất hiện một hệ lớn mới như PvP, faction hoặc story campaign, phải rà lại toàn bộ 5 pillar này trước khi nhận vào lõi game.

## Open Balance Variables

Ở cấp pillar, chưa đặt số balance cụ thể.

Thứ cần khóa ở các doc sau:
- mức nặng thực tế của mất mát
- nhịp reward theo chiều sâu
- vai trò mana trong từng phase tiến trình
- ngưỡng mà co-op bắt đầu vượt solo rõ rệt
