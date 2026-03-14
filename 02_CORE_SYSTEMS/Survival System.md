Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 07/03/2026

# Survival System

Tài liệu này chốt hệ sinh tồn cốt lõi của game: `Máu`, `Thức ăn`, `Mana`, các ngưỡng đói, `kiệt đói`, hồi máu, nạp mana và `resolve order` khi nhiều hiệu ứng chạm nhau trong cùng một nhịp. Đây là một trong những trục chính của game vì nó làm cho việc chuẩn bị, mang gì theo, đi bao xa và quay về lúc nào trở nên có trọng lượng thật.

## Mục tiêu

- Chốt đủ `đói`, `kiệt đói`, `heal`, `mana refill`, `resolve order`.
- Loại bỏ mọi placeholder cũ không còn dùng như `stamina`, `mana saturation`, `overcharge` hay các thanh survival phụ chưa được chốt.
- Xác định rõ hệ sinh tồn đang phạt và thưởng người chơi như thế nào.
- Tạo nguồn đúng cho `Combat System`, `Player Revive`, `Inventory System`, `Items` và implementation của player state.

## Phạm vi

Tài liệu này tập trung vào:
- ba resource lõi: `Máu`, `Thức ăn`, `Mana`
- state của người chơi liên quan trực tiếp tới survival
- ngưỡng thức ăn và hậu quả của từng ngưỡng
- hồi máu tự nhiên, hồi máu bằng item, heal over time
- quy tắc nạp mana cá nhân
- thứ tự resolve khi nhiều hiệu ứng sinh tồn chạy cùng lúc

Tài liệu này không đi sâu vào:
- flow revive / respawn chi tiết
- tombstone, hotbar drop và recovery logistics
- công thức damage / armor / status combat
- công thức cụ thể cho từng item đồ ăn hay từng bình mana

## Source Coverage

### Nguồn bắt buộc

- [10_QUESTIONS_LEVEL_6.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/10_QUESTIONS_LEVEL_6.md)
  - chốt vai trò của survival như trục chính tạo nhịp chuẩn bị và giới hạn chuyến đi
- [12_QUESTIONS_LEVEL_8.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/12_QUESTIONS_LEVEL_8.md)
  - khóa state model, fail state, mana use, ngưỡng thức ăn, và cấu trúc resolve / edge case
- [13_PLAYER_CORE_STATE_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/13_PLAYER_CORE_STATE_SHEET.md)
  - là nguồn đúng trực tiếp cho rule cuối về đói, kiệt đói, hồi máu, ăn uống, mana refill, downed / death handoff, và resolve order

### Nguồn hỗ trợ

- [08_QUESTIONS_LEVEL_4.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/08_QUESTIONS_LEVEL_4.md)
  - dùng để giữ đúng vai trò hệ sinh tồn trong core loop: tạo áp lực, tạo nhịp chuẩn bị, và phạt thất bại mà không thành việc lặt vặt vô nghĩa
- [Player Stats.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/03_PLAYER_SYSTEMS/Player%20Stats.md)
  - dùng để không mâu thuẫn với phần `max HP`, `max Mana`, `độ tụt thức ăn` và current/max rule

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - Hệ sinh tồn hiện đã đủ rõ để dùng làm nguồn đúng cho combat, item, revive và QA test case.
  - Các con số như tốc độ tụt đói, tốc độ hồi máu, thời gian chờ natural regen và dung lượng cụ thể của từng loại refill vẫn thuộc lớp balance.

## Conflict Resolution

- `Level 6` xác nhận `Survival System` là trục chính, không phải lớp phụ.
- `Level 8` từng có một số wording mở rộng về state model, nhưng bản chốt cuối ở `Sheet 13` đã thu gọn lõi thành:
  - `Máu`
  - `Thức ăn`
  - `Mana`
  - `Downed / Dead` như fail flow
- Placeholder cũ như:
  - `Stamina`
  - `Water`
  - `Sanity`
  - `Disease`
  - `Mana Saturation`
  - `Mana Overcharge`
  hiện **không thuộc** lõi survival của bản này.
- Khi có khác biệt giữa wording cũ và rule cuối, tài liệu này ưu tiên `13_PLAYER_CORE_STATE_SHEET.md`.

## Rule Summary

- Hệ sinh tồn hiện tại xoay quanh `Máu`, `Thức ăn`, `Mana`.
- `Máu` là fail bar trực tiếp.
- `Thức ăn` là thanh duy trì nền:
  - chi phối natural regen
  - ảnh hưởng hiệu suất chiến đấu
  - và ở mức tệ nhất có thể giết người chơi ngoài combat
- `Mana` là tài nguyên vận hành:
  - không tự hồi
  - dùng cho tool, utility, artifact và một phần skill
  - hết mana thì các hành động cần mana không dùng được, hiệu ứng duy trì bằng mana sẽ tắt
- Hệ này phải khiến người chơi:
  - chuẩn bị đúng
  - biết lúc nào nên rút
  - và cảm nhận rõ cái giá của việc đi sâu / đi lâu / đi thiếu đồ

## Core Resources

### Máu

- Là thước đo sinh tồn trực tiếp.
- Khi `Máu = 0`:
  - `solo`: chết ngay
  - `co-op`: vào `downed` trước rồi mới chết nếu không được cứu
- Máu có thể hồi qua:
  - hồi máu tự nhiên
  - item hồi máu trực tiếp
  - heal over time
  - respawn / revive flow

### Thức ăn

- Là thanh duy trì sinh tồn nền.
- Tụt đều theo thời gian.
- Không phải chỉ để “không chết đói”, mà còn quyết định:
  - có natural regen hay không
  - có bị phạt damage hay không
  - có rơi vào `kiệt đói` hay không

### Mana

- Là tài nguyên vận hành cá nhân.
- Không tự hồi.
- Không dùng như một thanh phép tự nạp vô hạn.
- Vai trò chính:
  - chạy tool / utility / artifact / item / một phần skill
  - hỗ trợ người chơi ở các lớp chuẩn bị, survival và xử lý tình huống

## State List

- `Normal`
  - trạng thái bình thường
- `No`
  - đủ no để có thể natural regen nếu thỏa điều kiện an toàn
- `Hungry`
  - thức ăn trong ngưỡng đói
- `Starving`
  - thức ăn về 0
- `Mana Depleted`
  - mana về 0
- `Downed`
  - chỉ có ở co-op, là fail flow trung gian
- `Dead`
  - trạng thái thất bại trực tiếp của chuyến đi

## Hunger State Rules

### Ngưỡng thức ăn

- `0 = Kiệt đói`
  - mất máu theo thời gian
  - có thể chết ngay cả khi đang ngoài combat
  - tốc độ mất máu đi theo nhịp đều
- `1 - 30 = Đói`
  - giảm sát thương
  - không hồi máu tự nhiên
- `30 - 70 = Vừa`
  - trạng thái trung tính
- `70 - 100 = No`
  - có thể hồi máu tự nhiên nếu đủ an toàn

### Ý đồ thiết kế

- Người chơi đói vẫn chơi được, nhưng chơi kém đi.
- `Kiệt đói` không phải debuff nhẹ; nó là tín hiệu xử lý khẩn cấp.
- Survival system thưởng cho người chuẩn bị tốt bằng việc:
  - giữ được chất lượng chuyến đi lâu hơn
  - hồi máu tự nhiên được
  - ít bị ép quay về sớm hơn

## Food Consumption And Eating Rules

### Tụt đói

- Thức ăn tụt đều theo thời gian.
- Điểm chỉ số vào `Độ tụt thức ăn` chỉ làm tốc độ tụt chậm hơn.
- Chỉ số này chỉ ảnh hưởng các nhịp sau, không sửa ngay thanh hiện tại.

### Ăn

- Khi ăn:
  - có animation ngắn
  - cộng no ngay
  - rồi áp dụng lại rule mới theo ngưỡng hiện tại
- Không dùng cooldown toàn cục chung cho mọi món.
- Cooldown chi tiết nếu có thuộc về từng item sau này.

### Đồ ăn

- Mỗi loại đồ ăn có giá trị riêng.
- Có thể:
  - cộng tức thì
  - hoặc thêm hiệu ứng hồi dần / buff
- Các nhóm đồ ăn chính:
  - `đồ ăn rẻ`
  - `đồ ăn tốt`
  - `đồ ăn buff`
- `Đồ ăn buff` thiên về:
  - sinh tồn là chính
  - combat ít hơn
  - utility / môi trường ở nhánh đặc thù

### Khi ăn gần đầy

- Phần no dư bị mất.
- Buff phụ của món ăn vẫn kích hoạt nếu item có cho hiệu ứng đó.

## Healing Rules

### Hồi máu tự nhiên

- Chỉ bắt đầu khi:
  - người chơi ở ngưỡng `No`
  - và không bị đánh trong vài giây
- Bất kỳ hit nào cũng reset timer hồi máu tự nhiên.
- Nếu người chơi đủ no và đủ an toàn, natural regen có thể hồi đầy.

### Item hồi máu trực tiếp

- Có tồn tại.
- Hiếm và đắt.
- Vai trò chính là `cứu nguy khẩn cấp`, nhưng vẫn có thể dùng như nguồn hồi giữa chuyến đi khi cần.
- Dùng được cả khi đang `Đói / Kiệt đói`.

### Heal over time

- Vẫn tiếp tục chạy dù người chơi đang đói.
- Nếu đồng thời có `Kiệt đói`, hai hiệu ứng triệt tiêu nhau theo số thực.
- Vẫn tiếp tục chạy khi người chơi ở trạng thái `downed`.
- Có thể bị xóa khi respawn nếu rule của điểm hồi sinh xóa hiệu ứng ngắn hạn.

### Nhiều nguồn hồi / mất máu

- Nhiều nguồn hồi máu cộng dồn bình thường ở giai đoạn hiện tại.
- Nhiều nguồn mất máu cũng cộng dồn bình thường.
- Nếu chạm `0` ở bất kỳ bước nào của nhịp resolve, người chơi chết hoặc vào fail flow ngay.

## Mana Rules

### Mana Depleted

Khi `Mana = 0`:
- không dùng được hành động cần mana
- các thiết bị hoặc hiệu ứng duy trì bằng mana sẽ tắt nếu không có nguồn thay thế

### Nguồn nạp mana cá nhân

- `Nguồn chính`
  - nạp ở base
  - bằng cách mang quặng mana về chiết xuất thành mana tích trữ
- `Nguồn cứu nguy`
  - bình chứa dự trữ / pin / lõi / vật phẩm cùng họ
- `Nguồn cơ hội`
  - quặng tinh khiết
  - mana rơi từ sinh vật

### Quy tắc hiệu quả

- Base là nơi nạp hiệu quả nhất.
- Bình chứa là giải pháp cơ động khi đi xa.
- Quặng tinh khiết có thể dùng tại chỗ nhưng hiệu quả kém hơn mang về base.
- Mana từ sinh vật là nguồn phụ, không thay thế khai khoáng.

### Mana refill item

- Nhóm refill tức thì là nhánh chính.
- Có animation ngắn như ăn.
- Các phiên bản hồi dần có thể xuất hiện về sau nhưng không phải chuẩn MVP.

### Rule tương thích với vật chứa charge

- `Pin / lõi mana` có thể tồn tại như vật chứa charge riêng.
- Trong trường hợp đó:
  - dùng tới đâu trừ charge tới đó
  - không nhất thiết bỏ phí phần dư như consumable một lần
- Chi tiết inventory, hotbar và charge container thuộc phạm vi `Inventory System`, nhưng `Survival System` công nhận đây là một nguồn nạp mana hợp lệ của player.

## Failure And Recovery Interface

### Fail mềm

- `Đói`
- `Kiệt đói`
- `Cạn mana`

Đây là các fail mềm hoặc áp lực vận hành.

### Fail nặng

- `Máu = 0`
- chuyển sang:
  - `Downed` trong co-op
  - `Dead` trong solo

### Handoff sang revive / respawn

- Survival system chỉ khóa điểm giao:
  - lúc nào vào downed / dead
  - trạng thái resource nào được giữ / reset theo source hồi sinh
- Chi tiết revive / tombstone / respawn nằm ở doc khác.

## Resolve Order

### Resolve order chuẩn khi người chơi vừa ăn vừa ở trạng thái nguy hiểm

1. cập nhật hành động `ăn`
2. tính lại ngưỡng `Thức ăn`
3. rồi mới xử lý `mất máu / hồi máu`

### Hit và regen

- Nếu người chơi vừa ăn xong vừa bị hit:
  - hit reset natural regen ngay
- Natural regen và heal over time là hai lớp khác nhau:
  - natural regen bị khóa bởi ngưỡng no và hit
  - heal over time thì không

### Kiểm tra chết

- Nếu trong cùng một nhịp có cả drain và heal:
  - hệ thống resolve theo thứ tự trên
  - nhưng nếu chạm `0` ở bất kỳ bước nào thì chết ngay

## Placeholder Removed

Các hệ / thanh sau hiện **không thuộc Survival System** của bản này:
- `Stamina`
- `Water`
- `Sanity`
- `Disease`
- `Mana Saturation`
- `Mana Overcharge`

Nếu tương lai muốn thêm, phải mở như nhánh thiết kế mới thay vì ngầm nhét vào hệ hiện tại.

## Signs Of A Good Survival System

- Người chơi cảm được rõ cái giá của một chuyến đi dài hơn.
- Chuẩn bị tốt giúp chuyến đi bền hơn thật.
- Đói tạo áp lực rõ nhưng không biến game thành việc vặt vô nghĩa.
- Mana hết làm utility tắt đúng lúc và tạo quyết định khó thật.
- Natural regen, heal item, heal over time có vai trò khác nhau, không đè lên nhau hoàn toàn.

## Signs Of A Broken Survival System

- Đói chỉ là việc lặt vặt phải bấm ăn đều đều mà không đổi quyết định nào.
- Kiệt đói không đáng sợ hoặc ngược lại phũ tới mức không có đường cứu.
- Mana cạn nhưng người chơi không cảm thấy mất gì quan trọng.
- Heal systems chồng nhau tới mức một nhánh làm các nhánh khác vô nghĩa.
- Survival quá nhẹ làm câu hỏi `tham hay rút` mất lực.

## Implementation Hooks

- Player state tối thiểu cần field:
  - `current_hp`
  - `max_hp`
  - `current_food`
  - `max_food`
  - `current_mana`
  - `max_mana`
  - `food_drain_modifier`
  - `last_damage_time`
  - `natural_regen_enabled`
- Cần state / tag:
  - `normal`
  - `hungry`
  - `starving`
  - `mana_depleted`
  - `downed`
  - `dead`
- Cần event tối thiểu:
  - `eat_item`
  - `apply_direct_heal`
  - `apply_heal_over_time`
  - `consume_mana`
  - `refill_mana`
  - `tick_food_drain`
  - `tick_starving_damage`
  - `evaluate_survival_state`
- Cần test hook cho:
  - ăn đúng lúc chuyển ngưỡng
  - hit đúng lúc đang regen
  - starving và HoT cùng lúc
  - mana về 0 khi utility đang bật
  - nhiều nguồn heal / damage cùng tick

## Open Design Questions

- Tốc độ natural regen nên bắt đầu sau bao nhiêu giây không bị đánh.
- Bao nhiêu % sát thương bị giảm khi ở ngưỡng `Đói`.
- Loại heal over time nào nên phổ biến tới đâu trong early / mid game.
- Có nên thêm một số food / utility rất đặc thù tác động vào `Kiệt đói` hay không.

## Open Balance Variables

- Tốc độ tụt thức ăn cơ bản
- Tốc độ mất máu khi `Kiệt đói`
- Tốc độ natural regen
- Giá trị hồi của item heal trực tiếp
- Giá trị và độ hiếm của mana refill item
- Tỷ lệ xuất hiện các nguồn nạp mana cứu nguy ngoài hiện trường
