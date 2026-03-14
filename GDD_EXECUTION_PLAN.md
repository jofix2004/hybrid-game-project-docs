Project Code: HYBRID
Version: 0.8 (Draft)
Author: null
Date: 11/03/2026

# GDD_EXECUTION_PLAN

Tài liệu này là kế hoạch chính thức để chuyển toàn bộ nội dung trong `12_QUESTION_FRAMEWORK` thành bộ GDD hoàn chỉnh trong `GAME_PROJECT_DOCS`.

Kế hoạch này được viết lại theo nguyên tắc:
- không rút gọn `12_QUESTION_FRAMEWORK`
- không coi một file là nguồn duy nhất nếu hệ đó còn bị chi phối bởi file khác
- mọi rule, ngoại lệ, edge case, ghi chú chốt tạm và mối liên hệ hệ thống đều phải được truyền sang GDD đích
- chỉ bắt đầu viết GDD sau khi có mapping nguồn đầy đủ

## 1. Mục tiêu thật sự của kế hoạch

Mục tiêu không phải là "viết vài doc cho có", mà là:
- tạo bộ GDD dùng được để thiết kế, code, QA và balance
- giữ lại `12_QUESTION_FRAMEWORK` như bộ nền tư duy và bộ log quyết định đầy đủ
- bảo đảm mỗi doc trong GDD có thể truy ngược về đúng các file nguồn đã sinh ra nó

Kết quả cuối cùng phải đạt:
- `12_QUESTION_FRAMEWORK` còn nguyên vai trò discovery, decision log và lớp truy vết
- `00-11` trở thành lớp GDD production
- mỗi doc production có đủ độ chi tiết để giao việc
- không còn tình trạng rule nằm rải rác mà chưa được hợp nhất

## 2. Quy tắc cứng khi chuyển từ Framework sang GDD

### 2.1. Không rút gọn nguồn

Không được làm theo kiểu:
- lấy 1 file "chính"
- rồi bỏ qua các file cùng ảnh hưởng

Mỗi doc GDD phải là kết quả tổng hợp từ toàn bộ file nguồn liên quan.

### 2.2. Không làm mất rule

Khi chuyển sang GDD, phải mang theo đủ:
- rule chính
- rule phụ
- mode differences
- fail state
- recovery
- edge cases
- ghi chú chốt tạm đã được xác nhận

Không được chỉ lấy phần "ý chính" rồi bỏ các trường hợp khó.

### 2.3. Mỗi doc GDD phải có `Source Coverage`

Mỗi doc đích bắt buộc phải có mục:
- `Source Coverage`

Mục này phải ghi:
- file nguồn nào đã được dùng
- phần nào của hệ được lấy từ file nào
- file nào chỉ cung cấp context
- file nào cung cấp rule chốt cuối

### 2.4. Mỗi doc GDD phải có `Decision Status`

Mỗi phần trong doc đích phải được phân loại:
- `Locked`: đã chốt
- `Derived`: suy ra trực tiếp từ các rule đã chốt
- `Open`: còn thiếu, còn tranh cãi, hoặc chưa đủ nguồn

### 2.5. Không được viết tắt độ chi tiết

Nếu `Question Framework` mô tả:
- thứ tự resolve
- điều kiện hủy action
- tương tác với mode
- interaction với inventory, revive, death, gate, mana, party

thì GDD đích phải ghi lại, không được bỏ vì "quá chi tiết".

## 3. Vai trò của từng lớp tài liệu

### 3.1. `12_QUESTION_FRAMEWORK`

Dùng làm:
- lớp khám phá
- bộ câu hỏi tăng độ sâu
- decision log
- nơi chứa reasoning
- nơi chứa các sheet trung gian để tổng hợp rule

Không dùng làm:
- doc production cuối cùng cho team bám vào implement

### 3.2. `00-11` trong `GAME_PROJECT_DOCS`

Dùng làm:
- GDD chính thức
- source of truth để giao việc
- bộ tài liệu review liên phòng ban
- nơi khóa luật chơi, schema, checklist, balance

## 4. Tiêu chuẩn hoàn thành của một doc GDD

Một doc chỉ được xem là đạt chuẩn khi có đủ:
- `Mục tiêu`
- `Phạm vi`
- `Source Coverage`
- `Rule Summary`
- `State`
- `Transition`
- `Cost / Reward`
- `Fail State`
- `Recovery`
- `Edge Cases`
- `Implementation Hooks`
- `Open Design Questions`
- `Open Balance Variables`

Nếu thiếu một trong các phần trên, doc đó chưa được xem là đủ nghiêm túc để giao việc.

## 5. Ma trận phủ nguồn cho toàn bộ `12_QUESTION_FRAMEWORK`

Phần này là mapping toàn bộ file nguồn, không chỉ file "chính".

### 5.1. `01_LEVEL_LADDER.md`

Vai trò:
- xác định thang độ sâu của bộ câu hỏi
- giải thích level nào đang giải quyết loại vấn đề nào

Ảnh hưởng tới:
- toàn bộ kế hoạch viết GDD
- cách đánh giá một doc đang ở mức vision, system hay implementation detail

Phải được dùng trong:
- `GDD_EXECUTION_PLAN.md`
- checklist review toàn cục

### 5.2. `02_CONTENT_MAP.md`

Vai trò:
- map các nhóm nội dung của game
- cho biết hệ nào đang kết nối với hệ nào

Ảnh hưởng tới:
- `00_GAME_VISION`
- `01_GAMEPLAY_LOOP`
- `02_CORE_SYSTEMS`
- `08_CONTENT_DATABASE`

Phải được dùng để:
- tránh bỏ sót module
- tránh viết lệch ưu tiên tài liệu

### 5.3. `03_USAGE_ROADMAP.md`

Vai trò:
- chỉ cách dùng bộ framework
- chỉ thứ tự đào sâu

Ảnh hưởng tới:
- kế hoạch làm việc
- cách chia phase và batch tài liệu

Phải được dùng trong:
- `GDD_EXECUTION_PLAN.md`
- kế hoạch viết theo đợt

### 5.4. `04_QUESTIONS_LEVEL_0.md`

Vai trò:
- chốt lớp hạt giống của game
- fantasy, hứa hẹn cốt lõi, bản chất cuộc chơi

Ảnh hưởng tới:
- `00_GAME_VISION`
- `01_GAMEPLAY_LOOP`

### 5.5. `05_QUESTIONS_LEVEL_1.md`

Vai trò:
- làm rõ dạng game, nhịp chơi, áp lực chính

Ảnh hưởng tới:
- `00_GAME_VISION`
- `01_GAMEPLAY_LOOP`
- `07_PROGRESSION_SYSTEM`

### 5.6. `06_QUESTIONS_LEVEL_2.md`

Vai trò:
- làm rõ cảm xúc người chơi, vòng trải nghiệm, escalation

Ảnh hưởng tới:
- `00_GAME_VISION`
- `01_GAMEPLAY_LOOP`
- `05_DUNGEON_SYSTEM`

### 5.7. `07_QUESTIONS_LEVEL_3.md`

Vai trò:
- làm rõ hành vi người chơi và cấu trúc tương tác cấp game

Ảnh hưởng tới:
- `01_GAMEPLAY_LOOP`
- `03_PLAYER_SYSTEMS`
- `09_MULTIPLAYER`

### 5.8. `08_QUESTIONS_LEVEL_4.md`

Vai trò:
- làm rõ co-op, session flow, social friction, độ nặng của rủi ro

Ảnh hưởng tới:
- `01_GAMEPLAY_LOOP`
- `09_MULTIPLAYER`
- `10_TECHNICAL_DESIGN`

### 5.9. `09_QUESTIONS_LEVEL_5.md`

Vai trò:
- làm rõ content structure, encounter class, risk source

Ảnh hưởng tới:
- `05_DUNGEON_SYSTEM`
- `08_CONTENT_DATABASE`
- `11_BALANCE_DATA`

### 5.10. `10_QUESTIONS_LEVEL_6.md`

Vai trò:
- làm rõ economy, faucet, sink, progression pacing

Ảnh hưởng tới:
- `06_ECONOMY_SYSTEM`
- `07_PROGRESSION_SYSTEM`
- `11_BALANCE_DATA`

### 5.11. `11_QUESTIONS_LEVEL_7.md`

Vai trò:
- làm rõ production-facing design direction, technical implication, content scaling

Ảnh hưởng tới:
- `05_DUNGEON_SYSTEM`
- `07_PROGRESSION_SYSTEM`
- `10_TECHNICAL_DESIGN`

### 5.12. `12_QUESTIONS_LEVEL_8.md`

Vai trò:
- lớp đặc tả rule, state, transition, fail flow, edge case

Ảnh hưởng tới:
- `02_CORE_SYSTEMS`
- `03_PLAYER_SYSTEMS`
- `04_WORLD_SYSTEMS`
- `05_DUNGEON_SYSTEM`
- `06_ECONOMY_SYSTEM`
- `07_PROGRESSION_SYSTEM`
- `09_MULTIPLAYER`
- `10_TECHNICAL_DESIGN`
- `11_BALANCE_DATA`

Ghi chú:
- đây là file rule tổng hợp lớn nhất
- nhưng vẫn không được coi là nguồn duy nhất

### 5.13. `13_PLAYER_CORE_STATE_SHEET.md`

Vai trò:
- sheet chi tiết riêng cho player core

Ảnh hưởng tới:
- `03_PLAYER_SYSTEMS`
- `02_CORE_SYSTEMS`
- `09_MULTIPLAYER`
- `10_TECHNICAL_DESIGN`
- `11_BALANCE_DATA`

### 5.14. `14_INVENTORY_AND_ITEM_RULES_SHEET.md`

Vai trò:
- sheet chi tiết riêng cho inventory, equipment, item durability, repair

Ảnh hưởng tới:
- `03_PLAYER_SYSTEMS`
- `06_ECONOMY_SYSTEM`
- `08_CONTENT_DATABASE`
- `09_MULTIPLAYER`
- `10_TECHNICAL_DESIGN`
- `11_BALANCE_DATA`

### 5.15. `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

Vai trò:
- sheet chi tiết riêng cho gate, boss gatekeeper, milestone và refarm

Ảnh hưởng tới:
- `04_WORLD_SYSTEMS`
- `05_DUNGEON_SYSTEM`
- `07_PROGRESSION_SYSTEM`
- `09_MULTIPLAYER`
- `10_TECHNICAL_DESIGN`
- `11_BALANCE_DATA`

## 6. Mapping từ thư mục đích sang bộ nguồn đầy đủ

Phần này đi ngược lại: mỗi thư mục GDD phải hút dữ liệu từ những file nào.

### 6.1. `00_GAME_VISION`

Nguồn bắt buộc:
- `01_LEVEL_LADDER.md`
- `02_CONTENT_MAP.md`
- `03_USAGE_ROADMAP.md`
- `04_QUESTIONS_LEVEL_0.md`
- `05_QUESTIONS_LEVEL_1.md`
- `06_QUESTIONS_LEVEL_2.md`

Nguồn bổ trợ:
- `07_QUESTIONS_LEVEL_3.md`

### 6.2. `01_GAMEPLAY_LOOP`

Nguồn bắt buộc:
- `02_CONTENT_MAP.md`
- `03_USAGE_ROADMAP.md`
- `05_QUESTIONS_LEVEL_1.md`
- `06_QUESTIONS_LEVEL_2.md`
- `07_QUESTIONS_LEVEL_3.md`
- `08_QUESTIONS_LEVEL_4.md`

Nguồn bổ trợ:
- `10_QUESTIONS_LEVEL_6.md`
- `11_QUESTIONS_LEVEL_7.md`

### 6.3. `02_CORE_SYSTEMS`

Nguồn bắt buộc:
- `02_CONTENT_MAP.md`
- `09_QUESTIONS_LEVEL_5.md`
- `10_QUESTIONS_LEVEL_6.md`
- `11_QUESTIONS_LEVEL_7.md`
- `12_QUESTIONS_LEVEL_8.md`
- `13_PLAYER_CORE_STATE_SHEET.md`
- `14_INVENTORY_AND_ITEM_RULES_SHEET.md`

Nguồn bổ trợ:
- `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### 6.4. `03_PLAYER_SYSTEMS`

Nguồn bắt buộc:
- `07_QUESTIONS_LEVEL_3.md`
- `08_QUESTIONS_LEVEL_4.md`
- `12_QUESTIONS_LEVEL_8.md`
- `13_PLAYER_CORE_STATE_SHEET.md`
- `14_INVENTORY_AND_ITEM_RULES_SHEET.md`

Nguồn bổ trợ:
- `10_QUESTIONS_LEVEL_6.md`
- `11_QUESTIONS_LEVEL_7.md`

### 6.5. `04_WORLD_SYSTEMS`

Nguồn bắt buộc:
- `02_CONTENT_MAP.md`
- `09_QUESTIONS_LEVEL_5.md`
- `10_QUESTIONS_LEVEL_6.md`
- `11_QUESTIONS_LEVEL_7.md`
- `12_QUESTIONS_LEVEL_8.md`
- `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### 6.6. `05_DUNGEON_SYSTEM`

Nguồn bắt buộc:
- `06_QUESTIONS_LEVEL_2.md`
- `09_QUESTIONS_LEVEL_5.md`
- `10_QUESTIONS_LEVEL_6.md`
- `11_QUESTIONS_LEVEL_7.md`
- `12_QUESTIONS_LEVEL_8.md`
- `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### 6.7. `06_ECONOMY_SYSTEM`

Nguồn bắt buộc:
- `09_QUESTIONS_LEVEL_5.md`
- `10_QUESTIONS_LEVEL_6.md`
- `11_QUESTIONS_LEVEL_7.md`
- `12_QUESTIONS_LEVEL_8.md`
- `14_INVENTORY_AND_ITEM_RULES_SHEET.md`

### 6.8. `07_PROGRESSION_SYSTEM`

Nguồn bắt buộc:
- `05_QUESTIONS_LEVEL_1.md`
- `10_QUESTIONS_LEVEL_6.md`
- `11_QUESTIONS_LEVEL_7.md`
- `12_QUESTIONS_LEVEL_8.md`
- `13_PLAYER_CORE_STATE_SHEET.md`
- `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### 6.9. `08_CONTENT_DATABASE`

Nguồn bắt buộc:
- `02_CONTENT_MAP.md`
- `09_QUESTIONS_LEVEL_5.md`
- `10_QUESTIONS_LEVEL_6.md`
- `11_QUESTIONS_LEVEL_7.md`
- `12_QUESTIONS_LEVEL_8.md`
- `14_INVENTORY_AND_ITEM_RULES_SHEET.md`
- `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### 6.10. `09_MULTIPLAYER`

Nguồn bắt buộc:
- `07_QUESTIONS_LEVEL_3.md`
- `08_QUESTIONS_LEVEL_4.md`
- `12_QUESTIONS_LEVEL_8.md`
- `13_PLAYER_CORE_STATE_SHEET.md`
- `14_INVENTORY_AND_ITEM_RULES_SHEET.md`
- `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### 6.11. `10_TECHNICAL_DESIGN`

Nguồn bắt buộc:
- `03_USAGE_ROADMAP.md`
- `10_QUESTIONS_LEVEL_6.md`
- `11_QUESTIONS_LEVEL_7.md`
- `12_QUESTIONS_LEVEL_8.md`
- `13_PLAYER_CORE_STATE_SHEET.md`
- `14_INVENTORY_AND_ITEM_RULES_SHEET.md`
- `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### 6.12. `11_BALANCE_DATA`

Nguồn bắt buộc:
- `09_QUESTIONS_LEVEL_5.md`
- `10_QUESTIONS_LEVEL_6.md`
- `11_QUESTIONS_LEVEL_7.md`
- `12_QUESTIONS_LEVEL_8.md`
- `13_PLAYER_CORE_STATE_SHEET.md`
- `14_INVENTORY_AND_ITEM_RULES_SHEET.md`
- `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

## 7. Quy tắc viết doc đích

Mỗi doc GDD khi bắt đầu phải đi theo pipeline này:

1. Liệt kê toàn bộ source file liên quan
2. Đọc toàn bộ phần liên quan trong mỗi source
3. Tách:
   - rule chốt
   - rule liên đới
   - edge case
   - open question
4. So khớp xung đột giữa các nguồn
5. Chốt cách ưu tiên nguồn
6. Viết doc đích
7. Ghi lại `Source Coverage`
8. Ghi lại chỗ còn mở

Không được bỏ qua bước 4 và 7.

## 8. Quy tắc ưu tiên nguồn khi có xung đột

Thứ tự ưu tiên mặc định:
1. sheet chuyên sâu mới nhất (`13-15`)
2. `12_QUESTIONS_LEVEL_8.md`
3. `10_QUESTIONS_LEVEL_6.md` và `11_QUESTIONS_LEVEL_7.md`
4. `09_QUESTIONS_LEVEL_5.md`
5. `04-08`
6. `01-03`

Nếu có xung đột:
- không tự ý bỏ qua
- phải ghi vào mục `Conflict Resolution`
- nếu chưa đủ chắc thì mới hỏi lại

## 9. Cấu trúc bắt buộc cho mỗi doc GDD đích

Mỗi doc đích phải có ít nhất các mục sau:
- `Mục tiêu`
- `Phạm vi`
- `Source Coverage`
- `Rule Summary`
- `State List`
- `Transition Rules`
- `Core Flows`
- `Failure and Recovery`
- `Edge Cases`
- `Implementation Hooks`
- `Open Design Questions`
- `Open Balance Variables`

Không được dùng stub kiểu:
- "Chờ hoàn thiện"
- "Khung ban đầu"
- "sẽ bổ sung sau"

như nội dung chính của doc.

## 10. Tiêu chuẩn độ chi tiết

Mỗi doc GDD phải đủ chi tiết để:
- designer khác đọc vào vẫn hiểu rule
- dev có thể code flow chính
- QA có thể viết test case

Điều đó có nghĩa là doc phải truyền được:
- điều kiện bắt đầu action
- điều kiện hủy action
- thứ tự resolve
- khi nào mất tài nguyên
- khi nào hoàn tài nguyên
- mode nào khác mode nào
- state nào được giữ
- state nào bị reset

Nếu doc chưa trả lời được các câu này, xem như chưa đạt chuẩn.

## 11. Giai đoạn thực hiện lại từ đầu

Do các bản thử trước chưa đặt tiêu chuẩn đủ sâu, lộ trình phải làm lại từ bước kế hoạch với các phase chặt hơn.

### Phase A. Lập ma trận nguồn

Làm:
- xác định đầy đủ source coverage cho từng thư mục đích
- khóa quy tắc ưu tiên nguồn
- khóa cấu trúc chuẩn của doc đích

Output:
- `GDD_EXECUTION_PLAN.md` hoàn chỉnh

### Phase B. Lập danh sách doc đích theo thứ tự viết

Không viết ngay nội dung.

Làm:
- liệt kê toàn bộ doc đích sẽ phải hoàn thiện
- gán source coverage cho từng doc
- gán độ ưu tiên
- gán mức phụ thuộc

Output:
- backlog GDD theo doc, không theo cảm hứng

### Phase C. Viết từng doc production

Chỉ khi xong Phase A và B mới bắt đầu viết từng file.

Mỗi lần chỉ làm:
- 1 doc đích
- với đầy đủ source coverage
- và rà xung đột trước khi chốt

## 12. Thứ tự ưu tiên backlog GDD sau khi lập kế hoạch xong

### Đợt 1: Player core và survival

- `03_PLAYER_SYSTEMS/Player Stats.md`
- `03_PLAYER_SYSTEMS/Player Progression.md`
- `02_CORE_SYSTEMS/Survival System.md`
- `09_MULTIPLAYER/Player Revive.md`

Nguồn phải dùng đồng thời:
- `07_QUESTIONS_LEVEL_3.md`
- `08_QUESTIONS_LEVEL_4.md`
- `10_QUESTIONS_LEVEL_6.md`
- `11_QUESTIONS_LEVEL_7.md`
- `12_QUESTIONS_LEVEL_8.md`
- `13_PLAYER_CORE_STATE_SHEET.md`

### Đợt 2: Inventory, equipment, repair, item logic

- `03_PLAYER_SYSTEMS/Inventory System.md`
- `03_PLAYER_SYSTEMS/Equipment System.md`
- `06_ECONOMY_SYSTEM/Crafting Economy.md`
- `08_CONTENT_DATABASE/Items.md`

Nguồn phải dùng đồng thời:
- `09_QUESTIONS_LEVEL_5.md`
- `10_QUESTIONS_LEVEL_6.md`
- `11_QUESTIONS_LEVEL_7.md`
- `12_QUESTIONS_LEVEL_8.md`
- `14_INVENTORY_AND_ITEM_RULES_SHEET.md`

### Đợt 3: Gate, boss, milestone, dungeon

- `05_DUNGEON_SYSTEM/Boss System.md`
- `05_DUNGEON_SYSTEM/Floor Hierarchy.md`
- `07_PROGRESSION_SYSTEM/Dungeon Progression.md`
- `04_WORLD_SYSTEMS/World Generation.md`

Nguồn phải dùng đồng thời:
- `06_QUESTIONS_LEVEL_2.md`
- `09_QUESTIONS_LEVEL_5.md`
- `10_QUESTIONS_LEVEL_6.md`
- `11_QUESTIONS_LEVEL_7.md`
- `12_QUESTIONS_LEVEL_8.md`
- `15_GATE_AND_BOSS_MILESTONE_SHEET.md`

### Đợt 4: Technical design và content schema

- toàn bộ doc schema ở `08_CONTENT_DATABASE`
- các doc logic ở `10_TECHNICAL_DESIGN`

### Đợt 5: Balance data

- toàn bộ `11_BALANCE_DATA`

## 13. Điều không được làm

- Không biến `12_QUESTION_FRAMEWORK` thành đồ bỏ sau khi viết GDD
- Không chọn 1 file nguồn rồi bỏ qua các file ảnh hưởng còn lại
- Không lược bỏ edge case để doc "gọn hơn"
- Không viết doc production khi chưa có `Source Coverage`
- Không coi stub hoặc outline là hoàn thành

## 14. Định nghĩa hoàn thành cuối cùng

Kế hoạch này chỉ được xem là hoàn thành khi:
- toàn bộ file trong `12_QUESTION_FRAMEWORK` đã có vai trò rõ trong sơ đồ nguồn
- mỗi doc đích có mapping nguồn đầy đủ
- việc viết GDD chuyển sang backlog có thứ tự rõ ràng
- không còn phải quay lại đoán xem file nào là nguồn của file nào

## 15. Hành động tiếp theo

Bước tiếp theo sau khi khóa kế hoạch này là:
- lập `backlog doc đích` chi tiết cho toàn bộ `00-11`
- mỗi doc có:
  - mức ưu tiên
  - source coverage
  - phụ thuộc
  - tiêu chuẩn hoàn thành riêng

Chỉ sau bước đó mới bắt đầu viết lại từng doc GDD production.
