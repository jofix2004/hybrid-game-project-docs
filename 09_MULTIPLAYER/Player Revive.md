Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 08/03/2026

# Player Revive

Tài liệu này chốt toàn bộ fail flow và recovery flow của người chơi khi `Máu = 0` trong bối cảnh co-op: khi nào vào `downed`, khi nào chết thật, ai cứu được, cứu bằng giá gì, đứng dậy với trạng thái nào, khi nào chuyển sang `respawn`, và các hệ nào phải nối vào flow này như `Survival`, `Multiplayer`, `hotbar drop`, `bia mộ`, `recovery marker`.

## Mục tiêu

- Chốt baseline `downed -> revive -> dead -> respawn` để dev, design và QA dùng chung một nguồn đúng.
- Tách rõ ranh giới giữa:
  - `revive trong combat`
  - `chết thật`
  - `respawn từ điểm hồi sinh`
- Khóa toàn bộ interaction quan trọng với:
  - `Máu`
  - `Thức ăn`
  - `Mana`
  - `recovery marker`
  - `hotbar rơi đất`
  - `bia mộ`
  - `mode thường / PvP mode`
- Làm rõ cost, reward, fail cost và edge cases của việc cứu nhau trong co-op.

## Phạm vi

Tài liệu này tập trung vào:
- điều kiện chuyển từ `Alive` sang `Downed` hoặc `Dead`
- trạng thái `Downed`
- hành động cứu dậy cơ bản
- kết quả của việc cứu dậy thành công hoặc thất bại
- flow chết thật và chuyển sang recovery
- các nguồn respawn đã chốt
- trạng thái người chơi sau khi respawn theo từng nguồn
- những rule liên quan trực tiếp tới co-op và recovery logistics

Tài liệu này không đi sâu vào:
- network packet, authority, rollback hay sync kỹ thuật thấp
- UI/UX chi tiết của prompt revive
- công thức damage, aggro hay combat tuning
- schema save/load đầy đủ
- inventory schema chi tiết của bia mộ ngoài các rule cần cho revive flow

## Source Coverage

### Nguồn bắt buộc

- [08_QUESTIONS_LEVEL_4.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/08_QUESTIONS_LEVEL_4.md)
  - chốt vai trò tối thiểu của co-op support: `downed/revive`, cứu nhau, thấy trạng thái đồng đội, đồng bộ hành động
- [12_QUESTIONS_LEVEL_8.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/12_QUESTIONS_LEVEL_8.md)
  - chốt state model, `downed`, `dead`, `recovery marker`, `hotbar rơi đất`, `bia mộ`, quyền mở bia mộ theo mode, reset effect theo điểm hồi sinh
- [13_PLAYER_CORE_STATE_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/13_PLAYER_CORE_STATE_SHEET.md)
  - là nguồn đúng trực tiếp cho toàn bộ rule hiện hành về `downed`, `revive`, `death`, `respawn`, trạng thái sau revive và sau respawn

### Nguồn hỗ trợ

- [14_INVENTORY_AND_ITEM_RULES_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/14_INVENTORY_AND_ITEM_RULES_SHEET.md)
  - dùng để khóa interaction với `hotbar`, `bia mộ`, free-loot và pickup sau khi chết
- [Multiplayer Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Multiplayer%20Loop.md)
  - dùng để giữ đúng vai trò cảm xúc và tactical value của việc cứu nhau
- [Survival System.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/02_CORE_SYSTEMS/Survival%20System.md)
  - dùng để giữ đúng handoff giữa `Máu`, `heal over time`, `Downed`, `Dead`, `Respawn`

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - baseline revive flow đã đủ rõ để làm nguồn đúng cho gameplay, QA và technical design
  - các lớp nâng cao như kỹ năng hồi sinh đặc biệt, item hồi sinh đặc chủng, hay variation riêng theo mode khó hơn có thể mở rộng sau, nhưng không được phá baseline đang khóa ở đây

## Conflict Resolution

- `Level 4` chốt nhu cầu hệ thống: co-op phải có cứu nhau, downed/revive và thấy được đồng đội.
- `Level 8` chốt rule gameplay tổng quát của death, tombstone, recovery và respawn.
- `13_PLAYER_CORE_STATE_SHEET.md` chốt bản cuối chi tiết nhất về:
  - `60 giây downed`
  - cứu cơ bản dùng `máu` của người cứu
  - đứng dậy với `50% HP`
  - vài giây miễn nhiễm hoặc giảm sát thương
  - respawn theo từng nguồn
- Khi wording giữa các nguồn khác nhau ở mức tổng quát và chi tiết, tài liệu này ưu tiên:
  1. `13_PLAYER_CORE_STATE_SHEET.md`
  2. `12_QUESTIONS_LEVEL_8.md`
  3. `08_QUESTIONS_LEVEL_4.md`

## Rule Summary

- Khi `Máu = 0`:
  - `solo`: chết thật ngay
  - `co-op`: vào `Downed` trước
- `Downed` là cửa sổ cứu nhau của co-op.
- Cứu cơ bản:
  - do đồng đội thực hiện
  - tiêu hao `máu` của người đi cứu
  - nếu hoàn tất trước khi timer về `0` thì cứu thành công
- Người được cứu:
  - đứng dậy với khoảng `50% HP`
  - có vài giây miễn nhiễm hoặc giảm sát thương
- Nếu `Downed` hết thời gian mà không được cứu:
  - chết thật ngay
- Khi chết thật:
  - có `recovery marker` ở đúng nơi chết
  - item trên `hotbar` rơi xuống đất
  - item trong túi vào `bia mộ`
- `Respawn` không đồng nghĩa với revive trong combat.
- Chất lượng respawn phụ thuộc nguồn hồi sinh:
  - `Base` tốt nhất
  - `điểm hồi sinh mở` kém hơn
  - `đồng đội / kỹ năng` yếu hơn nữa nếu là nhánh đặc biệt

## State List

- `Alive`
  - người chơi đang hoạt động bình thường
- `Downed`
  - chỉ tồn tại trong co-op
  - chưa chết thật, nhưng không còn ở trạng thái vận hành
- `Reviving`
  - đang có hành động cứu dậy diễn ra
- `Revived`
  - vừa được cứu thành công, đang ở cửa sổ an toàn ngắn
- `Dead`
  - chết thật, kết thúc fail flow chiến đấu hiện tại
- `Respawning`
  - đang chuyển từ trạng thái chết thật sang nguồn hồi sinh hợp lệ
- `Respawned`
  - đã quay lại game theo rule của điểm hồi sinh tương ứng

## Transition Rules

### Alive -> Downed

Xảy ra khi:
- người chơi ở `co-op`
- `Máu = 0`

Không xảy ra khi:
- đang chơi `solo`

### Alive -> Dead

Xảy ra khi:
- người chơi ở `solo`
- `Máu = 0`

Hoặc khi:
- người chơi ở `co-op`
- đã ở `Downed`
- timer về `0` mà không được cứu

### Downed -> Reviving

Xảy ra khi:
- một đồng đội bắt đầu hành động cứu

### Reviving -> Revived

Xảy ra khi:
- hành động cứu hoàn tất trước khi timer `Downed` chạm `0`

### Reviving -> Downed

Xảy ra khi:
- hành động cứu bị ngắt
- hoặc chưa hoàn tất xong
- người bị downed vẫn còn thời gian

### Downed -> Dead

Xảy ra khi:
- hết thời gian `Downed`
- hoặc fail flow của cứu không kịp hoàn tất

### Dead -> Respawning

Xảy ra khi:
- hệ thống đã xác định được nguồn hồi sinh hợp lệ
  - `Base`
  - `điểm hồi sinh mở`
  - `công trình hồi sinh`
  - hoặc nhánh `đồng đội / kỹ năng` nếu hệ đó tồn tại trong build đang dùng

### Respawning -> Respawned

Xảy ra khi:
- trạng thái hồi sinh theo nguồn tương ứng đã được áp dụng xong

## Downed Rules

### Điều kiện tồn tại

- Chỉ có trong `co-op`.
- Là lớp đệm giữa `Alive` và `Dead`.

### Hành vi khi Downed

- người chơi nằm im
- không di chuyển
- không hành động
- không tiếp tục vòng chơi bình thường

### Thời gian

- thời gian mặc định là `60 giây`
- có thể scale theo mode hoặc độ khó về sau, nhưng baseline hiện tại là `60 giây`

### Heal over time khi Downed

- `heal over time` vẫn tiếp tục chạy
- nhưng không thay thế rule cứu dậy
- người chơi vẫn cần được revive đúng flow để quay lại trạng thái vận hành

## Revive Rules

### Revive cơ bản

- do đồng đội thực hiện
- dùng `máu` của người cứu để đổi lấy lượt cứu đồng đội

### Điều kiện thành công

- hành động cứu phải hoàn tất trước khi timer `Downed` về `0`
- nếu hoàn tất trước `0` thì cứu thành công

### Cứu sát giờ

- nếu action hoàn tất trước khi timer chạm `0`
  - cứu thành công
- nếu timer chạm `0` trước khi action hoàn tất
  - người chơi chết thật

### Kết quả khi cứu thành công

- người được cứu đứng dậy với khoảng `50% HP`
- `Thức ăn` và các trạng thái vận hành khác nhìn chung giữ theo trạng thái trước lúc vào `Downed`, trừ khi một nguồn cứu đặc biệt có rule riêng
- `Mana` nhìn chung không được nạp lại miễn phí chỉ vì vừa được cứu
- có vài giây miễn nhiễm hoặc giảm sát thương
- các trạng thái khác không được reset như một lần respawn đầy đủ

### Effect đang có sau khi cứu dậy

- đây không phải `respawn đầy đủ`
- vì vậy logic giữ/reset effect nên bám gần trạng thái trước lúc ngã hơn là trạng thái của một điểm hồi sinh
- `heal over time` đang chạy có thể tiếp tục chạy
- các debuff chiến đấu nhìn chung không được coi là đã được "rửa sạch" chỉ vì vừa được đồng đội kéo dậy

### Revive nâng cao

- có thể tồn tại dưới dạng:
  - vật phẩm
  - kỹ năng
  - hoặc cơ chế đặc biệt
- nhưng baseline doc này chỉ khóa `cứu cơ bản`
- mọi revive nâng cao về sau phải:
  - không phá vỡ logic `downed`
  - không biến revive thành hành động miễn phí
  - không làm `respawn point` mất vai trò

## Death And Recovery Rules

### Khi chết thật

- tạo `recovery marker` rõ ở đúng nơi chết
- marker này giúp quay lại recovery dễ đọc hơn

### Hotbar

- item trên `hotbar` rơi thẳng xuống đất
- rơi đúng từng món theo logic vật lý đơn giản
- nếu món đang stack trên hotbar thì rơi theo stack đó

### Túi chính

- item trong túi đi vào `bia mộ`
- `bia mộ` hoạt động gần như một rương
- `bia mộ` biến mất khi bên trong rỗng

### Quyền mở bia mộ

- `mode thường`
  - ai cũng mở được
  - ai cũng có thể lấy tự do
- `PvP mode`
  - chỉ `chủ nhân / đồng đội` được mở

### Độ bền của bia mộ

- không thể phá hủy
- không thể chạy mất
- thời gian tồn tại:
  - tùy mode
  - có thể vô hạn
  - hoặc biến mất sau thời gian dài

## Respawn Sources

### Base

- là `điểm spawn gốc` hoặc `giường`
- là nguồn hồi sinh tốt nhất

### Điểm hồi sinh mở

- là công trình hồi sinh / điểm hồi sinh đã mở
- dùng hữu hạn lần
- tốn chi phí xây dựng
- hiệu quả hồi kém hơn `Base`

### Đồng đội / kỹ năng

- là nhánh hồi sinh yếu hơn nếu có triển khai
- hồi sinh thường sẽ chậm và yếu hơn
- nếu có kỹ năng chuyên hồi sinh thì chất lượng tốt hơn

## Respawn Outcome By Source

### Base respawn

- `Máu`: đầy
- `Thức ăn`: vừa hoặc no
- `Mana`: không nhất thiết đầy
- xóa sạch debuff ngắn
- xóa đa số debuff thường
- không cho buff an toàn riêng ngoài việc bản thân `Base` đã là nơi hồi tốt nhất

### Điểm hồi sinh mở

- `Máu`: khoảng nửa hoặc hơn
- `Thức ăn`: thấp hơn base
- `Mana`: thấp hoặc gần như không có
- giữ lại nhiều debuff hơn `Base`

### Hồi sinh bởi đồng đội / kỹ năng

- `Máu`: thấp hay cao tùy kỹ năng, nhưng mặc định thấp hơn điểm hồi sinh mở
- `Thức ăn`: giữ nguyên
- `Mana`: giữ nguyên hoặc rất thấp
- giữ gần như toàn bộ debuff hiện có

## Core Flows

### 1. Flow cứu dậy cơ bản thành công

1. Một người chơi trong `co-op` bị đưa `Máu` về `0`.
2. Người đó chuyển sang `Downed` thay vì chết ngay.
3. Đồng đội tiếp cận và bắt đầu hành động cứu.
4. Người cứu trả giá bằng `máu` của chính mình.
5. Nếu action hoàn tất trước khi timer `Downed` về `0`, cứu thành công.
6. Người bị downed đứng dậy với khoảng `50% HP`.
7. Người này có vài giây miễn nhiễm hoặc giảm sát thương để không bị đè chết ngay.
8. Party phải quyết định ngay: giữ nhịp đánh tiếp, rút lui, hay xoay sang recovery.

### 2. Flow cứu hụt dẫn tới chết thật

1. Một người chơi vào `Downed`.
2. Party không cứu, hoặc cứu nhưng không kịp hoàn tất.
3. Timer `Downed` chạm `0`.
4. Người chơi chuyển sang `Dead`.
5. Hệ thống tạo `recovery marker` đúng nơi chết.
6. Item trên `hotbar` rơi xuống đất.
7. Item trong túi đi vào `bia mộ`.
8. Phần còn lại của party chọn tiếp tục run, rút lui, hay mở một `recovery run`.

### 3. Flow chết thật và quay lại vòng chơi

1. Người chơi chết thật và kết thúc nhánh combat hiện tại.
2. Hệ thống xác định nguồn hồi sinh hợp lệ:
   - `Base`
   - `điểm hồi sinh mở`
   - `công trình hồi sinh`
   - hoặc nhánh `đồng đội / kỹ năng` nếu có
3. Người chơi respawn với bộ trạng thái theo nguồn tương ứng.
4. Debuff được reset hoặc giữ lại theo đúng chất lượng của nguồn hồi sinh đó.
5. Người chơi quay lại game trong trạng thái yếu hơn, ngang hoặc tốt hơn tùy nguồn.
6. Nếu còn giá trị ở hiện trường, vòng chơi chuyển sang recovery: nhặt `hotbar`, mở `bia mộ`, gom lại tài nguyên còn cứu được.

## Failure And Recovery

### Fail cost của Downed

- làm cả đội mất nhịp
- ép đồng đội phải chọn giữa:
  - cứu người
  - giữ combat
  - rút lui
- người đi cứu phải trả `máu`

### Fail cost của chết thật

- mất nhịp chuyến đi
- hotbar rơi đất
- túi chính chuyển vào bia mộ
- có thể ép cả đội thành `recovery run`

### Recovery value của co-op

- co-op không xóa fail state
- nhưng thêm đường cứu:
  - cứu dậy tại chỗ
  - giữ người còn sống để quay lại recovery
  - chia người nhặt đồ, giữ quái, mở đường rút

### Recovery sau wipe hoặc chết lẻ

- người chơi hoặc party có thể quay lại:
  - nhặt đồ hotbar rơi đất
  - mở bia mộ
  - thu hồi giá trị còn lại
- đây là phần bắt buộc của vòng chơi, không phải ngoại lệ

## Edge Cases

### 1. Solo

- `Máu = 0` là chết thật ngay
- không có `Downed`
- không có cứu dậy bởi đồng đội

### 2. Co-op nhưng không ai cứu

- người chơi giữ trạng thái `Downed` cho tới khi timer về `0`
- hết giờ là chết thật ngay

### 3. Được cứu dậy và ngay lập tức bị đè lại

- có vài giây miễn nhiễm hoặc giảm sát thương để tránh chết lại ngay
- nhưng cửa sổ này chỉ là lớp bảo vệ ngắn, không phải giấy phép lao lại vô hạn

### 4. Heal over time và Downed

- `heal over time` vẫn chạy
- nhưng không tự biến `Downed` thành `Alive`
- người chơi vẫn phải qua hành động cứu hoặc nguồn hồi sinh hợp lệ

### 5. Ăn / buff / regen ngay trước lúc chết

- resolve order tổng thể vẫn bám `Survival System`
- nếu chạm `0` ở bất kỳ bước nào thì chết hoặc vào fail flow ngay
- không có rule "thoát chết miễn phí" chỉ vì animation ăn gần hoàn tất

### 6. Respawn không phải revive

- `respawn` là quay lại từ nguồn hồi sinh
- `revive` là được kéo dậy trong combat
- hai flow này không được trộn lẫn khi viết code hay test case

### 7. Bia mộ trong mode thường

- free-loot là rule đã chốt
- đây không phải bug hay ngoại lệ
- phải được xem như một phần của social risk trong co-op mode thường

## Signs Of A Good Revive System

- người chơi thấy rõ co-op đáng giá hơn solo vì cứu nhau được
- revive đủ mạnh để tạo hy vọng
- nhưng đủ đắt để quyết định cứu ai, cứu lúc nào vẫn có trọng lượng
- chết thật vẫn đau, nhưng luôn có đường recovery hợp lệ
- sự khác nhau giữa `revive` và `respawn` dễ hiểu, không nhập nhằng

## Signs Of A Broken Revive System

- revive quá rẻ, làm `Máu = 0` gần như vô nghĩa trong co-op
- revive quá khó, khiến `Downed` chỉ là delay vô ích trước khi chết
- người chơi không hiểu vì sao lúc thì giữ debuff, lúc thì sạch debuff
- respawn point quá mạnh làm mất giá trị của cứu nhau trong field
- free-loot và tombstone khiến recovery thành hỗn loạn không đọc được

## Implementation Hooks

- Player state tối thiểu cần field:
  - `is_downed`
  - `downed_timer`
  - `is_dead`
  - `is_reviving_target`
  - `recently_revived`
  - `revive_protection_timer`
  - `death_marker_id`
  - `respawn_source_type`
- Event tối thiểu cần có:
  - `enter_downed`
  - `start_revive`
  - `cancel_revive`
  - `complete_revive`
  - `downed_timer_expired`
  - `enter_dead`
  - `spawn_recovery_marker`
  - `drop_hotbar_items`
  - `create_tombstone`
  - `begin_respawn`
  - `complete_respawn`
- Cần sync rõ trong multiplayer:
  - ai đang `Downed`
  - còn bao nhiêu thời gian
  - ai đang cứu ai
  - revive đã hoàn tất hay bị hủy
  - bia mộ thuộc ai và ai có quyền mở theo mode
- QA hook tối thiểu:
  - cứu thành công trước `0`
  - cứu hụt đúng lúc timer chạm `0`
  - revive thành công rồi bị hit ngay
  - `heal over time` khi downed
  - solo chết ngay không qua downed
  - respawn theo `Base`
  - respawn theo `điểm hồi sinh mở`
  - mode thường vs `PvP mode` ở quyền mở bia mộ

## Open Design Questions

- Có cần khóa rõ hơn thời lượng và mức bảo vệ của vài giây an toàn sau revive hay chưa.
- Nhánh `kỹ năng / vật phẩm hồi sinh đặc biệt` có đi vào MVP hay để sang đợt thiết kế sau.
- Cần tách riêng `công trình hồi sinh` và `điểm hồi sinh mở` ở doc hệ thống world/save hay vẫn coi cùng một lớp cho MVP.

## Open Balance Variables

- thời gian `Downed`
- lượng `máu` người cứu phải trả
- lượng `HP` người được cứu hồi lại
- độ dài và cường độ bảo vệ ngắn sau revive
- trạng thái `Mana` mặc định khi hồi từ nhánh `đồng đội / kỹ năng`
- thời gian tồn tại của `bia mộ` ở từng mode
