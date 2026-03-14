Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 03/03/2026

# Long Progression Loop

Tài liệu này chốt vòng tiến trình dài hạn của game qua nhiều phiên chơi. Nếu `Core Gameplay Loop` trả lời câu hỏi “mỗi chuyến đi vận hành ra sao”, thì `Long Progression Loop` trả lời câu hỏi “sau nhiều chuyến đi, người chơi mạnh lên và đi sâu hơn bằng cách nào”. Trục của tài liệu này không phải chỉ là tăng số, mà là `tích lũy để dám xuống sâu hơn, rồi dùng thứ mang về để mở tiếp chiều sâu sau đó`.

## Mục tiêu

- Chốt hình dạng của vòng tiến trình dài hạn xuyên nhiều phiên chơi.
- Làm rõ game đi từ `sống sót nền` tới `ổn định`, `chạm mana`, `mở gate`, `ổn định logistics tầng sâu` bằng cách nào.
- Chỉ ra phần thưởng dài hạn nào là thật sự có giá trị: mở tầng, mở utility, mở machine, mở mana infrastructure, mở tuyến ổn định, mở gate, mở stat point.
- Khóa vai trò của boss, gate, workstation, mana, repair và đầu tư build trong tiến trình dài hạn.
- Tạo nền cho các doc tiếp theo như `Player Progression`, `Dungeon Progression`, `Crafting Economy`, `Gate System`, `Boss System` và `Tech Tree`.

## Phạm vi

Tài liệu này tập trung vào:
- tiến trình dài hạn qua nhiều run và nhiều phiên chơi
- các mốc chuyển pha của game từ đầu tới giữa và sâu hơn về sau
- quan hệ giữa `đi sâu`, `mở tầng`, `mở công nghệ`, `mở mana`, `mở gate`, `ổn định tuyến`
- entry cost, reward, fail cost và đường phục hồi ở cấp tiến trình dài hạn
- vai trò của base, workstation, utility, logistics và stable gate trong việc giảm độ đau của những chuyến đi sau

Tài liệu này không đi sâu vào:
- công thức combat, durability, chi phí sửa đồ chi tiết
- số balance cụ thể cho từng tier, từng tầng, từng loại quặng
- schema dữ liệu chi tiết của từng item, workstation, boss hay gate

## Source Coverage

### Nguồn bắt buộc

- [10_QUESTIONS_LEVEL_6.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/10_QUESTIONS_LEVEL_6.md)
  - là nguồn xương sống cho progression dài hạn: chia chặng phát triển, faucet và sink, tech tree, vai trò của gear, utility, base, mana, gate và open depth structure
- [11_QUESTIONS_LEVEL_7.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/11_QUESTIONS_LEVEL_7.md)
  - dùng để giữ progression dài hạn trong phạm vi thực thi hợp lý, không đẻ ra hệ quá phức tạp vượt khung MVP hoặc vượt sức production hiện tại
- [12_QUESTIONS_LEVEL_8.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/12_QUESTIONS_LEVEL_8.md)
  - khóa các rule cụ thể tạo thành milestone dài hạn thật: mana usage, workstation tier, repair tier, gate repair, boss gatekeeper, stat point, stable route, boss farm, fuel logic

### Nguồn hỗ trợ

- [13_PLAYER_CORE_STATE_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/13_PLAYER_CORE_STATE_SHEET.md)
  - dùng để chốt phần tăng trưởng cá nhân dài hạn: stat point nhận chủ yếu từ mở tầng, boss và milestone là nguồn phụ, cho phép all in, có respec đắt
- [15_GATE_AND_BOSS_MILESTONE_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/15_GATE_AND_BOSS_MILESTONE_SHEET.md)
  - dùng để chốt value dài hạn của gate, boss gatekeeper, repair module, gate stability, boss respawn, logistics tầng sâu

### Nguồn đối chiếu bắt buộc

- [Core Gameplay Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Core%20Gameplay%20Loop.md)
  - dùng để đảm bảo progression dài hạn vẫn là phần kéo dài của core loop chứ không trở thành lớp meta tách rời
- [Short Session Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Short%20Session%20Loop.md)
  - dùng để đảm bảo progression dài hạn vẫn được nuôi bằng nhiều phiên ngắn hợp lệ, không bắt buộc mọi tiến bộ phải đến từ run dài
- [Target Experience.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/00_GAME_VISION/Target%20Experience.md)
  - dùng để giữ đúng cảm giác “chuẩn bị -> mạo hiểm -> mang về -> muốn đi tiếp”, đồng thời khóa ý “giữa game bắt đầu mở rộng mạnh khi mana trở thành thật”

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - Hình dạng của long progression đã đủ rõ để làm nguồn đúng cho `Player Progression`, `Dungeon Progression`, `Tech Tree`, `Economy`, `Gate System` và `Boss System`.
  - Các con số chính xác như số run cho mỗi chặng, chi phí từng gate, lượng điểm cho từng boss hay từng tầng vẫn là lớp balance về sau.

## Conflict Resolution

- `Level 6` là nguồn chính để dựng xương sống của tiến trình dài hạn.
- `Level 7` không định nghĩa progression theo nghĩa gameplay sâu, nhưng giúp giữ doc này trong khung triển khai khả thi, tránh biến tiến trình dài hạn thành danh sách hệ thống không thể sản xuất.
- `Level 8` không thay `Level 6`, mà cung cấp rule cụ thể để những milestone dài hạn trở thành thứ người chơi thật sự cảm được: chạm mana, mở workstation tier, sửa gate, đánh boss gatekeeper, ổn định tuyến sâu, đầu tư stat point.
- Khi cần chọn wording, tài liệu này ưu tiên:
  1. `Level 6` cho cấu trúc tiến trình dài hạn
  2. `Level 8` cho mốc và rule cụ thể
  3. `Core Gameplay Loop` và `Target Experience` để kiểm tra xem tiến trình đó có còn nuôi đúng fantasy và cảm xúc hay không

## Rule Summary

- Long progression không chỉ là “đánh mạnh hơn” mà là `sống ổn hơn, chuẩn bị tốt hơn, logistic khỏe hơn, mở sâu hơn và quay về đáng tin hơn`.
- Vòng dài hạn chuẩn là: `sống sót nền -> ổn định công cụ và căn cứ -> mở utility đi sâu -> chạm mana thật sự -> mở tầng sâu và gate -> ổn định logistics tầng sâu -> tái đầu tư để đi sâu hơn nữa`.
- Người chơi không tiến lên chủ yếu nhờ farm EXP liên tục, mà chủ yếu nhờ:
  - mở tầng
  - mang tài nguyên về
  - mở workstation và utility
  - chạm quặng mana và hạ tầng chiết xuất
  - sửa gate
  - hạ boss để ổn định tuyến
- Mana đánh dấu điểm chuyển pha rõ của game. Trước đó game thiên về tool, repair, food, resource loop; sau đó game mở thêm machine, utility cao hơn, fuel, gate và logistics.
- Boss trong trục này không phải lúc nào cũng là ổ khóa cứng. Vai trò mạnh nhất của boss là `milestone ổn định`: muốn sửa gate yên ổn, muốn biến tuyến sâu thành tuyến dùng được lâu dài, thường phải giải quyết boss gatekeeper.
- Stable gate là một trong những phần thưởng dài hạn mạnh nhất vì nó biến rủi ro và quãng đường của tương lai thành thứ rẻ hơn, nhanh hơn, ổn định hơn.
- Build variety nên đến từ `ưu tiên đầu tư` chứ không phải `class cứng`. Người chơi có thể all in vào một hướng chỉ số, nhưng tiến trình dài hạn vẫn buộc họ quan tâm tới tool, utility, repair, mana và logistics.
- Tài nguyên tier thấp không được trở nên vô nghĩa quá sớm. Chúng phải tiếp tục có giá trị trong repair, build, fuel phụ, chain craft hoặc logistic layer.
- Long progression phải có sink đủ khỏe để chống inflation và snowball, nếu không mọi chuyến đi về sau sẽ mất trọng lượng.

## State List

### 1. Sống Sót Nền

Người chơi còn đang ở trạng thái:
- tool thô
- nguồn lực mỏng
- căn cứ sơ sài
- repair và craft còn yếu
- mỗi chuyến đi chủ yếu để tồn tại và gom đủ bộ vật tư cơ bản

### 2. Ổn Định Công Cụ Và Căn Cứ

Người chơi bắt đầu:
- có tool và weapon đáng tin hơn
- có loop sửa đồ ổn hơn
- có kho, workstation và utility cơ bản
- bớt bị một cái chết nhỏ đẩy về gần như tay trắng

### 3. Mở Utility Đi Sâu

Người chơi bắt đầu có:
- utility phục vụ môi trường
- khả năng mang đồ, sửa đồ, hồi phục và tổ chức chuyến đi tốt hơn
- căn cứ hoạt động như một nơi chuẩn bị thật chứ không chỉ là chỗ thả đồ

### 4. Chạm Mana Thật Sự

Đây là bước chuyển pha lớn. Người chơi:
- chạm quặng mana
- có khả năng chiết xuất mana ở base
- bắt đầu dùng mana cho tool, utility, machine và hạ tầng
- cảm nhận rõ game đi sang lớp công nghệ sâu hơn nhưng vẫn giữ low-tech steampunk magitech

### 5. Mở Tầng Sâu Và Gate Milestone

Người chơi:
- xuống được các tầng sâu hơn
- gặp gate hỏng, boss gatekeeper, module sửa chữa, fuel pressure
- bắt đầu thấy việc “đi sâu” không chỉ là đi xuống, mà là mở tuyến vận hành được

### 6. Ổn Định Logistics Tầng Sâu

Người chơi:
- sửa được gate từng phần rồi ổn định hoàn toàn
- thiết lập tuyến đi về rẻ hơn và an toàn hơn
- giảm chi phí cho các chuyến lặp lại
- bắt đầu vận hành mạng lưới mana, fuel, machine và mốc hồi sinh theo hướng bền hơn

### 7. Tái Đầu Tư Để Đi Sâu Hơn Nữa

Người chơi:
- dùng thành quả của tầng trước để chuẩn bị cho tầng sau
- dùng stable route để mở tiếp chiều sâu mới
- tiếp tục lặp chu kỳ `mở - ổn định - tái đầu tư - đi sâu hơn`

## Transition Rules

### Sống Sót Nền -> Ổn Định Công Cụ Và Căn Cứ

Xảy ra khi người chơi đã:
- có đủ resource loop cơ bản để không bị đứt hơi sau mỗi run
- có cách sửa đồ đáng tin hơn
- có chỗ chứa, chỗ craft, chỗ chuẩn bị tốt hơn
- bắt đầu biến loot thành hạ tầng thay vì chỉ đốt vào sống sót trước mắt

### Ổn Định Công Cụ Và Căn Cứ -> Mở Utility Đi Sâu

Xảy ra khi người chơi:
- không còn chỉ chạy theo food và repair
- bắt đầu mở utility phục vụ đi xa, sống lâu hơn, xử lý hazard tốt hơn
- có workstation tier và item tier đủ để hỗ trợ những run tham hơn

### Mở Utility Đi Sâu -> Chạm Mana Thật Sự

Xảy ra khi người chơi:
- chạm được quặng mana hoặc tầng có mana trở thành resource thật
- dựng được máy chiết xuất hoặc hạ tầng xử lý mana ở base
- bắt đầu thấy mana không còn là flavor, mà là một hệ năng lượng có giá trị chiến lược

### Chạm Mana Thật Sự -> Mở Tầng Sâu Và Gate Milestone

Xảy ra khi người chơi:
- dùng được mana cho machine, tool, utility hoặc logistics
- đẩy được xuống các tầng sâu hơn
- bắt đầu tiếp xúc với gate, fuel pressure, boss gatekeeper và module sửa chữa

### Mở Tầng Sâu Và Gate Milestone -> Ổn Định Logistics Tầng Sâu

Xảy ra khi người chơi:
- không chỉ chạm được tầng sâu, mà còn bắt đầu sửa, vận hành và ổn định gate
- xử lý boss gatekeeper để có cửa sổ sửa chữa yên hơn
- chuyển tiến trình “đi được một lần” thành “đi được nhiều lần với giá thấp hơn”

### Ổn Định Logistics Tầng Sâu -> Tái Đầu Tư Để Đi Sâu Hơn Nữa

Xảy ra khi:
- stable gate, workstation, machine, mana network và utility bắt đầu giảm chi phí cho run tiếp theo
- người chơi có thể dùng surplus để nhắm tới mốc sâu hơn thay vì chỉ vá víu mốc cũ

### Tái Đầu Tư Để Đi Sâu Hơn Nữa -> Mở Tầng Sâu Và Gate Milestone

Xảy ra mỗi khi người chơi:
- chọn một tầng, tuyến hoặc mốc sâu hơn
- đẩy loop dài hạn sang chu kỳ tiếp theo ở mức rủi ro và giá trị cao hơn

## Core Flows

### 1. Flow Từ Tay Trắng Tới Ổn Định Đầu Game

1. Người chơi sống sót bằng các run gần, tài nguyên thường, tool thô và sửa chữa nghèo nàn.
2. Loot mang về chủ yếu đổ vào food, repair, tool cơ bản, kho và workstation nền.
3. Khi loop sửa đồ, craft đồ, chứa đồ và chuẩn bị run đã bớt gãy, game chuyển sang pha ổn định đầu.
4. Từ đây, từng phiên chơi không còn chỉ nhằm “sống qua hôm nay”, mà bắt đầu nhằm “chuẩn bị cho cú đẩy tiếp theo”.

### 2. Flow Từ Ổn Định Đầu Game Tới Pha Mana

1. Người chơi tiếp tục mở tầng, mở utility và mở workstation tier.
2. Tài nguyên mang về không chỉ tạo ra đồ mạnh hơn, mà tạo ra năng lực đi sâu, chịu hazard và tổ chức hậu cần tốt hơn.
3. Khi chạm được quặng mana và dựng được máy chiết xuất, game bước sang pha mới.
4. Mana lúc này mở thêm lớp machine, utility, fuel, automation nhẹ và logistics, thay vì thay hoàn toàn core survival.

### 3. Flow Từ Pha Mana Tới Logistics Tầng Sâu

1. Người chơi xuống sâu hơn, thấy gate hỏng, boss gatekeeper, repair module và áp lực fuel.
2. Boss không chỉ là combat check, mà là lực cản ổn định tuyến.
3. Người chơi vừa hạ boss vừa sửa gate từng phần, hoặc sửa liều trong khi boss còn sống với rủi ro mất tài nguyên.
4. Khi gate ổn định, run tương lai đổi chất: quãng đường ngắn hơn, recovery đỡ đau hơn, chuẩn bị sâu trở nên thực tế hơn.
5. Từ đây, thành quả không còn chỉ là đồ tốt hơn, mà là `mạng lưới đi sâu` tốt hơn.

## Cost / Reward

### Cost

Long progression đòi hỏi các lớp cost cộng dồn qua nhiều phiên:
- thời gian lặp lại nhiều run để gom đủ resource
- chi phí duy trì tool, weapon, armor, artifact, repair và food
- chi phí mở workstation, utility, machine và mana infrastructure
- chi phí thử sai, chết, recovery, mất loot hoặc fail một nhánh sâu
- chi phí fuel, gate energy, chuẩn bị logistics và ổn định tuyến

### Reward

Phần thưởng dài hạn đúng không chỉ là “số damage cao hơn”.

Reward thật gồm:
- tool và gear đáng tin hơn
- utility và survivability tốt hơn
- workstation tier cao hơn
- mana extraction và mana usage rõ hơn
- mở tầng sâu hơn
- mở stat point chủ yếu từ floor opening, boss và milestone là nguồn phụ
- gate ổn định và tuyến sâu dùng được lâu dài
- giảm chi phí cho các chuyến tương lai
- mở ra lựa chọn đầu tư mới thay vì chỉ tăng cùng một trục

### Anti-Inflation Requirement

Economy dài hạn phải giữ được:
- tài nguyên tier thấp vẫn có việc để làm
- sink đủ lớn để đồ mang về không phá hỏng nhịp survival
- growth không snowball đến mức từ giữa game trở đi mọi chuyến đi chỉ còn thủ tục

Nếu low-tier resource mất giá quá sớm, gate quá rẻ, repair quá nhẹ hoặc mana quá dư, long progression sẽ xẹp.

## Failure and Recovery

### Expedition Failure Không Được Xóa Tiến Trình Dài Hạn

Một run sâu thất bại có thể:
- làm mất loot của run đó
- làm trì hoãn gate repair
- làm tốn repair, food, fuel, mana item
- buộc người chơi quay lại chạy recovery

Nhưng nó không được:
- xóa stable gate đã ổn định
- xóa stat point đã đầu tư
- xóa toàn bộ hạ tầng base
- biến nhiều chục giờ trước đó thành số không

### Recovery Phải Đi Qua Các Loop Nhỏ Hơn

Recovery đúng thường diễn ra bằng:
- run ngắn để gom lại vật tư
- phiên chuẩn bị để sửa đồ và nạp lại hạ tầng
- quay lại tầng sâu với mục tiêu nhỏ hơn
- hoặc lùi một nhịp để ổn định base rồi mới đẩy tiếp

### Stable Route Giảm Độ Đau Của Tương Lai

Một giá trị rất lớn của long progression là:
- càng nhiều thứ đã được ổn định, càng ít phải trả lại toàn bộ giá cho mỗi lần thử sâu hơn
- stable gate, workstation tốt hơn, mana infrastructure tốt hơn và utility tốt hơn đều làm recovery bớt phũ

## Edge Cases

### 1. Gear Khá Nhưng Logistics Yếu

Người chơi có thể đánh mạnh hơn nhưng vẫn không đi sâu bền được nếu:
- repair yếu
- food yếu
- utility thiếu
- gate chưa ổn định
- mana logistics còn mỏng

Long progression đúng phải cho thấy `gear` một mình không đủ.

### 2. Đã Chạm Tầng Sâu Nhưng Chưa Ổn Định Gate

Người chơi vẫn có thể đi xuống, farm liều hoặc chạm milestone.
Nhưng chi phí đi lại, rủi ro boss, rủi ro fuel và recovery vẫn phải cao hơn rõ.
Điều này giữ cho stable gate còn giá trị thật.

### 3. All In Chỉ Số Nhưng Thiếu Utility Và Base

Người chơi được phép all in build, nhưng long progression không được để stat point một mình thay thế hoàn toàn:
- repair
- workstation
- food
- mana preparation
- gate logistics

### 4. Ở Safe Zone Quá Lâu

Nếu người chơi có thể farm vùng an toàn quá lâu mà vẫn mạnh lên đủ để bỏ qua tầng sâu, loop dài hạn sẽ hỏng.
Safe zone và tầng nông phải nuôi nền, không được thay cả chiều sâu.

### 5. Boss Không Bị Giết Nhưng Tuyến Vẫn Bị Lách

Game cho phép một số trường hợp lách, sửa từng phần hoặc đi liều khi boss còn sống.
Nhưng đường đó phải luôn:
- đắt hơn
- bấp bênh hơn
- mất tài nguyên hơn
- khó duy trì hơn

Nếu lách lúc nào cũng tối ưu hơn giết boss và ổn định gate, milestone boss sẽ mất vai trò.

### 6. Co-op Đi Nhanh Hơn Solo

Co-op được phép:
- giúp phục hồi nhanh hơn
- chia việc hiệu quả hơn
- mở sâu an toàn hơn

Nhưng solo vẫn phải có đường tiến bộ dài hạn hợp lệ. Long progression không được ngầm biến co-op thành điều kiện bắt buộc để chạm các mốc chính.

## Signs Of Good Long Progression

Long progression được xem là khỏe khi người chơi thường có cảm giác:
- “mỗi vài phiên là mình mở được một khả năng mới thật”
- “giữa game có một cú chuyển pha rõ khi mana trở thành thứ mình phải quan tâm thật”
- “ổn định được một gate thấy như vừa thay đổi cả nhịp chơi”
- “đồ cũ và tài nguyên thấp không bị thành rác quá sớm”
- “mình có quyền ưu tiên đầu tư theo hướng riêng, chứ không phải game ép một đường duy nhất”
- “thất bại đau, nhưng không làm hàng chục giờ trước đó vô nghĩa”

## Signs Of A Broken Long Progression

Long progression đang hỏng nếu người chơi thường cảm thấy:
- “mạnh lên chỉ là số to hơn, chứ cách chơi không đổi”
- “tới giữa game thì đồ/tài nguyên cũ thành vô giá trị”
- “mana đến quá sớm nên survival nền mất ý nghĩa”
- “hoặc mana đến quá muộn nên giữa game không có chuyển pha”
- “boss chỉ là ổ khóa cứng và không tạo ra giá trị ổn định tuyến”
- “gate ổn định xong mà không đỡ được gì đáng kể”
- “đầu game thì khổ, giữa game thì lạm phát, cuối game thì mọi thứ thành thủ tục”

## Implementation Hooks

- Cần tag progression stage tối thiểu:
  - `baseline_survival`
  - `early_stability`
  - `utility_open`
  - `mana_contact`
  - `deep_gate_candidate`
  - `deep_logistics_stable`
  - `next_depth_preparation`
- Cần tag nguồn mở khóa tối thiểu:
  - `floor_open`
  - `boss_milestone`
  - `resource_threshold`
  - `workstation_tier`
  - `mana_access`
  - `gate_stable`
- Cần world persistence rõ cho:
  - tầng đã mở
  - gate đã ổn định
  - module gate đã sửa
  - boss gatekeeper đang sống/chết/đang đếm hồi sinh
  - workstation và hạ tầng mana ở base
- Cần analytics hoặc telemetry cho:
  - thời gian từ đầu game tới khi chạm mana
  - thời gian từ lần thấy gate đầu tiên tới lúc ổn định gate đầu tiên
  - thời gian từ một hard failure sâu tới khi người chơi quay lại được cùng mốc
  - tần suất low-tier resource còn được dùng ở từng giai đoạn
- Cần hook rõ cho stat point gain:
  - mở tầng là nguồn chính
  - boss và milestone là nguồn phụ

## Open Design Questions

- Tầng chính xác nào sẽ được xem là điểm “mana trở thành resource thật” trong bản cân bằng sau cùng, dù hiện định hướng là từ tầng 3 trở đi.
- Mỗi macro-stage nên có bao nhiêu loại gate và bao nhiêu lớp milestone logistics khác nhau.
- Mức độ tự động hóa của machine và mana network sẽ dừng ở đâu để không phá cảm giác low-tech steampunk magitech.
- Cách biểu diễn trực quan cho “người chơi đã bước sang pha progression mới” sẽ dùng UI, world change, unlock screen hay phối hợp nhiều lớp.

## Open Balance Variables

- Số phiên trung bình để đi từ `baseline_survival` sang `early_stability`
- Số phiên trung bình từ lúc chạm mana tới lúc có tuyến sâu đầu tiên đủ ổn định
- Tỷ lệ cost giữa `duy trì hiện tại` và `mở mốc mới`
- Mức tiêu hao food, repair, mana item và fuel hợp lý cho mỗi macro-stage
- Giá trị thực tế của stable gate so với việc vẫn chạy tay từ base
- Lượng stat point từ mở tầng so với boss và milestone
- Mức sink cần thiết để low-tier resource không mất giá quá sớm nhưng cũng không gây inflation
