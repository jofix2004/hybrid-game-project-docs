Project Code: HYBRID
Version: 0.8 (Draft)
Author: null
Date: 12/03/2026

# GDD_DOC_BACKLOG

Tài liệu này là backlog thực thi để viết lại toàn bộ GDD production trong `00-11`.

Nó được dùng để:
- xác định viết file nào trước
- biết mỗi file phải đọc những nguồn nào trong `12_QUESTION_FRAMEWORK`
- biết file nào phụ thuộc file nào
- biết mức chi tiết tối thiểu của từng file

Ghi chú:
- backlog này bắt đầu lại từ đầu
- các bản nháp không đạt chuẩn trước đó không được xem là đầu ra hợp lệ

## 1. Quy ước trạng thái

- `P0`: bắt buộc làm sớm, chặn nhiều doc khác
- `P1`: quan trọng, nên làm ngay sau P0
- `P2`: cần thiết nhưng có thể làm sau khi core đã khóa
- `P3`: hoàn thiện thêm, không chặn tiến độ trước mắt

Trạng thái:
- `Not Started`
- `Planned`
- `In Progress`
- `Review`
- `Locked`

## 2. Thứ tự thực thi tổng thể

### Wave 1. Khóa lõi chơi được

- `00_GAME_VISION`
- `01_GAMEPLAY_LOOP`
- `03_PLAYER_SYSTEMS/Player Stats.md`
- `03_PLAYER_SYSTEMS/Player Progression.md`
- `02_CORE_SYSTEMS/Survival System.md`
- `09_MULTIPLAYER/Player Revive.md`

### Wave 2. Khóa vận hành item và inventory

- `03_PLAYER_SYSTEMS/Inventory System.md`
- `03_PLAYER_SYSTEMS/Equipment System.md`
- `06_ECONOMY_SYSTEM/Crafting Economy.md`
- `08_CONTENT_DATABASE/Items.md`

### Wave 3. Khóa dungeon gate boss progression

- `05_DUNGEON_SYSTEM/Boss System.md`
- `05_DUNGEON_SYSTEM/Floor Hierarchy.md`
- `07_PROGRESSION_SYSTEM/Dungeon Progression.md`
- `04_WORLD_SYSTEMS/World Generation.md`

### Wave 4. Khóa core systems còn lại

- `02_CORE_SYSTEMS/Combat System.md`
- `02_CORE_SYSTEMS/Crafting System.md`
- `02_CORE_SYSTEMS/Building System.md`
- `06_ECONOMY_SYSTEM/Resource Types.md`
- `06_ECONOMY_SYSTEM/Resource Distribution.md`
- `08_CONTENT_DATABASE/Recipes.md`

### Wave 5. Schema, sync, balance

- toàn bộ `10_TECHNICAL_DESIGN`
- toàn bộ `11_BALANCE_DATA`
- phần còn lại của `08_CONTENT_DATABASE`

## 3. Backlog theo thư mục

## 00_GAME_VISION

### `README.md`

- Priority: `P1`
- Status: `Planned`
- Mục tiêu: giới thiệu phạm vi thư mục vision và quan hệ với loop/system
- Nguồn bắt buộc:
  - `01_LEVEL_LADDER.md`
  - `02_CONTENT_MAP.md`
  - `03_USAGE_ROADMAP.md`
  - `04_QUESTIONS_LEVEL_0.md`
- Done khi:
  - nói rõ vision docs dùng để chốt cái gì
  - liệt kê các file vision còn lại và vai trò của chúng

### `Game Pillars.md`

- Priority: `P0`
- Status: `Locked`
- Nguồn bắt buộc:
  - `04_QUESTIONS_LEVEL_0.md`
  - `05_QUESTIONS_LEVEL_1.md`
  - `06_QUESTIONS_LEVEL_2.md`
- Nguồn bổ trợ:
  - `07_QUESTIONS_LEVEL_3.md`
- Done khi:
  - có 3-5 pillars rõ
  - mỗi pillar có ý nghĩa gameplay thật
  - pillar nối được tới loop và system

### `Player Fantasy.md`

- Priority: `P0`
- Status: `Locked`
- Nguồn bắt buộc:
  - `04_QUESTIONS_LEVEL_0.md`
  - `05_QUESTIONS_LEVEL_1.md`
  - `06_QUESTIONS_LEVEL_2.md`
- Done khi:
  - trả lời người chơi đang hóa thân thành ai
  - muốn gì
  - sợ gì
  - chiến thắng kiểu gì

### `Target Experience.md`

- Priority: `P0`
- Status: `Locked`
- Nguồn bắt buộc:
  - `05_QUESTIONS_LEVEL_1.md`
  - `06_QUESTIONS_LEVEL_2.md`
  - `07_QUESTIONS_LEVEL_3.md`
- Done khi:
  - mô tả cảm xúc đầu game, giữa game, về sâu
  - mô tả nhịp đau - hồi - mở khóa

### `Inspirations.md`

- Priority: `P3`
- Status: `Locked`
- Nguồn bắt buộc:
  - `04_QUESTIONS_LEVEL_0.md`
  - `06_QUESTIONS_LEVEL_2.md`
- Done khi:
  - chỉ ra ảnh hưởng để định hướng
  - không biến thành danh sách tham khảo lan man

### `Unique Selling Points.md`

- Priority: `P1`
- Status: `Locked`
- Nguồn bắt buộc:
  - `04_QUESTIONS_LEVEL_0.md`
  - `05_QUESTIONS_LEVEL_1.md`
  - `06_QUESTIONS_LEVEL_2.md`
- Done khi:
  - chốt được điều game này bán khác gì
  - USP nối được tới feature thật, không chỉ là slogan

## 01_GAMEPLAY_LOOP

### `README.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `02_CONTENT_MAP.md`
  - `03_USAGE_ROADMAP.md`
- Done khi:
  - giải thích logic tách short loop, long loop, multiplayer loop

### `Core Gameplay Loop.md`

- Priority: `P0`
- Status: `Locked`
- Nguồn bắt buộc:
  - `05_QUESTIONS_LEVEL_1.md`
  - `06_QUESTIONS_LEVEL_2.md`
  - `07_QUESTIONS_LEVEL_3.md`
  - `08_QUESTIONS_LEVEL_4.md`
- Done khi:
  - vẽ được vòng `prepare -> descend -> gather/fight -> survive -> recover -> upgrade -> descend again`
  - chỉ ra entry cost và fail cost

### `Short Session Loop.md`

- Priority: `P1`
- Status: `Locked`
- Nguồn bắt buộc:
  - `06_QUESTIONS_LEVEL_2.md`
  - `07_QUESTIONS_LEVEL_3.md`
  - `08_QUESTIONS_LEVEL_4.md`
- Done khi:
  - mô tả 1 session 10-30 phút người chơi làm gì

### `Long Progression Loop.md`

- Priority: `P1`
- Status: `Locked`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `11_QUESTIONS_LEVEL_7.md`
  - `12_QUESTIONS_LEVEL_8.md`
- Done khi:
  - giải thích vòng `đi sâu -> mở tầng -> mở công nghệ -> mạnh hơn -> đi sâu`

### `Multiplayer Loop.md`

- Priority: `P1`
- Status: `Locked`
- Nguồn bắt buộc:
  - `08_QUESTIONS_LEVEL_4.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `13_PLAYER_CORE_STATE_SHEET.md`
  - `14_INVENTORY_AND_ITEM_RULES_SHEET.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`
- Done khi:
  - mô tả loop co-op riêng
  - mô tả tại sao đi cùng nhau có giá trị hơn solo

## 02_CORE_SYSTEMS

### `README.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `02_CONTENT_MAP.md`
  - `12_QUESTIONS_LEVEL_8.md`
- Done khi:
  - giải thích phạm vi từng core system

### `Mana Network System.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`
- Done khi:
  - phân biệt mana cá nhân, mana base, fuel, gate energy
  - có state, source, sink, refill path

### `Survival System.md`

- Priority: `P0`
- Status: `Locked`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `13_PLAYER_CORE_STATE_SHEET.md`
- Done khi:
  - có đủ đói, kiệt đói, heal, mana refill, resolve order
  - không còn placeholder kiểu stamina, mana saturation

### `Combat System.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `09_QUESTIONS_LEVEL_5.md`
  - `10_QUESTIONS_LEVEL_6.md`
  - `11_QUESTIONS_LEVEL_7.md`
  - `12_QUESTIONS_LEVEL_8.md`
- Nguồn bổ trợ:
  - `13_PLAYER_CORE_STATE_SHEET.md`
- Done khi:
  - có damage groups
  - attack commitment
  - stagger, iframe, block rule
  - interaction với armor và downed

### `Enchanting System.md`

- Priority: `P3`
- Status: `Planned`
- Nguồn bắt buộc:
  - rà lại toàn bộ framework xem có rule thật hay chưa
- Done khi:
  - nếu chưa có đủ nguồn thì đánh dấu `Open`
  - không được bịa hệ thống

### `Crafting System.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `14_INVENTORY_AND_ITEM_RULES_SHEET.md`
- Done khi:
  - có hand craft vs workstation
  - recipe unlock
  - input source
  - craft time

### `Building System.md`

- Priority: `P2`
- Status: `Planned`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `14_INVENTORY_AND_ITEM_RULES_SHEET.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`
- Done khi:
  - có place / remove / refund / durability / destruction rule cho công trình

## 03_PLAYER_SYSTEMS

### `README.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `07_QUESTIONS_LEVEL_3.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `13_PLAYER_CORE_STATE_SHEET.md`
  - `14_INVENTORY_AND_ITEM_RULES_SHEET.md`

### `Player Stats.md`

- Priority: `P0`
- Status: `Locked`
- Nguồn bắt buộc:
  - `07_QUESTIONS_LEVEL_3.md`
  - `10_QUESTIONS_LEVEL_6.md`
  - `11_QUESTIONS_LEVEL_7.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `13_PLAYER_CORE_STATE_SHEET.md`
- Done khi:
  - có stat list chuẩn
  - điểm chỉ số
  - all-in
  - respec
  - current/max rule

### `Player Skills.md`

- Priority: `P2`
- Status: `Planned`
- Nguồn bắt buộc:
  - `11_QUESTIONS_LEVEL_7.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `13_PLAYER_CORE_STATE_SHEET.md`
- Done khi:
  - chỉ viết phần skill thật sự đã có nguồn
  - không tự mở rộng thành cây kỹ năng giả định

### `Equipment System.md`

- Priority: `P0`
- Status: `Locked`
- Nguồn bắt buộc:
  - `12_QUESTIONS_LEVEL_8.md`
  - `14_INVENTORY_AND_ITEM_RULES_SHEET.md`
- Done khi:
  - có armor slot
  - artifact slot
  - equip/unequip/swap rule
  - combat swap edge case

### `Inventory System.md`

- Priority: `P0`
- Status: `Locked`
- Nguồn bắt buộc:
  - `12_QUESTIONS_LEVEL_8.md`
  - `14_INVENTORY_AND_ITEM_RULES_SHEET.md`
- Done khi:
  - có hotbar, túi chính, pickup order, overflow, tombstone interaction

### `Player Progression.md`

- Priority: `P0`
- Status: `Locked`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `11_QUESTIONS_LEVEL_7.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `13_PLAYER_CORE_STATE_SHEET.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`
- Done khi:
  - có nguồn điểm, nhịp mở tầng, boss/milestone contribution

## 04_WORLD_SYSTEMS

### `README.md`

- Priority: `P2`
- Status: `Planned`

### `Biomes.md`

- Priority: `P2`
- Status: `Planned`
- Nguồn bắt buộc:
  - `09_QUESTIONS_LEVEL_5.md`
  - `11_QUESTIONS_LEVEL_7.md`

### `Weather.md`

- Priority: `P3`
- Status: `Planned`
- Nguồn bắt buộc:
  - rà framework để xác định có đủ rule hay chưa

### `Flora.md`

- Priority: `P2`
- Status: `Planned`
- Nguồn bắt buộc:
  - `09_QUESTIONS_LEVEL_5.md`
  - `12_QUESTIONS_LEVEL_8.md`

### `Fauna.md`

- Priority: `P2`
- Status: `Planned`
- Nguồn bắt buộc:
  - `09_QUESTIONS_LEVEL_5.md`
  - `12_QUESTIONS_LEVEL_8.md`

### `World Generation.md`

- Priority: `P1`
- Status: `Locked`
- Nguồn bắt buộc:
  - `06_QUESTIONS_LEVEL_2.md`
  - `09_QUESTIONS_LEVEL_5.md`
  - `11_QUESTIONS_LEVEL_7.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

## 05_DUNGEON_SYSTEM

### `README.md`

- Priority: `P2`
- Status: `Planned`

### `Floor Hierarchy.md`

- Priority: `P0`
- Status: `Locked`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `11_QUESTIONS_LEVEL_7.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### `Dungeon Generation.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `09_QUESTIONS_LEVEL_5.md`
  - `11_QUESTIONS_LEVEL_7.md`

### `Room Types.md`

- Priority: `P2`
- Status: `Planned`
- Nguồn bắt buộc:
  - `09_QUESTIONS_LEVEL_5.md`
  - `11_QUESTIONS_LEVEL_7.md`

### `Trap System.md`

- Priority: `P2`
- Status: `Planned`
- Nguồn bắt buộc:
  - `09_QUESTIONS_LEVEL_5.md`
  - `12_QUESTIONS_LEVEL_8.md`

### `Boss System.md`

- Priority: `P0`
- Status: `Locked`
- Nguồn bắt buộc:
  - `09_QUESTIONS_LEVEL_5.md`
  - `10_QUESTIONS_LEVEL_6.md`
  - `11_QUESTIONS_LEVEL_7.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`
- Done khi:
  - có gatekeeper logic
  - respawn
  - refarm
  - reward class

## 06_ECONOMY_SYSTEM

### `README.md`

- Priority: `P2`
- Status: `Planned`

### `Resource Types.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `09_QUESTIONS_LEVEL_5.md`
  - `10_QUESTIONS_LEVEL_6.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `14_INVENTORY_AND_ITEM_RULES_SHEET.md`

### `Resource Tiers.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `11_QUESTIONS_LEVEL_7.md`
  - `12_QUESTIONS_LEVEL_8.md`

### `Resource Distribution.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `09_QUESTIONS_LEVEL_5.md`
  - `10_QUESTIONS_LEVEL_6.md`
  - `11_QUESTIONS_LEVEL_7.md`

### `Crafting Economy.md`

- Priority: `P0`
- Status: `Locked`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `14_INVENTORY_AND_ITEM_RULES_SHEET.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

## 07_PROGRESSION_SYSTEM

### `README.md`

- Priority: `P2`
- Status: `Planned`

### `Tech Tree.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `11_QUESTIONS_LEVEL_7.md`

### `Dungeon Progression.md`

- Priority: `P0`
- Status: `Locked`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `11_QUESTIONS_LEVEL_7.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### `Player Level.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `13_PLAYER_CORE_STATE_SHEET.md`

### `Unlock Conditions.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `11_QUESTIONS_LEVEL_7.md`
  - `12_QUESTIONS_LEVEL_8.md`

## 08_CONTENT_DATABASE

### `README.md`

- Priority: `P2`
- Status: `Planned`

### `Items.md`

- Priority: `P0`
- Status: `Locked`
- Nguồn bắt buộc:
  - `09_QUESTIONS_LEVEL_5.md`
  - `10_QUESTIONS_LEVEL_6.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `14_INVENTORY_AND_ITEM_RULES_SHEET.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### `Enemies.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `09_QUESTIONS_LEVEL_5.md`
  - `11_QUESTIONS_LEVEL_7.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### `Buildings.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `14_INVENTORY_AND_ITEM_RULES_SHEET.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### `Recipes.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `14_INVENTORY_AND_ITEM_RULES_SHEET.md`

### `Drop Tables.md`

- Priority: `P2`
- Status: `Planned`
- Nguồn bắt buộc:
  - `09_QUESTIONS_LEVEL_5.md`
  - `10_QUESTIONS_LEVEL_6.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

## 09_MULTIPLAYER

### `README.md`

- Priority: `P2`
- Status: `Planned`

### `Co-op Mechanics.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `08_QUESTIONS_LEVEL_4.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `13_PLAYER_CORE_STATE_SHEET.md`
  - `14_INVENTORY_AND_ITEM_RULES_SHEET.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### `Shared Resources.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `08_QUESTIONS_LEVEL_4.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `14_INVENTORY_AND_ITEM_RULES_SHEET.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### `Player Revive.md`

- Priority: `P0`
- Status: `Locked`
- Nguồn bắt buộc:
  - `08_QUESTIONS_LEVEL_4.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `13_PLAYER_CORE_STATE_SHEET.md`

### `Network Sync Rules.md`

- Priority: `P2`
- Status: `Planned`
- Nguồn bắt buộc:
  - `08_QUESTIONS_LEVEL_4.md`
  - `11_QUESTIONS_LEVEL_7.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `14_INVENTORY_AND_ITEM_RULES_SHEET.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

## 10_TECHNICAL_DESIGN

### `README.md`

- Priority: `P2`
- Status: `Planned`

### `Mana Network Logic.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### `AI Behavior Trees.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `11_QUESTIONS_LEVEL_7.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### `Save System.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `12_QUESTIONS_LEVEL_8.md`
  - `13_PLAYER_CORE_STATE_SHEET.md`
  - `14_INVENTORY_AND_ITEM_RULES_SHEET.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### `World Chunk System.md`

- Priority: `P2`
- Status: `Planned`
- Nguồn bắt buộc:
  - `11_QUESTIONS_LEVEL_7.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### `Networking.md`

- Priority: `P2`
- Status: `Planned`
- Nguồn bắt buộc:
  - `08_QUESTIONS_LEVEL_4.md`
  - `11_QUESTIONS_LEVEL_7.md`
  - `12_QUESTIONS_LEVEL_8.md`

## 11_BALANCE_DATA

### `README.md`

- Priority: `P2`
- Status: `Planned`

### `Combat Numbers.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `09_QUESTIONS_LEVEL_5.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `13_PLAYER_CORE_STATE_SHEET.md`

### `Mana Consumption.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `13_PLAYER_CORE_STATE_SHEET.md`
  - `14_INVENTORY_AND_ITEM_RULES_SHEET.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### `Crafting Costs.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `10_QUESTIONS_LEVEL_6.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `14_INVENTORY_AND_ITEM_RULES_SHEET.md`

### `Enemy Difficulty.md`

- Priority: `P1`
- Status: `Planned`
- Nguồn bắt buộc:
  - `09_QUESTIONS_LEVEL_5.md`
  - `11_QUESTIONS_LEVEL_7.md`
  - `12_QUESTIONS_LEVEL_8.md`
  - `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

## 4. Nguyên tắc vận hành backlog

Khi bắt đầu một file trong backlog:
1. kiểm tra `Source Coverage`
2. đọc toàn bộ phần liên quan trong các file nguồn
3. lập `Conflict Notes`
4. chỉ khi không còn mơ hồ mới viết doc đích
5. nếu thiếu rule hoặc không tìm được nguồn tương ứng thì mới hỏi lại

## 5. Đầu ra của bước này

Sau tài liệu backlog này:
- đã có danh sách doc phải viết
- đã có thứ tự ưu tiên
- đã có mapping nguồn cho từng file
- đã có tiêu chuẩn đủ chi tiết để bắt đầu viết lại GDD production từng bước một
