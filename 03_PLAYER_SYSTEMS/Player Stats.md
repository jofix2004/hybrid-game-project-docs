Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 05/03/2026

# Player Stats

Tài liệu này chốt bộ chỉ số nền của người chơi, cách chúng tăng lên, cách người chơi đầu tư `điểm chỉ số`, quyền `all-in`, luật `respec`, và cách các giá trị `current / max` cập nhật khi build thay đổi. Đây là doc định nghĩa “player mạnh lên theo nền cá nhân như thế nào”, nhưng không biến game thành một RPG cây level lớn hay class tree cứng.

## Mục tiêu

- Chốt `stat list` chuẩn của người chơi ở lớp nền cá nhân.
- Chốt đúng 3 trục đầu tư bằng `điểm chỉ số`.
- Mô tả quyền `all-in`, không cảnh báo UI, không soft cap/hard cap ở bản hiện tại.
- Chốt flow `respec`: ở đâu, bằng gì, hoàn lại kiểu nào.
- Chốt các rule `current / max` khi tăng điểm, giảm điểm hoặc đổi build.

## Phạm vi

Tài liệu này tập trung vào:
- bộ chỉ số nền gắn với người chơi
- chỉ số nào là trục đầu tư thật, chỉ số nào không phải trục đầu tư chính
- nguồn nhận `điểm chỉ số` ở mức khái quát
- cách áp dụng điểm, cách respec, và cách cập nhật giá trị hiện tại

Tài liệu này không đi sâu vào:
- nhịp mở tầng, boss milestone hay macro progression chi tiết
- công thức damage, armor, crit, stagger hay combat scaling
- effect tạm thời từ food, artifact, gear, utility
- cây skill giả định hay class system

## Source Coverage

### Nguồn bắt buộc

- [07_QUESTIONS_LEVEL_3.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/07_QUESTIONS_LEVEL_3.md)
  - dùng làm guardrail để giữ progression phục vụ core loop, không che mất quyết định `đi tiếp hay quay về`
- [10_QUESTIONS_LEVEL_6.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/10_QUESTIONS_LEVEL_6.md)
  - khóa hướng progression tổng: người chơi mạnh lên chủ yếu qua đồ, utility, căn cứ, mana, chiều sâu và tuyến ổn định; không nên biến game thành cây level nhân vật phình to
- [11_QUESTIONS_LEVEL_7.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/11_QUESTIONS_LEVEL_7.md)
  - dùng như guardrail triển khai: không tự mở rộng hệ chỉ số thành một RPG tree lớn thiếu cơ sở production
- [12_QUESTIONS_LEVEL_8.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/12_QUESTIONS_LEVEL_8.md)
  - là nguồn rule gameplay cụ thể về player core state, fail state, stat point, current/max, all-in, respec
- [13_PLAYER_CORE_STATE_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/13_PLAYER_CORE_STATE_SHEET.md)
  - là nguồn đúng trực tiếp cho stat list, điểm chỉ số, all-in, respec và current/max rule

### Nguồn đối chiếu bắt buộc

- [Core Concept.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/00_GAME_VISION/Core%20Concept.md)
  - dùng để giữ đúng fantasy survival co-op theo chiều sâu, tránh trôi sang RPG character-build nặng
- [Long Progression Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Long%20Progression%20Loop.md)
  - dùng để đảm bảo stat point chỉ là một nhánh tăng trưởng, không nuốt mất vai trò của tool, utility, mana, gate và logistics

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - Bộ chỉ số nền và luật đầu tư đã đủ rõ để làm nguồn đúng cho `Player Progression`, `Survival System`, `Equipment System`, `Player Revive` và data schema của player.
  - Các con số tăng mỗi điểm, ngưỡng giá của từng lần cộng và cost cụ thể của item respec vẫn thuộc lớp balance về sau.

## Conflict Resolution

- `Level 6` nghiêng về hướng progression không nên biến thành `cây level nhân vật phình to`.
- `Level 8` và `Sheet 13` khóa bản final: vẫn có lớp tăng trưởng nền cá nhân, nhưng rất hẹp, chỉ qua `điểm chỉ số`, không phải level tree lớn, không thành class system.
- Trước đó từng có hướng `hard cap / soft cap`, nhưng quyết định cuối đã bỏ hướng này:
  - người chơi được `all-in` tự do
  - không có cảnh báo UI
  - chấp nhận khả năng trap người chơi mới
- Khi cần ưu tiên wording, tài liệu này dùng:
  1. `13_PLAYER_CORE_STATE_SHEET.md` cho rule cuối
  2. `12_QUESTIONS_LEVEL_8.md` để đối chiếu edge case
  3. `10_QUESTIONS_LEVEL_6.md` và `11_QUESTIONS_LEVEL_7.md` để giữ đúng phạm vi, không phình hệ

## Rule Summary

- Người chơi có lớp tăng trưởng nền cá nhân, nhưng nó không phải trục mạnh nhất của toàn game.
- Trục mạnh lên chính của game vẫn là:
  - vũ khí và công cụ
  - utility
  - căn cứ và workstation
  - mana và machine
  - gate và logistics chiều sâu
- Lớp `Player Stats` chỉ giữ vai trò:
  - cho người chơi cảm giác build có cá tính
  - tạo ra quyền ưu tiên đầu tư
  - hỗ trợ survival loop và utility loop
- Người chơi nhận `điểm chỉ số` chủ yếu từ:
  - `mở tầng`
  - `boss / milestone` là nguồn phụ
- Điểm chỉ số hiện chỉ đầu tư vào `3 trục`:
  - `Máu tối đa`
  - `Mana tối đa`
  - `Độ tụt thức ăn`
- Người chơi được phép `all-in` hoàn toàn.
- Không có hard cap, soft cap hay cảnh báo UI ở bản hiện tại.
- Có `respec`, nhưng:
  - đắt
  - chỉ ở `base / shrine mốc lớn`
  - cần item chuyên dụng dùng một lần
  - hoàn lại toàn bộ điểm

## Stat List

### Nhóm chỉ số nền bắt buộc

### 1. Máu hiện tại

- Là lượng máu người chơi đang có ở thời điểm hiện tại.
- Chạm `0` sẽ dẫn tới:
  - `downed` trong co-op
  - `dead` ngay trong solo

### 2. Máu tối đa

- Là trần máu nền của người chơi.
- Là một trong ba chỉ số được đầu tư bằng `điểm chỉ số`.
- Là trục đầu tư nền rõ nhất cho độ bền sống sót.

### 3. Mana hiện tại

- Là lượng mana cá nhân còn lại.
- Dùng cho tool, utility, artifact hoặc thiết bị cá nhân theo rule của từng hệ.
- Không tự hồi theo thời gian.

### 4. Mana tối đa

- Là trần mana cá nhân của người chơi.
- Là một trong ba chỉ số được đầu tư bằng `điểm chỉ số`.
- Không phải nguồn năng lượng khổng lồ như network mana ở base; nó giống “sạc dự phòng” cá nhân.

### 5. Thức ăn hiện tại

- Là thanh no hiện tại của người chơi.
- Tụt đều theo thời gian.
- Quyết định:
  - khả năng hồi máu tự nhiên
  - ngưỡng đói / kiệt đói
  - áp lực sống sót nền

### 6. Thức ăn tối đa

- Là trần của thanh thức ăn.
- Hiện tồn tại như stat vận hành, nhưng không phải trục đầu tư chính bằng điểm chỉ số ở bản hiện tại.
- Nếu về sau có tăng trưởng ở chỉ số này, phải được chốt ở doc khác; doc này chưa mở nó thành trục build riêng.

### 7. Độ tụt thức ăn

- Là tốc độ thanh thức ăn tụt theo thời gian.
- Đây là chỉ số đầu tư thứ ba.
- Đầu tư theo hướng làm đói `tụt chậm hơn`, không phải làm món ăn “ăn lời hơn”.

### Nhóm chỉ số không phải trục đầu tư chính

### Tốc độ di chuyển

- Không phải trục tăng trưởng lớn.
- Nếu có tăng theo tiến trình thì chỉ tăng rất ít.
- Không nằm trong bảng `điểm chỉ số` hiện tại.

### Sát thương cơ bản

- Có thể tăng rất ít theo tiến trình nền.
- Nhưng không phải nguồn sức mạnh chính.
- Sức mạnh chính vẫn đến từ:
  - vũ khí
  - trang bị
  - đồ ăn / buff

## Nguồn Nhận Điểm Chỉ Số

- Nguồn chính: `mở tầng`
- Nguồn phụ: `boss / milestone`
- Điểm chưa dùng:
  - giữ luôn trên nhân vật
  - không cần về base mới “nhận”

## Quy Tắc Đầu Tư Điểm

### Phân bổ

- Người chơi chỉ được cộng điểm ở:
  - `base`
  - `shrine`
  - `shrine mốc lớn`
- Không mở thao tác cộng điểm ở mọi nơi.

### Giá điểm

- Giai đoạn hiện tại để `giá như nhau` giữa các chỉ số.
- Nếu về sau cần tách giá, sẽ xử lý ở lớp balance.

### Áp dụng

- Điểm áp dụng `ngay khi cộng`.
- Không chờ rời base mới có hiệu lực.

### All-in

- Người chơi được phép dồn toàn bộ điểm vào một chỉ số nếu muốn.
- Không có cảnh báo UI.
- Game chấp nhận khả năng trap người chơi mới như một phần của quyền tự do build.

## Current / Max Rules

### Khi cộng vào Máu tối đa

- Tăng `máu tối đa`.
- Đồng thời tăng cả `máu hiện tại` tương ứng.
- Cập nhật theo `%` để giữ tỷ lệ hiện tại.

Ví dụ:
- nếu người chơi đang ở `50% HP`
- sau khi tăng `máu tối đa`
- thì `máu hiện tại` vẫn giữ quanh `50%` của trần mới

### Khi cộng vào Mana tối đa

- Chỉ tăng `trần mana`.
- `Mana hiện tại` giữ nguyên.
- Không bơm thêm mana miễn phí chỉ vì vừa cộng điểm.

### Khi cộng vào Độ tụt thức ăn

- Giảm theo `%`.
- Chỉ ảnh hưởng các nhịp tụt đói về sau.
- Không sửa ngay giá trị hiện tại của thanh thức ăn.

### Khi giảm Máu tối đa qua Respec

- `Máu hiện tại` co theo `%` tương ứng với trần mới.

### Khi giảm Mana tối đa qua Respec

- `Mana hiện tại` bị `clamp` về trần mới.

## Respec

### Mục đích

- Cho phép người chơi sửa build khi đã đầu tư lệch hoặc muốn đổi hướng.
- Không nhằm khuyến khích đổi build liên tục giữa các chuyến đi nhỏ.

### Điều kiện sử dụng

- Chỉ dùng được ở:
  - `base`
  - `shrine mốc lớn`
- Không cần cấm riêng trong combat, vì bản thân nơi dùng đã là vùng không hợp lệ cho combat thật.

### Chi phí

- Cần `item chuyên dụng`
  - ví dụ cùng họ với “thuốc trí nhớ”
- Item này dùng `một lần rồi mất`
- Chi phí respec phải `đắt`

### Kết quả

- Hoàn lại `toàn bộ điểm chỉ số`
- Tính lại chỉ số ngay theo build mới

## Interaction With Death And Recovery

- `Điểm chỉ số` không mất khi chết, kể cả ở mode nặng.
- Death penalty không được xóa lớp tăng trưởng nền cá nhân.
- Respawn xử lý chỉ số theo doc `Player Revive`, nhưng không đụng vào số điểm đã đầu tư.

## Interaction With Equipment, Artifact, And Buff

- Trang bị, giáp và artifact không phải nguồn tăng nền chính của `Player Stats`.
- Tuy vậy, chúng vẫn là `loadout cơ học nặng` và có thể ảnh hưởng mạnh tới cách người chơi vận hành build.
- Quy tắc của doc này là:
  - `Player Stats` định nghĩa nền cá nhân lâu dài
  - `Equipment / Artifact / Food Buff` định nghĩa lớp điều chỉnh tình huống và phong cách chiến đấu

## Signs Of A Good Player Stat System

- Người chơi hiểu rất nhanh mình đang đầu tư vào cái gì.
- Mỗi điểm cộng tạo khác biệt có cảm nhận được ngay trong run.
- Stat point hỗ trợ survival và utility, không nuốt mất vai trò của tool, item, machine và gate.
- Người chơi có thể build lệch thật sự, nhưng game vẫn giữ giá trị của phần chuẩn bị và logistics.

## Signs Of A Broken Player Stat System

- Chỉ số nền mạnh tới mức vũ khí, utility và căn cứ trở nên thứ yếu.
- Người chơi chỉ cần cộng điểm mà không cần chuẩn bị, sửa đồ hay quản lý tài nguyên nữa.
- Build tối ưu bị khóa cứng thành một đường duy nhất.
- Respec rẻ tới mức quyết định đầu tư mất trọng lượng.
- Hệ chỉ số phình thành class tree hoặc skill tree lớn mà không có đủ source design hỗ trợ.

## Implementation Hooks

- Player entity cần field tối thiểu:
  - `current_hp`
  - `max_hp`
  - `current_mana`
  - `max_mana`
  - `current_food`
  - `max_food`
  - `food_drain_modifier`
  - `unspent_stat_points`
  - `spent_stat_hp`
  - `spent_stat_mana`
  - `spent_stat_food_drain`
- Hệ thống phải hỗ trợ event:
  - `grant_stat_point`
  - `apply_stat_point`
  - `respec_full_stats`
  - `recalculate_player_max_values`
- Cần có rule recalculation riêng cho:
  - tăng `max_hp`
  - tăng `max_mana`
  - giảm `max_hp`
  - giảm `max_mana`
  - thay đổi `food_drain_modifier`
- Save data phải giữ:
  - tổng điểm đã nhận
  - tổng điểm chưa dùng
  - phân bổ hiện tại

## Open Design Questions

- Mỗi điểm cộng tăng bao nhiêu `máu tối đa`.
- Mỗi điểm cộng tăng bao nhiêu `mana tối đa`.
- Mỗi điểm cộng giảm bao nhiêu `% độ tụt thức ăn`.
- Có nên cho một số milestone đặc biệt tăng `thức ăn tối đa` như phần thưởng world/system riêng hay không.

## Open Balance Variables

- Tỷ trọng thực tế giữa sức mạnh từ `điểm chỉ số` và sức mạnh từ `gear / utility / mana infrastructure`
- Mức chênh tối đa chấp nhận được giữa build all-in HP và build all-in Mana
- Giá item respec hợp lý ở từng chặng
- Số điểm trung bình người chơi sẽ có ở mỗi macro-stage
