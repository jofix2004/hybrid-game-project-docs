Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 08/03/2026

# Inventory System

Tài liệu này chốt hệ thống túi đồ của người chơi như một `bộ luật phát triển item`, không phải danh sách item cụ thể. Nó trả lời các câu hỏi nền: item được phép nằm ở đâu, nhặt vào theo thứ tự nào, stack ra sao, khi đầy túi thì chuyện gì xảy ra, khi chết thì món nào rơi đất và món nào vào bia mộ, loot trên đất được ai nhặt, và các trường hợp overflow được xử lý thế nào.

Doc này là `grammar` của item/inventory. Về sau `Items.md`, `Recipes.md`, `Equipment System.md` và `Crafting Economy.md` sẽ cắm nội dung cụ thể vào bộ luật này.

## Mục tiêu

- Chốt `hotbar`, `túi chính`, `pickup order`, `overflow`, `ground loot`, `tombstone interaction`.
- Biến toàn bộ rule inventory trong `Level 8` và `Inventory/Item Rules Sheet` thành doc production dùng được cho design, code và QA.
- Tách rõ:
  - `Inventory System`
  - `Equipment System`
  - `Items content`
- Giữ đúng nguyên tắc hiện tại:
  - inventory là luật vận hành
  - không giả lập danh sách item khi content chưa được xây

## Phạm vi

Tài liệu này tập trung vào:
- cấu trúc túi đồ của người chơi
- loại không gian chứa item
- rule nhặt item và sắp item
- stack / non-stack behavior ở cấp hệ thống
- item trên đất
- overflow
- interaction giữa inventory với death, revive, tombstone
- interaction giữa inventory với phụ kiện tăng túi
- interaction inventory tối thiểu với item có `charge riêng`

Tài liệu này không đi sâu vào:
- slot giáp, slot artifact, equip/unequip/swap chi tiết
- công thức durability, repair, salvage
- data table item cụ thể
- network schema chi tiết
- UI pixel-perfect của drag/drop

## Source Coverage

### Nguồn bắt buộc

- [12_QUESTIONS_LEVEL_8.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/12_QUESTIONS_LEVEL_8.md)
  - là nguồn tổng quát cho `hotbar + túi chính`, slot logic, pickup order, death drop, bia mộ và các rule inventory chạm vào survival/death loop
- [14_INVENTORY_AND_ITEM_RULES_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/14_INVENTORY_AND_ITEM_RULES_SHEET.md)
  - là nguồn đúng trực tiếp cho:
    - số ô hotbar
    - số ô túi chính
    - pickup order
    - stack behavior
    - tombstone interaction
    - free-loot
    - auto-loot
    - phụ kiện tăng túi
    - item có charge riêng

### Nguồn hỗ trợ

- [13_PLAYER_CORE_STATE_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/13_PLAYER_CORE_STATE_SHEET.md)
  - dùng để khóa interaction giữa inventory và `death / respawn / recovery marker`
- [Player Revive.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/09_MULTIPLAYER/Player%20Revive.md)
  - dùng để giữ đúng handoff giữa `hotbar rơi đất`, `bia mộ`, `mode thường / PvP mode`
- [Multiplayer Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Multiplayer%20Loop.md)
  - dùng để giữ đúng vai trò social/tactical của free-loot, recovery và chia đồ trong co-op

### Nguồn đối chiếu bắt buộc

- [Player Stats.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/03_PLAYER_SYSTEMS/Player%20Stats.md)
  - dùng để không lẫn inventory với layer `current/max stat`

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - doc này đã đủ rõ để làm nguồn đúng cho `Equipment System`, `Items.md`, `Crafting Economy`, `Player Revive`, `Multiplayer Support`, và QA test case của pickup / overflow / death recovery
  - các con số cụ thể như stack cap từng item, bán kính auto-loot hay icon UI vẫn thuộc lớp balance/UI refinement

## Conflict Resolution

- Bản nháp cũ từng gợi ý `weight system`, nhưng rule chốt cuối là `slot system`.
- Pickup order cũ từng có hướng `túi > hotbar`; rule chốt cuối là:
  - `stack cũ hotbar`
  - `stack cũ túi`
  - `ô trống hotbar`
  - `ô trống túi`
- Các rule về `slot giáp`, `artifact`, `combat swap`, `durability`, `repair`, `salvage` chỉ được giữ ở mức inventory cần biết; phần sâu hơn sẽ chuyển sang doc khác.
- `Pin / lõi mana` không còn dùng rule tiêu thụ theo thứ tự slot. Chúng là item có `charge riêng`, và inventory chỉ cần hiểu chúng là `non-stack container` dùng được từ hotbar hoặc túi theo rule item.
- `Hotbar khi chết` và `bia mộ` là hai nhánh tách riêng:
  - hotbar luôn rơi đất
  - túi chính đi vào bia mộ

## Rule Summary

- Hệ inventory hiện tại dùng mô hình `hotbar + túi chính`.
- Giới hạn theo `slot`, chưa dùng `weight`.
- `Hotbar` là không gian dùng nhanh.
- `Túi chính` là không gian chứa loot, vật tư, đồ dự phòng.
- Khi nhặt item:
  - ưu tiên gộp vào `stack cũ hotbar`
  - rồi `stack cũ túi`
  - rồi `ô trống hotbar`
  - rồi `ô trống túi`
  - full cả hai thì item ở lại đất
- `Mode thường` đang dùng rule free-loot rất mở:
  - loot rơi đất ai cũng nhặt được
  - bia mộ ai cũng mở được
- Khi chết:
  - `hotbar` rơi xuống đất
  - `túi chính` đi vào `bia mộ`
- `Túi tăng theo phụ kiện` là hợp lệ, nhưng nếu tháo phụ kiện làm overflow thì đồ dư rơi ra ngoài ngay.
- Inventory chỉ chốt luật vận hành của nhóm item; không liệt kê item cụ thể ở giai đoạn này.

## State List

### Trạng thái của item theo vị trí

- `On Ground`
  - item đang nằm trên đất
- `In Hotbar`
  - item đang ở một ô hotbar
- `In Main Bag`
  - item đang ở một ô túi chính
- `In Tombstone`
  - item đang ở bia mộ sau khi người chơi chết
- `Equipped`
  - item đã rời inventory thông thường để sang slot trang bị
  - trạng thái này chỉ được nhắc ở mức handoff, chi tiết do `Equipment System` quản lý

### Trạng thái logic của stack

- `Can Stack`
  - item có thể gộp stack
- `Full Stack`
  - stack đã đạt giới hạn
- `Non-Stack`
  - item luôn chiếm một slot riêng

### Trạng thái logic của sức chứa

- `Has Space`
  - còn ít nhất một đích hợp lệ để nhét item vào
- `Overflow`
  - không còn đích hợp lệ trong inventory hiện tại

## Inventory Structure

### Hotbar

- Có `8 ô`.
- Là khu dùng nhanh.
- Dùng cho:
  - tool
  - weapon
  - consumable
  - utility cầm tay
  - item nạp mana dùng nhanh
- Hotbar không phải slot trang bị.
- Hotbar là phần chịu rủi ro cao hơn khi chết vì rơi thẳng xuống đất.

### Túi chính

- Đầu game có `24 ô`.
- Là nơi chứa:
  - loot
  - nguyên liệu
  - consumable dự phòng
  - item không cần giữ ở tay
- Có thể tăng sức chứa theo:
  - tiến trình
  - hoặc phụ kiện tăng túi

### Không dùng weight

- Inventory hiện không dùng `weight`.
- Toàn bộ luật giới hạn dựa trên:
  - số ô
  - stack cap của từng nhóm item

## Item Classes At Inventory Level

Doc này không liệt kê item cụ thể, nhưng khóa các `họ item` để content về sau cắm vào:

### 1. Tài nguyên thường

- thường có stack
- stack cap nằm khoảng `20-40` tùy item
- là nhóm chính của loot nền

### 2. Consumable

- thường có stack
- stack cap nằm khoảng `20-40` tùy item
- có thể nằm ở hotbar hoặc túi

### 3. Tool / Weapon / Equipment

- mặc định `non-stack`
- chiếm từng slot riêng

### 4. Mana container / pin / lõi

- `non-stack`
- vì có `charge riêng`
- có thể nằm ở hotbar để dùng nhanh
- inventory phải bảo toàn state charge của từng món

### 5. Milestone item

- stack `tùy loại`
- có món stack thấp
- có món không stack
- inventory không giả định tất cả milestone item đều vận hành như tài nguyên thường

## Placement Rules

### Hotbar hợp lệ với gì

- tool
- weapon
- consumable
- utility cầm tay
- item nạp mana nhanh

### Túi chính hợp lệ với gì

- gần như mọi item không bị khóa bởi system khác
- là đích mặc định khi hotbar không phù hợp hoặc không còn chỗ

### Equipped là handoff sang system khác

- Khi item được trang bị thực sự, nó không còn chỉ là item nằm trong grid inventory nữa.
- Rule equip/unequip/swap chi tiết thuộc `Equipment System`.

## Pickup Order

### Thứ tự ưu tiên

Khi người chơi nhặt một item từ đất, game xử lý theo thứ tự:

1. nhét vào `stack cũ trên hotbar`
2. nếu chưa được, nhét vào `stack cũ trong túi`
3. nếu chưa được, nhét vào `ô trống trên hotbar`
4. nếu chưa được, nhét vào `ô trống trong túi`
5. nếu vẫn không được, item ở lại đất

### Ý nghĩa thiết kế

- Hotbar được ưu tiên cao hơn túi ở mức `stack` và `ô trống`.
- Điều này làm cho flow dùng nhanh và refill nhanh bám sát tay người chơi hơn.
- Nó cũng giữ cho người chơi thấy phần mình đang dùng được gom logic hơn khi nhặt thêm cùng loại.

## Stack Rules

### Rule chung

- Hệ inventory không gán một stack cap chung cho mọi item.
- Stack cap là property của từng `item family` hoặc từng item cụ thể về sau.

### Rule hiện đã khóa

- `tài nguyên thường`: thường stack khoảng `20-40`
- `consumable`: thường stack khoảng `20-40`
- `mana container / pin / lõi`: không stack
- `milestone item`: tùy loại, có món không stack

### Gộp stack khi kéo trong hotbar

- nếu cùng loại thì ưu tiên gộp stack trước
- nếu không gộp được thì mới đổi vị trí

## Ground Loot Rules

### Loot rơi đất

- Khi item không vào được inventory, nó ở lại đất.
- Nhiều loại loot mặc định xuất hiện trên đất trước rồi mới được nhặt.

### Auto-loot

- Có cơ chế tự hút trong bán kính gần.
- Có `độ trễ ngắn` rồi mới hút.
- Áp dụng cho `mọi item` ở mode thường, bao gồm cả nhiều loại rơi từ:
  - khai thác
  - quái
  - hotbar rơi khi chết

### Free-loot ở mode thường

- Ở `mode thường`, loot rơi đất là tự do hoàn toàn.
- Điều này áp dụng cho:
  - loot quái / khai thác
  - đồ rơi từ hotbar khi chết
  - đồ trong bia mộ nếu người khác mở ra

### PvP mode

- Override rõ nhất hiện đã khóa là `bia mộ`.
- Các luật ownership sâu hơn cho loose ground loot ở PvP mode chưa được khóa đầy đủ ở doc này và phải được chốt ở doc multiplayer/network nếu cần.

## Overflow Rules

### Khi inventory đầy

- Nếu không còn:
  - stack hợp lệ
  - ô hotbar trống
  - ô túi trống
- thì item ở lại đất

### Khi tháo phụ kiện tăng túi

- Nếu việc tháo phụ kiện làm sức chứa giảm ngay và phát sinh overflow:
  - đồ dư rơi ra ngoài ngay
- Không dùng rule:
  - cấm tháo
  - hay khóa mềm slot mà không xử lý đồ

### Thứ tự rơi khi overflow

- Đồ dư rơi theo logic xếp đồ thông thường / theo thứ tự ô bị tràn
- Không có cơ chế ưu tiên “item ít quan trọng hơn” ở giai đoạn này

## Death, Tombstone, And Recovery Interaction

### Khi chết

- `recovery marker` xuất hiện đúng nơi chết
- `hotbar` rơi xuống đất
- `túi chính` đi vào `bia mộ`

### Hotbar

- rơi theo từng món
- nếu đang stack thì rơi theo stack đó
- không được đưa vào bia mộ

### Bia mộ

- hoạt động gần như một rương
- UI hiển thị kiểu `full lưới như rương`
- giữ đúng layout của `túi người chết`
- không chứa layout hotbar vì hotbar đã tách riêng xuống đất
- chỉ cho lấy đồ ra
- không cho nhét đồ vào
- không cho sắp xếp lại như một container dùng chung

### Quyền truy cập

- `mode thường`
  - ai cũng mở được
  - ai cũng lấy được
- `PvP mode`
  - chỉ `chủ nhân / đồng đội` được mở

### Thời gian tồn tại

- tùy mode
- có thể vô hạn
- hoặc rất dài
- bia mộ biến mất khi bên trong rỗng

## Bag Expansion Rules

### Nguồn tăng túi

- tiến trình
- phụ kiện tăng túi

### Phụ kiện tăng túi

- nằm ở `equipment slot riêng`
- khi mất phụ kiện:
  - sức chứa giảm ngay
- nếu việc giảm sức chứa gây overflow:
  - đồ dư rơi ra ngoài theo rule overflow

### Khi chết ở mode nặng

- phụ kiện tăng túi có thể rơi như item thường
- inventory phải chấp nhận việc sức chứa giảm sau khi mất phụ kiện

## Charge Container Rules At Inventory Level

Inventory chỉ chốt phần hành vi cần thiết cho item có charge:

- `pin / lõi mana` là item `non-stack`
- chúng có `charge riêng`
- có thể nằm ở hotbar để dùng nhanh
- dùng tới đâu trừ charge tới đó
- không buộc dùng hết cả món như consumable một lần
- hiển thị charge nên có:
  - thanh
  - và số tuyệt đối

Chi tiết effect gameplay của mana refill vẫn do `Survival System` và `Items` quyết định.

## Broken Item Interaction With Inventory

- đa số item khi `0 durability` có thể:
  - vỡ mất
  - làm slot trống ngay
- một số item đặc biệt:
  - vẫn ở lại slot
  - nhưng bị xám đi / vô tác dụng

Inventory không quyết định item nào “vỡ mất” hay “xám đi”; inventory chỉ phải hỗ trợ cả hai outcome.

## Transition Rules

### On Ground -> In Hotbar

Xảy ra khi:
- item hợp lệ với hotbar
- và vào được theo `pickup order`

### On Ground -> In Main Bag

Xảy ra khi:
- item không vào được hotbar trước
- hoặc hotbar không còn đích hợp lệ
- và túi chính còn đích hợp lệ

### On Ground -> On Ground

Xảy ra khi:
- inventory full
- hoặc item không có đích hợp lệ để nhận

### In Hotbar -> On Ground

Xảy ra khi:
- người chơi chết
- item rơi khỏi hotbar

Hoặc khi:
- item bị overflow do thay đổi sức chứa / hệ khác buộc drop ra đất

### In Main Bag -> In Tombstone

Xảy ra khi:
- người chơi chết

### In Tombstone -> In Hotbar / In Main Bag

Xảy ra khi:
- người chơi hoặc người khác lấy item ra
- inventory bên nhận còn đích hợp lệ theo rule thường

### In Main Bag / In Hotbar -> Equipped

Xảy ra khi:
- item được trang bị
- và rule equip cho phép

Chi tiết thuộc `Equipment System`.

## Core Flows

### 1. Flow nhặt loot bình thường

1. Item rơi trên đất.
2. Người chơi đi vào vùng nhặt hoặc auto-loot bắt đầu hút sau độ trễ ngắn.
3. Hệ thống thử nhét item theo thứ tự:
   - stack hotbar
   - stack túi
   - ô trống hotbar
   - ô trống túi
4. Nếu thành công, item rời khỏi đất và vào inventory.
5. Nếu thất bại, item vẫn ở lại đất.

### 2. Flow chết và recovery

1. Người chơi chết.
2. Hệ thống tạo `recovery marker`.
3. Item trong hotbar rơi xuống đất.
4. Item trong túi đi vào `bia mộ`.
5. Khi quay lại:
   - người chơi nhặt hotbar từ đất
   - mở bia mộ
   - lấy từng món ra theo layout cũ của túi

### 3. Flow tháo phụ kiện tăng túi gây overflow

1. Người chơi tháo phụ kiện tăng túi.
2. Sức chứa inventory giảm ngay.
3. Hệ thống tính toán item nào vượt quá sức chứa mới.
4. Các item dư rơi ra ngoài theo logic overflow.
5. Inventory còn lại ổn định ở sức chứa mới.

### 4. Flow dùng item có charge từ hotbar

1. Người chơi kích hoạt `pin / lõi mana` từ hotbar.
2. Item không biến mất ngay nếu còn charge.
3. Charge bị trừ tới đúng mức đã dùng.
4. Item tiếp tục ở hotbar hoặc túi với trạng thái charge mới.

## Failure And Recovery

### Failure ở cấp inventory

- đầy túi và không nhặt được loot
- tháo phụ kiện gây rơi đồ
- chết làm:
  - mất kiểm soát trực tiếp với hotbar
  - tách túi ra thành bia mộ

### Recovery ở cấp inventory

- quay lại nhặt hotbar rơi đất
- quay lại mở bia mộ
- thu hồi dần item về inventory mới
- chấp nhận bỏ lại những gì không đủ sức chứa hoặc không đáng cứu

### Ý đồ thiết kế

- inventory không chỉ là nơi chứa đồ
- mà là nơi biến `quyết định mang gì, bỏ gì, cứu gì` thành gameplay thật

## Edge Cases

### 1. Nhặt item khi hotbar đầy nhưng túi còn chỗ

- item mới đi vào túi nếu không còn đích hợp lệ trên hotbar

### 2. Nhặt item khi có stack dở cả ở hotbar lẫn túi

- luôn ưu tiên stack trên hotbar trước

### 3. Inventory đầy hoàn toàn

- item ở lại đất
- không được tự xóa item cũ để nhường chỗ

### 4. Hotbar và bia mộ

- không trộn
- hotbar không được copy vào bia mộ

### 5. Bia mộ khi inventory không đủ chỗ

- lấy món nào ra thì món đó ra
- không tự `loot all` và không tự nén phần dư theo cơ chế khác

### 6. Đồ milestone không stack

- nếu rơi nhiều món giống nhau trên đất thì hiển thị riêng từng món
- inventory không được tự coi chúng là một stack chỉ vì cùng id cơ bản nếu rule item nói là không stack

### 7. Item có charge

- không stack vì state khác nhau
- charge riêng phải được bảo toàn khi di chuyển giữa hotbar, túi và đất

### 8. Auto-loot và free-loot

- mode thường chấp nhận việc người khác cũng có thể hút hoặc nhặt loot trên đất
- đây là rule thiết kế, không phải bug

## Signs Of A Good Inventory System

- người chơi hiểu rất nhanh:
  - cái gì đang ở tay
  - cái gì đang ở túi
  - cái gì rơi đất
  - cái gì vào bia mộ
- việc nhặt đồ tạo quyết định thật mà không gây rối vô nghĩa
- overflow có đau nhưng đọc được
- death recovery rõ ràng, không nhập nhằng giữa hotbar và túi
- item có charge, item milestone, item stack thường cùng sống được trong một grammar thống nhất

## Signs Of A Broken Inventory System

- pickup order khó đoán
- hotbar và túi giành nhau theo logic ngẫu nhiên
- bia mộ và hotbar drop chồng lên nhau làm recovery rối
- overflow xử lý lúc rơi đất, lúc cấm thao tác, lúc khóa slot mà không có quy tắc chung
- item có charge bị mất state, gộp nhầm, hoặc bị coi như consumable thường
- inventory phải dựa vào danh sách hard-code item thay vì dựa vào item class và rule

## Implementation Hooks

- Player inventory cần field tối thiểu:
  - `hotbar_slot_count`
  - `main_bag_slot_count`
  - `hotbar_slots[]`
  - `main_bag_slots[]`
  - `bag_bonus_from_accessory`
- Item placement metadata tối thiểu:
  - `can_stack`
  - `max_stack`
  - `can_place_in_hotbar`
  - `can_place_in_main_bag`
  - `is_milestone_item`
  - `has_unique_charge_state`
- Event tối thiểu:
  - `pickup_item`
  - `auto_loot_tick`
  - `move_item`
  - `merge_stack`
  - `split_stack`
  - `drop_item`
  - `player_death_inventory_split`
  - `create_tombstone`
  - `loot_from_tombstone`
  - `recalculate_bag_capacity`
  - `apply_overflow_drop`
- Tombstone data tối thiểu:
  - owner
  - mode access rule
  - grid layout snapshot của túi
  - expire policy
- QA hook tối thiểu:
  - nhặt item khi có stack ở hotbar
  - nhặt item khi chỉ còn ô túi
  - nhặt item khi full cả hai
  - chết với hotbar + túi đầy
  - nhặt lại hotbar từ đất
  - mở bia mộ ở mode thường
  - mở bia mộ ở PvP mode
  - tháo phụ kiện tăng túi làm overflow
  - dùng item charge dở từ hotbar

## Open Design Questions

- PvP mode có cần khóa ownership sâu hơn cho `đồ rơi đất từ hotbar` hay không.
- Auto-loot có nên có whitelist nhỏ cho item quá quan trọng hay hiện tại cứ giữ “mọi item đều hút”.
- Có cần một UI action `loot all` cho bia mộ về sau hay vẫn giữ lấy từng món.

## Open Balance Variables

- stack cap thật của từng họ item
- bán kính auto-loot
- độ trễ auto-loot
- tốc độ hút item
- số ô túi tăng thêm từ từng loại phụ kiện
- quy mô item loss thực tế sau một lần chết và recovery
