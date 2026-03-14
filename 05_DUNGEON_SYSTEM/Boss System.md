Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 11/03/2026

# Boss System

Tài liệu này chốt `hệ boss` của game như một lớp nội dung milestone, áp lực và ký ức mạnh, không chỉ là “quái to hơn”. Nó trả lời các câu hỏi nền: boss tồn tại để làm gì trong loop này, có những họ boss nào, boss khác elite ở đâu, `gatekeeper boss` vận hành ra sao, khi nào boss được xem là reward milestone thay vì chỉ là loot pinata, boss reset và hồi sinh theo rule nào, và việc farm lại boss được phép tới mức nào mà không làm vỡ tiến trình.

Doc này là `grammar` cho toàn bộ lớp boss. Về sau:
- `Boss Database.md`
- `Boss Arenas.md`
- `Gate System.md`
- `Dungeon Progression.md`
- `Loot Tables.md`

sẽ cắm dữ liệu, encounter cụ thể, phase profile và con số balance vào khung này.

## Mục tiêu

- Thay stub cũ bằng một doc production dùng được cho design, code, content và QA.
- Chốt vai trò của boss trong game theo đúng fantasy hiện tại:
  - rare nhưng đáng nhớ
  - gắn với chiều sâu, milestone và logistics
  - kiểm tra chuẩn bị, quản lý tài nguyên và vị trí nhiều hơn là chỉ phản xạ
- Tách rõ:
  - `boss như một lớp nội dung`
  - `gatekeeper boss như một lớp milestone tiến trình`
- Khóa rule về:
  - aggro / disengage / reset
  - phase và state
  - boss respawn
  - refarm reward
  - quan hệ giữa boss và gate
  - boss hostile, boss special, boss non-hostile

## Phạm vi

Tài liệu này tập trung vào:
- vai trò gameplay của boss
- các họ boss chính
- state model và transition model cho boss
- rule riêng của `gatekeeper boss`
- reward, milestone và refarm loop
- quan hệ giữa boss với:
  - chiều sâu tầng
  - gate
  - route stability
  - progression dài hạn
  - co-op pressure

Tài liệu này không đi sâu vào:
- moveset chi tiết từng con boss
- hitbox, frame data, animation detail
- layout arena cụ thể
- bảng loot chi tiết từng boss
- con số máu, damage, cooldown cuối cùng

## Source Coverage

### Nguồn bắt buộc

- [09_QUESTIONS_LEVEL_5.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/09_QUESTIONS_LEVEL_5.md)
  - là nguồn nền cho:
    - vai trò của boss như content family
    - nguyên tắc “ít nhưng rõ vai trò”
    - phân vai boss theo milestone, biome, loot guard, technology
    - tiêu chí boss phải tạo cao trào thật, không chỉ là elite da khác
- [12_QUESTIONS_LEVEL_8.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/12_QUESTIONS_LEVEL_8.md)
  - là nguồn rule chi tiết cho:
    - behavior priority của gatekeeper boss
    - aggro / lose aggro / reset / respawn
    - máu boss, phase reset, farm loop
    - boss đa dạng từ hostile tới special NPC
- [15_GATE_AND_BOSS_MILESTONE_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/15_GATE_AND_BOSS_MILESTONE_SHEET.md)
  - là nguồn đúng cho:
    - gatekeeper boss
    - boss phá gate theo module
    - boss chết rồi hồi lại nếu gate chưa sửa xong
    - boss refarm không rơi lại milestone
    - boss biến mất để clear khu sau khi chết

### Nguồn đối chiếu bắt buộc

- [Long Progression Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Long%20Progression%20Loop.md)
  - dùng để đảm bảo boss vẫn là một milestone của tiến trình dài hạn, không trôi thành boss rush thuần
- [Multiplayer Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Multiplayer%20Loop.md)
  - dùng để giữ đúng vai trò boss trong co-op: áp lực hồi sinh, chia vai mềm, cứu nhau giữa áp lực
- [Floor Hierarchy.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/05_DUNGEON_SYSTEM/Floor%20Hierarchy.md)
  - dùng để cắm boss đúng vào trục chiều sâu, gate milestone và route stability
- [Crafting Economy.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/06_ECONOMY_SYSTEM/Crafting%20Economy.md)
  - dùng để đồng bộ refarm reward, gate material, boss material và economy của loot boss

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - doc này đủ rõ để làm nguồn đúng cho:
    - `Boss Database.md`
    - `Gate System.md`
    - `Boss Arenas.md`
    - `Dungeon Progression.md`
    - `Drop Tables.md`
  - phase detail, skill list, con số damage, con số HP và loot amount vẫn là lớp balance/content về sau

## Conflict Resolution

- Stub cũ từng hiểu boss theo hướng quá hẹp:
  - phase
  - cơ chế riêng
  - unique drop
  - phối hợp solo/co-op

  Cách hiểu đó không sai, nhưng quá hẹp so với game hiện tại.

- Quyết định cuối:
  - `Boss` là một lớp nội dung milestone hoặc major encounter có trọng lượng đặc biệt.
  - Boss không bắt buộc luôn là một con hostile thuần combat.
  - Có thể tồn tại:
    - boss hostile
    - boss deception / special behavior
    - boss thân thiện / NPC bán đồ / thực thể đặc biệt

- Tuy nhiên:
  - với core progression hiện tại, `gatekeeper boss` vẫn là lớp boss quan trọng nhất cho MVP và midgame progression.

- Quyết định bổ sung:
  - boss không được phép rơi thành “elite to hơn”.
  - boss phải làm ít nhất một trong các việc sau:
    - khóa milestone
    - đổi luật của khu vực
    - mở route ổn định
    - mở utility / technology / recipe
    - tạo ký ức mạnh cho một mốc sâu

## Rule Summary

- Boss phải là nội dung `hiếm nhưng đáng nhớ`.
- Tốt hơn là `ít boss nhưng rõ vai trò` thay vì nhiều boss na ná nhau.
- Boss nên kiểm tra:
  - chuẩn bị
  - quản lý tài nguyên
  - vị trí
  - đọc tình huống

  nhiều hơn là chỉ ép phản xạ.

- Không phải mọi boss đều là gatekeeper.
- Không phải mọi floor đều có boss.
- Không phải mọi boss đều hostile.
- `Gatekeeper boss` là boss milestone chuyên:
  - canh gate
  - gây áp lực lên hành vi sửa gate
  - biến việc ổn định route thành một bài test thật

- Gatekeeper boss có behavior priority:
  1. đánh người chơi
  2. phá gate định kỳ
  3. đi loanh quanh

- Khi boss còn sống:
  - người chơi vẫn có thể sửa gate từng phần
  - nhưng boss có thể phá module ngẫu nhiên
  - và có thể làm rơi mất một phần tài nguyên vừa nhét vào

- Boss gatekeeper chết:
  - biến mất ngay để clear khu
  - nếu gate chưa sửa xong thì bắt đầu bộ đếm hồi sinh
  - hồi sinh theo thời gian thực
  - hồi đầy máu như mới

- Gọi lại boss để farm:
  - bằng cách phá gate theo logic phá công trình
  - gate chỉ hỏng một phần
  - rơi ra một phần nguyên liệu ở khe sửa
  - gate ngừng hoạt động
  - boss gọi lại chỉ rơi vật liệu farm, không rơi lại milestone

## Boss Role In The Game

## 1. Tạo cột mốc cảm xúc

Boss là nơi game nén rủi ro, phần thưởng và ký ức thành một điểm chạm đậm hơn run thường. Chúng giúp người chơi nhớ:
- “chỗ này là mốc mình suýt chết”
- “mốc này là lần đầu mình mở được route thật”
- “boss này là lúc nhóm mình phải chuẩn bị tử tế hơn”

## 2. Kiểm tra readiness, không chỉ power

Một boss tốt trong game này không chỉ hỏi:
- damage đủ chưa

mà còn hỏi:
- food đủ chưa
- repair ổn chưa
- utility có phù hợp không
- đường lui có đủ không
- mana / fuel / gate logistics có đang quá mỏng không

## 3. Gắn boss vào progression thật

Boss phải đổi được trạng thái của thế giới hoặc trạng thái tiến trình:
- gate được sửa an toàn hơn
- route trở nên ổn định hơn
- công nghệ hoặc utility mới được mở
- tầng sâu trở thành thứ khai thác lâu dài được

## 4. Tạo áp lực không gian

Đặc biệt với gatekeeper boss, vai trò lớn nhất không chỉ là “đánh nhau”, mà là:
- khiến người chơi không thể yên ổn đứng sửa gate
- biến hành vi logistics thành hành vi có rủi ro chiến đấu

## Boss Families

## 1. Gatekeeper Boss

Vai trò:
- boss milestone cốt lõi của trục chiều sâu
- canh gate hoặc một route ổn định lớn
- gắn trực tiếp với việc sửa gate, mở route, giảm chi phí quay lại

Reward chính:
- cửa sổ an toàn để sửa gate
- ổn định route
- vật liệu farm phụ nếu gọi lại

## 2. Biome Boss

Vai trò:
- đại diện cho một biome hoặc một lớp nguy hiểm đặc thù
- làm đậm bản sắc của biome đó
- có thể khóa loot đặc trưng, POI đặc thù hoặc một bước tiến nhỏ trong mastery của biome

Reward chính:
- loot / material / utility gắn với biome
- ký ức và mastery của khu vực

## 3. Technology / Utility Milestone Boss

Vai trò:
- đứng ở mốc mở một lớp utility, machine, mana infrastructure hoặc công nghệ quan trọng
- không nhất thiết phải gắn với gate

Reward chính:
- recipe lớn
- material cho machine
- core item cho utility cao hơn

## 4. Loot Guardian / Mini-Boss

Vai trò:
- canh rare POI, rare cache, room đặc biệt hoặc tài nguyên hiếm
- nhỏ hơn boss milestone toàn cục nhưng vẫn đậm hơn enemy thường

Reward chính:
- loot giá trị cao
- material đặc thù
- room payoff mạnh

## 5. Special / Non-hostile Boss Entity

Vai trò:
- thực thể đặc biệt mang trọng lượng ngang boss nhưng không nhất thiết là combat hostile
- có thể là:
  - boss thân thiện
  - NPC bán đồ
  - thực thể lừa người chơi
  - encounter đặc biệt có logic riêng

Reward chính:
- world texture
- twist
- giao dịch / unlock / thông tin / utility

### Guardrail

- Lớp này là hợp lệ về mặt content.
- Nhưng không được dùng nó để làm mờ vai trò của `gatekeeper boss` trong core progression.

## Boss State Model

Doc này dùng một state model đủ rộng để chứa cả hostile boss lẫn special boss, nhưng hostile milestone boss vẫn là trường hợp chuẩn.

## 1. Dormant / Anchored

- boss đang neo ở khu vực của nó
- chưa vào combat active
- có thể:
  - canh gate
  - tuần tra
  - đứng chờ
  - làm hành vi ambience / special interaction

## 2. Aggro / Active

- boss đã coi người chơi là mục tiêu cần xử lý
- bắt đầu áp dụng AI priority, combat pressure hoặc hành vi cản milestone

## 3. Phase Active

- boss đang ở một phase cụ thể trong encounter
- số phase và điều kiện đổi phase là content/balance layer
- phase là state con của `Aggro / Active`

## 4. Disengaged / Resetting

- boss mất aggro hoặc người chơi rút đủ xa
- boss bắt đầu:
  - quay về anchor
  - hồi máu hay không hồi máu tùy loại
  - reset phase hay không tùy loại

## 5. Dead

- boss đã bị đánh bại
- với gatekeeper boss, thường sẽ biến mất khỏi khu ngay sau khi chết

## 6. Respawn Pending

- boss đã chết
- nhưng rule world cho phép hồi lại
- điển hình là gatekeeper boss khi gate chưa sửa xong

## 7. Special Interaction

- state này dùng cho boss special / non-hostile
- boss không đi theo flow combat chuẩn
- có thể giao dịch, lừa, đổi điều kiện, hoặc chờ trigger khác

## Boss Transition Rules

## Dormant / Anchored -> Aggro / Active

Xảy ra khi:
- người chơi bước vào vùng trigger
- boss nhìn thấy người chơi
- boss bị đánh
- người chơi đụng vào milestone mà boss canh

Chi tiết trigger:
- tùy boss type
- không có một rule cứng cho toàn bộ họ boss

## Aggro / Active -> Phase Active kế tiếp

Xảy ra khi:
- máu qua ngưỡng
- module gate bị chạm ngưỡng sự kiện
- người chơi vào vị trí / hành vi nhất định
- boss đạt điều kiện mechanic riêng

## Aggro / Active -> Disengaged / Resetting

Xảy ra khi:
- người chơi rút khỏi combat logic của boss
- boss mất mục tiêu đủ lâu

Rule chung:
- tùy loại boss, có con quay lại gate, có con hồi máu, có con không

## Disengaged / Resetting -> Dormant / Anchored

Xảy ra khi:
- boss về lại anchor
- reset xong phase / aggro state

## Any Hostile State -> Dead

Xảy ra khi:
- HP về 0

## Dead -> Respawn Pending

Xảy ra khi:
- boss được gắn rule hồi lại
- điển hình là gatekeeper boss khi gate chưa sửa xong

## Respawn Pending -> Dormant / Anchored

Xảy ra khi:
- bộ đếm hồi sinh kết thúc
- boss xuất hiện lại với trạng thái mới tinh

## Global Reset Rule

- Nếu người chơi rời khỏi hầm ngục hoặc tầng:
  - boss có thể `reset phase`
  - hoặc `reset hẳn`
  - tùy loại boss

## Gatekeeper-Specific Rules

## 1. Vai trò

Gatekeeper boss là boss milestone gắn trực tiếp với một gate hoặc route ổn định quan trọng.

Nó tồn tại để:
- cản người chơi
- đánh người chơi
- phá tiến độ sửa gate
- giữ cho “ổn định route” là một thành tựu thật

## 2. Behavior Priority

Thứ tự ưu tiên:
1. `Đánh người chơi`
2. `Phá gate định kỳ`
3. `Đi loanh quanh`

Ghi chú:
- hành vi phá gate có cooldown
- AI cụ thể vẫn có thể khác nhau theo từng boss

## 3. Gate Pressure Model

Khi gatekeeper boss còn sống:
- người chơi vẫn được phép sửa gate từng module
- boss có thể phá ngẫu nhiên một module đang có
- nếu module vừa được nhét tài nguyên:
  - có thể mất một phần tài nguyên vừa nhét

Điều này làm gate pressure trở thành:
- rủi ro vật lý
- không phải chỉ là tụt thanh tiến độ trừu tượng

## 4. Relationship With Repair Action

- Nếu người chơi đang sửa gate mà bị hit:
  - hủy thao tác sửa ngay

Điểm này giúp boss thực sự can thiệp vào logistics moment-to-moment, thay vì chỉ tồn tại như khóa mềm ở xa.

## 5. Death Window

Khi gatekeeper boss chết:
- boss biến mất ngay để clear khu
- người chơi có một cửa sổ yên hơn để sửa gate

Nhưng:
- nếu gate chưa sửa xong hoàn toàn
  - boss chỉ mới bị gỡ tạm
  - chưa phải milestone đã chốt vĩnh viễn

## 6. Respawn Rule

Gatekeeper boss chỉ hồi lại nếu:
- người chơi chưa sửa gate xong

Khi hồi lại:
- bộ đếm hồi sinh chạy theo thời gian thực
- boss hồi đủ máu như mới

## 7. Recall Rule

Người chơi có thể gọi lại boss bằng cách:
- phá gate theo logic phá công trình

Kết quả:
- một vài nguyên liệu ở khe sửa rơi ra
- gate ngừng hoạt động
- boss có thể được gọi lại để farm

## Aggro, Reset, And Persistence

## 1. Aggro Diversity

Game không dùng một rule aggro duy nhất cho mọi boss.

Boss có thể:
- ngu
- xảo quyệt
- lừa người chơi
- phản ứng mạnh khi người chơi chạm milestone
- hoặc chỉ bùng nổ combat khi trigger đúng vùng

## 2. Lose Aggro

Khi mất aggro:
- có boss quay lại anchor
- có boss hồi máu
- có boss không hồi máu
- có boss reset phase
- có boss chỉ giảm nhịp giao tranh

## 3. HP Persistence

Máu boss trong cùng một lần thám hiểm:
- tùy loại boss

Điều này cho phép có cả:
- boss giữ máu
- boss hồi một phần
- boss reset cứng

### Guardrail

- Những khác biệt này phải là `boss profile decision`.
- Không được để từng màn code tự xử lý theo cách khác nhau mà không có tag dữ liệu rõ.

## 4. Floor / Dungeon Exit Reset

Nếu người chơi rời khỏi tầng hoặc hầm ngục:
- boss có thể reset phase hoặc reset hẳn
- đây là global rule lớn, dễ đọc hơn cho người chơi

## Boss Rewards And Milestones

## 1. Boss Reward Không Chỉ Là Loot

Reward từ boss có thể là:
- safe window để sửa gate
- stable route
- utility unlock
- recipe unlock
- material mở machine
- loot chiến lược
- ký ức mạnh

## 2. Milestone Reward

`Milestone reward` là reward mốc lớn, không nên rơi vô hạn.

Ví dụ:
- core item để hoàn tất gate
- quyền mở route ổn định
- unlock recipe / technology lớn

## 3. Farm Reward

`Farm reward` là vật liệu có thể kiếm lại:
- combat material
- mana / magic material
- machine / ancient crafting material

## 4. Reward Tùy Loại Boss

Boss thiên chiến đấu:
- nghiêng về vật liệu combat

Boss dạng pháp sư / ma thú:
- nghiêng về mana, material phép, utility

Boss dạng máy móc / vật cổ:
- nghiêng về vật liệu chế tạo, machine part, ancient component

## Refarm Loop

## 1. Cho Phép Refarm, Nhưng Không Reset Milestone

Khi gọi lại boss để farm:
- chỉ rơi vật liệu farm
- không rơi lại milestone

Đây là rule khóa để:
- cho người chơi một loop farm phụ
- nhưng không cho phá progression chính

## 2. Gate Damage Cost Của Refarm

Muốn gọi lại boss:
- phải chấp nhận phá một phần gate
- làm route đó ngừng hoạt động
- tốn chi phí sửa lại

## 3. Loot Form

Loot từ boss refarm:
- tùy loại boss

Doc này chưa khóa boss loot phải rơi:
- trực tiếp ra đất
- chest
- core

vì đó là lớp content presentation về sau.

## Relationship With Floor Hierarchy

Boss bám vào `Floor Hierarchy` như sau:

- không phải tầng nào cũng có boss
- không phải boss nào cũng là cổng chặn cứng
- boss mạnh nhất trong trục progression là `gatekeeper boss` ở các mốc đủ sâu và đủ giá trị

Một tầng hoặc một band được xem là thật sự “đã ổn định” khi:
- không chỉ chạm tới được
- mà route của nó đã được boss/gate milestone giải quyết đủ

Boss do đó không chỉ là:
- combat spike

mà là:
- route stability event

## Relationship With Co-op

Boss là nơi co-op có giá trị thật vì:
- tạo áp lực cứu đồng đội
- buộc chia vai mềm theo loadout / utility / vị trí
- tăng giá trị của revive window
- tăng giá trị của việc mang đúng tool, đúng utility, đúng fuel

Game hiện không dùng class cứng, nên boss không kiểm tra “đủ tank/healer/dps” theo kiểu MMORPG.
Boss kiểm tra:
- nhóm có chuẩn bị tử tế không
- có đọc tình huống và biết kéo nhịp không
- có hy sinh ngắn hạn để giữ người / giữ route / giữ tài nguyên hay không

## Core Flows

## 1. Gatekeeper First Encounter Flow

1. Người chơi chạm một mốc gate quan trọng.
2. Nhận ra có boss gatekeeper đang canh.
3. Thử chạm gate, sửa gate hoặc quan sát boss.
4. Hiểu boss không chỉ là combat, mà còn là áp lực lên hành vi sửa gate.

## 2. Kill-And-Repair Flow

1. Người chơi chuẩn bị run.
2. Tiếp cận gatekeeper boss.
3. Hạ boss.
4. Boss biến mất, khu được clear tạm thời.
5. Người chơi tranh thủ sửa gate từng module.
6. Gate ổn định.
7. Route sâu đổi chất lượng.

## 3. Greedy Partial Repair Flow

1. Người chơi chưa muốn hoặc chưa đủ sức hạ boss.
2. Vẫn cố sửa gate từng phần.
3. Boss quấy, đánh người chơi, phá module, làm mất một phần tài nguyên.
4. Người chơi được phép lách, nhưng phải trả giá cao hơn.

## 4. Refarm Flow

1. Gate đã từng được xử lý.
2. Người chơi chủ động phá một phần gate.
3. Gate ngừng hoạt động, rơi ra một phần nguyên liệu.
4. Boss được gọi lại.
5. Hạ boss để lấy vật liệu farm phụ.
6. Không nhận lại milestone reward.

## Failure And Recovery

## Failure

Boss failure thường làm người chơi mất:
- thời gian chuẩn bị
- consumable / food / mana item / repair cost
- cơ hội sửa gate yên ổn
- tài nguyên đã nhét vào module nếu bị phá đúng lúc

## Recovery

Boss recovery đúng thường đi qua:
- quay về base
- repair / refill / restock
- chạy lại một phiên ngắn hơn
- hoặc lùi về mốc ổn định trước đó

### Guardrail

- Boss thất bại không được xóa các milestone đã khóa ổn trước đó.
- Stable gate đã mở không được bị xóa chỉ vì một fail run khác.

## Edge Cases

## 1. Người chơi vẫn sửa gate khi boss còn sống

- hợp lệ
- nhưng phải chịu toàn bộ áp lực:
  - bị đánh
  - bị hủy thao tác sửa
  - bị phá module
  - bị mất một phần tài nguyên vừa nhét

## 2. Boss chết nhưng gate chưa sửa xong

- boss chưa bị loại vĩnh viễn
- chỉ bắt đầu bộ đếm hồi sinh
- route chưa được coi là ổn định

## 3. Người chơi rời tầng giữa trận

- boss reset phase hoặc reset hẳn
- tùy boss type
- đây là rule lớn, ưu tiên tính đọc được hơn là chiều sâu giả

## 4. Boss Friendly / Special

- hợp lệ
- nhưng không được để làm mờ nghĩa của từ “boss” trong production doc
- boss special phải được tag rõ là:
  - non-hostile
  - interaction-heavy
  - deception-heavy
  - utility / vendor / story node

## 5. Boss Refarm

- chỉ farm material
- không rơi lại milestone
- nếu refarm mà luôn lời hơn giữ gate ổn định, hệ boss đang hỏng

## Signs Of A Good Boss System

- boss ít nhưng mỗi con có vai trò rõ
- người chơi nhớ boss vì nó đổi tiến trình hoặc route, không chỉ vì HP to
- boss chuẩn bị tốt thì dễ hơn rõ rệt, không thành phản xạ thuần
- gatekeeper boss tạo căng thẳng thật lên hành vi sửa gate
- refarm tồn tại nhưng không phá progression
- có chỗ cho boss hostile lẫn boss special mà không làm loãng trục chính

## Signs Of A Broken Boss System

- boss chỉ là elite phóng to
- boss nhiều nhưng na ná nhau
- thắng boss mà world không đổi gì đáng kể
- refarm boss trả lại milestone
- lách sửa gate lúc boss sống lúc nào cũng lời hơn hạ boss
- boss reset theo rule khó đoán, mỗi nơi một kiểu, QA không nắm được
- boss special xuất hiện nhưng không có tag logic riêng, làm pipeline production mơ hồ

## Implementation Hooks

## Boss Definition Tối Thiểu

- `boss_id`
- `boss_family`
- `hostility_class`
- `milestone_role`
- `anchor_location_id`
- `aggro_profile`
- `reset_profile`
- `phase_profile`
- `respawn_rule`
- `reward_profile`
- `refarm_profile`
- `gate_interaction_profile`

## Boss Runtime State Tối Thiểu

- `alive`
- `current_hp`
- `current_phase`
- `aggro_state`
- `disengage_state`
- `respawn_timer`
- `milestone_claimed`
- `gate_anchor_id`

## Event Hook Tối Thiểu

- `discover_boss_zone`
- `aggro_boss`
- `lose_aggro`
- `change_boss_phase`
- `damage_gate_module`
- `kill_boss`
- `start_boss_respawn_timer`
- `respawn_boss`
- `call_back_boss_by_breaking_gate`

## Authority Requirement

- Boss state nên do host/server authoritative.
- Những thứ không được để client tự đoán:
  - aggro state
  - phase state
  - HP state
  - respawn timer
  - gate-module damage do boss gây ra
  - milestone claim state

## QA Hook Tối Thiểu

- đánh boss chết khi gate chưa sửa xong
- chờ đủ thời gian để boss hồi lại
- sửa gate khi boss còn sống và bị hit giữa thao tác
- để boss phá module vừa nhét tài nguyên
- phá gate để gọi lại boss
- refarm boss không rơi lại milestone
- rời tầng giữa fight và xác nhận reset đúng profile
- xác nhận boss special không bị ép đi qua flow combat hostile

## Open Design Questions

- MVP thực tế có bao nhiêu `gatekeeper boss` thật sự handcrafted.
- Bao nhiêu tỷ lệ boss trong game là:
  - hostile milestone
  - biome boss
  - loot guardian
  - special / non-hostile
- Có bao nhiêu boss nên giữ HP giữa cùng một expedition, và bao nhiêu boss nên reset cứng để giữ readability.
- Mức độ “xảo quyệt” của AI boss nên dừng ở đâu để vẫn giữ production scope thực tế.

## Open Balance Variables

- số phase trung bình của từng họ boss
- cooldown phá gate của gatekeeper boss
- tỷ lệ tài nguyên mất khi boss phá module
- thời gian hồi sinh của gatekeeper boss
- giá trị farm reward khi gọi lại boss
- khoảng cách giữa các mốc boss quan trọng trong chiều sâu
- mức độ boss special nên xuất hiện dày hay thưa để không làm loãng nhịp hostile milestone
