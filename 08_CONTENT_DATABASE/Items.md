Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 10/03/2026

# Items

Tài liệu này chốt `hợp đồng dữ liệu` cho toàn bộ hệ vật phẩm của game. Nó không phải danh sách item cụ thể. Nó trả lời các câu hỏi nền: một item phải có những field gì, item được chia thành những họ nào, món nào stack hay không stack, món nào vào hotbar, món nào là equipment, món nào có durability hoặc charge riêng, món nào nuôi mana hoặc gate, món nào là milestone, và item được nối sang các hệ `Inventory`, `Equipment`, `Survival`, `Crafting`, `Building`, `Gate` như thế nào.

Doc này là `grammar` cho content item. Về sau:
- `Recipes.md`
- `Buildings.md`
- `Drop Tables.md`
- `Balance Data`
- các bảng content cụ thể

sẽ cắm item thật vào khung dữ liệu này.

## Mục tiêu

- Thay stub cũ bằng một `schema contract` dùng được cho design, code và data entry.
- Chốt `item family` đủ rõ để content về sau không bị trộn vai trò.
- Chốt các field lõi của `item definition` và `item instance`.
- Khớp toàn bộ rule item với:
  - `Inventory System`
  - `Equipment System`
  - `Survival System`
  - `Crafting Economy`
  - `Player Revive`
  - `Gate/Boss milestone`
- Giữ đúng nguyên tắc hiện tại:
  - chưa liệt kê item giả
  - chưa dựng content database giả
  - chỉ khóa bộ luật để item thật cắm vào sau

## Phạm vi

Tài liệu này tập trung vào:
- taxonomy của item
- schema chung cho item
- rule field bắt buộc và field theo họ item
- trạng thái runtime tối thiểu của item
- interaction của item với:
  - inventory
  - equipment
  - survival
  - crafting
  - durability
  - charge
  - gate fuel
  - death / tombstone / drop

Tài liệu này không đi sâu vào:
- danh sách item cụ thể
- con số cụ thể của từng item
- icon, art, rarity presentation chi tiết
- balance cuối cùng của từng item
- recipe table hoàn chỉnh
- drop rate cụ thể

## Source Coverage

### Nguồn bắt buộc

- [09_QUESTIONS_LEVEL_5.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/09_QUESTIONS_LEVEL_5.md)
  - dùng để khóa `họ tài nguyên`, vai trò content family và chỗ item nằm trong hệ sinh thái biome, POI, boss, loot
- [10_QUESTIONS_LEVEL_6.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/10_QUESTIONS_LEVEL_6.md)
  - dùng để khóa `resource tier`, `economy role`, `mana tier`, `milestone tier`, `đầu tư cạnh tranh`
- [12_QUESTIONS_LEVEL_8.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/12_QUESTIONS_LEVEL_8.md)
  - dùng để khóa rule gameplay trực tiếp của item:
    - slot behavior
    - stack logic
    - durability outcome
    - mana refill
    - repair / salvage
    - gate fuel
    - milestone item
- [14_INVENTORY_AND_ITEM_RULES_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/14_INVENTORY_AND_ITEM_RULES_SHEET.md)
  - là nguồn đúng trực tiếp cho:
    - hotbar / main bag behavior
    - stack vs non-stack
    - pin / lõi mana có charge riêng
    - artifact / armor durability outcome
    - phụ kiện tăng túi
    - repair kit là công trình đặt xuống
- [15_GATE_AND_BOSS_MILESTONE_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/15_GATE_AND_BOSS_MILESTONE_SHEET.md)
  - là nguồn đúng cho:
    - gate fuel family
    - gate repair input
    - milestone material
    - boss refarm material

### Nguồn đối chiếu bắt buộc

- [Inventory System.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/03_PLAYER_SYSTEMS/Inventory%20System.md)
- [Equipment System.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/03_PLAYER_SYSTEMS/Equipment%20System.md)
- [Survival System.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/02_CORE_SYSTEMS/Survival%20System.md)
- [Crafting Economy.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/06_ECONOMY_SYSTEM/Crafting%20Economy.md)
- [Player Revive.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/09_MULTIPLAYER/Player%20Revive.md)

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - doc này đủ rõ để trở thành nguồn đúng cho:
    - `Recipes.md`
    - `Buildings.md`
    - `Drop Tables.md`
    - `Combat Numbers.md`
    - `Mana Consumption.md`
    - các bảng item thật về sau
  - các bảng item thật phải tuân theo schema này thay vì tự thêm field ngẫu hứng

## Conflict Resolution

- Stub cũ từng mô tả item bằng một khung quá mỏng:
  - `ItemID`
  - `Name`
  - `Type`
  - `Rarity`
  - `Weight`
  - `StackSize`

  Khung đó không còn đủ dùng.

- `Weight` không còn là field lõi của item ở giai đoạn hiện tại, vì inventory đã chốt theo `slot system`.
- `Rarity` không được xem là field gameplay cốt lõi ở lớp hiện tại. Nếu có, nó chỉ là `content / presentation tag`, không phải thứ quyết định rule nền của item.
- Không phải mọi item đều chạy theo một logic stack chung:
  - tài nguyên thường và consumable thường có stack
  - tool, weapon, armor, artifact, accessory đa số không stack
  - pin / lõi mana không stack vì có charge riêng
  - milestone item stack tùy loại
- `Repair kit` không còn được xem là một tool cầm tay đơn giản. Ở lớp item, nó phải được nhìn như một `deployable / construction item` có đầu ra là công trình đặt xuống.

## Rule Summary

- `Items.md` là hợp đồng dữ liệu cho toàn bộ vật phẩm của game.
- Mỗi item phải được phân vào một `item family` đủ rõ để kéo ra đúng rule hệ thống.
- Hệ item hiện tại phải hỗ trợ tối thiểu các họ:
  - tài nguyên thường
  - consumable sinh tồn
  - tool
  - weapon
  - armor
  - artifact
  - functional accessory
  - mana container / fuel
  - milestone item
  - deployable / construction item
- Hệ item phải phân biệt rõ:
  - `item definition`: dữ liệu tĩnh dùng chung
  - `item instance`: trạng thái runtime của từng món hay từng stack
- `Weight` chưa nằm trong grammar hiện tại.
- `Durability` và `charge` là state thật, không được nhét chung như text mô tả.
- `Death split` của item chủ yếu phụ thuộc vào vị trí chứa item:
  - hotbar rơi đất
  - main bag vào bia mộ
  - equipped items theo rule của hệ equipment / mode tương ứng

## Item As Data Contract

Mỗi item trong game phải trả lời được 6 câu hỏi:

1. Nó là `họ item` nào.
2. Nó có thể nằm ở đâu:
   - hotbar
   - túi
   - slot equipment
   - slot xử lý của công trình
   - khe gate
3. Nó được dùng theo kiểu nào:
   - instant
   - animation ngắn
   - channel
   - passive khi equipped
   - chạy liên tục bằng mana
   - đặt xuống thành công trình
4. Nó có `durability`, `charge`, `stack` hay `milestone state` gì không.
5. Nó được sửa, tháo rã, tiêu hao, tái nạp hay phá hủy ra sao.
6. Nó kéo vào nhánh economy nào:
   - craft
   - repair
   - salvage
   - mana
   - gate
   - progression

Nếu một item chưa trả lời được 6 câu này, item đó chưa đủ rõ để vào production database.

## Item Definition Và Item Instance

## Item Definition

`Item Definition` là dữ liệu tĩnh dùng chung cho mọi bản sao của cùng một item type.

Ví dụ lớp này trả lời:
- item thuộc họ nào
- có stack không
- max stack bao nhiêu
- có được vào hotbar không
- có phải equipment không
- có durability / charge không
- có thể repair / salvage không
- có thể dùng làm fuel cho gate không

## Item Instance

`Item Instance` là trạng thái runtime của một món cụ thể hoặc một stack cụ thể.

Lớp này tồn tại vì game hiện tại đã có nhiều item không thể coi là “một id tĩnh là đủ”, ví dụ:
- tool có durability hiện tại
- armor có durability hiện tại
- artifact có thể đang active hoặc đã vỡ
- pin / lõi mana có charge hiện tại
- stack item có số lượng hiện tại
- item đang nằm trong:
  - hotbar
  - túi
  - bia mộ
  - slot công trình
  - slot gate

## Nguyên tắc

- `Definition` đi vào bảng content.
- `Instance` đi vào save/runtime/network state.
- Stackable item vẫn cần `instance` ở cấp stack slot, vì mỗi stack có số lượng và vị trí riêng.

## Item Families

## 1. Tài nguyên thường

Ví dụ vai trò:
- gỗ
- đá
- sợi
- quặng phổ thông

Rule lớp này:
- thường stack được
- stack cap thường nằm trong khoảng `20-40`
- chủ yếu ở `main bag`
- là đầu vào cho:
  - craft nền
  - repair
  - building
  - công thức trung gian

## 2. Consumable sinh tồn

Ví dụ vai trò:
- đồ ăn
- item hồi máu trực tiếp
- item hồi máu theo thời gian
- item nạp mana
- item utility tiêu hao

Rule lớp này:
- thường stack được
- stack cap thường nằm trong khoảng `20-40`
- thường cho vào:
  - hotbar
  - main bag
- có `use mode` rõ:
  - instant
  - short animation use
  - effect over time

## 3. Tool

Ví dụ vai trò:
- búa
- cuốc
- rìu
- tool utility chuyên dụng

Rule lớp này:
- mặc định `non-stack`
- thường vào:
  - hotbar
  - main bag
- có durability
- đa số về `0` thì gãy hoặc biến mất
- có thể được repair và salvage theo rule tương ứng

## 4. Weapon

Ví dụ vai trò:
- vũ khí cận chiến
- vũ khí tầm xa cơ bản

Rule lớp này:
- mặc định `non-stack`
- thường vào:
  - hotbar
  - main bag
- có durability nếu line vũ khí đó dùng durability
- chịu rule combat chứ không phải rule equipment slot bền vững

## 5. Armor

Rule lớp này:
- `non-stack`
- đi qua inventory rồi sang `equipment slot`
- có durability
- khi `0 durability`:
  - vẫn nằm ở slot
  - nhưng vô tác dụng
- có thể repair / salvage theo rule economy

## 6. Artifact

Rule lớp này:
- `non-stack`
- đi qua inventory rồi sang `artifact slot`
- là `loadout cơ học khá nặng`
- có loại:
  - dùng mana
  - có durability
- artifact loại dùng mana:
  - còn mana thì chạy
  - hết mana thì tắt ngay
- artifact loại có durability:
  - về `0` thì vỡ mất luôn
  - hiện tại không sửa được

## 7. Functional Accessory

Rule lớp này:
- `non-stack`
- đi qua inventory rồi sang `equipment slot`
- không nhất thiết trực tiếp tăng combat
- ví dụ đã khóa hiện tại:
  - phụ kiện tăng túi

## 8. Mana Container / Fuel

Ví dụ vai trò:
- pin mana
- bình mana
- lõi mana

Rule lớp này:
- `non-stack`
- có `charge` riêng
- có thể nằm ở:
  - hotbar
  - main bag
- dùng tới đâu trừ charge tới đó
- không bỏ phần dư khi nạp mana người chơi
- cùng họ logic với fuel dùng cho gate

## 9. Milestone Item

Ví dụ vai trò:
- boss core
- vật mở gate
- vật mở unlock lớn
- component milestone hiếm

Rule lớp này:
- stack `tùy loại`
- có món không stack
- không được mặc định đối xử như tài nguyên thường
- thường gắn mạnh với:
  - unlock
  - gate
  - boss milestone
  - tiến trình dài hạn

## 10. Deployable / Construction Item

Rule lớp này:
- là item trong inventory nhưng dùng để `đặt xuống` thành:
  - công trình
  - station
  - utility placeable
- đã có source chắc chắn cho ít nhất:
  - `repair kit`
- không được đối xử như consumable dùng một phát rồi mất nếu rule của công trình không phải như vậy
- cần field chỉ ra `deploy result`

## Universal Item Definition Fields

Mỗi `item definition` tối thiểu nên có các field sau:

### Nhóm identity

- `item_id`
- `display_name`
- `item_family`
- `content_tier`
- `short_role_description`

### Nhóm storage

- `can_stack`
- `max_stack`
- `can_place_in_hotbar`
- `can_place_in_main_bag`
- `can_enter_processing_slot`
- `can_enter_gate_slot`

### Nhóm use / activation

- `use_mode`
- `is_consumed_on_use`
- `can_use_from_hotbar`
- `requires_target`
- `requires_channel`

### Nhóm equipment

- `can_equip`
- `equipment_family`
- `equip_slot_type`

### Nhóm durability / charge

- `has_durability`
- `has_charge`
- `repairable`
- `salvageable`
- `break_behavior_at_zero`

### Nhóm economy / progression

- `craft_path`
- `unlock_rule_class`
- `is_milestone_item`
- `can_feed_gate`
- `can_place_as_building`

## Universal Item Instance Fields

Mỗi `item instance` hoặc `stack instance` tối thiểu nên có:

- `instance_id`
- `item_id`
- `location_state`
- `container_ref`
- `slot_index`
- `stack_amount`
- `current_durability`
- `current_charge`
- `runtime_flags`

### Ghi chú

- `stack_amount` vẫn cần tồn tại cho stack instance.
- `current_durability` chỉ meaningful nếu item có durability.
- `current_charge` chỉ meaningful nếu item có charge.
- `runtime_flags` có thể chứa các state như:
  - broken
  - inactive_due_to_mana
  - locked_to_process
  - in_gate_slot

## Family-Specific Field Extensions

## Tài nguyên thường

Nên có thêm:
- `resource_class`
- `common_sink_group`

## Consumable sinh tồn

Nên có thêm:
- `consumable_effect_class`
- `survival_channel`
- `effect_duration_class`
- `over_time_rule`

## Tool / Weapon

Nên có thêm:
- `action_class`
- `tool_tier_or_weapon_tier`
- `durability_class`
- `harvest_or_damage_role`

## Armor

Nên có thêm:
- `armor_role`
- `resistance_profile`
- `set_or_piece_group`

## Artifact

Nên có thêm:
- `artifact_mode`
- `mana_upkeep_class`
- `artifact_effect_class`
- `durability_loss_rule`

## Functional Accessory

Nên có thêm:
- `accessory_effect_class`
- `capacity_bonus` nếu là phụ kiện tăng túi

## Mana Container / Fuel

Nên có thêm:
- `max_charge`
- `charge_spend_mode`
- `charge_display_mode`
- `can_refill_player_mana`
- `can_refill_gate_energy`
- `empty_state_behavior`

## Milestone Item

Nên có thêm:
- `milestone_role`
- `consumed_by_unlock`
- `refarmable_or_not`

## Deployable / Construction Item

Nên có thêm:
- `deploy_result_type`
- `placement_rule_class`
- `recover_rule_class`
- `destroy_rule_class`

## Không Còn Là Field Lõi

Các field sau không được xem là lõi bắt buộc ở bản hiện tại:

- `weight`
  - vì inventory đang theo slot
- `rarity`
  - có thể tồn tại như tag phụ, nhưng chưa phải field điều khiển rule gameplay lõi
- `magic_school`
  - chưa phải grammar nền của game hiện tại
- `class_requirement`
  - game hiện chưa dùng class cứng

## Placement And Slot Behavior

## Hotbar

Nhóm item mặc định phù hợp với hotbar:
- consumable sinh tồn
- tool
- weapon
- utility dùng nhanh
- mana container / fuel dùng để nạp nhanh

Nhóm item không nên mặc định ưu tiên hotbar:
- tài nguyên thường
- milestone item
- đa số deployable lớn

## Main Bag

`Main bag` là nơi item có thể sống mặc định nếu:
- không phải equipment đang được mặc
- không phải item đang nằm ở processing slot
- không phải item đã gắn vào gate

## Equipment Slot

Chỉ các họ sau đi vào equipment layer:
- armor
- artifact
- functional accessory

## Processing Slot

Một số item phải cho phép đi vào `processing slot` của hệ khác, ví dụ:
- repair kit
- workstation

Item definition cần có field để biết item nào được phép vào loại slot xử lý nào.

## Gate Slot

Một số item có thể được nhét vào:
- khe sửa gate
- khe fuel gate

Điều này không được hard-code theo tên item; phải đi qua field họ item / role item.

## Durability And Charge Rules

## Durability

Game hiện có ít nhất 4 outcome durability khác nhau:

### 1. Gãy mất ở 0

Áp dụng điển hình cho:
- tool
- weapon kiểu dùng durability
- một số item đặc biệt khác

### 2. Vẫn còn item nhưng vô tác dụng

Áp dụng điển hình cho:
- armor

### 3. Vỡ mất luôn

Áp dụng điển hình cho:
- artifact loại có durability

### 4. Tùy loại item

Schema phải cho phép từng item chọn đúng outcome của nó, không ép mọi item chung một rule.

## Charge

Game hiện có một họ charge rất quan trọng:
- pin / bình / lõi mana

Rule đã khóa:
- non-stack
- có `current_charge`
- có `max_charge`
- dùng tới đâu trừ tới đó
- không bỏ phần dư
- có món về `0 charge` thì còn vỏ
- có món về `0 charge` thì biến mất

Vì vậy schema phải hỗ trợ cả hai outcome:
- `empty_but_remains`
- `empty_and_destroyed`

## Use And Activation Modes

Mỗi item có thể được gán một `use mode` chính:

### 1. `instant_use`

Dùng một phát và resolve ngay.

### 2. `short_animation_use`

Dùng với animation ngắn, như:
- ăn
- uống bình mana

### 3. `channel_use`

Phải giữ thao tác trong một khoảng thời gian.

### 4. `equipped_passive`

Phải được mặc hoặc gắn vào loadout thì mới chạy.

### 5. `continuous_mana_upkeep`

Phải được giữ hoạt động bằng mana cá nhân.

### 6. `deployable_use`

Dùng để đặt thành công trình hoặc thiết bị ngoài world.

Schema phải cho phép một item định nghĩa:
- cách kích hoạt
- có bị tiêu hao không
- có cần mana không
- có cần channel không
- có bị hủy khi bị hit hay không

## Death, Drop, Tombstone And Recovery Hooks

Ở lớp item, rule chết hiện tại chủ yếu phụ thuộc vào `item location`, không phụ thuộc hoàn toàn vào `item family`.

## Nếu item ở hotbar khi chết

- rơi xuống đất
- giữ stack như lúc ở hotbar
- có thể bị auto-loot lại theo rule ground loot

## Nếu item ở main bag khi chết

- vào bia mộ
- giữ layout túi

## Nếu item là equipment

Schema item phải đủ rõ để system khác biết:
- món này có thể rơi như item thường hay không
- có bị mất nếu vỡ từ trước hay không
- có ảnh hưởng gián tiếp tới inventory capacity hay không

## Crafting, Repair, Salvage And Processing Hooks

Mỗi item nên cho biết nó tham gia vào những vòng nào:

### 1. Crafting Input

- có dùng như ingredient không
- thuộc class nguyên liệu nào

### 2. Craft Output

- có phải thành phẩm craft được không
- craft tay hay qua workstation

### 3. Repair Target

- có sửa được không
- sửa ở base hay repair kit
- nếu hỏng thì outcome là gì

### 4. Salvage Target

- có tháo rã được không
- tháo rã ra nhóm gì

### 5. Processing Item

- có thể được nhét vào:
  - repair kit
  - machine
  - station
  - gate slot

## Gate And Mana Hooks

Item schema phải hỗ trợ ít nhất ba vai trò liên quan tới mana và gate:

## 1. Nạp mana cá nhân

Ví dụ:
- pin
- bình
- lõi mana

## 2. Fuel cho gate

Cùng họ logic với item nạp mana, nhưng phải có field riêng để biết:
- món nào feed gate được
- giá trị feed là bao nhiêu

## 3. Vật liệu sửa gate / milestone

Phải tách rõ với fuel:
- fuel là vận hành
- repair material là milestone / module progression

## Transition Rules

### Definition-Level

- `Item Definition` không đổi trạng thái runtime.
- Nó chỉ định nghĩa khả năng.

### Instance-Level

Một `item instance` có thể đi qua các transition chính:

1. `On Ground -> In Inventory`
2. `In Inventory -> In Hotbar`
3. `In Inventory -> Equipped`
4. `Equipped -> Broken But Present`
5. `Equipped -> Destroyed`
6. `In Inventory -> Processing Slot`
7. `Processing Slot -> In Inventory`
8. `In Inventory -> Gate Slot`
9. `Gate Slot -> Consumed / Returned / No Effect`

Schema phải hỗ trợ mô tả đúng các transition này bằng field và flag, không ép mọi item cùng một đường đi.

## Core Flows

## 1. Flow tài nguyên thường

1. Nhặt tài nguyên từ đất.
2. Vào stack hotbar hoặc túi theo pickup order.
3. Mang về làm input cho craft / repair / building.

## 2. Flow consumable sinh tồn

1. Item nằm ở hotbar hoặc túi.
2. Người chơi dùng item.
3. Item resolve theo `use mode`.
4. Nếu là consumable chuẩn:
   - giảm stack
   - hoặc mất món

## 3. Flow mana container

1. Item nằm ở hotbar hoặc túi.
2. Người chơi dùng để nạp mana.
3. Hệ trừ `current_charge` đúng phần đã dùng.
4. Không bỏ phí phần dư.
5. Khi charge về `0`, outcome tùy item:
   - còn vỏ
   - hoặc biến mất

## 4. Flow armor / artifact

1. Item đi từ inventory sang equipment slot.
2. Hệ áp effect ngay.
3. Nếu hết durability hoặc hết mana:
   - armor: còn ở slot nhưng vô tác dụng
   - artifact dùng mana: tắt ngay
   - artifact có durability: vỡ mất luôn

## 5. Flow deployable item

1. Item nằm trong inventory.
2. Người chơi dùng ở vị trí hợp lệ.
3. Item chuyển thành công trình đặt trong world.
4. Khi thu hồi hoặc bị phá, outcome theo rule của deployable đó.

## Failure And Recovery

### Failure ở lớp item

- nhét sai item vào gate nhưng không có tác dụng
- cố stack item có charge riêng
- item bị overflow và rơi đất
- dùng sai loại item trong sai ngữ cảnh
- item về `0 durability` dẫn tới outcome khác nhau mà system không biểu diễn đúng

### Recovery ở lớp item

- repair item nếu thuộc loại repairable
- salvage item để thu hồi một phần giá trị
- sạc lại item charge nếu loại đó cho phép
- nhặt lại item từ đất hoặc bia mộ

## Edge Cases

### 1. Hai món cùng `item_id` nhưng khác `current_charge`

- không được stack

### 2. Hai món cùng `item_id` nhưng khác `current_durability`

- không được merge thành một object duy nhất

### 3. Artifact vỡ

- item biến mất
- không tự sinh “phế liệu artifact” nếu source không nói có

### 4. Armor hỏng

- vẫn hiện ở equipment slot
- nhưng không còn hiệu lực

### 5. Tool gãy ở hit cuối

- nếu hit cuối đã hợp lệ thì loot vẫn ra
- sau đó tool mới gãy

### 6. Milestone item

- có món stack thấp
- có món không stack
- schema không được mặc định mọi milestone item đều cùng một rule

### 7. Repair kit

- ở lớp item nó là `deployable / construction item`
- không được lẫn với tool cầm tay dùng trực tiếp

### 8. Pin / lõi mana

- là `charge container`
- không được xử lý như potion một lần dùng rồi bỏ phần dư

## Signs Of A Good Item Schema

- thêm item mới chủ yếu là điền field, không phải sửa logic code lõi
- nhìn vào item family là đoán được phần lớn behavior của item
- item có durability, charge, stack, equip, deploy cùng sống trong một grammar thống nhất
- không cần hard-code “item đặc biệt” chỉ vì schema thiếu field
- `Inventory`, `Equipment`, `Survival`, `Crafting`, `Gate` đọc cùng một item theo cùng một hợp đồng

## Signs Of A Broken Item Schema

- mọi item đều nhét vào một field `Type` chung chung rồi code tự đoán tiếp
- `weight` tồn tại dù inventory không dùng weight
- charge và durability bị nhét thành text mô tả thay vì state thật
- item deployable và consumable bị dùng chung logic
- milestone item bị đối xử như tài nguyên thường
- phải làm ngoại lệ code riêng chỉ để hỗ trợ:
  - armor 0 vẫn ở slot
  - artifact 0 vỡ mất
  - pin dùng dở vẫn còn

## Implementation Hooks

### Bảng dữ liệu tối thiểu

- `item_definitions`
- `item_family_rules`
- `item_instances`

### Field nhóm definition tối thiểu

- `item_id`
- `display_name`
- `item_family`
- `content_tier`
- `can_stack`
- `max_stack`
- `can_place_in_hotbar`
- `can_place_in_main_bag`
- `can_equip`
- `equipment_family`
- `equip_slot_type`
- `has_durability`
- `has_charge`
- `repairable`
- `salvageable`
- `use_mode`
- `is_milestone_item`
- `can_feed_gate`
- `can_place_as_building`

### Field nhóm instance tối thiểu

- `instance_id`
- `item_id`
- `location_state`
- `container_ref`
- `slot_index`
- `stack_amount`
- `current_durability`
- `current_charge`
- `runtime_flags`

### QA hook tối thiểu

- stack item thường
- item charge không stack
- armor 0 vẫn ở slot nhưng vô tác dụng
- artifact 0 vỡ mất
- mana container dùng dở không mất phần dư
- item hotbar rơi đất khi chết
- item túi vào bia mộ khi chết
- deployable item đặt xuống thành công trình
- item nhét sai vào gate nhưng không có tác dụng

## Open Design Questions

- Quy ước `item_id` cuối cùng nên theo pattern nào.
- Có cần chuẩn hóa `rarity_tag` thành field content phụ ngay từ bây giờ hay để sau.
- Nhóm `deployable / construction item` có nên tách thêm nhánh con:
  - station kit
  - trap kit
  - field utility kit
  hay hiện tại chỉ giữ ở mức family chung.
- Milestone item có nên chia rõ subfamily:
  - key item
  - boss material
  - gate module material
  - unlock artifact component
  hay để `milestone_role` xử lý sau.
- Có cần thêm field riêng cho `ownership / anti-theft` ở PvP mode hay để layer multiplayer quản lý ngoài item schema.

## Open Balance Variables

- stack cap thật của từng family
- family nào được vào hotbar mặc định
- độ rộng thật của `content_tier`
- dải durability của từng family
- dải max charge của từng mana container
- item nào thuộc nhóm milestone stack thấp hay không stack
- item nào cho phép deploy trực tiếp từ hotbar
- số lượng family deployable thật sự cần có trong MVP
