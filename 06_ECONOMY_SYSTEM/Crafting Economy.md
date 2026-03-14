Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 09/03/2026

# Crafting Economy

Tài liệu này chốt `dòng chảy kinh tế` đi qua các hành vi `craft`, `repair`, `salvage`, `workstation`, `mana extraction` và phần `chuẩn bị nhiên liệu / logistics` có liên quan trực tiếp tới chế tạo. Nó không phải danh sách recipe. Nó trả lời các câu hỏi nền: người chơi phải trả giá gì để có đồ mới, món nào craft tay được, món nào buộc phải qua workstation, vật tư được lấy từ đâu, công trình chế tạo ăn tài nguyên thế nào, repair rẻ hay đắt ở đâu, salvage trả lại bao nhiêu giá trị, và mana/gate trở thành sink vận hành ra sao sau khi game chạm tầng sâu.

Doc này là `bộ luật phát triển kinh tế chế tạo`. Về sau:
- `Crafting System.md` sẽ lo flow thao tác và state machine
- `Building System.md` sẽ lo luật place/destroy công trình
- `Items.md`
- `Recipes.md`
- `Crafting Costs.md`
sẽ cắm dữ liệu cụ thể vào grammar này.

## Mục tiêu

- Chốt `crafting` như một trục `economy sink + conversion loop`, không chỉ là menu tạo đồ.
- Chốt ranh giới giữa:
  - `craft tay`
  - `craft ở workstation`
  - `repair`
  - `salvage`
  - `chiết xuất mana`
- Chốt nguồn đầu vào cho chế tạo:
  - inventory cá nhân
  - kho gần đó
  - vật tư nhét vào công trình
- Chốt vai trò kinh tế của:
  - workstation
  - repair kit
  - máy sửa base
  - máy chiết xuất mana
  - gate fuel / pin / lõi mana

## Phạm vi

Tài liệu này tập trung vào:
- vai trò kinh tế của crafting trong core loop và long progression loop
- chi phí đầu vào của chế tạo
- nhịp craft theo thời gian
- nhịp mở recipe và signposting kinh tế
- investment loop của workstation
- repair / salvage economy
- mana extraction economy
- gate fuel và logistics fuel như nhánh sink liên quan tới crafting

Tài liệu này không đi sâu vào:
- UI craft
- queue/cancel behavior chi tiết của từng station
- bảng recipe cụ thể
- con số nguyên liệu cụ thể cho từng item
- layout base hoặc placement detail của công trình
- thống kê balance số cuối cùng

## Source Coverage

### Nguồn bắt buộc

- [10_QUESTIONS_LEVEL_6.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/10_QUESTIONS_LEVEL_6.md)
  - là nguồn macro cho:
    - faucets
    - sinks
    - resource tier
    - investment loop
    - vị trí của mana trong economy
- [12_QUESTIONS_LEVEL_8.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/12_QUESTIONS_LEVEL_8.md)
  - là nguồn rule gameplay trực tiếp cho:
    - craft tay vs workstation
    - craft time
    - recipe unlock
    - nguồn nguyên liệu khi craft
    - workstation tier
    - workstation dùng mana
    - repair kit
    - máy sửa base
    - chiết xuất mana
- [14_INVENTORY_AND_ITEM_RULES_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/14_INVENTORY_AND_ITEM_RULES_SHEET.md)
  - là nguồn đúng trực tiếp cho:
    - repair kit dạng công trình đặt xuống
    - 1 slot sửa / tháo rã
    - nguyên liệu sửa lấy từ inventory + kho gần đó
    - hủy tiến trình repair/salvage
    - hoàn đồ / rơi đồ khi nhặt lên hoặc phá công trình
    - salvage yield
    - charge container / pin / lõi mana
- [15_GATE_AND_BOSS_MILESTONE_SHEET.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/15_GATE_AND_BOSS_MILESTONE_SHEET.md)
  - là nguồn đúng cho:
    - gate fuel
    - gate energy sink
    - gate repair as milestone sink
    - refarm boss material as non-milestone crafting input

### Nguồn đối chiếu bắt buộc

- [Core Gameplay Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Core%20Gameplay%20Loop.md)
  - dùng để giữ đúng vai trò của craft trong vòng `prepare -> descend -> recover -> upgrade`
- [Long Progression Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Long%20Progression%20Loop.md)
  - dùng để giữ đúng chỗ đứng của workstation, mana machine và gate trong macro progression
- [Inventory System.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/03_PLAYER_SYSTEMS/Inventory%20System.md)
  - dùng để khớp rule đầu vào / overflow / item charge
- [Equipment System.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/03_PLAYER_SYSTEMS/Equipment%20System.md)
  - dùng để khớp rule repair/durability outcome cho giáp và artifact
- [Survival System.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/02_CORE_SYSTEMS/Survival%20System.md)
  - dùng để khớp rule mana cá nhân, mana refill và utility cost

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - doc này đã đủ rõ để làm nguồn đúng cho:
    - `Crafting System.md`
    - `Building System.md`
    - `Items.md`
    - `Recipes.md`
    - `Crafting Costs.md`
    - `Mana Consumption.md`
  - những chỗ như:
    - số nguyên liệu từng recipe
    - thời gian từng món
    - phạm vi kho liên kết thực tế
    - efficiency cụ thể của máy
    vẫn thuộc balance/data layer

## Conflict Resolution

- Bản nháp cũ từng xem `repair kit` như công cụ cầm tay dùng mãi. Quyết định cuối đã đổi sang:
  - `repair kit` là `công trình đặt xuống`
  - có thể thu hồi
  - có durability riêng
  - dùng slot bên trong để sửa hoặc tháo rã
- `Repair kit bị phá` không còn rơi lại nguyên kit như một rule chung. Rule cuối là:
  - `thu hồi chủ động` thì lấy lại nguyên kit với độ bền còn lại
  - `bị phá` thì rơi ra nguyên liệu chế tạo nó theo logic phá công trình
- `Pin / lõi mana` không còn dùng logic tiêu thụ theo thứ tự slot. Quyết định cuối là:
  - chúng là `vật chứa charge`
  - dùng tới đâu trừ tới đó
  - không bỏ phần dư
- `Artifact có durability` hiện không thuộc vòng repair economy:
  - về `0` thì vỡ mất luôn
  - không sửa được
- `Crafting Economy` không định nghĩa toàn bộ flow bấm nút craft; nó định nghĩa:
  - cost
  - conversion
  - sink
  - nguồn vào
  - investment loop

## Rule Summary

- `Đồ đơn giản` có thể craft tay.
- `Đồ cao hơn` cần workstation.
- `Đồ nhỏ` ra ngay.
- `Đồ lớn / đồ cao / đồ mana` có thời gian craft.
- `Công thức` mở theo nhiều nguồn:
  - đồ cơ bản mở khi thấy nguyên liệu hoặc có workstation
  - đồ cao mở qua blueprint, research hoặc milestone
- `Nguyên liệu khi craft` lấy từ:
  - inventory cá nhân
  - và kho chung trong phạm vi quy định quanh bàn
- `Workstation` có tier, nhưng phải hạn chế số loại.
- `Workstation cấp thấp` không cần mana.
- `Workstation cấp cao` có loại:
  - vẫn chạy tay rất chậm
  - hoặc thiếu mana là tắt hẳn
- `Repair ở base`:
  - nhanh hơn
  - rẻ hơn
  - hồi full độ bền
- `Repair dã chiến`:
  - làm được
  - nhưng kém hiệu quả hơn
  - tốn chi phí bất lợi hơn base
- `Salvage` luôn trả lại ít hơn craft mới.
- `Chiết xuất mana` cần machine/workstation riêng, hiệu suất tùy tier.
- `Gate` là sink vận hành lớn:
  - sửa gate ăn tài nguyên milestone
  - dùng gate ăn năng lượng
  - nhiên liệu gate dùng chung họ với `pin / bình / lõi mana`

## Crafting Economy Role In The Game Loop

### 1. Chuẩn bị chuyến đi

Crafting cung cấp:
- công cụ
- utility
- vật tư dự phòng
- repair access
- fuel/mana container

Tức là crafting là một phần của `giá vé` trước khi xuống sâu.

### 2. Chuyển loot thành tiến trình thật

Loot chưa tự có nghĩa chỉ vì nhặt được. Nó chỉ thành tiến trình khi được biến qua các vòng:
- craft thành đồ
- repair để kéo dài giá trị đồ
- nâng workstation / machine
- chiết xuất thành mana
- nạp vào gate hoặc logistics infrastructure

### 3. Tạo cạnh tranh tài nguyên

Crafting economy phải làm cho cùng một lượng tài nguyên có thể tranh nhau giữa:
- đồ chiến đấu
- công cụ
- utility
- base / workstation
- mana machine
- gate / route stability

Nếu mọi người luôn craft cùng một thứ theo cùng thứ tự, economy chỉ còn là checklist.

## Resource Classes At Economy Level

### 1. Vật liệu nền

- gỗ
- đá
- sợi
- thức ăn nền

Vai trò:
- nuôi craft cơ bản
- nuôi repair
- nuôi base đầu game
- vẫn còn giá trị ở giữa game vì dùng cho consumable, công thức trung gian và bảo trì

### 2. Vật liệu tiến trình

- kim loại tốt hơn
- vật liệu utility
- vật liệu công cụ/workstation tốt hơn

Vai trò:
- mở tầng power tiếp theo của tool, weapon, utility và station

### 3. Vật liệu mana

- quặng mana
- tinh thể năng lượng
- pin / bình / lõi mana

Vai trò:
- nuôi mana machine
- nạp mana cá nhân
- nuôi utility và station cấp cao
- nuôi gate

### 4. Vật liệu milestone

- boss drop
- lõi cổ
- vật liệu mở mốc hiếm

Vai trò:
- mở gate
- mở machine lớn
- mở recipe / utility đặc biệt
- không nên trở thành vật tư thường ngày

## Craft Paths

## 1. Hand Craft

- Dùng cho đồ đơn giản.
- Thường ra ngay.
- Phù hợp với:
  - survival đầu game
  - emergency craft
  - tool/utility nền

Về kinh tế:
- giảm friction đầu game
- nhưng không nên nuốt vai trò của workstation ở đồ cao hơn

## 2. Workstation Craft

- Dùng cho đồ cao hơn hoặc đồ có tính kỹ thuật rõ hơn.
- Có tier.
- Đồ lớn / đồ cao / đồ mana có thời gian craft.

Về kinh tế:
- là chỗ chuyển loot thành giá trị cao hơn
- là sink đầu tư dài hạn
- tạo mốc “về base rồi mới tối ưu được”

## 3. Repair

- Có hai nhánh:
  - repair chuẩn ở base
  - repair dã chiến qua repair kit

Về kinh tế:
- repair làm đồ bền vững hơn, giảm pressure phải craft mới liên tục
- nhưng không được miễn phí hoàn toàn

## 4. Salvage

- Là nhánh thu hồi giá trị từ đồ cũ/hỏng.
- Không được trả đủ như craft mới.
- Là đường phục hồi một phần tài nguyên, không phải exploit loop hoàn vốn đầy đủ

## 5. Mana Extraction

- Là nhánh chuyển `quặng mana` thành `mana tích trữ`.
- Bắt buộc qua machine/workstation.
- Hiệu suất và tốc độ tùy tier.

## 6. Gate Preparation

- Gate ăn tài nguyên qua:
  - vật liệu sửa gate
  - fuel / mana container
  - chi phí kích hoạt và sử dụng

Vì vậy gate là một nhánh kinh tế sát crafting dù không phải “recipe bàn chế tạo” truyền thống.

## Input Sources And Access Rules

### Crafting Input

- Crafting lấy nguyên liệu từ:
  - `inventory cá nhân`
  - `kho chung trong phạm vi quy định`

### Phạm vi kho liên kết

- Ví dụ hiện tại trong source là khoảng `10x10` tính từ bàn chế tạo.
- Con số chính xác thuộc balance/layer kỹ thuật sau.

### Repair Kit Input

- Repair kit lấy nguyên liệu từ:
  - inventory người chơi
  - và kho gần đó

### Gate Input

- Gate có các ô nhét item riêng.
- Nhét đúng vật tư thì tiến độ sửa hoặc module hoàn tất.
- Nhét sai item:
  - cho nhét
  - nhưng không có tác dụng

## Unlock Logic And Economic Signposting

### Mở công thức

- `Đồ cơ bản`
  - mở khi thấy nguyên liệu hoặc có workstation
- `Đồ cao`
  - mở qua blueprint
  - research
  - milestone

### Ý nghĩa kinh tế

- người chơi luôn nhìn thấy “mình đang thiếu gì”
- unlock gắn với:
  - vật liệu đã gặp
  - station đã có
  - milestone đã vượt

Điều này biến crafting thành mục tiêu kinh tế dễ đọc, không cần wiki mới biết đi đâu tiếp.

## Time Cost And Processing Cost

### Craft Time

- `Đồ nhỏ`
  - ra ngay
- `Đồ lớn / đồ cao / đồ mana`
  - có thời gian craft

### Ý nghĩa

- đầu game bớt rườm
- late game giữ trọng lượng cho đồ lớn
- tạo nền cho automation và mana-powered production

### Processing Cost

Một món craft không chỉ ăn:
- nguyên liệu

Mà còn có thể ăn:
- thời gian chờ
- slot machine
- mana vận hành
- cơ hội dùng machine đó cho việc khác

## Workstation Investment Loop

### Workstation Tier

- Workstation có tier.
- Phải hạn chế số loại để tránh quá nhiều bàn riêng lẻ.

### Mỗi bước nâng tier nên khác biệt về

- khả năng chế
- kích cỡ vật cần chế
- tốc độ chế

### Upgrade Rule

- Upgrade theo kiểu `đập bỏ làm mới`.

### Refund Rule

- Khi đập bỏ workstation:
  - hoàn một phần vật liệu
  - lượng hoàn tùy công cụ dùng để đập

### Mana At Workstation

- `Workstation cấp thấp`
  - không cần mana
- `Workstation cấp cao`
  - dùng mana như nguồn năng lượng tự động
  - có loại thiếu mana thì vẫn chạy tay rất chậm
  - có loại thiếu mana là tắt hẳn

### Ý nghĩa kinh tế

- workstation là sink đầu tư dài hạn
- mana biến từ resource utility thành operating cost
- người chơi có lý do xây infrastructure thay vì chỉ ôm nguyên liệu thô

## Repair Economy

## Base Repair

- sửa ở máy chuyên dụng tại base:
  - nhanh hơn
  - rẻ hơn
  - full độ bền

### Ý nghĩa

- khuyến khích mang đồ về
- giữ giá trị của căn cứ và station chuyên dụng

## Repair Kit

- chủ yếu craft ở workstation
- có thể mua nếu người chơi dư tiền hoặc loot ít
- là công trình đặt xuống
- có thể thu hồi
- có durability riêng
- có `4 cấp`

### Slot xử lý

- hiện chỉ có `1 slot` xử lý tại một thời điểm

### Repair Economy Rule

- sửa bằng repair kit:
  - đắt hơn base
  - hoặc hiệu quả thấp hơn base
- kit cấp thấp:
  - không sửa được đồ cao tier

### Cancel / Break Rule

- nếu muốn lấy món đang sửa dở ra:
  - phải hủy tiến trình trước
  - nguyên liệu hoàn về túi
  - thiếu chỗ thì rơi ra đất
- nếu repair kit đang sửa dở mà bị nhặt lên hoặc bị phá:
  - hủy tiến trình
  - đồ đang sửa rơi ra đất

### Recover / Destruction Rule

- thu hồi chủ động:
  - lấy lại nguyên kit
  - giữ nguyên độ bền còn lại
- nếu bị phá:
  - không trả nguyên kit
  - rơi ra nguyên liệu chế tạo nó như tháo/phá công trình

## Salvage Economy

### Salvage chung

- đồ tháo rã chỉ thu lại `một phần giá trị`
- luôn ít hơn chi phí craft mới

### Theo độ bền

- đồ còn độ bền:
  - lượng thu hồi ổn định theo loại
- đồ đã `0 durability`:
  - thu hồi ít hơn nữa

### Theo nơi thao tác

- ở workstation:
  - nhanh hơn
  - hiệu suất cao hơn
- ngoài hiện trường qua repair kit:
  - chậm hơn
  - hiệu suất kém hơn

### Output Handling

- ưu tiên trả đồ vào túi
- không đủ chỗ thì phần dư rơi ra đất

## Mana Extraction Economy

### Quặng Mana

- nguồn chính nằm từ tầng sâu hơn, nhất là từ `tầng 3+`
- không nên hiếm đến mức chỉ là biểu tượng
- nhưng đủ nguy hiểm để mỗi chuyến lấy mana có trọng lượng

### Chiết Xuất

- quặng mana không đổi thẳng thành mana miễn phí
- phải qua workstation / máy chiết xuất

### Efficiency

- hiệu suất và tốc độ chiết xuất phụ thuộc tier máy

### Quặng Tinh Khiết

- có thể dùng trực tiếp
- nhưng hiệu quả kém
- đem về base chiết xuất thì hiệu quả cao hơn nhiều

### Mana Từ Sinh Vật

- tồn tại
- tùy loài
- nhưng không được thay thế vai trò của khai khoáng

## Gate Fuel And Logistics Sink

### Gate Repair

- sửa gate là một sink milestone lớn
- ăn vật liệu vào từng module
- boss có thể phá module và làm mất một phần vật liệu vừa nhét

### Gate Fuel

- dùng chung họ item với:
  - `pin`
  - `bình`
  - `lõi mana`

### Cost Per Use

- chi phí dùng gate tính theo:
  - khoảng cách
  - tầng
  - lần dùng

### Undercharged Use

- gate thiếu năng lượng vẫn dùng được
- nhưng:
  - rất đắt
  - có tỷ lệ lỗi
  - có thể mất mana vô ích

### Personal Mana Fallback

- khi thiếu năng lượng, gate có thể hút bù từ:
  - cả party đứng gần cổng

### Ý nghĩa kinh tế

- gate không chỉ là unlock
- nó là sink vận hành thật
- chuẩn bị logistics trước chuyến đi giúp:
  - rẻ hơn
  - ổn định hơn
  - ít ăn vào mana cá nhân hơn

## Transition Rules

### Raw Resource -> Crafted Item

Xảy ra khi:
- người chơi có recipe hợp lệ
- có input hợp lệ
- có nơi craft hợp lệ

### Crafted Item -> Repaired State

Xảy ra khi:
- item repairable
- có station hoặc repair kit hợp lệ
- có đủ input repair

### Item -> Salvage Output

Xảy ra khi:
- item thuộc loại tháo được
- người chơi dùng workstation hoặc repair kit phù hợp

### Mana Ore -> Stored Mana

Xảy ra khi:
- người chơi mang quặng mana về base
- chạy qua machine/workstation chiết xuất hợp lệ

### Fuel Item -> Gate Energy

Xảy ra khi:
- người chơi nhét nhiên liệu đúng họ vào gate
- gate nhận charge / energy tương ứng

## Core Flows

### 1. Craft nền đầu game

1. Người chơi nhặt vật liệu nền.
2. Craft tay món cơ bản ngay.
3. Tạo công cụ/utility đủ để đi xa hơn một chút.

### 2. Về base để tối ưu giá trị loot

1. Người chơi mang vật liệu và đồ hỏng về.
2. Dùng workstation để craft đồ cao hơn.
3. Dùng máy sửa để repair rẻ hơn và full bền.
4. Dùng máy chiết xuất để chuyển quặng mana thành mana tích trữ.

### 3. Repair dã chiến

1. Người chơi đặt repair kit tại nơi cho phép xây.
2. Nhét món đồ vào slot xử lý.
3. Hệ thống lấy input từ inventory + kho gần.
4. Chạy tiến trình sửa hoặc tháo rã.
5. Nếu hủy/bị phá thì đồ rơi ra, tiến trình mất.

### 4. Đầu tư workstation

1. Người chơi tích lũy vật liệu.
2. Dựng hoặc nâng tier workstation.
3. Mở khả năng craft mới / nhanh hơn / lớn hơn.
4. Từ tier cao bắt đầu chạm vào vận hành bằng mana.

### 5. Chuẩn bị gate run

1. Người chơi tích lũy vật liệu milestone và fuel.
2. Sửa từng module gate.
3. Nhét fuel vào gate hoặc chuẩn bị mana container.
4. Dùng gate như tuyến đi ổn định, chấp nhận chi phí vận hành theo quãng đi.

## Failure And Recovery

### Failure ở lớp kinh tế chế tạo

- craft nhầm ưu tiên, làm chậm tiến trình
- dồn tài nguyên vào đồ chưa cần
- repair dã chiến quá đắt làm hụt vật tư chuyến đi
- workstation tier cao nhưng không đủ mana vận hành
- đổ fuel vào gate thiếu chuẩn bị rồi bị lỗi và mất năng lượng
- salvage đồ quá sớm làm mất giá trị sử dụng còn lại

### Recovery

- quay về vật liệu nền và build lại từ station rẻ hơn
- dùng salvage để gỡ lại một phần giá trị
- quay về base repair để tiết kiệm chi phí
- đổi hướng đầu tư sang utility/base thay vì nhồi vào đồ combat
- farm vật liệu phụ từ boss refarm nhưng không mong lấy lại milestone

## Edge Cases

### 1. Craft thiếu nguyên liệu

- không commit output
- item không được tạo
- system phải đọc rõ thiếu ở inventory hay thiếu ở kho liên kết

### 2. Craft ở workstation nhưng ngoài phạm vi kho

- chỉ được tính phần inventory cá nhân
- kho ngoài phạm vi không tham gia

### 3. Đồ lớn / đồ mana

- không ra ngay
- phải chấp nhận time cost

### 4. Workstation cấp cao thiếu mana

- tùy loại bàn:
  - có bàn vẫn chạy tay rất chậm
  - có bàn tắt hẳn

### 5. Repair kit bị phá khi đang sửa

- tiến trình hủy
- đồ đang sửa rơi ra đất
- kit không còn như cũ, chỉ trả nguyên liệu công trình nếu bị phá

### 6. Salvage đồ 0 durability

- thu hồi thấp hơn đồ còn độ bền
- không được coi như salvage đồ nguyên

### 7. Artifact có durability

- không nằm trong vòng repair economy
- vỡ là mất luôn

### 8. Gate nhét sai item

- cho nhét
- nhưng không có tác dụng
- làm phát sinh risk lãng phí vật tư nếu người chơi thao tác sai

## Signs Of A Good Crafting Economy

- người chơi hiểu rõ:
  - đồ nào craft tay
  - đồ nào phải về bàn
  - đồ nào đáng sửa
  - đồ nào nên tháo rã
  - lúc nào nên đầu tư machine
- vật liệu nền vẫn còn giá trị về sau
- mana không chỉ là thanh cá nhân mà là resource vận hành thật
- workstation, repair, extraction và gate cùng nối thành một mạng sink/faucet dễ đọc
- người chơi luôn có vài hướng đầu tư cạnh tranh nhau

## Signs Of A Broken Crafting Economy

- mọi tài nguyên chỉ đổ vào một recipe tối ưu duy nhất
- repair rẻ đến mức craft mới vô nghĩa
- repair đắt đến mức không ai muốn sửa
- salvage trả lại quá nhiều khiến loop craft/phá/craft bị exploit
- workstation tier cao chỉ là “số to hơn” mà không đổi mục tiêu đầu tư
- mana tồn tại nhưng không tạo operating cost thật
- gate mở xong mà không còn là sink nào nữa

## Implementation Hooks

- Recipe metadata tối thiểu:
  - `craft_path`
  - `required_inputs`
  - `input_source_rule`
  - `craft_time_class`
  - `unlock_rule`
  - `required_station_tier`
  - `mana_requirement_mode`
- Station metadata tối thiểu:
  - `station_family`
  - `tier`
  - `supported_recipe_classes`
  - `supports_manual_operation`
  - `uses_mana`
  - `refund_rule_on_demolish`
- Repair metadata tối thiểu:
  - `repairable`
  - `repair_tier_required`
  - `repair_input_class`
  - `base_repair_efficiency`
  - `field_repair_efficiency`
- Salvage metadata tối thiểu:
  - `salvageable`
  - `salvage_output_class`
  - `salvage_yield_rule`
  - `broken_item_penalty`
- Mana extraction metadata tối thiểu:
  - `ore_type`
  - `extraction_machine_tier`
  - `yield_efficiency`
  - `process_time`
- Gate fuel metadata tối thiểu:
  - `can_feed_gate`
  - `energy_value`
  - `shared_family_with_player_mana_container`

## Open Design Questions

- Phạm vi kho liên kết thực tế của workstation là bao nhiêu.
- Những nhóm bàn cấp cao nào “vẫn chạy tay chậm” và những nhóm nào “thiếu mana là tắt”.
- Gate có nên có thêm một lớp phí chuẩn bị ngoài fuel trực tiếp hay không.
- Có cho một số công thức craft cao dùng vật liệu thay thế kém hiệu quả hay không.

## Open Balance Variables

- thời gian craft thực tế theo class item
- giá repair dã chiến so với repair base
- tỷ lệ thu hồi salvage theo từng nhóm item
- efficiency từng tier workstation
- efficiency từng tier máy chiết xuất mana
- cost fuel của gate theo khoảng cách / tầng / lần
- mức cạnh tranh tài nguyên giữa:
  - đồ combat
  - utility
  - base
  - mana machine
  - gate logistics
