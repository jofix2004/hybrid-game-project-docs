Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 06/03/2026

# Player Progression

Tài liệu này mô tả cách người chơi mạnh dần lên theo thời gian ở cấp độ `player-facing progression`. Nếu `Player Stats` trả lời câu hỏi “chỉ số nền cá nhân tăng ra sao”, thì `Player Progression` trả lời câu hỏi lớn hơn: người chơi thật sự mạnh lên qua những lớp nào, theo nhịp nào, thấy mục tiêu kế tiếp ở đâu, và boss / milestone đóng góp gì vào hành trình đó.

## Mục tiêu

- Chốt các lớp tiến trình thật sự làm người chơi mạnh lên.
- Làm rõ nguồn `điểm chỉ số`, nhịp `mở tầng`, và vai trò `boss / milestone contribution`.
- Tách rõ cái gì là tăng trưởng của người chơi, cái gì là tăng trưởng của thế giới / căn cứ / logistics.
- Giữ đúng tinh thần game: progression phải mở thêm cách chơi, không chỉ làm số to hơn.

## Phạm vi

Tài liệu này tập trung vào:
- các lớp sức mạnh mà người chơi cảm được trực tiếp theo thời gian
- nguồn nhận điểm chỉ số và cách nó chen vào tiến trình chung
- nhịp tiến trình người chơi qua các chặng từ đầu game tới giữa game và sâu hơn
- vai trò của boss, gate, utility, workstation, mana và route ổn định trong việc làm người chơi “mạnh lên thật”

Tài liệu này không đi sâu vào:
- công thức từng chỉ số cụ thể
- schema chi tiết của item, workstation, boss hay gate
- world progression ở cấp biome / floor layout
- balance số cho từng tầng, từng boss hay từng tier

## Source Coverage

### Nguồn bắt buộc

- [10_QUESTIONS_LEVEL_6.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/10_QUESTIONS_LEVEL_6.md)
  - là nguồn xương sống cho các trục progression, chia chặng phát triển, faucet / sink, và build variety
- [11_QUESTIONS_LEVEL_7.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/11_QUESTIONS_LEVEL_7.md)
  - dùng như guardrail để giữ doc trong phạm vi thực thi hợp lý, không phình thành design tree quá tải sản xuất
- [12_QUESTIONS_LEVEL_8.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/12_QUESTIONS_LEVEL_8.md)
  - khóa rule gameplay cụ thể cho player core state, stat point, mana usage, gate milestone, boss farm và recovery
- [13_PLAYER_CORE_STATE_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/13_PLAYER_CORE_STATE_SHEET.md)
  - là nguồn đúng trực tiếp cho điểm chỉ số, all-in, respec, và phần tăng trưởng cá nhân
- [15_GATE_AND_BOSS_MILESTONE_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/15_GATE_AND_BOSS_MILESTONE_SHEET.md)
  - khóa contribution của boss gatekeeper, stable gate, farm boss và milestone world-persistent

### Nguồn đối chiếu bắt buộc

- [Player Stats.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/03_PLAYER_SYSTEMS/Player%20Stats.md)
  - dùng để không lặp hoặc mâu thuẫn về stat list, điểm chỉ số, current / max rule và respec
- [Long Progression Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Long%20Progression%20Loop.md)
  - dùng để đảm bảo `Player Progression` là lát cắt player-facing của macro progression, không viết lại toàn bộ long progression
- [Core Gameplay Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Core%20Gameplay%20Loop.md)
  - dùng để kiểm tra progression có còn nuôi đúng câu hỏi `đi tiếp hay quay về`

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - Doc này đã đủ rõ để làm nguồn cho `Equipment System`, `Dungeon Progression`, `Boss System`, `Crafting Economy` và các bảng data progression về sau.
  - Các con số chính xác như mỗi tầng cho bao nhiêu điểm, mỗi boss cho bao nhiêu điểm hay chặng nào nên mở bao nhiêu utility vẫn thuộc lớp balance.

## Conflict Resolution

- `Level 6` xác định người chơi mạnh lên chủ yếu qua:
  - đồ và công cụ
  - utility expedition
  - căn cứ và workstation
  - mana như lớp năng lượng thật
  - chiều sâu và tuyến đi ổn định
- `Level 6` cũng nói rõ `Character Level Tree` chưa cần nếu các trục trên đã đủ dày.
- `Level 8` và `Sheet 13` khóa bản final:
  - vẫn có lớp tăng trưởng nền cá nhân
  - nhưng rất hẹp, đi qua `điểm chỉ số`
  - không phải thanh EXP liên tục
  - không thành class tree
- `Sheet 15` khóa vai trò boss / gate trong progression:
  - boss gatekeeper tạo cửa sổ ổn định cho gate
  - stable gate là phần thưởng dài hạn cực mạnh
  - gọi lại boss để farm không rơi lại milestone
- Khi cần ưu tiên wording:
  1. `Long Progression Loop` cho macro shape
  2. `Player Stats` cho lớp điểm chỉ số
  3. `Sheet 15` cho contribution của boss / gate

## Rule Summary

- Người chơi mạnh lên không chỉ qua một trục.
- Các lớp tiến trình player-facing chính là:
  - `Gear / Tool Quality`
  - `Utility Expedition`
  - `Base and Workstation Support`
  - `Mana Literacy and Mana Usage`
  - `Stat Point Investment`
  - `Depth Access and Stable Route`
- Trong đó:
  - `điểm chỉ số` là lớp tăng trưởng nền cá nhân
  - `gear / utility / mana / route ổn định` mới là thứ đổi chất lượng run mạnh nhất
- Nguồn điểm chỉ số:
  - `mở tầng` là nguồn chính
  - `boss / milestone` là nguồn phụ
- Boss không phải lúc nào cũng là cổng chặn tuyệt đối.
  - Người chơi vẫn có thể lách sâu hơn trong một số trường hợp
  - nhưng nếu muốn biến mốc sâu thành `tuyến dùng được lâu dài`, thường phải xử lý boss giữ gate
- Stable gate, workstation tốt hơn, utility đúng chỗ và mana extraction là những thứ làm người chơi “mạnh lên” ngay cả khi damage không tăng nhiều.

## Các Lớp Progression Của Người Chơi

### 1. Gear Và Tool Progression

Người chơi cảm nhận mình mạnh lên đầu tiên qua:
- tool khai thác tốt hơn
- vũ khí đáng tin hơn
- giáp và artifact hỗ trợ đúng tình huống hơn
- đồ bền hơn, sửa dễ hơn, mang đi an tâm hơn

Đây là lớp progression chạm trực tiếp nhất vào cảm giác điều khiển và chuyến đi.

### 2. Utility Expedition Progression

Người chơi mạnh lên không chỉ vì đánh khỏe hơn, mà vì:
- chịu được hazard tốt hơn
- mang đủ đồ cho chuyến dài hơn
- sửa đồ, tháo đồ, hồi phục, hỗ trợ môi trường tốt hơn
- xử lý được nhiều tình huống mà đầu game không xử lý nổi

Đây là lớp progression đổi “cách sống sót” chứ không chỉ đổi chỉ số.

### 3. Base Và Workstation Support

Base không phải meta ngoài lề.
Nó là lớp progression trực tiếp làm người chơi mạnh hơn qua:
- repair rẻ hơn, nhanh hơn
- craft đồ cao hơn
- chiết xuất mana
- chuẩn bị loadout tốt hơn
- phục hồi sau thất bại nhẹ hơn

Một người chơi có căn cứ khỏe thực chất là một người chơi mạnh hơn ở cấp expedition.

### 4. Mana Literacy Và Mana Usage

Từ khoảng tầng 3+ trở đi, mana không còn là flavor.
Người chơi mạnh lên qua mana khi:
- biết tìm quặng mana
- biết mang nó về chiết xuất
- biết dùng mana cho tool, utility, machine
- biết khi nào dùng mana cá nhân, khi nào dựa vào network / infrastructure

Đây là cú chuyển pha giữa game.

### 5. Stat Point Investment

Đây là lớp tăng trưởng nền cá nhân mỏng nhưng rõ.
Người chơi đầu tư vào:
- `Máu tối đa`
- `Mana tối đa`
- `Độ tụt thức ăn`

Lớp này cho phép build cá tính hơn, nhưng không được thay thế vai trò của gear, utility, repair, mana logistics và stable route.

### 6. Depth Access Và Stable Route

Người chơi thật sự mạnh lên khi:
- đi sâu được
- quay về được
- rồi đi lại được nhiều lần với giá rẻ hơn và ổn định hơn

Vì vậy, `mở tầng`, `sửa gate`, `ổn định route`, `giảm chi phí quay lại` đều là progression của người chơi, không chỉ là progression của thế giới.

## Nguồn Tiến Trình Chính

### Mở tầng

- Là nguồn tiến trình cá nhân quan trọng nhất.
- Là nguồn chính cho `điểm chỉ số`.
- Đồng thời cũng là chỉ báo rằng người chơi đã đủ mạnh để bước vào lớp nguy hiểm / reward mới.

### Tài nguyên mang về

- Là nguồn mở khóa thực dụng nhất.
- Nuôi:
  - gear
  - repair
  - utility
  - workstation
  - machine
  - mana infrastructure

### Boss và milestone

- Là nguồn phụ cho `điểm chỉ số`.
- Là nguồn chính cho:
  - cửa sổ ổn định tuyến
  - phần thưởng mốc
  - mở nhánh utility / gate / machine lớn

### Research / blueprint / unlock tổ chức hóa

- Là lớp định hướng và hệ thống hóa.
- Không thay thế hoàn toàn khám phá thật.
- Người chơi vẫn phải ra ngoài, lấy đúng thứ, chạm đúng mốc thì unlock mới có ý nghĩa.

## Nhịp Mở Tầng

- `Mở tầng` là nhịp tiến trình cá nhân rõ nhất của game.
- Mỗi lần mở được một tầng mới, người chơi nên cảm được ít nhất một trong các thay đổi sau:
  - có thêm nguồn tài nguyên mới
  - có thêm mức nguy hiểm và reward mới
  - có thêm utility hoặc preparation requirement mới
  - có thêm một bước tăng trưởng nền cá nhân qua `điểm chỉ số`
  - có thêm tín hiệu rõ về mục tiêu kế tiếp như boss, gate, quặng mana, workstation tier hoặc tuyến sâu hơn
- Nhịp đúng không phải là:
  - mở tầng chỉ để thấy map khác
  - hoặc mở tầng nhưng cách chơi không đổi
- `Mở tầng` là nguồn chính cho stat point vì nó buộc tăng trưởng cá nhân phải bám vào chiều sâu, thay vì bám vào farm lặp an toàn.
- `Boss / milestone` chen vào như nhịp phụ để làm các mốc mở tầng nặng hơn, đáng nhớ hơn và có trọng lượng hơn, nhưng không thay thế hoàn toàn vai trò của việc tự mình đi sâu.

## Nhịp Progression Theo Chặng

### Chặng 1: Sống sót tay trắng

Người chơi mạnh lên qua:
- tool cơ bản
- nhịp farm gần
- food / repair tối thiểu
- căn cứ tạm

Ở chặng này, progression phải cho cảm giác:
- “mình vừa thoát khỏi cảnh quá yếu”
- chứ chưa phải “mình đã có build mạnh”

### Chặng 2: Ổn định công cụ và utility

Người chơi mạnh lên qua:
- tool và gear đáng tin hơn
- utility expedition
- workstation đầu tiên
- inventory / repair flow bớt đau hơn

Ở chặng này, chuyến đi bắt đầu có lời đều hơn và ít phụ thuộc may mắn hơn.

### Chặng 3: Chạm mana

Người chơi mạnh lên qua:
- quặng mana
- máy chiết xuất
- utility / machine dùng mana
- chuẩn bị cho tầng sâu hơn

Đây là lúc progression đổi chất rõ rệt nhất.

### Chặng 4: Gate và logistics tầng sâu

Người chơi mạnh lên qua:
- boss gatekeeper
- sửa gate
- ổn định tuyến đi
- giảm cost cho run tương lai

Ở chặng này, sức mạnh không còn đo bằng chỉ số hay gear đơn lẻ, mà bằng khả năng vận hành chiều sâu bền vững.

## Boss Và Milestone Contribution

### Boss contribution

- Boss là nguồn phụ cho `điểm chỉ số`
- Boss là nguồn loot đặc thù tùy loại
- Boss là mốc chiến lược để:
  - sửa gate yên hơn
  - mở route ổn định
  - chốt một lớp utility / machine / logistics mới

### Milestone contribution

- Milestone không nên rơi lại vô hạn.
- Phần thưởng milestone đúng là:
  - mở quyền dùng / mở quyền đi
  - mở route ổn định
  - mở công trình / utility / gate tier lớn

### Farm lại boss

- Nếu gọi lại boss để farm:
  - chỉ rơi vật liệu farm
  - không rơi lại milestone

Điều này giữ cho progression không bị phá bởi farm vòng lặp.

## Mối Quan Hệ Giữa Player Progression Và Player Stats

- `Player Stats` là lớp tăng trưởng nền cá nhân hẹp.
- `Player Progression` là bức tranh lớn hơn về mọi cách người chơi mạnh lên.
- Một build nhiều HP hơn chưa chắc là một người chơi tiến xa hơn nếu:
  - tool yếu
  - utility thiếu
  - căn cứ nghèo
  - mana chưa vào vận hành
  - gate chưa ổn định

## Cost / Reward

### Cost của progression

Mọi bước tiến thật đều ăn vào:
- thời gian
- rủi ro
- vật tư chuyến đi
- repair
- utility
- thất bại có thể làm chậm nhịp mở mốc

### Reward đúng

Một bước tiến đúng phải đem lại ít nhất một trong các thứ sau:
- chuyến đi an toàn hơn
- chuyến đi lời hơn
- chuyến đi sâu hơn
- chuyến đi hồi phục đỡ đau hơn
- mở thêm một cách giải quyết mới

Nếu reward chỉ là “số tăng nhẹ nhưng cách chơi không đổi”, progression đang yếu.

## Failure And Recovery

### Thất bại không được xóa progression nền

Sau một thất bại nặng:
- mất loot của run
- mất consumable
- phải recovery

Nhưng không được mất:
- điểm chỉ số đã đầu tư
- stable gate đã ổn định
- căn cứ và workstation nền
- các unlock nền đã mở

### Recovery vẫn là progression

Một người chơi đang recovery vẫn có thể tiến bộ nếu:
- sửa lại loadout
- mở thêm utility nền
- ổn định lại căn cứ
- làm các run ngắn để vá lớp yếu

Progression tốt không phải progression “không bao giờ thua”, mà là progression “thua xong vẫn còn đường gượng dậy”.

## Signs Of Good Player Progression

- Người chơi luôn còn thấy một mục tiêu kế tiếp đủ rõ.
- Mỗi chặng mở thêm một cách chơi hoặc một kiểu chuẩn bị mới.
- Mana xuất hiện như một chuyển pha thật, không quá sớm, không quá muộn.
- Stable gate tạo cảm giác rất đáng giá.
- Build variety đến từ ưu tiên đầu tư, không phải từ class cứng.
- Stat point có giá trị, nhưng không át các lớp progression khác.

## Signs Of A Broken Player Progression

- Mạnh lên chỉ là tăng số.
- Gear mới xóa sạch vai trò của đồ cũ quá sớm.
- Mana đến sớm tới mức survival nền mất ý nghĩa, hoặc muộn tới mức giữa game phẳng lì.
- Boss chỉ là khóa cứng chứ không tạo ra giá trị route / logistics.
- Stable gate mở xong mà nhịp chơi không khác đáng kể.
- Chỉ số nền mạnh đến mức người chơi bỏ qua utility, repair, machine và base.

## Implementation Hooks

- Cần tracking tối thiểu cho:
  - `highest_floor_opened`
  - `boss_milestones_cleared`
  - `stable_gates_opened`
  - `stat_points_total`
  - `stat_points_unspent`
  - `mana_phase_unlocked`
  - `workstation_tier_reached`
- Cần tag progression source cho từng lần tăng trưởng:
  - `floor_open`
  - `boss_milestone`
  - `world_milestone`
  - `gear_upgrade`
  - `utility_unlock`
  - `mana_unlock`
  - `gate_stable`
- Cần telemetry cho:
  - thời gian từ đầu game tới khi có điểm chỉ số đầu tiên
  - thời gian từ tầng đầu tới khi chạm mana
  - thời gian từ lần thấy gate đầu tiên tới khi ổn định gate đầu tiên
  - tỷ lệ người chơi all-in vào từng chỉ số

## Open Design Questions

- Mỗi tầng thường nên cho bao nhiêu điểm chỉ số.
- Boss thường nên cho `1 điểm` hay nhóm boss lớn mới cho nhiều điểm.
- Milestone nào ngoài boss nên cho điểm chỉ số.
- Mốc nào nên được xem là “đã chạm mana thật sự” trong bản balance cuối.

## Open Balance Variables

- Chênh lệch hợp lý giữa progression từ `stat point` và progression từ `gear / utility / gate`
- Tốc độ mở tầng mong muốn giữa các macro-stage
- Giá trị thực tế của stable gate so với chạy tay
- Tỷ lệ contribution của boss / milestone vào tổng tăng trưởng cá nhân
