Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 04/03/2026

# Multiplayer Loop

Tài liệu này chốt vòng lặp gameplay khi có nhiều người chơi cùng tham gia một chuyến đi. Nếu `Core Gameplay Loop` mô tả bộ khung chung của mọi run, thì `Multiplayer Loop` mô tả cách bộ khung đó đổi chất khi nhiều người cùng chia rủi ro, chia tải công việc, cứu nhau, mang chiến lợi phẩm về và cùng quyết định lúc nào nên tham, lúc nào nên rút.

## Mục tiêu

- Mô tả loop co-op riêng của game theo ngôn ngữ production, không dừng ở mức “đi cùng nhau sẽ vui hơn”.
- Chốt tại sao đi cùng nhau có giá trị hơn solo, nhưng vẫn không biến co-op thành điều kiện bắt buộc của toàn bộ game.
- Làm rõ các lớp giá trị thực của co-op: cứu nhau, chia tải chuẩn bị, chia vai tự nhiên, tăng khả năng kéo người và loot về, và tạo ra các quyết định nhóm đáng nhớ.
- Khóa các rule co-op nền đã được chốt ở `Level 8` và các sheet chi tiết: downed/revive, tombstone, free-loot mode thường, repair kit dùng chung, gate có thể hút mana của cả party.

## Phạm vi

Tài liệu này tập trung vào:
- loop co-op từ lúc tập hợp và chuẩn bị tới lúc quay về và chuyển kết quả thành lợi thế cho cả đội
- giá trị riêng của co-op trong field, rescue, extraction, recovery và gate milestone
- quan hệ giữa co-op và các hệ đã khóa: revive/downed, loot rơi đất, bia mộ, repair kit, gate, boss gatekeeper
- cost, reward, fail cost và recovery đặc thù của co-op

Tài liệu này không đi sâu vào:
- công thức damage, aggro AI hay combat tuning chi tiết
- schema mạng, packet sync hay netcode implementation
- UI trade nâng cao, social feature nhiều lớp, guild, quest party riêng
- PvP như một vòng lặp chính

## Source Coverage

### Nguồn bắt buộc

- [08_QUESTIONS_LEVEL_4.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/08_QUESTIONS_LEVEL_4.md)
  - chốt vai trò thật của hệ hỗ trợ co-op: revive/downed, chia đồ cơ bản, thấy trạng thái đồng đội, sync tương tác, join/chơi cùng không quá vướng
- [12_QUESTIONS_LEVEL_8.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/12_QUESTIONS_LEVEL_8.md)
  - khóa các rule gameplay cụ thể về death, tombstone, hotbar rơi đất, gate, boss gatekeeper, free-loot và mana logistics
- [13_PLAYER_CORE_STATE_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/13_PLAYER_CORE_STATE_SHEET.md)
  - chốt `downed`, `revive`, `death`, `respawn`, `heal over time`, reset effect theo điểm hồi sinh
- [14_INVENTORY_AND_ITEM_RULES_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/14_INVENTORY_AND_ITEM_RULES_SHEET.md)
  - chốt hotbar, bia mộ, free-loot mode thường, artifact swap, repair kit dùng chung, auto-loot
- [15_GATE_AND_BOSS_MILESTONE_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/15_GATE_AND_BOSS_MILESTONE_SHEET.md)
  - chốt loop co-op quanh gate, boss gatekeeper, sửa module, hút mana từ party gần cổng, loot farm boss

### Nguồn hỗ trợ

- [07_QUESTIONS_LEVEL_3.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/07_QUESTIONS_LEVEL_3.md)
  - cung cấp phrasing trực tiếp cho `Multiplayer Loop`: chia tải công việc, tăng khả năng mang tài nguyên về, rút lui thông minh hơn, co-op hiệu quả và đáng nhớ hơn

### Nguồn đối chiếu bắt buộc

- [Core Gameplay Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Core%20Gameplay%20Loop.md)
  - dùng để giữ cho co-op vẫn là biến thể của core loop, không trở thành loop tách rời
- [Short Session Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Short%20Session%20Loop.md)
  - dùng để đảm bảo phiên ngắn co-op vẫn có giá trị nhưng không trở thành mặc định bắt buộc
- [Long Progression Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Long%20Progression%20Loop.md)
  - dùng để kiểm tra co-op có hỗ trợ tốt hơn cho milestone dài hạn mà không phá giá solo

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - Loop co-op đã đủ rõ để làm nguồn đúng cho `Player Revive`, `Inventory System`, `Gate System`, `Boss System`, `Multiplayer Support` và các tài liệu technical về sync.
  - Các số cụ thể như thời gian hồi sinh, khoảng cách thấy đồng đội, độ trễ hút loot hay chi phí mana chia cho party vẫn là lớp balance về sau.

## Conflict Resolution

- `Level 3` khóa vai trò co-op ở mức loop: đi cùng nhau hiệu quả và đáng nhớ hơn, nhờ chia tải việc và rút lui thông minh hơn.
- `Level 4` khóa bộ hỗ trợ co-op tối thiểu: revive/downed, chia đồ cơ bản, thấy đồng đội, sync mở cửa/chest/tài nguyên.
- `Level 8` và các sheet chi tiết khóa rule cụ thể hơn về death, tombstone, free-loot, repair kit và gate.
- Khi wording chung và rule cụ thể có vẻ lệch nhau, tài liệu này ưu tiên:
  1. `Sheet 13-15` cho rule gameplay cụ thể
  2. `Level 4` cho phạm vi tối thiểu của hệ co-op
  3. `Level 3` cho tinh thần loop và giá trị cảm xúc

## Rule Summary

- Co-op không thay hình dạng macro loop. Vẫn là `chuẩn bị -> đi ra ngoài -> mạo hiểm -> mang loot về -> đổi loot thành khả năng đi sâu hơn`.
- Co-op đổi trọng lượng của từng bước trong loop: ít chỉ là “mỗi người thêm damage”, mà chủ yếu là `an toàn hơn`, `đáng nhớ hơn`, rồi mới `hiệu quả hơn`.
- Thứ tự giá trị chính của co-op là: `An toàn > Cảm xúc > Hiệu quả`.
- Game không dùng class cứng trong co-op. Vai trò nảy sinh tự nhiên từ:
  - tool và vũ khí đang cầm
  - loadout đồ ăn, utility, artifact
  - sức chứa và đồ đang mang
  - điểm chỉ số đã đầu tư
  - tình huống hiện tại của run
- Một party khỏe không phải party nào cũng đánh tốt, mà là party biết:
  - chia tải chuẩn bị
  - giữ đội không vỡ
  - chốt lúc rút đúng lúc
  - kéo được cả người lẫn loot về
- Solo vẫn là loop hợp lệ. Co-op làm run bền, linh hoạt và giàu câu chuyện hơn, nhưng không được làm solo thành đường chơi hạng hai.
- Trong mode thường, loot và recovery tạo ra cả hợp tác lẫn tension:
  - đồ từ khai thác/quái ai cũng có thể nhặt
  - bia mộ trong mode thường ai cũng mở và lấy được
  - hotbar khi chết rơi thẳng xuống đất và cũng theo rule loot thường
- Gate thiếu năng lượng có thể hút thêm mana từ cả party đang đứng gần cổng nếu cả nhóm bấm dùng cổng trong tình trạng thiếu chuẩn bị.
- Repair kit là công trình dùng chung trong co-op, nên nhịp sửa đồ, tháo đồ và chuẩn bị giữa run cũng có thể trở thành loop hỗ trợ của cả đội.

## State List

### 1. Tập Hợp Và Chốt Mục Tiêu Chung

Cả đội xác định:
- chuyến này đi để làm gì
- mốc nào được xem là “đủ”
- ưu tiên là loot, cứu người, sửa gate, farm boss hay chỉ chuẩn bị cho chuyến sâu hơn

### 2. Chia Tải Chuẩn Bị

Party phân tải tự nhiên:
- người mang nhiều đồ hồi phục hoặc utility
- người cầm tool phù hợp để mở đường / khai thác
- người thiên combat giữ nhịp an toàn
- người thiên logistics giữ vật tư, repair, fuel, mana item

Game không ép bằng class, nhưng loop đúng sẽ khiến sự phân tải này tự xuất hiện.

### 3. Tiến Ra Ngoài Với Đội Hình

Cả đội rời vùng an toàn và bắt đầu tiêu hao:
- food
- durability
- item hồi phục
- mana cá nhân
- khả năng chịu sai lầm của cả nhóm

Từ đây mọi quyết định không còn là cá nhân thuần túy nữa, mà là bài toán cả đội có kéo nhau về nổi không.

### 4. Chia Vai Tự Nhiên Trong Field

Trong field, co-op khỏe khi:
- có người mở đường hoặc khai thác
- có người giữ quái, giữ khoảng trống, giữ nhịp combat
- có người loot, gom đồ, giữ hậu cần
- có người xử lý utility hoặc hỗ trợ môi trường

Vai trò có thể đổi liên tục theo tình huống, không cần cố định từ đầu run.

### 5. Cứu Nhau Và Giữ Đội Không Vỡ

Khi có người ngã:
- solo thì chết thật ngay
- co-op thì vào `downed`

Cả đội phải quyết định:
- cứu ngay
- kéo combat ra xa
- chấp nhận bỏ người đó để giữ phần còn lại của run

Đây là lớp quyết định mà solo không có, và là một trong những nguồn tạo giá trị cảm xúc lớn nhất của co-op.

### 6. Chốt Quyết Định Chung: Tham Hay Rút

Ở solo, người chơi tự quyết nhanh hơn.
Ở co-op, cả đội phải cân giữa:
- người còn bao nhiêu hồi phục
- ai đang gãy đồ
- ai đang cạn mana
- ai đang đầy loot
- còn cứu ai được không
- nếu đi tiếp thì kéo được cả đội về không

Quyết định rút trong co-op nặng hơn vì cái giá và lợi ích không còn là của một người.

### 7. Mang Người Và Loot Về

Extraction trong co-op không chỉ là mang loot về, mà là:
- mang cả người bị thương về
- giữ không cho cả đội sụp dây chuyền
- vớt đồ rơi, mở bia mộ, nhặt hotbar rơi đất khi có người chết
- quyết định ai mang gì, bỏ gì, cứu gì trước

### 8. Chuyển Kết Quả Thành Lợi Thế Cho Cả Đội

Khi về căn cứ, thành quả co-op được đổi thành:
- đồ đã sửa
- utility đã dựng
- vật tư đã nạp
- gate đã sửa thêm
- người chết đã được cứu đồ hoặc phục hồi
- run sau an toàn hơn, nhanh hơn hoặc sâu hơn

## Transition Rules

### Tập Hợp Và Chốt Mục Tiêu Chung -> Chia Tải Chuẩn Bị

Xảy ra khi party đã chốt:
- mục tiêu chuyến đi
- ai đang thiếu gì
- ai nên mang gì
- điều kiện nào thì cả đội quay về

### Chia Tải Chuẩn Bị -> Tiến Ra Ngoài Với Đội Hình

Xảy ra khi:
- loadout chung đã đủ dùng
- repair, food, mana item và tool đã chốt
- cả đội rời vùng an toàn

### Tiến Ra Ngoài Với Đội Hình -> Chia Vai Tự Nhiên Trong Field

Xảy ra khi party bắt đầu:
- gặp quái
- gặp mạch tài nguyên
- gặp hazard
- hoặc cần chia nhau làm việc để tiến nhanh hơn

### Chia Vai Tự Nhiên Trong Field -> Cứu Nhau Và Giữ Đội Không Vỡ

Xảy ra khi:
- có người vào downed
- có người chết
- có người gãy đồ, cạn tài nguyên hoặc tụt lại
- boss hoặc hazard làm đội hình mất nhịp

### Cứu Nhau Và Giữ Đội Không Vỡ -> Chốt Quyết Định Chung: Tham Hay Rút

Xảy ra khi cả đội đã thấy rõ:
- vẫn còn cửa tiếp tục
- hay nên rút trước khi mất thêm người và mất luôn giá trị của run

### Chốt Quyết Định Chung: Tham Hay Rút -> Chia Vai Tự Nhiên Trong Field

Xảy ra khi party quyết định đi tiếp.
Loop quay lại ở mức rủi ro cao hơn vì:
- tài nguyên đã mỏng hơn
- đội hình đã mỏi hơn
- và một sai lầm mới có thể kéo theo sụp dây chuyền

### Chốt Quyết Định Chung: Tham Hay Rút -> Mang Người Và Loot Về

Xảy ra khi party quyết định rút.
Từ đây trọng tâm là:
- giữ được nhiều người nhất
- khóa được nhiều giá trị nhất
- tránh biến một run đã lời thành wipe muộn

### Mang Người Và Loot Về -> Chuyển Kết Quả Thành Lợi Thế Cho Cả Đội

Xảy ra khi cả đội đã:
- cất loot
- sửa đồ
- xử lý recovery
- chia lại tài nguyên
- nạp lại cho người và machine
- hoặc chốt thêm tiến độ cho gate / base / utility

### Bất Kỳ State Field Nào -> Failure And Recovery

Xảy ra khi:
- nhiều người chết
- đội hình gãy và không cứu kịp
- party tan hàng vì thiếu tài nguyên
- gate hút mana quá mạnh làm cả đội không còn khả năng xoay xở

## Core Flows

### 1. Flow Co-op Chuẩn Của Một Run Thành Công

1. Cả đội chốt mục tiêu và chia tải chuẩn bị.
2. Đi ra ngoài, mỗi người tự nhiên đảm nhận một phần công việc.
3. Trong field, party vừa khai thác vừa giữ nhịp an toàn cho nhau.
4. Khi áp lực tăng, cả đội tranh luận ngắn nhưng rõ: đi tiếp hay rút.
5. Chọn rút đúng lúc, mang được phần lớn người và loot về.
6. Ở căn cứ, loot được đổi thành repair, utility, fuel, gate progress hoặc chuẩn bị cho chuyến sâu hơn.
7. Cả đội cảm thấy chuyến đi này không chỉ lời hơn solo, mà còn tạo ra câu chuyện “cả nhóm vừa cứu nhau và kéo được mọi thứ về”.

### 2. Flow Co-op Cứu Người Và Recovery

1. Một người vào `downed`.
2. Một người giữ quái hoặc kéo nguy hiểm ra xa.
3. Một người quyết định có bỏ máu để hồi sinh đồng đội không.
4. Nếu cứu kịp trước khi hết timer, đồng đội đứng dậy với lượng máu giới hạn và một khoảng an toàn ngắn.
5. Cả đội phải lập tức chốt:
   - rút về
   - hay đánh tiếp nếu lợi nhuận vẫn còn đáng
6. Nếu không cứu kịp và người đó chết thật:
   - hotbar rơi xuống đất
   - đồ trong túi vào bia mộ
   - cả đội có thể quyết định recovery luôn hoặc quay lại sau

### 3. Flow Co-op Quanh Gate Và Boss Gatekeeper

1. Party đi xuống mốc gate đang hỏng.
2. Một hoặc vài người giữ boss / dọn áp lực.
3. Một người tranh thủ nhét vật liệu và sửa từng module.
4. Nếu boss đập trúng module:
   - tiến độ bị phá
   - một phần vật liệu vừa nhét có thể mất
5. Nếu boss chết, cả đội có cửa sổ yên hơn để sửa.
6. Khi gate đủ điều kiện và ổn định:
   - cả đội có thêm tuyến logistics dài hạn
   - chuyến sau rẻ hơn, bền hơn, ít đau hơn
7. Nếu gate thiếu năng lượng mà cả đội vẫn bấm dùng:
   - mana có thể bị hút thêm từ những người đứng gần cổng
   - rủi ro nhóm vì thế tăng lên theo cách rất “co-op”

## Cost / Reward

### Cost

Co-op có lợi, nhưng không miễn phí.

Các cost chính gồm:
- thời gian chờ và thống nhất mục tiêu
- chia tải chuẩn bị và chia lại tài nguyên
- phải tính tới người yếu nhất hoặc người chuẩn bị tệ nhất
- sai lầm của một người có thể kéo cả đội vào tình thế cứu hộ
- mất nhịp do revive, lượm đồ, mở bia mộ, quay lại cứu người
- gate có thể hút mana từ cả party gần cổng khi thiếu năng lượng
- mode thường free-loot hoàn toàn nên cũng có cost xã hội: tin tưởng, giữ kỷ luật, hoặc chấp nhận hỗn loạn

### Reward

Reward đúng của co-op không chỉ là “nhiều damage hơn”.

Reward thật gồm:
- tỷ lệ sống sót cao hơn
- có lớp downed/revive nên sai lầm chưa làm run gãy ngay
- chia tải công việc để vừa đánh, vừa đào, vừa giữ đồ, vừa sửa, vừa kéo nhau về
- mang được nhiều giá trị hơn về căn cứ
- recovery sau tai nạn dễ thở hơn vì còn người sống để xoay xở
- quyết định rút lui thông minh hơn vì có nhiều góc nhìn và nhiều tay để cứu tình thế
- tạo ra những khoảnh khắc rất khó có ở solo: cứu sát giờ, kéo nhau về với đồ hỏng nát, chia mana để qua cổng, giữ boss cho người khác sửa gate

## Failure And Recovery

### Downed Và Revive

- Trong co-op, khi máu về 0, người chơi vào `downed` thay vì chết ngay.
- `Downed` mặc định kéo dài khoảng `60 giây`.
- Đồng đội có thể hồi sinh bằng cách dùng máu của chính mình.
- Nếu hoàn tất hồi sinh trước khi timer chạm 0, người bị downed đứng dậy với khoảng `50% HP`.
- Sau khi đứng dậy, người đó có một khoảng an toàn ngắn để không bị đè chết ngay lập tức.

### Chết Thật Và Recovery

Nếu hết timer downed hoặc không ai cứu được:
- người chơi chết thật
- item hotbar rơi xuống đất
- item trong túi nằm trong bia mộ

Trong mode thường:
- ai cũng có thể mở bia mộ
- ai cũng có thể nhặt loot rơi đất

Nếu bật PvP mode:
- bia mộ chỉ chủ nhân hoặc đồng đội hợp lệ mới mở được
- loot sharing không còn hoàn toàn tự do như mode thường

Điều này làm recovery trong co-op vừa dễ hơn, vừa có thể tạo tension giữa tự do, hỗ trợ và kỷ luật nhóm.

### Recovery Run

Co-op khỏe ở chỗ recovery không nhất thiết là “quay lại một mình để gỡ lỗi”.
Party có thể:
- cử người quay lại nhặt đồ
- để một người giữ an toàn, một người loot, một người dọn đường
- dùng phiên ngắn chỉ để cứu người và kéo lại chiến lợi phẩm

### Failure Của Cả Đội

Co-op không xóa rủi ro. Nếu cả đội:
- đều cạn tài nguyên
- đều bị gate hút sạch mana đúng lúc
- hoặc wipe dây chuyền

thì fail cost có thể còn đau hơn solo vì giá trị bị dồn vào cùng một chuyến đi.

## Edge Cases

### 1. Một Người Chết, Cả Đội Vẫn Đi Tiếp

Đây là trường hợp hợp lệ.
Co-op không bắt buộc cứ có người chết là cả đội phải rút, nhưng khi làm vậy game phải khiến quyết định đó nặng:
- mất người chia tải
- tăng nguy cơ wipe muộn
- có nguy cơ mất luôn đồ của người đã chết nếu kéo dài quá lâu

### 2. Một Người Mở Và Lấy Bia Mộ Của Đồng Đội Trong Mode Thường

Đây là rule đã chốt, không phải bug.
Co-op mode thường chấp nhận tự do hoàn toàn với loot.
Vì vậy, game phải xem đây là một phần của động lực nhóm:
- hỗ trợ thật
- hỗn loạn vui
- hoặc tension do niềm tin và kỷ luật party

### 3. Một Người Chuẩn Bị Tệ Kéo Cả Đội Xuống

Đây là edge case phải chấp nhận.
Co-op không được tự san bằng mọi lỗ hổng chuẩn bị.
Một thành viên thiếu food, thiếu repair, thiếu mana item hoặc loadout sai vẫn có thể làm cả run xấu đi.

### 4. Party Tách Quá Xa

Khi tách quá xa:
- rescue khó hơn
- chia vai thành chia cắt
- loot và recovery khó gom hơn
- gate, boss, hazard dễ biến thành hai trận riêng lẻ thay vì một plan chung

Co-op khỏe khi tách vừa đủ để chia việc, nhưng không vỡ thành nhiều solo run song song.

### 5. Gate Hút Mana Cả Party Ngoài Dự Tính

Nếu gate thiếu năng lượng và cả đội vẫn bấm dùng:
- mana có thể bị hút từ cả những người đứng gần cổng
- decision sai của một người có thể làm cả team nghèo mana hơn

Đây là loại fail cost rất đúng chất co-op logistics.

### 6. Một Người Giữ Boss, Một Người Sửa Gate

Đây là pattern hợp lệ và nên được công nhận như giá trị thật của co-op.
Nhưng nó không được miễn phí:
- boss vẫn có thể phá module
- tài nguyên vừa nhét vẫn có thể mất
- nếu người giữ boss ngã, cả plan có thể sụp ngay

## Signs Of A Good Multiplayer Loop

Multiplayer loop được xem là khỏe khi người chơi thường cảm thấy:
- “đi cùng nhau an toàn hơn thật chứ không chỉ đông hơn”
- “mỗi người tự nhiên có việc để làm mà không cần class cứng”
- “cứu nhau, giữ nhau sống và kéo nhau về là phần hay nhất của co-op”
- “đi chung không xóa rủi ro, nhưng cho nhiều cách cứu tình thế hơn”
- “run co-op đáng nhớ hơn solo, kể cả khi loot không phải lúc nào cũng hơn hẳn”

## Signs Of A Broken Multiplayer Loop

Multiplayer loop đang hỏng nếu người chơi thường cảm thấy:
- “co-op chỉ là cộng damage, không có chiều quyết định riêng”
- “đi cùng nhau quá lời nên solo thành vô nghĩa”
- “hoặc ngược lại, đi cùng nhau chỉ thêm rối mà không tăng được gì”
- “thiếu revive, thiếu thấy trạng thái đồng đội, thiếu sync tương tác nên co-op rất gượng”
- “gate, death recovery, loot sharing làm party cãi nhau vô nghĩa thay vì tạo ra lựa chọn thú vị”

## Implementation Hooks

- Cần state ở cấp party tối thiểu:
  - `party_preparing`
  - `party_committed_to_run`
  - `party_split_tasking`
  - `party_rescue_state`
  - `party_retreating`
  - `party_recovery_run`
- Cần sync rõ cho:
  - vị trí và trạng thái đồng đội
  - `downed`, `revive`, `death`
  - mở cửa, mở chest, khai thác tài nguyên, tương tác gate
- Cần có rule flag rõ cho mode thường / PvP mode:
  - ai mở được bia mộ
  - ai nhặt được loot rơi đất
  - free-loot có áp dụng hoàn toàn hay không
- Cần telemetry cho:
  - tỷ lệ revive thành công
  - số run co-op chết dây chuyền sau khi cứu người
  - số lần gate hút mana của cả party
  - tỷ lệ recovery thành công sau khi có một người chết
  - chênh lệch hiệu quả giữa solo run và co-op run
- Cần support logic cho công trình dùng chung trong co-op như `repair kit`

## Open Design Questions

- Kích thước party tối ưu mà loop hiện tại phục vụ tốt nhất là bao nhiêu người.
- Cần thêm bao nhiêu lớp thấy đồng đội ngoài vị trí và trạng thái cơ bản: ping, marker, intent marker hay chưa cần.
- Độ xa tối đa trước khi co-op thực chất biến thành nhiều solo run song song.
- Các luật khác nhau giữa mode thường và mode PvP nên được bộc lộ qua UI và onboarding thế nào để tránh hiểu nhầm.

## Open Balance Variables

- Thời gian downed phù hợp cho nhịp cứu nhau trong co-op
- Chi phí máu hợp lý của hành động revive
- Mức chênh hợp lý giữa solo efficiency và co-op efficiency
- Độ trễ hút loot rơi đất trước khi auto-hút
- Mức drain mana thêm của gate khi hút từ cả party gần cổng
- Khoảng an toàn ngắn sau revive nên dài bao lâu để đủ công bằng nhưng không quá dễ
