Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 01/03/2026

# Core Gameplay Loop

Tài liệu này chốt vòng lặp gameplay cốt lõi mà người chơi sẽ lặp lại xuyên suốt game. Đây là lớp nối trực tiếp giữa `00_GAME_VISION` và các tài liệu hệ thống ở các thư mục sau, nên phải đủ rõ để designer, dev và QA cùng hiểu game vận hành quanh trục nào.

## Mục tiêu

- Chốt vòng lặp chơi cốt lõi mà game muốn người chơi lặp đi lặp lại.
- Làm rõ điểm bắt đầu, điểm leo thang áp lực, điểm quyết định và điểm quay về của mỗi chuyến đi.
- Chỉ ra cái giá phải trả để bắt đầu một chuyến đi, cái giá của thất bại, và phần thưởng của việc quay về an toàn.
- Tạo nền cho các doc tiếp theo như `Short Session Loop`, `Long Progression Loop`, `Survival System`, `Player Progression`, `Dungeon Progression` và `Multiplayer Loop`.

## Phạm vi

Tài liệu này tập trung vào:
- vòng lặp cốt lõi từ lúc chuẩn bị ở vùng an toàn tới lúc quay về và chuyển chiến lợi phẩm thành năng lực mới
- vai trò của quyết định `đi tiếp hay quay về`
- quan hệ giữa survival pressure, resource flow, co-op value và chiều sâu
- entry cost, reward, fail cost và đường phục hồi cơ bản

Tài liệu này không đi sâu vào:
- công thức combat, durability, mana consumption
- logic chi tiết của inventory, revive, gate hay boss
- số balance cụ thể cho mỗi chặng

## Source Coverage

### Nguồn bắt buộc

- [05_QUESTIONS_LEVEL_1.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/05_QUESTIONS_LEVEL_1.md)
  - khóa bản sắc gameplay, trục survival co-op, chiều sâu, mục tiêu quay về với chiến lợi phẩm
- [06_QUESTIONS_LEVEL_2.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/06_QUESTIONS_LEVEL_2.md)
  - khóa 10 phút đầu, buổi chơi đầu, nhịp áp lực - hồi phục, cấu trúc phiên ngắn/dài, hành trình cảm xúc
- [07_QUESTIONS_LEVEL_3.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/07_QUESTIONS_LEVEL_3.md)
  - là nguồn chốt trực tiếp cho `Action Loop`, `Core Gameplay Loop`, `Short Session Loop`, `Long Progression Loop`, `Risk and Reward Loop`, `Multiplayer Loop`
- [08_QUESTIONS_LEVEL_4.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/08_QUESTIONS_LEVEL_4.md)
  - xác nhận vai trò thực của `Survival`, `Resource/Gathering`, `Crafting/Building`, `Combat`, `Progression`, `Open Cave Depth Structure` và `Multiplayer Support` trong loop chính

### Nguồn hỗ trợ

- [02_CONTENT_MAP.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/02_CONTENT_MAP.md)
  - dùng để xác nhận `Core Gameplay Loop` là nhóm nội dung bắt đầu từ level 2 và đi sâu tới level 4
- [03_USAGE_ROADMAP.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/03_USAGE_ROADMAP.md)
  - dùng để xác nhận doc này thuộc chặng `dựng bộ khung gameplay`

### Nguồn đối chiếu bắt buộc

- [Core Concept.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/00_GAME_VISION/Core%20Concept.md)
  - dùng để giữ đúng trục `survival co-op theo chiều sâu` trên đảo hoang với style `low-tech steampunk magitech`
- [Game Pillars.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/00_GAME_VISION/Game%20Pillars.md)
  - dùng để kiểm tra loop có tiếp tục nuôi đúng 5 pillar đã khóa hay không
- [Target Experience.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/00_GAME_VISION/Target%20Experience.md)
  - dùng để kiểm tra loop có sinh ra đúng cảm giác `chuẩn bị -> mạo hiểm -> thoát về -> muốn đi tiếp` hay không

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - Hình dạng của loop đã đủ rõ để làm nguồn đúng cho các doc loop khác và các system doc liên quan.
  - Các số cụ thể như thời lượng, tỷ lệ lời/lỗ, ngưỡng tài nguyên an toàn vẫn thuộc lớp balance về sau.

## Conflict Resolution

- Không có xung đột cứng giữa các nguồn bắt buộc.
- `Level 1` và `Level 2` định nghĩa loop theo góc nhìn cảm xúc và lời hứa trải nghiệm.
- `Level 3` cung cấp hình dạng loop chuẩn bằng chữ và sơ đồ mũi tên.
- `Level 4` xác nhận các hệ nào là bắt buộc để loop đó đứng vững.
- Khi cần ưu tiên diễn giải, tài liệu này lấy `Level 3` làm xương sống của loop, rồi dùng `Level 1`, `Level 2` và `Level 4` để bổ sung vai trò, áp lực và giới hạn.

## Rule Summary

- Vòng lặp cốt lõi của game là: `chuẩn bị -> đi ra ngoài -> thu thập/khai thác/đối phó nguy hiểm -> quyết định tham hay rút -> mang chiến lợi phẩm về -> đổi chiến lợi phẩm thành khả năng sống sót và đi sâu hơn -> lặp lại`.
- Người chơi không ra ngoài chỉ để sống qua ngày, mà để lấy thứ mình chưa có, mở thứ mình chưa chạm tới, rồi dùng nó làm bàn đạp cho chuyến sau.
- Giá trị của loop nằm ở chỗ càng đi xa hoặc xuống sâu, phần thưởng càng lớn nhưng đường lui càng đắt.
- Câu hỏi trung tâm của mỗi chuyến đi luôn là `đi tiếp hay quay về`.
- Quay về không phải là kết thúc nhịp chơi, mà là giai đoạn chuyển loot thành năng lực mới: tool, repair, dự trữ, utility, machine, base upgrade, gate progress hoặc chuẩn bị cho chuyến tiếp theo.
- Thất bại phải đủ đau để giữ trọng lượng cho chuyến đi, nhưng luôn để lại đường phục hồi để vòng lặp không gãy.

## State List

### 1. Vùng An Toàn Tương Đối

Người chơi đang ở căn cứ hoặc khu vực đủ an toàn để:
- cất đồ
- sửa đồ
- craft
- hồi phục
- bàn kế hoạch
- chia tài nguyên

### 2. Chuẩn Bị Chuyến Đi

Người chơi bắt đầu chuyển từ trạng thái an toàn sang trạng thái mạo hiểm bằng việc:
- kiểm tra tool, weapon, armor, artifact
- mang đồ ăn, đồ hồi, fuel, mana item, utility cần thiết
- quyết định mục tiêu chuyến đi
- quyết định đi một mình hay đi cùng ai, nếu là co-op

### 3. Đi Ra Ngoài

Người chơi rời vùng an toàn và bước vào field run hiện tại:
- khoảng cách với căn cứ tăng lên
- chi phí rút lui bắt đầu hình thành
- nhịp survival pressure bắt đầu có ý nghĩa

### 4. Khai Thác Và Thám Hiểm

Người chơi:
- quan sát
- nhặt
- khai thác
- mở đường
- dò mối nguy
- xử lý hoặc né combat
- tích lũy giá trị trong túi đồ

### 5. Leo Thang Áp Lực

Sau một thời gian ở ngoài field, áp lực tăng lên do:
- tài nguyên hồi phục mỏng dần
- durability giảm
- máu/mana/food trở nên quan trọng hơn
- loot trong túi ngày càng có giá trị
- đường lui ngày càng dài hoặc nguy hiểm hơn
- độ sâu hoặc độ xa ngày càng lớn

### 6. Quyết Định Bước Tiếp

Người chơi hoặc cả nhóm phải chọn:
- đi tiếp để lấy thêm giá trị
- chạm mốc lớn hơn
- hay rút về để khóa lợi nhuận hiện tại

### 7. Trở Về Và Trích Xuất Giá Trị

Người chơi quay về an toàn tương đối và:
- cất loot
- sửa đồ
- hồi phục
- craft
- nâng cấp base hoặc infrastructure
- chuẩn bị mục tiêu mới

### 8. Sẵn Sàng Cho Chuyến Sau

Chiến lợi phẩm của chuyến trước đã được đổi thành:
- năng lực sống sót cao hơn
- năng lực logistic tốt hơn
- khả năng đi sâu hơn
- hoặc mục tiêu mới rõ hơn

Loop sau đó lặp lại ở một lớp nguy hiểm hoặc giá trị cao hơn.

## Transition Rules

### Vùng An Toàn Tương Đối -> Chuẩn Bị Chuyến Đi

Xảy ra khi người chơi:
- có mục tiêu cụ thể cho chuyến đi
- bắt đầu chọn loadout, tool, tài nguyên mang theo
- hoặc bắt đầu tổ chức party cho một run mới

### Chuẩn Bị Chuyến Đi -> Đi Ra Ngoài

Xảy ra khi người chơi:
- rời căn cứ hoặc khu an toàn
- chấp nhận entry cost của một run mới
- và không còn ở trạng thái chỉ sắp xếp hậu cần

### Đi Ra Ngoài -> Khai Thác Và Thám Hiểm

Xảy ra ngay khi người chơi bắt đầu:
- tương tác với môi trường
- nhặt/khai thác tài nguyên
- mở lối
- chạm vào nguy hiểm đầu tiên

### Khai Thác Và Thám Hiểm -> Leo Thang Áp Lực

Xảy ra dần theo:
- thời gian ở ngoài field
- độ sâu hoặc độ xa
- giá trị loot đang mang
- lượng tài nguyên hồi phục còn lại
- trạng thái hiện tại của đội

### Leo Thang Áp Lực -> Quyết Định Bước Tiếp

Xảy ra khi người chơi đủ thông tin để thấy rõ:
- nếu đi tiếp thì lời hơn
- nhưng nếu chết hoặc hỏng run thì mất cũng đau hơn

### Quyết Định Bước Tiếp -> Khai Thác Và Thám Hiểm

Xảy ra khi người chơi chọn:
- đi tiếp
- xuống sâu hơn
- hoặc đẩy thêm một đoạn nữa

Loop này quay lại nhưng ở mức áp lực cao hơn trước.

### Quyết Định Bước Tiếp -> Trở Về Và Trích Xuất Giá Trị

Xảy ra khi người chơi chọn:
- rút lui
- quay về căn cứ
- hoặc chốt lời ở mức an toàn hiện tại

### Trở Về Và Trích Xuất Giá Trị -> Sẵn Sàng Cho Chuyến Sau

Xảy ra khi loot đã được chuyển thành:
- đồ dùng được
- dự trữ
- repair
- nâng cấp
- hoặc điều kiện đi tiếp

### Bất Kỳ Trạng Thái Field Nào -> Failure and Recovery

Xảy ra khi:
- người chơi chết
- cả đội wipe
- phải bỏ dở run với thiệt hại đáng kể
- hoặc quay về trong trạng thái lỗ nặng so với kỳ vọng

## Entry Cost, Reward, And Fail Cost

### Entry Cost

Mỗi chuyến đi phải có cái giá mở đầu rõ ràng. Entry cost không nhất thiết luôn là mất thứ gì ngay lập tức, nhưng luôn là một cam kết thật.

Các lớp entry cost gồm:
- thời gian chuẩn bị
- loadout và tool đang mang theo
- đồ ăn, vật phẩm hồi phục, fuel, mana item, utility
- độ bền của đồ sẽ bị tiêu hao trong chuyến đi
- rủi ro mất thành quả nếu mang quá nhiều giá trị ra ngoài
- coordination cost trong co-op: chờ nhau, chia đồ, thống nhất mục tiêu

### Reward

Phần thưởng đúng của loop không chỉ là item rơi ra.

Reward thực gồm:
- tài nguyên thường để duy trì nhịp sống và craft
- tài nguyên hiếm để mở lớp tool, machine, utility, base capability hoặc chiều sâu mới
- tiến độ mở tầng, mở đường, gate, milestone
- hiểu biết thực tế về đường đi, nguy hiểm, vị trí tài nguyên, nhịp quái
- cảm giác làm chủ tốt hơn cho chuyến sau

### Fail Cost

Thất bại phải đủ nặng để câu hỏi `tham hay rút` có trọng lượng.

Fail cost có thể biểu hiện qua:
- mất một phần hoặc toàn bộ giá trị của run hiện tại
- mất đồ đang mang theo hoặc phải đi recovery
- tiêu hao đồ ăn, repair, fuel, durability mà không đổi được lợi nhuận tương xứng
- mất nhịp tiến sâu của run hiện tại
- tốn thêm thời gian và tài nguyên để quay lại mức sẵn sàng

Fail cost đúng không được phá hủy toàn bộ tiến trình dài hạn, nhưng phải làm cho từng chuyến đi có giá.

## Core Flows

### 1. Flow Chuẩn Của Một Chuyến Đi Thành Công

1. Ở căn cứ, người chơi chuẩn bị đồ và chốt mục tiêu.
2. Người chơi rời vùng an toàn, bắt đầu tiêu hao tài nguyên theo chuyến đi.
3. Người chơi khai thác, thám hiểm, né hoặc xử lý combat, tích lũy giá trị trong túi.
4. Khi áp lực tăng, người chơi cân nhắc giữa lời thêm và khả năng mất nhiều hơn.
5. Người chơi chọn rút đúng lúc và mang được chiến lợi phẩm về.
6. Ở căn cứ, chiến lợi phẩm được đổi thành repair, craft, base progress, utility hoặc năng lực đi sâu hơn.
7. Chuyến sau bắt đầu với nền tốt hơn hoặc mục tiêu lớn hơn.

### 2. Flow Ngắn, An Toàn, Có Tiến Triển

1. Chọn một mục tiêu nhỏ: farm gần, sửa đồ, lấy thêm một nhóm tài nguyên, mở thêm một đoạn ngắn.
2. Đi ra ngoài trong thời gian ngắn.
3. Kiếm được một lượng giá trị vừa đủ.
4. Quay về sớm, khóa lợi nhuận.
5. Cảm giác kết thúc là `mình có tiến thêm`, không phải `phiên này trôi mất`.

### 3. Flow Dài, Căng, Đáng Nhớ

1. Chuẩn bị kỹ hơn bình thường.
2. Đẩy sâu hơn hoặc xa hơn mốc quen thuộc.
3. Gặp nguy hiểm lớn, loot lớn hoặc mốc tiến trình lớn.
4. Quyết định tham thêm hay rút lui trở nên sắc hơn.
5. Nếu sống sót quay về, cảm giác phần thưởng cao hơn hẳn vì đã mang được thứ đáng giá qua một đoạn đường đắt đỏ.

## Failure and Recovery

### Soft Failure

Người chơi không chết nhưng:
- quay về quá sớm
- lời ít
- hao nhiều hơn dự kiến
- hoặc bỏ dở mục tiêu chính

Soft failure vẫn chấp nhận được nếu:
- người chơi học được điều gì đó
- còn giữ được một phần giá trị
- và vẫn chuyển được một phần thành tiến triển nhỏ

### Partial Failure

Người chơi:
- downed rồi được cứu
- mất bớt tài nguyên
- hỏng tool
- cạn hồi phục
- phải cắt ngắn run

Loop vẫn còn sống vì:
- người chơi còn mang về được chút gì đó
- hoặc ít nhất còn giữ được hiểu biết và đường đi cho lần sau

### Hard Failure

Người chơi chết hoặc cả đội wipe.

Hard failure đúng phải:
- làm mất giá trị của run hiện tại
- ép người chơi bước vào nhịp recovery
- nhưng không cắt đứt hẳn tiến trình dài hạn

### Recovery

Recovery là phần bắt buộc của core loop, không phải phần phụ.

Người chơi phải luôn có khả năng:
- quay lại nhặt
- build lại chuyến sau
- chuẩn bị tốt hơn
- đổi chiến thuật
- hoặc lùi một nhịp để ổn định căn cứ trước khi đi tiếp

Nếu sau thất bại mà người chơi thấy `không còn đường đứng dậy`, loop đang bị hỏng.

## Edge Cases

### 1. Phiên Rất Ngắn

Loop vẫn phải hoạt động nếu người chơi chỉ có một phiên ngắn:
- chuẩn bị
- làm một mục tiêu nhỏ
- quay về
- và có tiến triển thật

### 2. Solo

Loop của solo vẫn là loop chuẩn, nhưng:
- entry cost cảm giác nặng hơn
- fail cost cảm giác đau hơn
- quyết định quay về phải tới sớm hơn

Solo không được trở thành chế độ phá sản loop.

### 3. Co-op

Co-op không thay hình dạng loop, nhưng thay đổi sức nặng của từng quyết định:
- chuẩn bị có thêm lớp chia việc
- đi sâu có thêm lớp cứu nhau
- quay về có thêm lớp thương lượng rủi ro và lợi ích

### 4. Không Có Chuyến Đi Lớn

Game không được buộc mọi phiên phải là một chuyến đi lớn. Loop phải chấp nhận các run nhỏ, run hậu cần, run chuẩn bị và vẫn coi đó là tiến triển hợp lệ.

### 5. Loot Không Chỉ Là Item

Một run không được xem là vô giá trị chỉ vì không có đồ hiếm rơi ra. Nếu người chơi:
- mở đường
- học được cấu trúc khu
- xác định nguy hiểm
- hoặc mở điều kiện cho run sau

thì loop vẫn phải công nhận giá trị của run đó.

## Implementation Hooks

- Cần có state machine ở cấp chuyến đi với các state tối thiểu:
  - `safe_preparation`
  - `expedition_active`
  - `pressure_escalating`
  - `retreating`
  - `conversion_recovery`
- Cần xác định rõ khi nào một run được xem là bắt đầu:
  - thường là lúc rời vùng an toàn với loadout đã chốt
- Cần xác định rõ khi nào một run được xem là kết thúc:
  - thường là khi quay lại vùng an toàn hoặc rơi vào hard failure
- Cần có cách đo `haul value` của một run:
  - không chỉ theo item, mà còn theo milestone progress hoặc unlock progress
- Cần có event hoặc cờ cho `safe zone` để tách rõ:
  - chuẩn bị
  - hồi phục
  - craft/build
  - kết toán kết quả chuyến đi
- Cần có telemetry hoặc tag logic cho các điểm:
  - rời vùng an toàn
  - đạt mốc áp lực
  - quay đầu
  - wipe
  - quay về thành công
  - chuyển loot thành progress

## Open Design Questions

- Ranh giới kỹ thuật chính xác của `vùng an toàn tương đối` sẽ được khóa tiếp ở các doc world/base/save.
- Điều kiện analytics hoặc save-state để một chuyến đi được tính là `đã commit` cần khóa tiếp trong `Technical Design`.
- Quan hệ chính xác giữa `surface run`, `cave run`, `gate run` và `boss run` sẽ được đặc tả sâu hơn ở `Short Session Loop`, `Long Progression Loop`, `Dungeon Progression` và `Boss System`.

## Open Balance Variables

- Tỷ lệ thời gian hợp lý giữa `chuẩn bị` và `ở ngoài field`
- Mức lời tối thiểu để một phiên ngắn vẫn thấy đáng
- Ngưỡng mà người chơi thường chọn `đi tiếp` thay vì `rút`
- Mức đau phù hợp của soft failure, partial failure và hard failure
- Tốc độ leo thang áp lực theo độ sâu, độ xa và giá trị loot đang mang
- Mức chênh hợp lý giữa solo run và co-op run về hiệu quả và an toàn
