Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 09/03/2026

# Equipment System

Tài liệu này chốt `equipment` như một lớp `loadout cơ học` nằm giữa `Inventory`, `Player Stats`, `Survival` và `Combat`. Nó không liệt kê item cụ thể. Nó trả lời các câu hỏi nền: món nào được coi là `equipped`, có những nhóm slot nào, equip/unequip/swap diễn ra ra sao, khi đổi đồ giữa combat thì điều gì xảy ra, item dùng mana bật tắt thế nào, item có durability hỏng ra sao, và ranh giới giữa `đồ đang cầm ở hotbar` với `đồ thật sự đang trang bị` nằm ở đâu.

Doc này là `bộ luật phát triển equipment/loadout`. Về sau `Items.md`, `Combat System.md`, `Crafting Economy.md` và `Balance Data` sẽ cắm nội dung cụ thể vào grammar này.

## Mục tiêu

- Chốt `armor slot`, `artifact slot`, và lớp `equipment slot` hỗ trợ đã được source khóa.
- Chốt rule `equip`, `unequip`, `swap`, đặc biệt là `combat swap`.
- Chốt interaction của equipment với:
  - `mana`
  - `durability`
  - `inventory`
  - `player stat nền`
- Tách rõ:
  - `đồ nằm trong inventory`
  - `đồ nằm ở hotbar`
  - `đồ đang equipped`

## Phạm vi

Tài liệu này tập trung vào:
- nhóm trang bị và vai trò của từng nhóm
- cấu trúc slot ở mức hệ thống
- equip/unequip/swap rule
- interaction giữa equipment với mana
- interaction giữa equipment với durability
- behavior khi swap giữa combat
- handoff giữa `Inventory System` và `Equipment System`

Tài liệu này không đi sâu vào:
- data table từng món đồ
- công thức damage cụ thể
- công thức kháng, set bonus, stat number cụ thể
- recipe craft / repair cost
- UI drag-drop pixel-perfect
- cây item hay danh mục item hoàn chỉnh

## Source Coverage

### Nguồn bắt buộc

- [12_QUESTIONS_LEVEL_8.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/12_QUESTIONS_LEVEL_8.md)
  - là nguồn tổng quát cho:
    - slot giáp và artifact
    - vai trò của giáp
    - vai trò của artifact
    - durability của giáp
    - loadout thinking
- [14_INVENTORY_AND_ITEM_RULES_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/14_INVENTORY_AND_ITEM_RULES_SHEET.md)
  - là nguồn đúng trực tiếp cho:
    - khoảng `4 ô artifact`
    - đổi artifact tự do ở mọi lúc
    - đổi artifact giữa combat áp dụng ngay
    - thay giáp giữa combat áp dụng ngay
    - giáp `0 durability` vẫn nằm ở slot nhưng vô tác dụng
    - artifact có loại dùng mana, có loại có durability
    - artifact `0 durability` thì vỡ mất luôn
    - artifact có durability thì không sửa được
    - phụ kiện tăng túi nằm ở equipment slot riêng

### Nguồn đối chiếu bắt buộc

- [Inventory System.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/03_PLAYER_SYSTEMS/Inventory%20System.md)
  - dùng để giữ đúng ranh giới giữa:
    - `hotbar`
    - `túi chính`
    - `equipped`
- [Player Stats.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/03_PLAYER_SYSTEMS/Player%20Stats.md)
  - dùng để giữ đúng vai trò của equipment:
    - không phải nguồn tăng trưởng nền chính
    - nhưng là `loadout cơ học` nặng
- [Survival System.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/02_CORE_SYSTEMS/Survival%20System.md)
  - dùng để giữ đúng interaction giữa equipment và mana

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - doc này đã đủ rõ để làm nguồn đúng cho:
    - `Items.md`
    - `Combat System.md`
    - `Crafting Economy.md`
    - `Network Sync Rules.md`
    - QA test case về equip/swap/break state
  - những chỗ như:
    - số slot giáp cụ thể
    - số artifact slot cuối cùng
    - stat số của từng set
    - mana upkeep number
    vẫn thuộc lớp balance/content về sau

## Conflict Resolution

- Wording cũ từng mô tả `trang bị / giáp / artifact` như lớp buff tạm thời. Quyết định cuối là:
  - chúng không phải nguồn tăng trưởng nền chính như `điểm chỉ số`
  - nhưng là `loadout cơ học khá nặng`, có thể đổi cách người chơi vận hành build rõ rệt
- `Tool` và `Weapon` không được coi là slot equipment bền vững trong doc này. Chúng chủ yếu sống ở:
  - `hotbar`
  - `inventory`
  - trạng thái cầm dùng tức thời
- `Hotbar` không phải equipment slot.
- `Accessory tăng túi` là một ngoại lệ đã được source khóa:
  - nó thuộc equipment layer
  - nhưng tác động chính của nó đi vào inventory capacity
- Rule cuối cho combat swap hiện tại là rất mở:
  - đổi artifact giữa combat được
  - thay giáp giữa combat được
  - áp dụng ngay
  - không thêm delay chống abuse riêng ở giai đoạn này

## Rule Summary

- Người chơi có `slot equipment` riêng cho:
  - `giáp`
  - `artifact`
  - và ít nhất một nhánh `phụ kiện chức năng` đã khóa là `phụ kiện tăng túi`
- `Artifact` là lớp loadout rất quan trọng:
  - khoảng `4 ô`
  - có thể cho passive
  - mở hiệu ứng đặc biệt
  - tăng utility hoặc mana-related behavior
- `Giáp` là lớp giảm sát thương, kháng hiệu ứng hoặc mang hiệu ứng riêng.
- `Giáp` có thể mạnh theo:
  - set bonus
  - hoặc theo từng món riêng
- `Artifact` có hai hướng lớn đã khóa:
  - loại dùng mana
  - loại có durability
- `Artifact` loại dùng mana:
  - còn mana thì chạy
  - hết mana thì tắt ngay
- `Artifact` loại có durability:
  - hao theo từng loại
  - về `0` thì vỡ mất luôn
  - hiện tại không sửa được
- `Giáp` về `0 durability`:
  - vẫn nằm ở slot
  - nhưng vô tác dụng
- `Artifact` và `giáp` đều có thể đổi giữa combat.
- Đổi giữa combat hiện tại:
  - artifact cũ mất hiệu ứng ngay
  - artifact mới vào ngay
  - giáp mới áp stat ngay

## Equipment Families

## 1. Armor

- Là nhóm trang bị phòng thủ/chuyển hóa sát thương/chống hiệu ứng.
- Có thể:
  - giảm sát thương
  - kháng hiệu ứng
  - mang hiệu ứng riêng
- Có thể mạnh theo:
  - set bonus
  - hoặc từng món độc lập
- Có durability.
- Khi hỏng về `0`, món giáp không biến mất ngay nhưng mất hiệu lực.

## 2. Artifact

- Là nhóm trang bị đặc biệt định hình loadout mạnh.
- Có khoảng `4 ô artifact` ở bản hiện tại.
- Không phải loot stack đại trà.
- Có thể:
  - cộng chỉ số thụ động
  - mở hiệu ứng đặc biệt
  - tăng utility
  - tăng hoặc điều hướng khả năng dùng mana
- Có hai dạng lớn:
  - dạng dùng mana
  - dạng có durability

## 3. Functional Accessory

- Đây là nhóm phụ kiện không nhất thiết trực tiếp tăng combat, nhưng vẫn là equipment thật.
- Rule đã khóa hiện tại:
  - `phụ kiện tăng túi` nằm ở slot equipment riêng
- Hệ này cho phép về sau tồn tại thêm phụ kiện chức năng khác, nhưng doc hiện chỉ khóa những gì đã có nguồn.

## 4. Tool / Weapon không thuộc equipment slot bền vững

- Tool và weapon không được mô tả như armor/artifact trong doc này.
- Chúng chủ yếu sống ở:
  - `hotbar`
  - `inventory`
  - trạng thái action trực tiếp
- Equip layer hiện không gánh trách nhiệm quản lý `tool/weapon slot vĩnh viễn`.

## Slot Structure

## Slot giáp

- Có `slot giáp riêng`.
- Tài liệu nguồn hiện chưa khóa breakdown chi tiết kiểu:
  - đầu
  - ngực
  - tay
  - chân
- Vì vậy doc này chỉ khóa:
  - tồn tại `nhóm slot giáp`
  - mỗi món giáp đi vào một slot hợp lệ trong nhóm đó

## Slot artifact

- Có `slot artifact riêng`.
- Số lượng hiện tại: `khoảng 4 ô`.
- Đây là số đủ gần để định hình loadout, nhưng vẫn nên xem là biến balance/UI có thể tinh chỉnh.

## Slot phụ kiện chức năng

- Ít nhất có `slot phụ kiện tăng túi`.
- Slot này thuộc equipment layer, không thuộc hotbar và không thuộc grid inventory.

## State List

### Trạng thái vị trí

- `In Inventory`
  - item nằm trong túi hoặc hotbar
- `Equipped`
  - item đã rời khỏi luồng chứa thông thường để nằm trong slot equipment
- `Broken But Equipped`
  - áp dụng cho giáp:
    - vẫn còn ở slot
    - nhưng không còn hiệu lực
- `Destroyed`
  - áp dụng cho artifact có durability khi về `0`
  - item vỡ mất luôn

### Trạng thái hoạt động

- `Active`
  - equipment đang phát huy tác dụng
- `Inactive Due To Mana`
  - áp dụng cho artifact loại dùng mana khi người chơi hết mana
- `Inactive Due To Break`
  - áp dụng cho giáp 0 durability hoặc item hỏng nhưng còn tồn tại

## Equip Rules

### Điều kiện equip chung

- Item phải thuộc một `equipment family` hợp lệ.
- Phải có `slot` hợp lệ cho loại đó.
- Equip là hành vi tách item khỏi trạng thái inventory thông thường để chuyển vào equipment state.

### Unequip chung

- Unequip trả item về inventory.
- Nếu inventory không còn chỗ, hệ khác phải xử lý theo rule tương ứng:
  - ưu tiên trả về chỗ hợp lệ
  - nếu không có chỗ, phải rơi ra đất theo logic overflow/drop tương ứng
- Chi tiết overflow cuối cùng vẫn tuân theo `Inventory System`.

### Swap chung

- Swap là hành vi thay món đang equipped bằng món khác cùng nhóm.
- Ở bản hiện tại:
  - swap được phép rất tự do
  - không có cast time riêng
  - không có cooldown riêng
  - không có anti-abuse rule riêng ngoài friction tự nhiên của việc mở inventory/loadout

## Armor Rules

### Vai trò

- Giáp là lớp phòng thủ và chống chịu tình huống.
- Giáp không phải nguồn tăng trưởng nền chính như stat point.
- Nhưng giáp có thể đổi cách người chơi sống sót, tank, kháng môi trường hoặc chịu status.

### Combat swap

- Có thể thay giáp giữa combat.
- Mỗi lần thay là thay `từng món độc lập`.
- Khi thay:
  - giáp cũ mất hiệu lực ngay
  - giáp mới áp stat mới ngay
- Không có delay chống abuse riêng ở giai đoạn hiện tại.

### Durability

- Giáp có durability.
- Durability hao khác nhau giữa:
  - `hit vật lý`
  - `hit môi trường`
  - `ăn mòn đặc biệt`
- `Ăn mòn đặc biệt` hiện chỉ khóa ở mức:
  - trừ durability
  - chưa tự động thêm penalty khác trong doc này

### Khi về 0 durability

- Món giáp vẫn nằm ở slot.
- Nhưng trở thành `vô tác dụng`.
- Người chơi vẫn có thể thấy món giáp đang mang, nhưng không được hưởng hiệu lực gameplay từ nó.

## Artifact Rules

### Vai trò

- Artifact là lớp loadout có sức nặng cơ học cao.
- Nó không thay thế core survival, nhưng có thể đổi rõ:
  - utility
  - mana usage
  - passive effect
  - cách vận hành build

### Combat swap

- Có thể đổi artifact ở mọi lúc, kể cả giữa combat.
- Khi đổi:
  - buff cũ mất ngay
  - buff mới vào ngay
- Nếu việc đổi artifact làm giảm `mana tối đa`:
  - `mana hiện tại` bị clamp về trần mới

### Artifact dùng mana

- Chỉ cần người chơi còn mana là artifact chạy.
- Khi mana về `0`:
  - artifact tắt ngay
- Artifact loại này không nhất thiết có durability, tùy từng artifact cụ thể.

### Artifact có durability

- Durability hao `tùy loại artifact`.
- Khi về `0 durability`:
  - artifact `vỡ`
  - item `mất luôn`
  - slot trở thành trống
- Artifact loại này hiện `không sửa được`.

## Functional Accessory Rules

### Phụ kiện tăng túi

- Là một equipment thật, nằm ở slot riêng.
- Tác động chính:
  - tăng sức chứa inventory
- Khi mất hoặc tháo phụ kiện:
  - sức chứa giảm ngay
- Nếu việc giảm sức chứa gây overflow:
  - đồ dư rơi ra ngoài theo `Inventory System`

### Khi chết ở mode nặng

- Phụ kiện tăng túi có thể rơi như item thường.
- Điều này có thể kéo theo việc sức chứa giảm sau khi chết hoặc sau khi recovery.

## Interaction With Mana

- `Equipment System` không tự định nghĩa mana economy, nhưng phải tuân thủ `Survival System`.
- Artifact loại dùng mana:
  - phụ thuộc vào `mana cá nhân`
  - còn mana thì chạy
  - hết mana thì tắt ngay
- Equipment không được coi là nguồn tự sinh mana.
- Nếu effect equipment có liên quan tới mana tối đa hoặc mana sử dụng:
  - mọi thay đổi phải cập nhật ngay theo rule current/max đã khóa ở `Player Stats`

## Interaction With Durability

- Giáp:
  - có durability
  - hỏng thì vô tác dụng nhưng còn ở slot
- Artifact:
  - tùy loại
  - loại có durability thì vỡ mất luôn khi về `0`
- Doc này chỉ khóa `trạng thái và outcome`.
- Công thức trừ durability chi tiết, repair cost hoặc salvage outcome thuộc doc khác.

## Transition Rules

### In Inventory -> Equipped

Xảy ra khi:
- item thuộc family hợp lệ
- có slot hợp lệ
- người chơi thực hiện equip hoặc swap hợp lệ

### Equipped -> In Inventory

Xảy ra khi:
- người chơi unequip thành công
- inventory còn đích hợp lệ để nhận món đồ

### Equipped -> On Ground

Xảy ra khi:
- unequip nhưng inventory không nhận được
- hoặc phụ kiện/slot interaction buộc drop theo rule overflow

### Equipped -> Broken But Equipped

Áp dụng cho:
- `armor`

Xảy ra khi:
- durability về `0`

Kết quả:
- món đồ vẫn ở slot
- hiệu lực gameplay tắt

### Equipped -> Destroyed

Áp dụng cho:
- `artifact` loại có durability

Xảy ra khi:
- durability về `0`

Kết quả:
- món đồ vỡ mất luôn
- slot trống

### Active -> Inactive Due To Mana

Áp dụng cho:
- artifact loại dùng mana

Xảy ra khi:
- mana người chơi về `0`

Kết quả:
- effect dừng ngay
- item vẫn đang equipped nếu chưa bị tháo

## Core Flows

### 1. Equip giáp cơ bản

1. Người chơi chọn một món giáp hợp lệ trong inventory.
2. Hệ thống tìm slot giáp hợp lệ.
3. Món giáp chuyển sang trạng thái `Equipped`.
4. Stat/effect của món giáp được áp dụng ngay.

### 2. Thay giáp giữa combat

1. Người chơi mở inventory/loadout và chọn món giáp khác.
2. Món giáp cũ mất hiệu lực.
3. Món giáp mới vào slot.
4. Stat mới áp ngay.
5. Không có delay riêng ở lớp equipment.

### 3. Đổi artifact giữa combat

1. Người chơi chọn artifact mới.
2. Artifact cũ mất buff/effect ngay.
3. Artifact mới vào slot.
4. Buff/effect mới áp ngay.
5. Nếu max mana giảm, current mana bị clamp theo trần mới.

### 4. Artifact dùng mana bị cạn mana

1. Artifact đang active.
2. Mana người chơi tụt về `0`.
3. Artifact tắt ngay.
4. Khi người chơi có mana lại, artifact có thể chạy lại nếu rule item cụ thể không chặn.

### 5. Giáp hỏng về 0 durability

1. Một món giáp nhận thêm tổn hao durability.
2. Durability chạm `0`.
3. Món giáp vẫn nằm ở slot.
4. Hiệu lực của món giáp tắt.
5. Người chơi phải sửa hoặc thay món khác nếu muốn lấy lại hiệu lực.

### 6. Artifact vỡ về 0 durability

1. Artifact loại có durability tiếp tục bị hao.
2. Durability chạm `0`.
3. Artifact vỡ mất luôn.
4. Slot artifact trống ngay.

## Failure And Recovery

### Failure ở lớp equipment

- swap sai thời điểm làm build yếu đi ngay
- đổi artifact làm clamp mana hiện tại
- giáp hỏng mà người chơi không để ý, dẫn tới đang mang nhưng vô tác dụng
- artifact vỡ làm mất hẳn một phần loadout
- mất phụ kiện tăng túi làm kéo theo overflow inventory

### Recovery ở lớp equipment

- thay món khác ngay
- quay về repair/recraft nếu hệ item cho phép
- nạp mana lại để bật lại artifact loại dùng mana
- chấp nhận bỏ slot trống tạm thời và đổi chiến thuật

## Edge Cases

### 1. Thay giáp giữa combat

- được phép
- áp stat mới ngay
- không có delay đặc biệt

### 2. Đổi artifact giữa combat

- được phép
- buff cũ mất ngay
- buff mới vào ngay

### 3. Artifact làm giảm mana tối đa

- current mana bị clamp về trần mới
- không giữ mana vượt trần

### 4. Artifact dùng mana khi mana chạm 0

- tắt ngay
- không được “níu” tới hết nhịp hiện tại

### 5. Giáp 0 durability

- vẫn nằm ở slot
- nhưng vô tác dụng

### 6. Artifact 0 durability

- vỡ mất luôn
- không để lại trạng thái “broken but equipped”

### 7. Tháo phụ kiện tăng túi

- sức chứa giảm ngay
- overflow đẩy đồ dư ra ngoài theo logic inventory

### 8. Tool và weapon

- không xử lý như slot equipment bền vững ở doc này
- nếu cầm dùng thì do hotbar/inventory/combat layer quản lý

## Signs Of A Good Equipment System

- người chơi nhìn loadout và hiểu:
  - món nào là giáp
  - món nào là artifact
  - món nào chỉ là đồ cầm tay
- loadout tạo khác biệt lối chơi rõ mà không nuốt mất vai trò của survival, utility, machine và route preparation
- swap rule đọc được:
  - đổi là đổi ngay
  - hỏng là hỏng rõ
  - tắt do hết mana là tắt ngay
- armor và artifact cùng sống trong một grammar thống nhất nhưng vẫn khác outcome khi hỏng

## Signs Of A Broken Equipment System

- lẫn giữa `hotbar` và `equipped`
- equipment trở thành nguồn tăng trưởng nền chính, làm mờ `Player Stats`
- artifact dùng mana có trạng thái mập mờ lúc mana cạn
- giáp hỏng nhưng người chơi không biết nó còn hiệu lực hay không
- slot bag accessory không đồng bộ với inventory overflow
- armor/artifact swap trong combat có thêm nhiều ngoại lệ không đọc được

## Implementation Hooks

- Player equipment data tối thiểu:
  - `equipped_armor_slots`
  - `equipped_artifact_slots`
  - `equipped_functional_accessory_slots`
- Equipment item metadata tối thiểu:
  - `equipment_family`
  - `equip_slot_type`
  - `uses_mana`
  - `has_durability`
  - `breaks_at_zero`
  - `stays_equipped_when_broken`
  - `is_repairable`
  - `can_swap_in_combat`
- Event tối thiểu:
  - `equip_item`
  - `unequip_item`
  - `swap_equipment`
  - `equipment_broken`
  - `artifact_disabled_by_zero_mana`
  - `recalculate_equipment_effects`
  - `apply_inventory_overflow_from_equipment_change`
- QA hook tối thiểu:
  - equip giáp thường
  - thay giáp giữa combat
  - đổi artifact giữa combat
  - artifact dùng mana tắt khi mana về 0
  - artifact đổi làm clamp mana
  - giáp về 0 vẫn ở slot nhưng vô dụng
  - artifact về 0 vỡ mất luôn
  - tháo phụ kiện tăng túi làm rơi đồ dư ra ngoài

## Open Design Questions

- Breakdown chi tiết của `slot giáp` là gì.
- Số `artifact slot` cuối cùng có giữ đúng `4` hay tinh chỉnh nhẹ theo balance/UI.
- Có nên có thêm `functional accessory slot` khác ngoài phụ kiện tăng túi ở core game hay không.
- Artifact dùng mana khi được nạp mana trở lại có tự active lại hoàn toàn hay cần trigger riêng từ từng item.

## Open Balance Variables

- Số slot giáp thực tế
- Số artifact slot thực tế
- Mức độ chênh sức mạnh giữa build nhiều artifact utility và build thiên armor
- Đường cong hao durability của từng nhóm artifact
- Tỷ lệ set bonus so với sức mạnh từng món giáp riêng lẻ
- Tần suất người chơi nên đổi loadout giữa combat trước khi nó trở nên quá “miễn phí”
