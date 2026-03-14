Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 11/03/2026

# World Generation

Tài liệu này chốt `grammar của thế giới` ở cấp world-scale: thế giới game được tổ chức thành những lớp nào, lớp nào là nền khám phá chính, lớp nào là nút nội dung đậm, mặt đất và lòng đất quan hệ với nhau ra sao, biome, POI, interior, route, gate và boss milestone cắm vào bản đồ kiểu gì, và thế giới phải được sinh ra theo nguyên tắc nào để luôn nuôi đúng core loop.

Doc này không coi world generation chỉ là chuyện `seed + chunk + streaming`. Đó là lớp kỹ thuật bắt buộc phải có, nhưng chưa đủ để định nghĩa thế giới. Về mặt design, thế giới của game này phải luôn đọc ra được 4 sự thật:
- đây là một `đảo hoang` nhìn ra biển, nơi mặt đất vẫn còn sống được
- `mặt đất chỉ là nơi bám trụ`, không phải nơi chứa giá trị lớn nhất
- `giá trị thật nằm dưới lòng đất`
- phần dưới lòng đất được tổ chức thành `nhiều tầng hang tự nhiên`, và `mỗi tầng hang có một biome đặc thù`

## Mục tiêu

- Thay stub cũ bằng một doc production dùng được cho design, code, content và QA.
- Chốt thế giới như một `đảo hoang + nhiều tầng hang tự nhiên`, không phải sandbox vô hạn rời rạc hay chuỗi room tuyến tính.
- Tách rõ các lớp:
  - `surface`
  - `cave floor`
  - `biome identity`
  - `POI / structure`
  - `interior / dungeon pocket`
  - `gate milestone`
  - `boss milestone`
- Khóa nguyên tắc placement cho:
  - tài nguyên
  - mối nguy
  - route
  - POI
  - gate
  - boss
  - mana layer
- Giữ ranh giới giữa:
  - rule world generation ở cấp design
  - thuật toán seed / chunk / streaming ở cấp technical design

## Phạm vi

Tài liệu này tập trung vào:
- hình dáng tổng thể của thế giới
- quan hệ giữa surface island và underground cave stack
- các lớp nội dung chồng lên nhau trong world
- nguyên tắc phân vùng biome, resource, hazard và route
- vai trò của POI, ruins, structure và interior
- placement philosophy cho gate, boss và các mốc chiều sâu
- world persistence ở mức design-facing

Tài liệu này không đi sâu vào:
- thuật toán noise hay graph generation cụ thể
- công thức seed cụ thể
- data layout của chunk streaming
- schema netcode chi tiết
- số liệu spawn exact

## Source Coverage

### Nguồn bắt buộc

- [06_QUESTIONS_LEVEL_2.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/06_QUESTIONS_LEVEL_2.md)
  - là nguồn cho:
    - nhịp chuẩn bị rồi đi ra ngoài
    - vai trò của chuyến đi ngắn và chuyến đi sâu
    - lý do người chơi luôn còn “một bước tiếp theo rất cụ thể”
- [09_QUESTIONS_LEVEL_5.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/09_QUESTIONS_LEVEL_5.md)
  - là nguồn xương sống cho:
    - biome
    - tài nguyên theo lớp sâu
    - POI / structure / interior
    - boss milestone trong không gian world
- [11_QUESTIONS_LEVEL_7.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/11_QUESTIONS_LEVEL_7.md)
  - dùng để khóa:
    - host authority và shared world save
    - chunk / zone boundary
    - simplified simulation vùng xa
    - data-driven content pipeline
- [12_QUESTIONS_LEVEL_8.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/12_QUESTIONS_LEVEL_8.md)
  - dùng để đối chiếu:
    - state model của gate, boss, node và world interaction
    - gate milestone, death/recovery và world state liên quan
- [15_GATE_AND_BOSS_MILESTONE_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/15_GATE_AND_BOSS_MILESTONE_SHEET.md)
  - dùng để cắm đúng:
    - gate milestone
    - gatekeeper boss
    - route ổn định
    - world-persistent gate state

### Nguồn đối chiếu bắt buộc

- [Core Concept.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/00_GAME_VISION/Core%20Concept.md)
- [Core Gameplay Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Core%20Gameplay%20Loop.md)
- [Long Progression Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Long%20Progression%20Loop.md)
- [Floor Hierarchy.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/05_DUNGEON_SYSTEM/Floor%20Hierarchy.md)
- [Dungeon Progression.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/07_PROGRESSION_SYSTEM/Dungeon%20Progression.md)
- [Boss System.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/05_DUNGEON_SYSTEM/Boss%20System.md)

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - doc này đủ rõ để làm nguồn đúng cho:
    - `Biomes.md`
    - `Flora.md`
    - `Fauna.md`
    - `Dungeon Generation.md`
    - `Room Types.md`
    - `Trap System.md`
    - `Resource Distribution.md`
    - các doc technical về chunk, save và streaming
  - các chi tiết như:
    - số biome cụ thể
    - tỷ lệ xuất hiện từng POI
    - noise rule
    - graph connectivity cụ thể
    vẫn là lớp content / technical sau

## Conflict Resolution

- Stub cũ từng hiểu `World Generation` gần như chỉ là:
  - seed
  - chunk
  - streaming
  - consistency khi save/load

  Hướng đó đúng nhưng quá hẹp.

- Stub cũ cũng từng tách:
  - `hang mở theo chiều sâu`
  - `depth layer`
  - `biome layer`

  theo cách khiến `chiều sâu` và `biome` gần như là hai thứ rời nhau, và còn cho phép `biome lặp nhiều tầng` như quy tắc mặc định. Hướng đó không còn đúng với model thế giới hiện tại.

- Quyết định cuối:
  - `World Generation` ở đây là doc design + system-facing về cấu trúc thế giới
  - `seed / chunk / streaming` chỉ là implementation hook
  - thế giới không phải:
    - world vô hạn không mục tiêu
    - room crawler tuyến tính
    - hay map phẳng chỉ reskin biome
  - thế giới là:
    - một `đảo hoang` làm nơi bám trụ
    - một `surface` còn sống được với số biome mặt đất còn hạn chế
    - một `stack nhiều tầng hang tự nhiên` là trục khám phá thật
    - mỗi `tầng hang` có `một biome đặc thù` làm identity chính
    - với `POI / ruins / interior / dungeon / gate / boss` như các nút nội dung đậm cắm vào từng tầng hang

## Rule Summary

- Bề mặt là nơi:
  - sống
  - dựng base
  - hồi phục
  - tiêu hóa loot
  - chuẩn bị chuyến đi
- Surface hiện tại của đảo chỉ giữ vài biome nền cho MVP:
  - `rừng rậm`
  - `đồng bằng`
  - `bãi biển`
- Lòng đất là nơi:
  - tạo risk/reward chính
  - chứa tài nguyên chiến lược
  - chứa mana từ tầng 3+
  - chứa gate milestone và boss milestone
- Underground không được sinh theo kiểu:
  - chỗ nào cũng đậm như nhau
  - mọi vùng đều có giá trị ngang nhau
  - mọi route đều an toàn như nhau
- `Hang tự nhiên` phải là nền chính của khám phá.
- `Tầng hang` là đơn vị chính để tổ chức:
  - risk/reward
  - logistics
  - mana exposure
  - route stability
  - gate / boss milestone
- Mỗi `tầng hang` phải có `một biome đặc thù` đủ rõ để người chơi cảm nhận mình đã sang một lớp sâu mới.
- `POI / structure / dungeon pocket` phải là `nút nội dung đậm`, không thay thế toàn bộ tầng hang.
- `Interior` là nội dung nén bên trong các POI / structure / dungeon, không phải format chính của toàn bộ world.
- Gate và boss milestone phải thưa, có trọng lượng và gắn với route ổn định.
- World save phải giữ được những thay đổi world-facing thật sự có giá trị dài hạn.

## World Generation Role In The Game

## 1. Tạo nền cho quyết định “đi đâu hôm nay”

World generation phải làm cho câu hỏi `đi đâu hôm nay` có nghĩa. Người chơi không nên thấy mọi hướng chỉ khác màu. Mỗi hướng phải có lý do riêng:
- tài nguyên gì
- nguy hiểm gì
- lời hứa gì
- mức chuẩn bị cần gì

## 2. Giữ surface có giá trị mà không cướp vai trò lòng đất

Surface phải đủ hữu dụng để:
- hồi
- xây
- vá
- nuôi loop recovery

Nhưng không được giàu tới mức thay thế lòng đất. Giá trị thật phải kéo người chơi xuống dưới.

## 3. Tạo lời hứa “bên dưới còn thứ đáng để liều”

World generation tốt phải luôn giữ được cảm giác:
- còn tầng hang chưa chạm
- còn biome chưa hiểu
- còn POI / dungeon chưa dò
- còn mốc gate chưa ổn định
- còn resource band chưa khai thác được

## World Layers

## 1. Surface Layer

Lớp này gồm:
- spawn gốc
- base area
- các vùng tài nguyên nền
- vùng hồi phục và tổ chức loadout
- các biome mặt đất hiện tại:
  - `rừng rậm`
  - `đồng bằng`
  - `bãi biển`

Vai trò:
- neo người chơi vào một nơi hiểu được
- tạo nhịp an toàn giữa các chuyến đi
- giữ game có nơi “sống” chứ không chỉ có nơi “liều”

## 2. Cave Floor Layer

Đây là lớp khám phá chính của phần dưới lòng đất.

Đặc điểm:
- là các `tầng hang tự nhiên`
- tổ chức theo chiều sâu
- có route phân nhánh
- có thể có giếng sụt, lối phụ, vực, hồ ngầm, đường nguy hiểm
- không tổ chức toàn bộ bằng chuỗi phòng liên tục

Mỗi `tầng hang` là một đơn vị hoàn chỉnh ở cấp world generation, đủ để gắn:
- một biome chính
- một reward profile
- một threat profile
- một mức logistics riêng
- một lớp milestone có thể có hoặc không có

## 3. Biome Identity Layer

Biome ở doc này không phải một lớp rời hẳn khỏi tầng. Ở model hiện tại:
- mỗi `tầng hang` có `một biome đặc thù` làm identity chính
- biome đổi sẽ kéo theo đổi:
  - tín hiệu nhận biết
  - reward profile
  - threat profile
  - cách chuẩn bị

Subzone nhỏ hoặc dungeon pocket có thể khác nhẹ về chất, nhưng không được xóa identity chính của tầng.

## 4. POI / Structure Layer

Đây là các nút nội dung đậm như:
- ruins
- altar
- mỏ cổ
- trại bỏ hoang
- cổng tầng
- khu canh giữ loot
- khu milestone

Vai trò:
- hút khám phá
- đổi nhịp
- nén risk/reward
- đặt milestone

## 5. Interior / Dungeon Pocket Layer

Lớp này chỉ dùng khi người chơi bước vào structure / ruins / công trình đặc biệt / dungeon pocket.

Vai trò:
- nén content
- tạo:
  - phòng loot
  - phòng bẫy
  - phòng giao tranh
  - mê cung ngắn
  - phòng khóa
  - phòng boss / guardian

`Dungeon` ở đây là pocket nội dung đậm cắm vào trong một tầng hang, không phải toàn bộ underground.

## World Structure Principles

## 1. World phải đọc được ở cấp macro

Người chơi phải hiểu nhanh:
- đâu là chỗ sống
- đâu là chỗ farm nền
- đâu là chỗ liều
- đâu là mốc đáng nhớ

## 2. Không để mọi thứ phẳng đều

World tốt phải có:
- vùng nền
- vùng chuyển pha
- vùng đậm nội dung
- vùng reward lớn nhưng rút lui đau

## 3. Không để mọi nút quan trọng trở thành handmade bắt buộc

World generation phải chừa chỗ cho:
- data-driven spawn rule
- biome rule
- POI set
- resource distribution

Nhưng vẫn cho phép:
- milestone boss
- ruins đặc biệt
- gate quan trọng
- một số interior ký ức

được hand-made hơn.

## 4. Tách “khám phá chính” và “nội dung nén”

- khám phá chính: `surface` rồi `hang tự nhiên theo tầng`
- nội dung nén: `POI / ruins / interior / dungeon pocket`

Nếu phần lớn thời gian chơi diễn ra trong `room chain` thay vì `hang tự nhiên`, doc này đang bị vi phạm.

## Placement Axes

## 1. Reward Axis

Mỗi vùng phải gắn rõ với:
- resource nền
- resource chiến lược
- mana material
- milestone material

## 2. Threat Axis

Mỗi vùng phải có trọng tâm nguy hiểm rõ:
- visibility
- địa hình
- quái
- trap
- ăn mòn / nhiệt / độc / tối / rơi vực

## 3. Preparation Axis

Mỗi vùng phải gợi ý người chơi cần chuẩn bị gì:
- food
- tool tier
- repair
- utility
- mana support
- hồi phục

## 4. Milestone Axis

Một số vùng phải đóng vai:
- route reward
- gate milestone
- boss milestone
- POI ký ức

Nhưng không phủ đều lên toàn bộ map.

## Relationship Between Surface, Cave Floor, POI, And Interior

## Surface

Là lớp recovery và organization.

## Cave Floor

Là lớp khám phá mặc định của underground.

## POI / Structure

Là các điểm đổi nhịp trong từng tầng hang.

## Interior / Dungeon

Là lớp nén của POI, không phải world default.

## Guardrail

Nếu world generation làm cho phần lớn thời gian chơi diễn ra trong `room chain` thay vì `hang tự nhiên`, doc này đang bị vi phạm.

## Relationship With Floor Hierarchy And Dungeon Progression

[Floor Hierarchy.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/05_DUNGEON_SYSTEM/Floor%20Hierarchy.md) định nghĩa:
- mặt đất là đảo hoang
- underground là nhiều tầng hang
- mỗi tầng hang có một biome đặc thù
- tầng 3+ là mốc mana
- gatekeeper và gate chỉ xuất hiện ở các mốc đáng giá

`World Generation` phải tạo ra world đủ chỗ để các lớp đó được cảm nhận bằng:
- địa hình
- ánh sáng
- vật liệu nền
- loot profile
- hazard
- route shape

[Dungeon Progression.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/07_PROGRESSION_SYSTEM/Dungeon%20Progression.md) định nghĩa:
- Reached
- Unstable Access
- Milestone-Blocked
- Stable Route Unlocked
- Established Exploitation Layer

`World Generation` phải sinh ra world có thể chứa được các state đó một cách tự nhiên.

Ví dụ:
- phải có route phụ để lách
- phải có route chính để ổn định
- phải có chỗ đặt gate hợp lý
- phải có chỗ đặt boss gatekeeper đủ đáng giá

## Relationship With Boss And Gate

## Gate placement

Gate không nên rải như shortcut tiện lợi đơn thuần.

Gate nên đặt ở:
- mốc đổi tầng hang hoặc đổi lớp route quan trọng
- route có giá trị logistics cao
- nút mà khi ổn định sẽ đổi chất các chuyến đi sau

## Boss placement

Boss gatekeeper nên đặt ở:
- chỗ có ý nghĩa route thật
- chỗ nếu vượt qua sẽ giảm cost tương lai thật

Boss không nên đặt chỉ để:
- chặn cho có
- tăng combat density
- kéo dài đường tuyến tính giả

## World Signal Requirement

Khi người chơi thấy gate hoặc vùng boss milestone, world phải phát tín hiệu rõ:
- đây là chỗ có trọng lượng hơn hang thường
- đây là nút đổi nhịp
- đây là lời hứa về route ổn định

## Relationship With Save And Persistence

World generation phải giả định từ đầu rằng đây là `shared world progression`.

Vì vậy world save cần giữ:
- base
- workstation
- công trình
- stable gate
- boss milestone state
- thay đổi chunk đáng kể
- một phần depletion và state world quan trọng

Không phải mọi hòn đá lẻ đều cần persistence cùng cấp, nhưng milestone world-facing phải được giữ chắc.

## World Simulation Boundaries

Ở cấp design-facing, thế giới nên được hiểu là:
- mô phỏng đầy đủ quanh người chơi
- simplified simulation ở xa

Điều này áp dụng cho:
- AI
- machine state
- respawn rule
- depletion / refill nhẹ
- hazard logic xa

Mục tiêu:
- giữ cảm giác world sống
- nhưng không ép mô phỏng đầy đủ toàn bộ đảo và toàn bộ stack hang cùng lúc

## Core Flows

## 1. First Surface To Cave Flow

1. Người chơi chuẩn bị ở surface.
2. Đi vào tầng hang nông.
3. Nhận ra surface chỉ là điểm bám, còn reward thực nằm bên dưới.

## 2. New Cave Floor Discovery Flow

1. Người chơi đi sâu hơn xuống một tầng hang mới.
2. Tầng mới phải đổi ít nhất:
   - tín hiệu
   - mối nguy
   - phần thưởng
   - cách chuẩn bị
3. Người chơi hiểu mình vừa bước sang một biome mới của underground, không chỉ là “hang cũ khó hơn”.

## 3. POI Attraction Flow

1. Người chơi đang đi trong hang tự nhiên.
2. Thấy một POI, ruins hoặc dungeon pocket đủ khác để bị hút vào.
3. POI đổi nhịp chuyến đi:
   - đáng liều hơn
   - đậm reward hơn
   - hoặc đậm milestone hơn

## 4. Milestone World Flow

1. Người chơi chạm một route sâu có gate hoặc boss.
2. Thế giới cho thấy đó là mốc lớn chứ không chỉ là loot spot.
3. Khi mốc được xử lý, world phải đổi trạng thái đủ rõ để người chơi cảm được tiến trình.

## Edge Cases

## 1. Dungeon pocket khác chất biome nền của tầng

- hợp lệ
- miễn là biome chính của tầng vẫn đọc được rõ
- dungeon là pocket nội dung đậm, không được xóa cảm giác người chơi vẫn đang ở trong một tầng hang có identity riêng

## 2. Không phải mọi vùng sâu đều có POI đậm

- hợp lệ
- POI phải là điểm nhấn, không phủ đặc mọi nơi

## 3. Người chơi có thể lách sâu hơn qua route phụ

- world phải có chỗ cho điều đó
- nhưng route phụ phải:
  - đau hơn
  - ít ổn định hơn
  - khó vận hành lâu dài hơn

## 4. Gate đã ổn định nhưng world quanh nó vẫn nguy hiểm

- hợp lệ
- gate ổn định không có nghĩa biome hay quái quanh đó bị vô hiệu
- nó chỉ đổi chất lượng logistics

## 5. Surface vẫn còn giá trị ở giữa game

- bắt buộc
- nếu surface mất sạch vai trò quá sớm, world sẽ mất nhịp recovery

## Signs Of Good World Generation

- người chơi luôn hiểu chỗ nào là `base`, chỗ nào là `liều`, chỗ nào là `nút nội dung`
- surface đọc ra rõ là `đảo hoang còn sống được`
- mỗi tầng hang mới được nhận ra bằng rule chơi chứ không chỉ màu
- hang tự nhiên vẫn là nền khám phá chính
- POI đủ mạnh để đổi nhịp nhưng không nuốt mất tầng hang
- mana layer từ tầng 3+ được cảm nhận rõ trong world
- gate và boss milestone có vị trí đáng nhớ, không lẫn vào nền
- world persistence giữ được cảm giác “thế giới này đã bị mình tác động”

## Signs Of Broken World Generation

- surface quá nghèo, thành nơi bỏ đi
- hoặc surface quá giàu, thay luôn lòng đất
- tầng hang mới chỉ là palette swap
- world toàn POI đậm, không còn nhịp thở
- hoặc world quá phẳng, thiếu nút hút khám phá
- gate / boss placement cơ học như checklist
- world save không giữ được những thay đổi đáng giá dài hạn

## Implementation Hooks

## World Region Definition Tối Thiểu

- `region_id`
- `world_layer`
- `surface_or_underground_class`
- `floor_id`
- `depth_index`
- `primary_biome_id`
- `resource_profile`
- `hazard_profile`
- `poi_pool`
- `milestone_role`
- `simulation_class`

## Runtime World State Tối Thiểu

- `discovered`
- `depleted_state`
- `milestone_state`
- `structure_state`
- `gate_state`
- `boss_state`
- `chunk_change_level`

## Placement Data Tối Thiểu

- `poi_frequency`
- `resource_density`
- `route_difficulty`
- `milestone_density`
- `mana_presence_class`
- `interior_template_pool`

## Technical Boundary Notes

- seed, chunk và streaming là lớp triển khai bắt buộc
- nhưng nên được triển khai để phục vụ grammar của doc này
- không đảo ngược việc technical constraint làm hỏng world fantasy đã khóa

## QA Hook Tối Thiểu

- reveal nhanh một tầng hang mới
- ép spawn biome tầng khác để kiểm tra rule khác biệt
- mở gate state / boss state trong world
- kiểm tra world save giữ:
  - base
  - structure
  - gate milestone
  - boss milestone
  - chunk change đáng kể

## Open Design Questions

- số biome lõi tối thiểu cho MVP
- tỷ lệ POI đậm trên mỗi tầng hang
- số route phụ nguy hiểm nên có trên mỗi cụm sâu để giữ khả năng “lách”
- mức độ surface nên mở rộng tới đâu trước khi bắt đầu loãng trọng tâm lòng đất

## Open Balance Variables

- mật độ resource nền trên surface
- độ dày POI theo tầng hang
- khoảng cách trung bình giữa các mốc gate
- tần suất đổi biome giữa các tầng hang
- tỷ lệ vùng sâu chỉ để khám phá so với vùng sâu gắn milestone
- mức persistence hợp lý cho depletion và chunk change
