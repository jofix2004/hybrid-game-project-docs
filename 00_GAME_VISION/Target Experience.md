Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 27/02/2026

# Target Experience

Tài liệu này chốt trải nghiệm mục tiêu mà game phải tạo ra cho người chơi qua từng nhịp: từ 10 phút đầu, buổi chơi đầu tiên, các phiên ngắn và dài, cho tới giai đoạn đi sâu hơn. Đây là lớp tài liệu dùng để kiểm tra xem gameplay loop, survival pressure, co-op và progression có đang tạo đúng cảm giác đã hứa hay không.

## Mục tiêu

- Chốt cảm giác người chơi phải có ở từng giai đoạn làm quen và chơi sâu.
- Biến các câu trả lời ở `12_QUESTION_FRAMEWORK` thành tiêu chí kiểm tra trải nghiệm thật.
- Làm rõ nhịp căng, nhịp thở, phần thưởng, mất mát và lý do quay lại.
- Giữ cho trải nghiệm thực tế khớp với `Game Pillars` và `Player Fantasy`.

## Phạm vi

Tài liệu này tập trung vào:
- cảm giác của người chơi trong 10 phút đầu
- cảm giác sau buổi chơi đầu tiên
- nhịp trải nghiệm ở giữa game và khi đi sâu hơn
- khác biệt giữa phiên ngắn và phiên dài
- hành trình cảm xúc đúng của game
- khác biệt giữa solo và co-op
- các guardrail để không làm lệch trải nghiệm mục tiêu

Tài liệu này không đi sâu vào:
- công thức hệ thống
- số liệu balance
- bảng data item hoặc enemy
- chi tiết implementation kỹ thuật

## Source Coverage

### Nguồn bắt buộc

- [05_QUESTIONS_LEVEL_1.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/05_QUESTIONS_LEVEL_1.md)
  - chốt khung `Target Experience` theo đầu game, giữa game và giai đoạn chơi sâu
  - chốt yêu cầu giữ cân bằng giữa căng thẳng và cảm giác “đi thêm một chút nữa”
- [06_QUESTIONS_LEVEL_2.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/06_QUESTIONS_LEVEL_2.md)
  - chốt `10 phút đầu`, `buổi chơi đầu tiên`, `nhịp chơi chính`, `cấu trúc phiên chơi`, `hành trình cảm xúc`
- [07_QUESTIONS_LEVEL_3.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/07_QUESTIONS_LEVEL_3.md)
  - chốt `Action Loop`, `Core Gameplay Loop`, `Short Session Loop`, `Long Progression Loop`, `Risk and Reward Loop`, `Multiplayer Loop`

### Nguồn đối chiếu bắt buộc

- [Game Pillars.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/00_GAME_VISION/Game%20Pillars.md)
  - dùng để kiểm tra trải nghiệm có còn bám đúng 5 pillar hay không
- [Player Fantasy.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/00_GAME_VISION/Player%20Fantasy.md)
  - dùng để kiểm tra cảm giác “mình đang trở thành ai” có còn nhất quán hay không

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - Trải nghiệm mục tiêu đã đủ rõ để dùng làm chuẩn cho các doc loop, core systems, progression và multiplayer.
  - Nếu một hệ thống mới làm người chơi thấy game quá căng ngay từ đầu, quá an toàn ở đoạn sâu, hoặc quá rời khỏi trục `chuẩn bị -> đi sâu -> mang về -> đi sâu hơn`, hệ đó đang đi lệch.

## Rule Summary

Trải nghiệm mục tiêu của game được chốt như sau:

1. `10 phút đầu` phải dễ chạm vào, nhiều tương tác nhỏ, tò mò nhiều hơn sợ hãi.
2. `Buổi chơi đầu tiên` phải cho người chơi hoàn thành được một vòng nhỏ trọn vẹn, nhưng hiểu rõ mình mới chỉ chạm lớp đầu.
3. `Giữa game` phải luôn có việc để làm và luôn có một lời hứa ở phía trước.
4. `Giai đoạn đi sâu` phải căng hơn rõ rệt, nhưng phần thưởng và khả năng làm chủ cũng tăng tương ứng.
5. `Phiên ngắn` vẫn phải tạo ra tiến triển thật.
6. `Phiên dài` phải đủ sức tạo ra một chuyến đi đáng nhớ.
7. `Cảm giác đỉnh` đến từ việc thoát về được với chiến lợi phẩm lớn hoặc mở được mốc mới.
8. `Cảm giác đau` đến từ việc tham thêm một chút rồi trả giá, nhưng vẫn để lại bài học và động lực quay lại.

## 1. Trải Nghiệm Trong 10 Phút Đầu

Trong 10 phút đầu, người chơi phải thấy game dễ chạm vào hơn là đáng sợ. Họ nên nhanh chóng thử được các tương tác nền như đập đá, phá bụi cỏ, nhặt vật phẩm rơi ra, ghép món cơ bản đầu tiên và hiểu rằng thế giới này phản hồi khá rõ với hành động của mình.

Cảm giác đúng ở giai đoạn này là:
- tò mò
- muốn thử thêm
- thấy liên tục có thứ để chạm vào
- nhận ra rằng bên dưới mặt đất còn có lớp nội dung sâu hơn đang chờ

Giai đoạn này không được tạo cảm giác:
- bị ép tối ưu ngay
- bị survival bóp quá sớm
- hoặc phải hiểu quá nhiều hệ thì mới chơi được

## 2. Trải Nghiệm Sau Buổi Chơi Đầu Tiên

Sau buổi chơi đầu tiên, người chơi phải có cảm giác mình đã hoàn thành được một vòng nhỏ nhưng thật:
- tìm được tài nguyên cơ bản
- chạm vào mối nguy đầu tiên
- học cách xử lý hoặc rút lui
- mang thứ gì đó có ích về
- cải thiện được công cụ, chỗ ở hoặc khả năng chuẩn bị
- và chạm vào lớp khám phá đầu tiên

Điểm quan trọng là người chơi phải vừa thấy:
- `mình đã làm được việc thật`
- vừa thấy `mình mới chỉ chạm vào lớp đầu`

Buổi đầu không cần thưởng quá lớn, nhưng phải để lại:
- một mục tiêu kế tiếp rõ ràng
- một ranh giới đầu tiên cho thấy muốn xuống sâu hơn thì phải chuẩn bị tốt hơn

## 3. Trải Nghiệm Ở Giữa Game

Ở giữa game, người chơi phải luôn có việc để làm và luôn có một lời hứa ở phía trước. Họ không chỉ farm lặp lại cho đủ số, mà phải liên tục nhìn thấy:
- tầng sâu hơn
- tài nguyên hiếm hơn
- máy tốt hơn
- tuyến đi ổn định hơn
- chuyến đi lớn hơn

Cảm giác đúng ở giữa game là:
- bận rộn nhưng có mục tiêu
- có tiến triển thật mỗi vài phiên
- đã hiểu nhịp game đủ để chủ động chuẩn bị
- bắt đầu thấy các quyết định logistics, repair, mana và chia việc có trọng lượng rõ

## 4. Trải Nghiệm Khi Đi Sâu Hơn

Khi bắt đầu đi sâu hơn, game phải tăng cảm giác căng lên rõ rệt. Tuy nhiên, đây không được là kiểu căng vô lý hoặc chỉ phạt nặng hơn. Người chơi phải luôn cảm nhận được:
- nguy hiểm tăng
- giá trị phần thưởng tăng
- sai lầm đắt hơn
- nhưng khả năng làm chủ và công cụ của mình cũng tăng theo

Đoạn sâu đúng của game là nơi:
- survival pressure rõ hơn
- đường rút đắt hơn
- loot giá trị hơn
- câu hỏi `tham hay rút` sắc hơn
- và mỗi lần trở về an toàn đều có giá trị cảm xúc cao hơn

## 5. Nhịp Chơi Chính

Nhịp chơi chuẩn của game phải vận hành như sau:

- bắt đầu từ khoảng chuẩn bị tương đối yên
- rời vùng an toàn
- tiêu hao dần tài nguyên
- chạm vào nguy hiểm
- thu được thứ có giá trị
- đối mặt câu hỏi `đi tiếp hay quay về`
- quay về vùng an toàn tương đối
- sắp xếp thành quả
- chuẩn bị cho lượt sâu hơn

Nhịp thở của game nằm ở:
- chuẩn bị
- quay về
- nhìn thấy tiến triển

Nhịp căng của game nằm ở:
- lúc túi đồ bắt đầu có giá
- lúc hồi phục mỏng dần
- lúc vừa mở ra thứ mới nhưng chưa chắc có nên tham thêm

## 6. Phiên Chơi Ngắn

Một phiên ngắn phải đủ để người chơi hoàn thành một việc nhỏ nhưng thật. Ví dụ:
- đi farm nguyên liệu gần
- hoàn thiện một mắt xích ở căn cứ
- sửa đồ và chuẩn bị loadout
- mở thêm một đoạn đường
- thử đẩy thêm một nhịp ngắn rồi rút an toàn

Cuối phiên ngắn, cảm giác đúng là:
- “mình đã tiến thêm được một nấc”

Phiên ngắn không cần cao trào lớn, nhưng không được để người chơi cảm thấy:
- online xong không làm được gì
- hoặc chỉ có thể làm việc vặt vô nghĩa

## 7. Phiên Chơi Dài

Một phiên dài phải đủ để tạo ra một chuyến đi đáng nhớ. Nó nên có khả năng chứa:
- chuẩn bị bài bản
- xuống sâu
- gặp nguy hiểm lớn
- mở tầng hoặc mốc mới
- lấy được loot hiếm
- hạ boss hoặc chạm gate
- hoặc rút lui trong tình huống rất căng

Cuối phiên dài, người chơi phải có cảm giác:
- “hôm nay có chuyện để kể”
- “cả nhóm vừa làm được việc lớn”
- “căn cứ hoặc khả năng đi tiếp đã thay đổi thấy rõ”

## 8. Hành Trình Cảm Xúc Chuẩn

Hành trình cảm xúc chuẩn của game là:

`tò mò -> dè chừng -> căng thẳng -> phấn khích khi sống sót trở về -> ám ảnh muốn xuống sâu hơn`

Ý nghĩa của từng chặng:

- `Tò mò`
  - thấy nhiều thứ để chạm vào và muốn thử
- `Dè chừng`
  - hiểu mình còn yếu, không nên coi thường thế giới
- `Căng thẳng`
  - biết mình đang lời lớn nhưng cũng đang mạo hiểm lớn
- `Phấn khích khi sống sót trở về`
  - không chỉ vì nhặt được đồ, mà vì mang được thứ đáng giá về an toàn
- `Ám ảnh muốn xuống sâu hơn`
  - cảm giác còn một lớp nội dung nữa đang đợi và mình muốn quay lại thử tiếp

## 9. Khoảnh Khắc Đỉnh Và Khoảnh Khắc Đau

Khoảnh khắc đỉnh nên đến từ:
- cả nhóm thoát về được với chiến lợi phẩm hiếm
- mở ra tầng mới
- sửa được gate
- vượt qua một mốc mà trước đó tưởng chưa thể

Khoảnh khắc đau nhưng đáng nhớ nên đến từ:
- tham thêm một chút rồi trả giá
- mất một phần thành quả vì quyết định liều
- hoặc rút lui sát nút trong trạng thái kiệt tài nguyên

Khoảnh khắc đau đúng không phải là:
- chết vô lý
- mất mát không hiểu vì sao
- hoặc bị game phạt mà không học được gì

## 10. Trải Nghiệm Solo

Solo phải chơi được và vẫn có giá trị. Trải nghiệm solo đúng là:
- rõ ràng hơn về quản lý rủi ro cá nhân
- chậm hơn trong chuẩn bị và vận chuyển
- dễ căng hơn khi phải tự xử lý mọi tình huống
- nhưng vẫn phải cho phép tiến triển thật qua phiên ngắn và phiên dài

Solo không được bị biến thành:
- chế độ phụ bị bỏ quên
- hoặc kiểu chơi mà mọi mục tiêu meaningful đều đòi co-op

## 11. Trải Nghiệm Co-op

Co-op phải làm chuyến đi:
- hiệu quả hơn
- an toàn hơn khi phối hợp tốt
- và đáng nhớ hơn về mặt cảm xúc

Co-op đúng không chỉ là cộng DPS, mà là:
- chia việc
- chia rủi ro
- bàn nhau khi nào rút
- cứu nhau
- và cùng chịu sức nặng của quyết định lớn

Trải nghiệm co-op mạnh nhất là khi:
- mọi người thấy mình có ích
- chuyến đi tốt hơn vì có nhau
- và thành công hay thất bại đều để lại câu chuyện chung

## 12. Vai Trò Của Mana Trong Trải Nghiệm Mục Tiêu

Mana không nên là thứ làm lệch trải nghiệm đầu game thành fantasy caster. Trong target experience, mana nên xuất hiện theo hướng:

- đầu game: chỉ mới hé lộ là lớp utility và năng lượng quan trọng
- giữa game: bắt đầu ảnh hưởng rõ tới chuẩn bị, vận hành, tool và chuyến đi
- game sâu hơn: trở thành lớp hậu cần và khuếch đại năng lực đi xa, nhưng vẫn không thay survival pressure làm lõi

Nếu ở bất kỳ giai đoạn nào người chơi thấy:
- combat phép là lõi duy nhất
- hoặc mana làm biến mất áp lực survival

thì trải nghiệm đang bị lệch khỏi mục tiêu.

## 13. Dấu Hiệu Trải Nghiệm Đang Đúng

Trải nghiệm được xem là đúng nếu người chơi thường có các cảm giác hoặc câu nói kiểu:

- “vào cái là có thứ để làm ngay”
- “mới buổi đầu mà đã thấy còn cả đống thứ chưa mở”
- “đi thêm một chút nữa thì lời thật, nhưng cũng dễ chết”
- “mang được đống này về là quá đã”
- “lần sau chuẩn bị tốt hơn thì xuống sâu hơn được”
- “đi cùng nhau rõ ràng hiệu quả hơn”
- “hôm nay có một chuyến đi đáng nhớ”

## 14. Guardrail

Không được để `Target Experience` trượt sang các hướng sau:

- đầu game quá nặng survival, làm người chơi chưa kịp tò mò đã bị bóp
- giữa game chỉ còn farm lặp lại mà không có lời hứa mới ở phía trước
- đoạn sâu chỉ tăng số chứ không tăng cảm giác làm chủ và giá trị phần thưởng
- phiên ngắn không tạo ra tiến triển thật
- phiên dài không tạo ra câu chuyện đáng kể
- co-op chỉ là nhiều người cùng cày riêng lẻ
- mana cướp vai trò của survival và logistics

## 15. Cách Dùng Target Experience Để Duyệt Feature

Khi đánh giá một feature mới, phải trả lời được:

1. Feature này phục vụ giai đoạn trải nghiệm nào.
2. Nó làm tăng tò mò, tăng chiều sâu, tăng áp lực hay tăng phần thưởng ở đâu.
3. Nó làm phiên ngắn hoặc phiên dài tốt hơn theo cách nào.
4. Nó có làm câu hỏi `đi tiếp hay quay về` sắc hơn hay làm nó nhạt đi.
5. Nó có giúp solo/co-op giàu trải nghiệm hơn hay chỉ làm hệ thống phình ra.

Nếu không trả lời được các câu trên, feature đó chưa đủ rõ để vào core scope.

## Open Design Questions

- Hiện chưa có câu hỏi mở bắt buộc ở cấp `Target Experience`.
- Nếu sau này xuất hiện mode chơi mới hoặc cấu trúc phiên chơi mới, phải rà lại doc này trước khi nhận vào core.

## Open Balance Variables

Ở cấp trải nghiệm mục tiêu, chưa khóa số balance cụ thể.

Các tài liệu sau cần hiện thực hóa doc này bằng rule và data:
- `Core Gameplay Loop`
- `Short Session Loop`
- `Long Progression Loop`
- `Risk and Reward`
- `Multiplayer Loop`
- `Survival System`
- `Player Progression`
