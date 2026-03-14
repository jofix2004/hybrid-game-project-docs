Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 10/03/2026

# Floor Hierarchy

Tài liệu này chốt `hệ phân tầng chiều sâu` của phần dưới lòng đất như một trục tổ chức tiến trình, rủi ro, phần thưởng và logistics. Mô hình hiện tại của game là: phía trên là `một đảo hoang có mặt đất còn sống được`; phía dưới là `nhiều lớp hang`; mỗi `tầng hang` mang `một biome đặc thù`; còn `hầm ngục`, `POI`, `ruins` hay `công trình đặc biệt` là các pocket nội dung đậm nằm chen trong từng tầng hang. Nó trả lời các câu hỏi nền: thế nào là một tầng hang trong game này, mỗi lớp sâu phải đổi cái gì, tầng sâu hơn khác tầng nông ở đâu ngoài việc quái mạnh hơn, mana xuất hiện từ mốc nào, boss và gate cắm vào cấu trúc tầng ra sao, và một tầng được coi là `đã chạm tới` khác gì với `đã ổn định để khai thác lâu dài`.

Doc này là `grammar` cho chiều sâu hầm ngục. Về sau:
- `Dungeon Generation.md`
- `Room Types.md`
- `Trap System.md`
- `World Generation.md`
- `Dungeon Progression.md`

sẽ cắm dữ liệu, content và logic procedural cụ thể vào khung này.

## Mục tiêu

- Thay stub cũ bằng một doc production dùng được cho design, code, content và QA.
- Chốt `chiều sâu tầng` như một trục gameplay thật, không phải thang tăng số.
- Tách rõ:
  - `floor hierarchy`
  - `biome`
  - `POI / ruins / interior`
  - `gate milestone`
  - `boss gatekeeper`
- Chốt quan hệ giữa:
  - độ sâu
  - loại tài nguyên
  - áp lực quay về
  - gate ổn định
  - boss mốc
  - mana

## Phạm vi

Tài liệu này tập trung vào:
- định nghĩa `tầng` và `lớp sâu`
- các `depth band` chính
- tín hiệu cho biết người chơi đã sang lớp sâu mới
- quan hệ giữa tầng với:
  - tài nguyên
  - visibility / điều hướng
  - hazard
  - quái
  - mana
  - gate
  - boss milestone
- khác biệt giữa:
  - `đi xuống được`
  - `quay lại được`
  - `khai thác ổn định được`

Tài liệu này không đi sâu vào:
- thuật toán tạo map cụ thể
- layout chi tiết từng tầng
- danh sách biome hoàn chỉnh
- room nội thất cụ thể
- bảng spawn chính xác
- số liệu balance cuối cùng

## Source Coverage

### Nguồn bắt buộc

- [10_QUESTIONS_LEVEL_6.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/10_QUESTIONS_LEVEL_6.md)
  - là nguồn macro cho:
    - vai trò của chiều sâu trong tiến trình dài hạn
    - chặng 1-4
    - mốc `tầng 3+`
    - resource tier và economy theo độ sâu
- [11_QUESTIONS_LEVEL_7.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/11_QUESTIONS_LEVEL_7.md)
  - dùng để khóa ranh giới kỹ thuật và vận hành:
    - hang mở theo zone/chunk
    - ranh giới mô phỏng
    - tầng là lớp nội dung tổ chức tiến trình chứ không ép thành một chuỗi scene tuyến tính
- [15_GATE_AND_BOSS_MILESTONE_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/15_GATE_AND_BOSS_MILESTONE_SHEET.md)
  - là nguồn đúng cho:
    - gate ổn định
    - gatekeeper boss
    - sửa gate theo module
    - lách xuống sâu hơn trước khi ổn định tuyến
    - quan hệ giữa boss và tuyến đi lại bền vững

### Nguồn đối chiếu bắt buộc

- [Core Gameplay Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Core%20Gameplay%20Loop.md)
- [Long Progression Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Long%20Progression%20Loop.md)
- [Multiplayer Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Multiplayer%20Loop.md)
- [Crafting Economy.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/06_ECONOMY_SYSTEM/Crafting%20Economy.md)

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - doc này đủ rõ để làm nguồn đúng cho:
    - `Dungeon Generation.md`
    - `World Generation.md`
    - `Boss System.md`
    - `Dungeon Progression.md`
    - `Drop Tables.md`
  - các con số như số tầng thật, khoảng cách giữa các mốc gate, số dungeon pocket mỗi tầng hay số biome mặt đất giữ cho MVP vẫn thuộc balance/content layer sau

## Conflict Resolution

- Stub cũ từng mô tả chiều sâu như một dãy tầng cố định kiểu:
  - floor 1 là hang cơ bản
  - floor 2 là nấm
  - floor 3 là dung nham
  - floor 4 là tàn tích

  Hướng đó không còn đúng với cấu trúc game hiện tại.

- Quyết định cuối:
  - `tầng` hiện được hiểu là `một lớp hang` theo chiều sâu
  - mỗi `tầng hang` có `một biome đặc thù` làm identity chính
  - `dungeon / POI / ruins` là lớp nội dung chèn vào bên trong tầng hang, không thay thế định nghĩa của tầng

- Game hiện là `nhiều lớp hang tự nhiên theo chiều sâu`, không phải chuỗi room tuyến tính.
- `Đi tới một tầng sâu hơn` không đồng nghĩa với `đã làm chủ tầng đó`.
- `Gate ổn định` mới là thứ biến một lớp sâu thành tuyến đi lại bền vững.
- `Boss gatekeeper` chỉ nên xuất hiện ở các mốc đủ quan trọng, không phủ lên mọi tầng.

## Rule Summary

- Chiều sâu là một trong những trục tiến trình thật của game.
- Mỗi lớp sâu hơn phải đổi ít nhất:
  - loại tài nguyên đáng săn
  - loại nguy hiểm chính
  - giá quay về / phục hồi
  - yêu cầu chuẩn bị trước chuyến đi
- Từ `tầng 3+`, mana không còn là ý tưởng nền mà trở thành tài nguyên và hạ tầng thật.
- Người chơi có thể `lách xuống sâu hơn` qua lối nguy hiểm mà chưa ổn định được tuyến.
- `Boss gatekeeper + sửa gate` là cơ chế biến:
  - `đi xuống được`
  thành
  - `khai thác lâu dài được`
- Không phải mọi tầng đều có boss.
- Không phải mọi tầng đều có gate.
- Nhưng mỗi `tầng hang` nên có một `biome đặc thù` riêng đủ rõ để người chơi cảm được mình đã bước sang một lớp sâu mới.

## Floor Hierarchy Role In The Game

## 1. Tổ chức độ khó

Chiều sâu không chỉ tăng damage / HP của quái. Nó tổ chức:
- visibility
- điều hướng
- trap / hazard
- giá rút lui
- chất lượng phần thưởng
- độ ổn định của tuyến đi

## 2. Tổ chức economy

Chiều sâu quyết định:
- tier tài nguyên nào bắt đầu xuất hiện
- cái gì là loot nền
- cái gì là loot chiến lược
- mana bước vào economy từ đâu
- cái gì nên coi là milestone material

## 3. Tổ chức tiến trình dài hạn

Một tầng sâu hơn chỉ có giá trị bền khi người chơi đi qua đủ 3 nấc:

1. `chạm được`
2. `sống sót được`
3. `ổn định được tuyến khai thác`

## 4. Tổ chức cấu trúc không gian dưới đất

Trong mô hình hiện tại:
- `mặt đất` là một đảo hoang nhìn ra biển
- `mỗi tầng hang` là một lớp chiều sâu lớn
- `hang tự nhiên` là vật liệu nền chính của từng tầng
- `hầm ngục` là pocket nội dung đậm cắm vào trong tầng đó

Điều này giúp game giữ được cùng lúc:
- cảm giác đào sâu qua hang tự nhiên
- và cảm giác khám phá các điểm đậm như công trình cổ, khu milestone hay dungeon thực thụ

## Depth Bands

Doc này chưa khóa tên cụ thể của từng biome theo từng tầng, nhưng khóa rule rằng mỗi `tầng hang` phải có một `biome identity` rõ, đồng thời vẫn bám theo `các band chiều sâu` để production về sau tổ chức content và progression.

## Band 0: Bề mặt và vùng quay về

Vai trò:
- vùng hồi phục
- base / spawn / bed
- nguồn vật liệu và nhu yếu phẩm an toàn hơn
- nơi tiêu hóa loot thành tiến trình

Tín hiệu chính:
- an toàn tương đối
- visibility đọc được
- resource nền
- giá thất bại thấp hơn

## Band 1: Tầng nông học game

Vai trò:
- dạy loop cơ bản
- dạy nhặt, craft nền, đánh, rút lui
- cho phép tích lũy vật liệu nền và tài nguyên phổ thông

Đặc trưng:
- dễ định hướng hơn
- quái thiên về kiểm tra làm quen
- tài nguyên phổ thông là chính
- utility cần ít

## Band 2: Tầng giữa ổn định và utility

Vai trò:
- bắt đầu buộc người chơi chuẩn bị trước chuyến đi
- mở utility thật sự
- tăng áp lực visibility, đường đi, trap và hazard

Đặc trưng:
- tài nguyên chiến lược bắt đầu xuất hiện
- đường lui đắt hơn
- quái và môi trường bắt đầu ép quản lý nhiều lớp hơn
- căn cứ, workstation và utility có giá trị rõ hơn

## Band 3: Tầng mana và năng lượng

Vai trò:
- mốc bắt đầu của `mana economy`
- chuyển game từ survival + craft nền sang survival + hạ tầng năng lượng

Đặc trưng:
- xuất hiện từ `tầng 3+`
- bắt đầu có:
  - quặng mana
  - vật liệu năng lượng
  - machine / utility dùng mana
  - áp lực logistics khác với tầng nông

## Band 4: Tầng milestone và gatekeeper

Vai trò:
- nơi các mốc gate ổn định và boss gatekeeper trở nên quan trọng
- nơi “đi được” và “khai thác được” tách nhau rõ nhất

Đặc trưng:
- có thể có gate milestone
- có thể có boss gatekeeper
- có thể có lối lách xuống sâu hơn khi chưa hạ boss
- nhưng tuyến đi lại vẫn bất ổn cho tới khi gate được sửa ổn định

## Band 5: Tầng sâu để khai thác lặp lại

Đây không phải là một band nội dung riêng hoàn toàn, mà là `trạng thái tiến trình` của những vùng sâu đã được ổn định hóa.

Vai trò:
- biến chiều sâu thành nguồn tiến trình lặp lại lâu dài
- cho phép logistics sâu hơn
- giảm giá quay lại đúng nghĩa phần thưởng dài hạn

Đặc trưng:
- gate đã ổn định
- tuyến đi lại rõ hơn
- player có thể đầu tư khai thác, farm chiến lược, chuẩn bị cho mốc sâu hơn

## Floor Identity Axes

Mỗi tầng hoặc mỗi lớp sâu phải được định nghĩa tối thiểu qua các trục sau:

## 1. Reward Axis

- tài nguyên nền
- tài nguyên chiến lược
- tài nguyên mana
- vật liệu milestone

## 2. Risk Axis

- quái
- hazard môi trường
- trap / điều hướng
- giá rút lui

## 3. Preparation Axis

- thức ăn và vật tư expedition
- tool tier
- utility
- ánh sáng / nhìn đường
- mana / fuel / machine support

## 4. Stability Axis

- chưa chạm tới
- đã chạm tới
- chạm tới nhưng chưa ổn định
- đã có gate ổn định
- đã thành tuyến đi khai thác lâu dài

## Floor State Model

Doc này thêm một lớp state rất quan trọng: `trạng thái của tầng trong quan hệ với người chơi / world`.

## 1. Unreached

- người chơi chưa từng xuống tới tầng này

## 2. Reached

- người chơi đã tới được tầng này ít nhất một lần
- nhưng chưa có route ổn định

## 3. Unstable Access

- người chơi có thể xuống hoặc lách qua
- nhưng việc quay lại, rút lui và vận hành chuyến đi vẫn đắt và dễ vỡ

## 4. Milestone-Blocked

- tầng này hoặc route ổn định của nó đang bị boss / gate milestone chặn
- vẫn có thể có đường phụ nguy hiểm hơn đi xuyên qua

## 5. Stable Route Unlocked

- gate hoặc đường chính đã được ổn định
- route trở nên bền hơn, rõ hơn, rẻ hơn

## 6. Established Exploitation Layer

- tầng này không còn chỉ là nơi “vừa chạm tới”
- mà đã thành một nguồn tiến trình lặp lại được

## Floor Transition Rules

## Reached -> Unstable Access

Xảy ra khi:
- người chơi lần đầu xuống tới tầng
- hoặc lách qua bằng đường phụ nguy hiểm

## Unstable Access -> Milestone-Blocked

Xảy ra khi:
- world lộ rõ tầng đó có gate / boss / route chặn cần xử lý để ổn định

## Milestone-Blocked -> Stable Route Unlocked

Xảy ra khi:
- boss gatekeeper bị xử lý đủ
- gate được sửa ổn định

## Stable Route Unlocked -> Established Exploitation Layer

Xảy ra khi:
- người chơi đã thật sự dùng route đó để khai thác và tái đầu tư
- tầng sâu đó trở thành một phần ổn định của long progression loop

## Floor Transition Guardrails

- Không được coi `đã đặt chân tới` là `đã làm chủ tầng`.
- Không được coi `đã hạ boss` là `đã ổn định tuyến` nếu gate chưa được sửa.
- Không được coi `gate đã sửa` là `đã vận hành tốt` nếu gate đang đói năng lượng hoặc chưa có logistics đi kèm.

## Signals Of A New Depth Layer

Người chơi phải nhận ra mình đã sang lớp sâu mới qua tín hiệu world rõ ràng, không chỉ qua số damage.

Tối thiểu một lớp sâu mới nên đổi rõ:
- ánh sáng / màu / độ đọc không gian
- vật liệu nền
- âm thanh / ambience
- loại quái chính
- loại tài nguyên đáng săn
- cách chuẩn bị trước khi xuống

Nếu một tầng mới chỉ khác ở con số quái, đó là tầng yếu.

## Relationship Between Surface, Floor, Biome, POI, And Interior

## Mặt đất

Là phần `đảo hoang` nơi người chơi bám trụ, dựng base và chuẩn bị chuyến đi.

Hiện tại mặt đất chỉ giữ vài biome nền cho MVP:
- `rừng rậm`
- `đồng bằng`
- `bãi biển`

## Tầng hang

Là một `lớp hang tự nhiên` theo chiều sâu.
Đây là đơn vị chính để tổ chức:
- risk/reward
- tài nguyên
- mana exposure
- route stability
- boss/gate milestone

## Biome của tầng

Trong hướng hiện tại:
- mỗi `tầng hang` có `một biome đặc thù` làm bản sắc chính
- tầng mới không nên chỉ là tầng cũ đổi số
- subzone nhỏ có thể khác nhẹ, nhưng không được xóa identity của biome chính của tầng

## Hang tự nhiên

Là phần nền chiếm đa số không gian của từng tầng.
Nó tạo ra:
- cảm giác đào sâu
- điều hướng
- resource loop
- pressure của chuyến đi

## Hầm ngục / POI / Ruins / Công trình

Là các pocket nội dung đậm cắm vào trong một tầng hang.
Chúng có thể là:
- hầm ngục
- công trình cổ
- ruins
- khu milestone
- boss arena

Chúng làm giàu cho tầng, nhưng không thay thế việc định nghĩa tầng.

## Interior / Room

Là lớp nội dung nén bên trong dungeon hoặc công trình đặc biệt.
Đây là `nội dung trong tầng`, không phải cấu trúc chính của toàn bộ underground.

## Relationship With Resource Tiers

## Tầng nông

Nghiêng về:
- tài nguyên nền
- vật tư sống còn
- vật liệu build và craft cơ bản

## Tầng giữa

Nghiêng về:
- tài nguyên chiến lược
- vật liệu utility
- công cụ tốt hơn

## Tầng 3+

Bắt đầu nghiêng mạnh về:
- quặng mana
- vật liệu năng lượng
- input cho machine / gate / utility cao hơn

## Tầng milestone

Nghiêng về:
- boss material
- gate repair material
- vật liệu hiếm gắn với unlock lớn

## Relationship With Gate And Boss

## Gate

Gate không phải “thang máy bắt buộc để mới được xuống”.
Gate là:
- mốc sửa chữa
- reward logistics
- cơ chế biến chiều sâu thành tuyến đi bền

## Boss

Boss gatekeeper không cần xuất hiện dày.
Nó nên là:
- mốc chặn route ổn định
- áp lực thực khi đang sửa gate
- nguồn farm vật liệu phụ nếu bị gọi lại

## Rule cốt lõi

- Có thể xuống sâu hơn trước khi ổn định mốc cũ.
- Nhưng nếu chưa xử lý boss/gate milestone:
  - tuyến đi lại không bền
  - recovery khó hơn
  - logistics đắt hơn

## Relationship With Failure And Recovery

Chiều sâu phải làm tăng `giá thất bại` theo 3 cách:

## 1. Giá vật tư

- đồ mang theo đắt hơn
- utility và fuel tốn hơn

## 2. Giá quay lại

- đường lui xa hơn
- recovery marker khó lấy hơn
- gate chưa ổn định thì càng đau

## 3. Giá cơ hội

- mất một nhịp đẩy sâu
- mất tiến độ chuẩn bị mở mốc kế tiếp

Nhưng chiều sâu không được tạo deadlock:
- base còn
- tầng nông còn hữu ích
- gate đã mở ổn định vẫn giữ giá trị sau thất bại

## Core Flows

## 1. First Reach Flow

1. Người chơi chuẩn bị từ base.
2. Xuống tầng nông rồi tầng giữa.
3. Chạm lớp sâu mới.
4. Nhận ra tín hiệu tầng mới:
   - loot khác
   - quái khác
   - visibility / hazard khác
5. Quyết định:
   - tham tiếp
   - hay mang thành quả về

## 2. Touch Mana Flow

1. Người chơi xuống `tầng 3+`.
2. Lần đầu gặp quặng mana hoặc tài nguyên năng lượng.
3. Nhận ra game đã sang một lớp chuẩn bị mới.
4. Chuyến quay về bắt đầu nuôi:
   - machine
   - utility
   - gate logistics

## 3. Bypass Without Stability Flow

1. Người chơi tìm được đường phụ hoặc route nguy hiểm.
2. Lách xuống tầng sâu hơn dù mốc cũ chưa ổn định.
3. Thu được reward sớm hơn.
4. Đổi lại:
   - recovery tệ hơn
   - tuyến quay lại đắt hơn
   - farm lặp lại khó hơn

## 4. Stabilize A Milestone Floor Flow

1. Người chơi tới mốc gate.
2. Chạm boss gatekeeper.
3. Hạ boss hoặc tạo khoảng trống đủ để sửa gate.
4. Sửa từng module.
5. Gate ổn định.
6. Tầng đó chuyển sang trạng thái `Stable Route Unlocked`.

## 5. Exploitation Flow

1. Tầng đã ổn định được dùng như tuyến quay lại bền.
2. Người chơi farm chiến lược ở khu đó.
3. Tài nguyên sâu được mang về nuôi tầng sâu hơn nữa.
4. Loop dài hạn tiếp tục mở tới mốc mới.

## Failure And Recovery

### Failure ở lớp chiều sâu

- xuống tới tầng mới nhưng chưa rút kịp
- chạm mana quá sớm nhưng logistics chưa đủ
- lách xuống sâu hơn nhưng chưa ổn định route
- gate đã gần xong nhưng bị boss phá module

### Recovery

- quay về tầng nông để hồi phục nền
- dùng route đã ổn định trước đó
- tái chuẩn bị qua base / workstation / mana machine
- chấp nhận bỏ một lớp sâu chưa ổn định để giữ mạng lưới tiến trình còn lại

## Edge Cases

## 1. Người chơi chạm tầng sâu hơn trước khi xử lý mốc cũ

- hợp lệ
- nhưng tầng đó ở trạng thái `Unstable Access`, không được xem là progression ổn định

## 2. Boss chết nhưng gate chưa sửa xong

- tầng chưa được xem là ổn định
- boss chỉ mới mở ra khoảng trống sửa gate

## 3. Gate sửa xong nhưng thiếu năng lượng

- mốc chiều sâu đã được mở về mặt world
- nhưng route vẫn có thể vận hành kém, đắt hoặc lỗi do thiếu năng lượng

## 4. Một tầng có dungeon hoặc POI khác chất biome nền

- hợp lệ
- miễn là `biome chính của tầng` vẫn đọc được rõ
- dungeon là pocket nội dung đậm, không được xóa cảm giác rằng người chơi vẫn đang ở trong một tầng hang có identity riêng

## 5. Không phải tầng nào cũng có boss hay gate

- hợp lệ
- boss và gate là mốc nhấn, không phải template lặp máy móc cho mọi tầng

## 6. Tài nguyên cũ còn dùng ở tầng sâu

- đây là feature tốt, không phải dấu hiệu progression kém
- miễn là tầng mới vẫn mở thêm quyết định mới chứ không chỉ farm đồ cũ nhiều hơn

## Signs Of A Good Floor Hierarchy

- người chơi cảm nhận rõ “xuống sâu hơn” bằng luật chơi, không chỉ bằng số
- tầng sâu hơn mở thêm mục tiêu, không chỉ mở thêm địch mạnh
- tầng cũ vẫn còn giá trị trong recovery và chuẩn bị
- gate ổn định tạo ra cảm giác thắng dài hạn thật
- mana bước vào đúng như một nấc tiến trình mới, không quá sớm và không quá muộn

## Signs Of A Broken Floor Hierarchy

- mỗi tầng mới chỉ là reskin màu khác
- mọi tầng đều đòi cùng một kiểu chuẩn bị
- tầng 3+ không tạo ra khác biệt thật dù đã có mana
- boss/gate lặp lại như checklist máy móc
- xuống sâu hơn nhưng không thấy reward qualitatively khác
- tầng cũ thành rác quá nhanh hoặc tầng mới xóa sạch giá trị tầng cũ

## Implementation Hooks

### Floor Definition tối thiểu

- `floor_id`
- `depth_index`
- `depth_band`
- `primary_biome_id`
- `surface_or_underground_class`
- `reward_profile`
- `risk_profile`
- `visibility_profile`
- `hazard_profile`
- `resource_tier_profile`
- `mana_presence_class`
- `gate_presence`
- `boss_presence`
- `milestone_class`
- `dungeon_poi_pool`

### Floor Runtime State tối thiểu

- `reached`
- `stable_route_unlocked`
- `gate_state`
- `boss_state`
- `route_risk_modifier`

### Event hook tối thiểu

- `first_enter_floor`
- `discover_new_depth_band`
- `discover_gate_milestone`
- `bypass_to_deeper_floor`
- `kill_gatekeeper_boss`
- `repair_gate_module`
- `stabilize_gate`

### QA hook tối thiểu

- lần đầu chạm tầng mới có tín hiệu rõ
- xuống `tầng 3+` mở đúng lớp mana
- lách xuống tầng sâu hơn khi chưa ổn định mốc cũ
- hạ boss nhưng chưa sửa gate xong
- sửa gate xong nhưng chưa có năng lượng tốt
- tầng đã ổn định giữ giá trị sau khi chết

## Open Design Questions

- MVP thực tế có bao nhiêu tầng / cụm tầng.
- Khoảng cách giữa các mốc gatekeeper nên dày tới đâu.
- Tỷ lệ tầng có gate so với tầng chỉ là lớp khám phá thường.
- Có nên có một số tầng thiên hẳn về:
  - tài nguyên
  - điều hướng
  - hazard
  - POI milestone
  hay giữ phân bố trộn nhiều hơn.

## Open Balance Variables

- số tầng trong mỗi depth band
- mốc chính xác mà mana bắt đầu xuất hiện dày
- khoảng cách giữa các gate milestone
- độ dốc tăng của `retreat cost`
- độ dốc tăng của `preparation cost`
- mức độ “lách xuống sâu hơn” nên khó tới đâu trước khi thành exploit
