Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 12/03/2026

# Dungeon Progression

Tài liệu này chốt `tiến trình chinh phục hầm ngục` như một lớp progression riêng của game. Nếu [Floor Hierarchy.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/05_DUNGEON_SYSTEM/Floor%20Hierarchy.md) trả lời câu hỏi `chiều sâu được tổ chức ra sao`, còn [Player Progression.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/03_PLAYER_SYSTEMS/Player%20Progression.md) trả lời câu hỏi `người chơi mạnh lên bằng những lớp nào`, thì `Dungeon Progression` trả lời phần ở giữa: `một vùng sâu trong hầm ngục đi từ chỗ chưa biết, tới chỗ chạm được, tới chỗ sống được, tới chỗ khai thác ổn định được bằng cách nào`.

Doc này không coi hầm ngục là chuỗi checkpoint tuyến tính. Trong mô hình hiện tại, phần dưới đất gồm `nhiều tầng hang tự nhiên`, mỗi tầng có `một biome đặc thù`, còn `hầm ngục` là các pocket nội dung đậm nằm trong từng tầng. Vì vậy doc này coi dungeon progression là một mạng chiều sâu và route, nơi tiến trình thật đến từ:
- chạm tới lớp sâu mới
- mang được thành quả về
- giảm chi phí quay lại
- xử lý boss và gate milestone
- biến vùng sâu thành nguồn tiến trình lặp lại bền

## Mục tiêu

- Thay stub cũ bằng một doc production dùng được cho design, code, content và QA.
- Chốt `dungeon progression` như một chuỗi chuyển trạng thái rõ ràng, thay vì một dãy “floor mở khóa” mơ hồ.
- Tách rõ:
  - `đi xuống được`
  - `sống sót được`
  - `mang được tài nguyên về`
  - `ổn định được route`
  - `khai thác lặp lại được`
- Khóa vai trò của:
  - `chiều sâu tầng`
  - `mana`
  - `gate`
  - `boss gatekeeper`
  - `logistics`
  - `base support`
- Giữ đúng tinh thần game:
  - không biến dungeon progression thành chuỗi checkpoint cứng
  - không biến boss thành khóa tuyệt đối cho mọi tiến trình
  - không để thất bại của một run xóa các milestone ổn định đã dựng được trước đó

## Phạm vi

Tài liệu này tập trung vào:
- nghĩa của `tiến trình trong hầm ngục`
- state model của một route, một tầng hang, hoặc một mốc chiều sâu
- transition từ `Unknown` tới `Established Exploitation Layer`
- quan hệ giữa dungeon progression với:
  - floor hierarchy
  - boss system
  - stable gate
  - mana logistics
  - player progression
  - recovery sau thất bại
- các flow cốt lõi:
  - first reach
  - first mana contact
  - first gatekeeper milestone
  - ổn định route sâu
  - khai thác lặp lại

Tài liệu này không đi sâu vào:
- layout cụ thể của từng map
- thuật toán procedural generation
- room template chi tiết
- số liệu HP / damage / drop table
- data content cụ thể cho từng gate, boss hoặc floor

## Source Coverage

### Nguồn bắt buộc

- [10_QUESTIONS_LEVEL_6.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/10_QUESTIONS_LEVEL_6.md)
  - là nguồn macro cho:
    - các trục progression thật
    - bốn chặng phát triển
    - vai trò của mana từ tầng 3+
    - giá trị của tuyến đi ổn định
    - economy sink cho chuyến đi, base, thiết bị mana và cổng
- [11_QUESTIONS_LEVEL_7.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/11_QUESTIONS_LEVEL_7.md)
  - dùng để khóa ranh giới kỹ thuật và world persistence:
    - authority cho gate milestone, boss state và progression state
    - save world cho cổng ổn định, boss milestone, chunk state và công trình
    - data-driven pipeline cho gate, boss và world milestone
- [12_QUESTIONS_LEVEL_8.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/12_QUESTIONS_LEVEL_8.md)
  - là nguồn rule gameplay cụ thể cho:
    - gate repair theo module
    - boss phá gate
    - gate dùng mana / network mana / mana party
    - lỗi gate, giá dùng gate, route ổn định
    - down/fail/recovery gắn với mốc dungeon
- [15_GATE_AND_BOSS_MILESTONE_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/15_GATE_AND_BOSS_MILESTONE_SHEET.md)
  - là nguồn đúng cho:
    - boss gatekeeper
    - gate ổn định
    - logic gọi lại boss
    - refarm reward
    - mana drain từ cả party gần cổng

### Nguồn đối chiếu bắt buộc

- [Long Progression Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Long%20Progression%20Loop.md)
- [Floor Hierarchy.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/05_DUNGEON_SYSTEM/Floor%20Hierarchy.md)
- [Boss System.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/05_DUNGEON_SYSTEM/Boss%20System.md)
- [Player Progression.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/03_PLAYER_SYSTEMS/Player%20Progression.md)
- [Crafting Economy.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/06_ECONOMY_SYSTEM/Crafting%20Economy.md)

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - doc này đủ rõ để làm nguồn đúng cho:
    - `World Generation.md`
    - `Dungeon Generation.md`
    - `Gate System` về sau
    - `Unlock Conditions.md`
    - `Tech Tree.md`
  - các con số như:
    - bao nhiêu mốc gate trên mỗi band
    - thời gian hồi boss
    - chi phí cụ thể của từng route
    - số lần thất bại dự kiến trước khi ổn định một mốc
    vẫn là lớp balance sau

## Conflict Resolution

- Stub cũ từng hiểu dungeon progression theo kiểu:
  - mở cụm tầng
  - tới checkpoint
  - giết boss gate
  - đi tiếp

  Hướng đó không còn đúng với game hiện tại.

- Quyết định cuối:
  - game không dùng `checkpoint` như lớp lõi của dungeon progression
  - game dùng:
    - `điểm hồi sinh`
    - `gate ổn định`
    - `route stability`
    - `world-persistent milestone`
  - boss gatekeeper không phải ổ khóa tuyệt đối cho việc chạm chiều sâu
  - boss gatekeeper chủ yếu là ổ khóa cho `route ổn định` và `khai thác lâu dài`
  - người chơi vẫn có thể:
    - lách xuống sâu hơn
    - sửa gate từng phần khi boss còn sống
    - chấp nhận route đắt hơn, đau hơn, thiếu ổn định hơn

## Rule Summary

- `Dungeon progression` là quá trình biến `chiều sâu` thành `route đáng tin`, chứ không chỉ biến `map mới` thành `map cũ`.
- Phần dưới đất hiện được đọc theo cấu trúc:
  - `mặt đất` của đảo là lớp sống và chuẩn bị
  - `nhiều tầng hang tự nhiên` là lớp thám hiểm chính
  - `hầm ngục / POI đặc biệt` là nội dung đậm cắm trong từng tầng
- Một vùng sâu chỉ được xem là tiến trình bền khi đi qua đủ các nấc:
  1. `Reached`
  2. `Unstable Access`
  3. `Milestone-Blocked` nếu có mốc gatekeeper / gate
  4. `Stable Route Unlocked`
  5. `Established Exploitation Layer`
- Từ `tầng 3+`, mana trở thành yếu tố thật của dungeon progression:
  - tăng giá vé xuống sâu
  - mở utility, machine, gate logic và fuel pressure
- `Boss gatekeeper` là milestone logistics:
  - boss không chỉ cản combat
  - boss tạo áp lực thật lên hành vi sửa gate
- `Gate ổn định` là một trong những phần thưởng mạnh nhất của dungeon progression:
  - không xóa rủi ro hoàn toàn
  - nhưng làm các chuyến sau rẻ hơn, nhanh hơn, ít đau hơn
- Thất bại của một run sâu:
  - được phép làm trễ tiến trình
  - được phép làm mất loot chuyến đi
  - không được xóa các stable milestone đã chốt

## Dungeon Progression Role In The Game

## 1. Biến “đi được” thành “dùng được”

Trong game này, chạm tới một tầng sâu hơn chưa đủ để gọi là đã tiến. Tiến thật chỉ xảy ra khi:
- người chơi quay lại được
- sống sót được nhiều lần
- và dùng vùng đó như một phần của network tiến trình chung

## 2. Tổ chức nhịp tham và nhịp an toàn

Dungeon progression phải luôn giữ được hai lực kéo:
- `tham`: chạm sâu hơn sớm hơn, lách route nguy hiểm hơn, cầm đồ quý hơn
- `an toàn`: quay về base, sửa đồ, nạp mana, ổn định gate, làm route bền hơn

Nếu chỉ còn một lực, progression sẽ hỏng:
- chỉ tham thì thành roulette
- chỉ an toàn thì thành checklist chậm

## 3. Nối floor, boss, gate và economy

Dungeon progression là nơi:
- floor hierarchy đổi risk/reward
- boss system tạo mốc áp lực
- gate tạo reward logistics
- economy trả giá cho mỗi cú đẩy sâu

## Progression Axes

## 1. Depth Reach

Người chơi có thể chạm tới depth band nào, tầng nào, route nào.

## 2. Survival Viability

Người chơi có sống sót được trong lớp sâu đó đủ lâu để:
- nhìn
- hiểu
- lấy
- quay về

## 3. Return Value

Một chuyến xuống sâu có mang về được resource, mana, vật liệu milestone hay thông tin đủ giá trị để đáng lặp lại không.

## 4. Route Stability

Tuyến đó có còn là cú liều từng lần, hay đã trở thành đường dùng được nhiều lần.

## 5. Energy And Logistics

Tuyến đó có đang đòi:
- food
- repair
- mana
- fuel
- utility
- điểm hồi sinh

ở mức quá đắt hay chưa.

## 6. Exploitation Readiness

Một vùng sâu chỉ thật sự đi vào progression dài hạn khi:
- chi phí quay lại không vô lý
- reward đủ đều
- recovery không quá bế tắc

## Dungeon State Model

State model này bám chặt [Floor Hierarchy.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/05_DUNGEON_SYSTEM/Floor%20Hierarchy.md), nhưng được đọc theo nghĩa `tiến trình` thay vì `phân lớp chiều sâu`.

## 1. Unknown

- vùng sâu hoặc route này chưa được người chơi chạm tới

## 2. Reached

- người chơi đã đặt chân tới
- đã biết nó tồn tại
- nhưng chưa có cơ sở để xem nó là route hợp lệ

## 3. Unstable Access

- người chơi có thể xuống hoặc lách qua
- nhưng:
  - chi phí cao
  - recovery đau
  - quay lại kém ổn định
  - logistics còn quá mỏng

## 4. Milestone-Blocked

- route đó đã lộ rõ một mốc cần xử lý để ổn định
- thường là:
  - boss gatekeeper
  - gate hỏng
  - áp lực mana / fuel / module repair

## 5. Stable Route Unlocked

- mốc chính của route đã được xử lý
- gate đã ổn định hoặc tuyến thay thế đã đủ tin cậy
- chi phí quay lại đã giảm rõ

## 6. Established Exploitation Layer

- route này không còn chỉ là chỗ “đã mở”
- nó đã thành phần có thể dùng lặp lại để nuôi:
  - resource
  - mana
  - utility
  - tiến trình sâu hơn

## Dungeon Transition Rules

## Unknown -> Reached

Xảy ra khi người chơi lần đầu chạm vào route hoặc depth band mới.

Điều kiện đủ:
- không cần gate
- không cần boss chết
- không cần route ổn định

## Reached -> Unstable Access

Xảy ra khi người chơi đã chứng minh có thể:
- xuống tới nơi
- tương tác ở mức tối thiểu
- quay về ít nhất một lần có ý nghĩa

Nhưng route vẫn chưa bền.

## Unstable Access -> Milestone-Blocked

Xảy ra khi game đã lộ rõ rằng route này có một mốc logistics cần xử lý, ví dụ:
- boss canh gate
- gate cần sửa theo module
- fuel pressure hoặc mana pressure đủ mạnh để route không thể xem là ổn định

## Milestone-Blocked -> Stable Route Unlocked

Xảy ra khi:
- boss gatekeeper được xử lý đủ để tạo cửa sổ sửa gate
- gate được sửa ổn định
- route chính có thể dùng lại như một đường đi hợp lệ về mặt dài hạn

## Stable Route Unlocked -> Established Exploitation Layer

Xảy ra khi người chơi thực sự:
- dùng route đó lặp lại
- kéo được resource về đều hơn
- dùng thành quả đó để nuôi tiến trình sau

## Regression Rules

- `Reached` và `Stable Route Unlocked` là milestone world-persistent, không nên tụt về `Unknown`.
- `Established Exploitation Layer` có thể bị yếu đi nếu:
  - gate đói năng lượng
  - logistics suy sụp
  - người chơi chủ động phá gate để refarm boss

  nhưng không được xóa sạch lịch sử tiến trình.

## Relationship With Floor Hierarchy

[Floor Hierarchy.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/05_DUNGEON_SYSTEM/Floor%20Hierarchy.md) trả lời:
- tầng sâu khác nhau thế nào
- mana xuất hiện từ đâu
- depth band đổi risk/reward ra sao
- mỗi tầng hang mang biome gì
- dungeon nằm ở đâu trong từng tầng

`Dungeon Progression` trả lời:
- người chơi đi qua các depth band đó như thế nào
- depth nào chỉ là phát hiện
- depth nào đã dùng được
- depth nào đã thành nguồn tiến trình ổn định

Nói ngắn:
- `Floor Hierarchy` là grammar của chiều sâu
- `Dungeon Progression` là grammar của việc chinh phục chiều sâu đó

## Relationship With Natural Cave And Dungeon Pocket

Trong mô hình hiện tại:
- phần lớn chuyến đi diễn ra trong `hang tự nhiên` của từng tầng
- `dungeon` không thay thế cả tầng, mà là mục tiêu đậm nằm bên trong tầng đó

Điều này kéo theo:
- người chơi có thể tiến trong một tầng hang mà chưa cần chạm dungeon
- dungeon thường là nơi nén milestone, loot đậm, boss hoặc gate
- nhưng progression của cả tầng vẫn phải đọc được ngay cả ngoài dungeon

## Relationship With Boss And Gate

## Boss

Boss quan trọng nhất trong dungeon progression hiện tại là `gatekeeper boss`.

Vai trò của nó:
- không phải chặn mọi đường xuống
- mà chặn việc biến một route sâu thành tuyến đi bền

## Gate

Gate là reward logistics, không phải win button.

Khi gate chưa ổn định:
- route đắt
- recovery đau
- cạn mana dễ vỡ nhịp
- boss có thể làm hỏng tiến độ sửa

Khi gate đã ổn định:
- route vẫn còn cost
- nhưng đã đổi chất từ `liều` thành `vận hành được`

## Boss-Gate Coupling

Dungeon progression phải giữ đúng coupling này:
- muốn yên ổn sửa gate, thường phải hạ boss trước
- nếu chưa hạ boss, vẫn có thể sửa từng phần nhưng boss có thể phá module và làm mất tài nguyên
- nếu muốn farm lại boss, người chơi có thể phá gate để gọi lại
- refarm chỉ rơi vật liệu farm, không reset milestone chính

## Relationship With Player Progression

`Player Progression` lo việc người chơi mạnh lên bằng:
- gear
- utility
- base
- mana literacy
- stat point

`Dungeon Progression` lo việc các lớp sức mạnh đó được thử và đổi thành tiến trình world-facing như thế nào.

Ví dụ:
- stat point giúp đi sâu ổn hơn
- utility giúp sống lâu hơn ở tầng mới
- mana giúp vận hành machine, gate và route
- nhưng chỉ khi route sâu được ổn định, những thứ đó mới chuyển thành tiến trình bền

## Relationship With Failure And Recovery

Thất bại trong dungeon progression được phép:
- làm mất loot chuyến đi
- làm lỡ nhịp sửa gate
- làm chậm việc ổn định route
- làm tốn thêm food, repair, mana container, fuel

Thất bại không được phép:
- xóa gate đã ổn định từ trước
- xóa điểm chỉ số
- xóa hạ tầng base nền
- đưa người chơi vào deadlock không còn đường hồi

Nghĩa là:
- fail đau ở cấp `run`
- milestone giữ ở cấp `world progression`

## Core Flows

## 1. First Reach Flow

1. Người chơi chuẩn bị từ base.
2. Xuống lớp sâu mới.
3. Chạm resource / hazard / quái / mana signal mới.
4. Nhận ra vùng này có giá trị, nhưng chưa bền.
5. Quyết định:
   - quay về với thông tin và chút thành quả
   - hay tham sâu hơn với rủi ro cao hơn

## 2. First Mana Contact Flow

1. Người chơi chạm `tầng 3+`.
2. Quặng mana hoặc resource năng lượng bắt đầu có vai trò thật.
3. Chuyến quay về đầu tiên với mana không chỉ là loot, mà là bước mở pha progression mới.
4. Base bắt đầu chuyển thành nơi chiết xuất, nạp và chuẩn bị cho route sâu hơn.

## 3. First Gatekeeper Milestone Flow

1. Người chơi thấy route sâu bị gắn với gate hỏng và boss giữ cổng.
2. Có thể thử lách hoặc sửa liều từng phần.
3. Thất bại cho thấy route này chưa phải tuyến đi đáng tin.
4. Khi hạ boss và sửa gate thành công, route đổi chất rõ rệt.

## 4. Route Stabilization Flow

1. Người chơi đã có mana, utility và vật tư để sửa gate.
2. Boss tạo áp lực trực tiếp lên hành vi sửa.
3. Module được sửa dần.
4. Gate ổn định, route được world ghi nhận là bền hơn.
5. Các chuyến sau có cost thấp hơn và recovery đỡ đau hơn.

## 5. Deep Exploitation Flow

1. Route sâu đã ổn định.
2. Người chơi quay lại nhiều lần để khai thác resource chiến lược.
3. Thành quả từ route đó nuôi:
   - máy
   - utility
   - craft
   - route sâu hơn
4. Dungeon progression bước sang chu kỳ tiếp theo ở depth cao hơn.

## Edge Cases

## 1. Không phải tầng nào cũng có boss hoặc gate

- hợp lệ
- dungeon progression không được ép template:
  - tầng nào cũng boss
  - tầng nào cũng gate

## 2. Chạm sâu hơn trước khi ổn định mốc cũ

- hợp lệ
- nhưng route mới vẫn ở trạng thái `Unstable Access`
- không được xem là đã “vượt xong” progression cũ

## 3. Boss chết nhưng gate chưa sửa xong

- route chưa ổn định
- boss chỉ mới mở cửa sổ an toàn tạm thời
- nếu chậm, boss có thể hồi lại theo timer thực

## 4. Gate đã ổn định nhưng đói năng lượng

- route vẫn là milestone đã mở
- nhưng chất lượng vận hành của route giảm:
  - đắt hơn
  - lỗi nhiều hơn
  - có thể hút mana cả party gần cổng

## 5. Chủ động phá gate để gọi lại boss

- hợp lệ
- gate chỉ hỏng một phần
- dùng để refarm vật liệu
- không được hoàn milestone lần đầu

## 6. Chết ở vùng sâu sau khi route đã ổn định

- run đau
- recovery vẫn đau
- nhưng stable route phải tiếp tục có giá trị thật sau đó

## Signs Of Good Dungeon Progression

- người chơi luôn thấy một depth hoặc một route kế tiếp đủ cụ thể để nhắm tới
- chạm sâu hơn luôn tạo ít nhất một thay đổi chất lượng, không chỉ thêm số
- mana xuất hiện như một bước chuyển pha rõ từ tầng 3+
- boss gatekeeper làm người chơi hiểu giá trị của route ổn định
- gate ổn định thật sự đổi trải nghiệm của những chuyến sau
- thất bại đau nhưng không xóa những gì đã ổn định được trước đó
- người chơi có thể tham bằng cách lách, nhưng lách luôn có giá rõ

## Signs Of Broken Dungeon Progression

- mỗi tầng mới chỉ là reskin quái mạnh hơn
- route ổn định xong mà cảm giác không khác gì route chưa ổn định
- boss nào cũng thành khóa tuyệt đối, làm dungeon quá tuyến tính
- hoặc ngược lại, lách lúc nào cũng lời hơn xử lý milestone
- mana có mặt nhưng không thay đổi cách chuẩn bị và vận hành chuyến đi
- thất bại một run đủ sức làm vô nghĩa các mốc ổn định trước đó
- low-tier route và vùng nông mất sạch vai trò trong recovery

## Implementation Hooks

## Progression State Tối Thiểu Cho Route / Floor

- `progression_state`
- `first_reached`
- `stable_route_unlocked`
- `established_exploitation`
- `gate_state`
- `boss_state`
- `energy_readiness`

## Event Hook Tối Thiểu

- `first_reach_depth_band`
- `discover_gate_milestone`
- `enter_unstable_access`
- `kill_gatekeeper_boss`
- `repair_gate_module`
- `stabilize_gate`
- `deepen_exploitation_layer`
- `break_gate_for_refarm`

## Save / Persistence Requirement

- world save phải giữ được:
  - route nào đã từng chạm
  - gate nào đã ổn định
  - boss milestone nào đã xử lý lần đầu
  - route nào đang ở trạng thái refarm / gate hỏng một phần

## QA Hook Tối Thiểu

- chạm depth mới nhưng chưa ổn định route
- lách xuống sâu hơn trước khi xử lý gate cũ
- hạ boss nhưng để boss hồi lại vì gate chưa xong
- ổn định gate rồi để gate đói năng lượng
- phá gate để gọi lại boss
- xác nhận stable milestone không mất sau fail run thông thường

## Open Design Questions

- tỷ lệ route sâu nào nên có gate milestone rõ, và route nào chỉ là depth reward không cần gate
- bao nhiêu lớp “ổn định từng phần” nên được hiển thị rõ cho người chơi
- có cần một số route sâu ổn định nhờ logic khác `gatekeeper + gate repair` để tránh công thức lặp lại quá đều không
- mức độ hiển thị UI của `progression state` nên rõ tới đâu, hay để phần lớn cho world language tự nói

## Open Balance Variables

- khoảng cách giữa các mốc gate milestone
- thời gian trung bình từ lúc `Reached` tới lúc `Stable Route Unlocked`
- độ đau hợp lý của `Unstable Access`
- mức tiết kiệm thực tế mà stable gate mang lại cho các chuyến sau
- tần suất người chơi nên chọn `lách` thay vì `ổn định`
- chi phí hợp lý để refarm boss mà không biến nó thành loop tối ưu
