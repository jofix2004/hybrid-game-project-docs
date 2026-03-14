Project Code: HYBRID
Version: 0.9 (Draft)
Author: null
Date: 14/02/2026

# 12_QUESTIONS_LEVEL_8

Tài liệu này là khung câu hỏi cấp 8, dùng để biến bộ khung game đã có thành đặc tả chi tiết có thể giao việc: mỗi hệ cần biết state gì, chuyển state ra sao, công thức xử lý theo thứ tự nào, chi phí nằm ở đâu, fail như thế nào, và cần test case gì để tránh đoán mò khi implementation.

Cấp này đào sâu vào `rule gameplay` và `đặc tả hành vi`. Nhánh kỹ thuật sâu hơn của `lv7` có thể tiếp tục được soi riêng sau, nhưng ở đây ưu tiên chốt cho rõ game hoạt động thế nào khi người chơi thật sự bấm, mang đồ, chết, quay về, mở cổng, dùng mana và tương tác với thế giới.

## Mục tiêu của cấp độ này

- Chuyển game từ mức `khung định hướng` sang mức `đặc tả có thể làm`.
- Làm rõ rule để design, code, content và QA không hiểu khác nhau về cùng một hệ.
- Tránh tình trạng công thức chưa rõ, state chưa rõ, hoặc edge case bị bỏ trống tới lúc code mới cãi nhau.

## Nguyên tắc dùng tài liệu này

- Mỗi đặc tả phải đọc được như một `contract`: đầu vào gì, xử lý gì, đầu ra gì, giới hạn gì, ngoại lệ gì.
- Ưu tiên mô tả `hành vi nhìn thấy được trong game` trước khi nói tới cách cài đặt bên dưới.
- Nếu chưa chốt số tuyệt đối, vẫn phải chốt được `cấu trúc công thức`, `biến số`, `thứ tự xử lý`, `cap` và `ngưỡng`.
- Mỗi sheet nên đủ rõ để một người mới vào team đọc xong biết mình phải implement hay tune phần nào.

## Tiêu chí cố định cho mọi đặc tả chi tiết

1. Thực thể hay hệ này có những `state` nào.
2. Mỗi state chuyển sang state khác bằng điều kiện gì.
3. Nó nhận đầu vào gì và trả đầu ra gì.
4. Nó có công thức, cap, cooldown, decay hay floor nào.
5. Nó fail ở đâu và recover bằng cách nào.
6. Người chơi nhìn thấy tín hiệu gì để hiểu rule đang diễn ra.
7. Designer sẽ tune nó bằng biến nào.
8. QA phải có test case nào để bắt lỗi sớm.
9. Nếu thiếu đặc tả này, implementation sẽ phải tự đoán ở đoạn nào.

## Mục 1: Chọn bản đồ các sheet đặc tả bắt buộc

### Điều cần mô tả

- Những hệ nào cần có `spec sheet` chi tiết đầu tiên.
- Hệ nào phải chốt state, công thức và edge case trước khi viết sâu.
- Hệ nào có thể để ở mức mô tả ngắn trong giai đoạn đầu.

### Câu hỏi khung

- Những phần nào nếu không có đặc tả rõ thì code sẽ đoán mò nhiều nhất.
- Phần nào chạm trực tiếp tới core loop mỗi phiên.
- Phần nào chạm trực tiếp tới risk/reward, mất mát và tiến trình dài hạn.
- Phần nào có nhiều giao điểm giữa các hệ nên dễ sinh bug hiểu sai.

### Đầu ra mong muốn

- Một danh sách `Detailed Spec Candidates` theo mức ưu tiên.

### Trả lời

- `Phải đặc tả ngay`: player core state, inventory và tải trọng, gathering, tool action, combat resolution, survival drain, mana exposure, crafting/workstation, gate milestone, death và recovery.
- `Nên đặc tả sớm`: boss state, ruins interior interaction, utility expedition, base service flow, loot/drop rules, chi phí vận hành các thiết bị mana.
- `Để sau`: mutation branch sâu, enchant nâng cao, automation chain dài, weather formula chi tiết, class hóa build hay specialization cứng.

## Mục 2: State model và state transition

### Điều cần mô tả

- Mỗi thực thể quan trọng có những state nào.
- Điều kiện vào state và thoát state.
- Những transition nào được phép, những transition nào bị cấm.

### Câu hỏi khung

- Player có những state cốt lõi nào ngoài sống và chết.
- Resource node, gate, boss, workstation có vòng đời state ra sao.
- Có state trung gian nào rất dễ bị bỏ quên nhưng lại ảnh hưởng mạnh tới gameplay.
- Transition nào cần rollback, transition nào đã commit thì không quay lại.

### Đầu ra mong muốn

- Một đoạn `State Model and Transition Rules`.

### Trả lời

Mỗi hệ cốt lõi của game nên có state model riêng và đọc được. `Player` tối thiểu nên có các state gắn trực tiếp với lõi MVP hiện tại: bình thường, đói, kiệt đói, cạn mana, downed và dead. `Resource node` nên có nguyên vẹn, đang khai thác, cạn và trạng thái hồi hoặc không hồi tùy loại. `Gate` nên có chưa phát hiện, đã phát hiện, bị boss canh giữ, đã ổn định và đang hoạt động. `Boss` nên có dormant, aggro, phase theo mốc máu hoặc cơ chế, rồi dead. Điều quan trọng là phải chốt rõ transition nào được phép nhảy thẳng và transition nào không; ví dụ gate không nên nhảy từ `phát hiện` sang `ổn định` nếu chưa qua state `đã xử lý mốc canh giữ`, còn player không nên từ `downed` hay `dead` quay lại trạng thái vận hành mà không đi qua đúng flow cứu dậy hoặc hồi sinh.

### Ghi chú chốt tạm hiện tại

- `Player` hiện được thiết kế quanh 3 thanh chính:
  `Máu`,
  `Thức ăn`,
  `Mana`.
- Chưa đưa vào ở giai đoạn này:
  `nước`,
  `tinh thần`,
  `bệnh tật`,
  các lớp survival nâng cao khác.
- `Thức ăn` đang có 4 ngưỡng:
  `0 = Kiệt đói`,
  `1 -> 30 = Đói`,
  `30 -> 70 = Vừa`,
  `70 -> 100 = No`.
- `Kiệt đói`:
  trừ máu theo thời gian và có thể dẫn tới chết nếu không có đồ ăn cứu lại.
- `Đói`:
  giảm sát thương và đưa tốc độ hồi máu tự nhiên về `0`.
- `No`:
  cho phép hồi máu tự nhiên dần.
- `Máu = 0`:
  `solo` chết ngay,
  `co-op` vào trạng thái `downed` trước.

## Mục 3: Quy tắc xử lý hành động và tương tác

### Điều cần mô tả

- Một action được resolve theo thứ tự nào.
- Điều kiện hợp lệ của action là gì.
- Khi nhiều người hoặc nhiều hệ cùng chạm vào một action, rule ưu tiên ra sao.

### Câu hỏi khung

- Hành động khai thác, đánh, nhặt, craft, đặt đồ, kích hoạt cổng đi qua các bước nào.
- Check hợp lệ nằm trước hay sau animation, trước hay sau tiêu hao chi phí.
- Nếu hai người cùng khai thác hoặc cùng loot một thứ thì rule phân xử là gì.
- Khi action bị hủy giữa chừng, thứ gì mất rồi và thứ gì được hoàn lại.

### Đầu ra mong muốn

- Một đoạn `Action Resolution and Interaction Contract`.

### Trả lời

Mọi action cốt lõi nên đi qua một hợp đồng xử lý chung: `nhận input -> check điều kiện -> khóa mục tiêu nếu cần -> chạy windup hoặc thời gian thực hiện -> resolve kết quả -> tiêu hao chi phí -> phát feedback -> commit state`. Ví dụ `khai thác quặng` phải check tầm với, đúng công cụ, còn chỗ chứa đồ và node còn tài nguyên trước khi cho chạy hit khai thác; `đánh quái` phải chốt rõ hit check, tiêu hao durability, mana hay thời gian hở diễn ra trước hay sau hit; `kích hoạt gate` phải chốt rõ là action giữ nút, action cúng tài nguyên, hay action chỉ mở được khi milestone đã hoàn thành. Nếu hai người cùng tương tác một mục tiêu, đặc tả phải nói rõ là `first lock wins`, `chia reward`, hay `cùng đóng góp vào một progress bar`.

## Mục 4: Công thức, cap và quy tắc scaling

### Điều cần mô tả

- Công thức cốt lõi của các hệ.
- Thứ tự cộng trừ nhân chia hoặc clamp.
- Ngưỡng, cap, floor và điểm bẻ gãy của scaling.

### Câu hỏi khung

- Combat dùng công thức nào ở mức cấu trúc.
- Gathering, utility, mana exposure, hồi phục và tiêu hao được tính ra sao.
- Mỗi công thức có biến nào là `base`, biến nào là `modifier`, biến nào là `cap`.
- Scaling theo tier có đổi cách chơi hay chỉ tăng số.

### Đầu ra mong muốn

- Một đoạn `Formula, Cap and Scaling Rules`.

### Trả lời

Các công thức chính nên được chốt theo cấu trúc trước khi chốt số. Ví dụ `Damage = BaseWeapon + ToolOrRuneBonus + ContextModifier - ArmorOrResistance`, trong đó phải chốt rõ phần nào cộng trước, phần nào clamp sau và có cho âm hay không. `HarvestYield = BaseNodeYield + ToolTierBonus + ContextBonus`, rồi clamp theo minimum floor và node remaining. `ActionCost = BaseUseCost x ToolFactor x ContextFactor`, trong đó context có thể là địa hình, trạng thái item hay loại utility đang dùng. `ManaUse = BaseManaCost + DeviceOrToolBonus + ContinuousDrainModifier`, nhưng phải chốt rõ khi nào trừ theo lần dùng, khi nào trừ theo thời gian và khi nào bị ngắt do cạn mana. Điều quan trọng ở cấp này không phải là chốt con số đẹp, mà là chốt `khung tính` để ai viết data table hay code cũng không hiểu lệch nhau.

### Ghi chú chốt tạm hiện tại

- `Máu` hồi tự nhiên theo tốc độ cố định.
- Chỉ hồi khi:
  người chơi đang ở ngưỡng `No (70 -> 100)` của thanh thức ăn
  và không bị đánh trong vài giây.
- `Dung tích mana` tăng theo:
  `tiến trình chung`
  cộng thêm một phần từ `trang bị / artifact`.

## Mục 5: Chi phí, cooldown và tiêu hao

### Điều cần mô tả

- Mỗi hành động mạnh phải trả giá bằng gì.
- Chi phí nào là ngắn hạn, chi phí nào là dài hạn.
- Cooldown, charge hay vận hành liên tục được áp dụng ở đâu.

### Câu hỏi khung

- Đi sâu, đánh, khai thác, mở gate, vận hành máy mana và hồi phục đều tiêu hao thứ gì.
- Có hành động nào đang quá mạnh vì gần như không có giá.
- Consumable, durability, mana, thời gian setup và chi phí base cạnh tranh với nhau ra sao.
- Nếu một utility mạnh lên, game đã có sink để trả giá cho nó chưa.

### Đầu ra mong muốn

- Một đoạn `Cost, Cooldown and Consumption Rules`.

### Trả lời

Game nên phân biệt rõ `chi phí tức thời` và `chi phí chiến lược`. Đòn đánh, khai thác, chạy thoát và utility nhanh nên ăn vào durability, mana, consumable hoặc khoảng hở thời gian ở mức nhỏ nhưng thường xuyên. Những thứ đổi mạnh nhịp chơi như dựng workstation mới, ổn định gate hay bật thiết bị mana nên có `chi phí đầu tư` rõ ràng và có thể thêm `chi phí vận hành` để economy không bị vỡ. Một chuyến đi xuống sâu cũng nên có `giá vé` riêng: đồ hồi phục, thức ăn, ánh sáng, vật tư utility và rủi ro mất đồ. Cooldown chỉ nên dùng khi cần giữ nhịp hoặc ngăn spam; còn nếu một hành động mạnh đã có chi phí và khoảng hở tự nhiên, không nên thêm cooldown chỉ để “cho cân”.

### Ghi chú chốt tạm hiện tại

- `Mana` không tự hồi.
- `Mana` được nạp bằng:
  `vật phẩm nạp mana`,
  `trạm nạp`,
  `nguồn mana tự nhiên đặc biệt ở tầng sâu`.
- Khi `Mana = 0`:
  không dùng được hành động cần mana
  và các thiết bị hoặc hiệu ứng cần mana đang duy trì sẽ ngắt nếu không có nguồn thay thế.

## Mục 6: Thất bại, chết và hồi phục

### Điều cần mô tả

- Các fail state chính của game.
- Điều gì bị mất ở từng loại thất bại.
- Người chơi quay lại loop bằng con đường nào.

### Câu hỏi khung

- Hết máu, đói nặng, kiệt đói, cạn mana và chết khác nhau ra sao.
- Solo và co-op có khác nhau ở bước downed, revive hay không.
- Sau khi chết, người chơi mất gì, giữ gì, và có đường nhặt lại không.
- Fail state nào là cảnh báo, fail state nào là reset thật.

### Đầu ra mong muốn

- Một đoạn `Failure, Death and Recovery Rules`.

### Trả lời

Game nên có `fail mềm` và `fail nặng` thay vì chỉ một kiểu chết. Với lõi hiện tại, `đói`, `kiệt đói` hay `cạn mana` là các fail mềm hoặc áp lực vận hành trước khi thành fail nặng. `Chết` mới là fail nặng của chuyến đi. Trong co-op, có một nhịp `downed` để đồng đội cứu; trong solo, người chơi chết ngay và đi vào flow hồi sinh hợp lệ theo từng điểm hồi sinh. Khi chết, người chơi nên mất ở cấp `chuyến đi`: item trên hotbar rơi ra đất, item trong túi đi vào `bia mộ`, mất consumable, lỡ nhịp khai thác và phải quay lại recovery. Nhưng căn cứ, unlock nền, gate đã ổn định và năng lực hồi phục cơ bản phải còn để game không rơi vào deadlock.

### Ghi chú chốt tạm hiện tại

- Sau khi chết, mức mất mát phụ thuộc `chế độ game`:
  `Nhẹ`: không rơi gì hoặc chỉ rơi một phần.
  `Vừa`: rơi hết đồ mang theo.
  `Nặng`: rơi đồ và có thể mất thêm một phần tích lũy phụ nếu mode đó bật luật này, nhưng không làm mất điểm chỉ số nền.
- Người chơi có thể hồi lại ở:
  `căn cứ`,
  `điểm hồi sinh đã mở`,
  `công trình hồi sinh`,
  hoặc nhờ `kỹ năng / khả năng hồi sinh của đồng đội`.
- Trong co-op:
  cứu cơ bản tiêu hao `máu` của người đi cứu để đổi lấy lượt hồi sinh cho đồng đội.
- Cứu nâng cao:
  vật phẩm hoặc kỹ năng giúp cứu nhanh hơn hoặc an toàn hơn.
- Khi được cứu dậy:
  mặc định người chơi quay lại với `50% máu`.
- Các chỉ số khác:
  giữ như trước lúc chết hoặc trước lúc vào trạng thái downed.
- Các khác biệt do `kỹ năng / vật phẩm cứu`:
  để cân bằng sâu hơn ở bước sau.
- Khi `downed`:
  người chơi nằm im,
  không di chuyển,
  không làm action.
- Thời gian `downed` mặc định:
  `60 giây`,
  và có thể thay đổi theo `độ khó / chế độ`.
- Khi chết:
  có `recovery marker` rõ ở đúng nơi chết.
- Item trên `hotbar`:
  rơi thẳng xuống đất.
- Item trong túi:
  đi vào `bia mộ` hoạt động gần như một rương,
  và bia mộ biến mất khi bên trong rỗng.
- Ở mode thường:
  ai cũng có thể mở bia mộ.
- Nếu bật `PvP mode`:
  chỉ chủ nhân hoặc đồng đội được mở.
- Hiệu ứng sau khi hồi sinh:
  được reset theo `điểm hồi sinh`.
- `Base respawn`:
  xóa sạch debuff ngắn và đa số debuff thường.
- `Điểm hồi sinh mở`:
  giữ lại nhiều debuff hơn base.
- `Hồi sinh bởi đồng đội / kỹ năng`:
  giữ gần như toàn bộ debuff hiện có.

## Ghi chú chốt tạm thêm: Death và Revive

- Khi được cứu dậy trong co-op:
  mặc định người chơi quay lại với `50% máu`.
- Các chỉ số khác:
  giữ như trước lúc chết hoặc trước lúc vào trạng thái downed.
- Khác biệt do vật phẩm hoặc kỹ năng cứu:
  sẽ cân bằng sâu hơn ở bước sau.

## Mục 7: Hợp đồng giữa các hệ

### Điều cần mô tả

- Hệ nào gọi vào hệ nào.
- Dữ liệu nào được dùng chung giữa các hệ.
- Những rule liên hệ nào phải chốt trước để tránh chồng chéo.

### Câu hỏi khung

- Gathering có đụng inventory, tool durability, mana hỗ trợ và node state theo thứ tự nào.
- Combat có đụng survival, mana, loot, aggro và recovery ở đâu.
- Gate milestone có phụ thuộc boss state, resource cost, mana input và world state ra sao.
- Crafting và base có lấy nguyên liệu từ inventory cá nhân, kho chung hay cả hai.

### Đầu ra mong muốn

- Một đoạn `Cross-system Interaction Contracts`.

### Trả lời

Các hệ cốt lõi nên được nối với nhau bằng hợp đồng rõ, không để chạm nhau theo cảm tính. `Gathering` phải đọc trạng thái node, tool, mana hỗ trợ và chỗ chứa đồ; chỉ khi đủ điều kiện mới commit yield vào inventory hay rơi ra đất. `Combat` không chỉ sửa máu, mà còn có thể gọi vào knockback, status effect, loot trigger và fail state. `Mana` không nên là một thanh độc lập sống riêng; nó phải liên hệ với utility, device, gate và tình trạng cạn năng lượng. `Gate milestone` phải chốt rõ nó đọc boss state, tài nguyên cúng, trạng thái khu vực và quyền kích hoạt từ ai. `Crafting` phải chốt nguồn đầu vào là inventory cá nhân, kho chung hay theo rule kết hợp; nếu không, chỉ riêng chuyện “ai được tiêu đồ ở đâu” cũng đủ gây hiểu lệch giữa design, code và QA.

## Ghi chú chốt tạm thêm: Gathering và Tool

- `Node cơ bản khởi đầu`:
  có thể dùng tay để khai thác, nhưng rất chậm.
- `Các node còn lại`:
  phải dùng đúng tool mới khai thác được.
- `Sai tool`:
  không khai thác được, chỉ vung như một đòn đánh và không ra tài nguyên.
- `Node sau khi khai thác hết`:
  xử lý tùy loại node và có thể mọc lại qua cơ chế sinh sản ngẫu nhiên.
- `Tài nguyên khi khai thác`:
  đa số rơi ra đất,
  chỉ một vài dạng thu hoạch hoặc chiết suất đặc biệt mới vào thẳng inventory.
- `Inventory đầy`:
  tài nguyên vẫn rơi ra đất bình thường.
- `Khai thác node`:
  là hành động nhiều hit, hit cuối mới phá node và rơi loot.
- `Tool tier` ảnh hưởng cả 3:
  mở quyền khai thác node tier cao,
  tăng tốc độ khai thác,
  tăng yield.
- Việc quản lý khai thác nên đi qua `sát thương vật chất`:
  tool cấp cao gây sát thương cao hơn,
  khoáng sản xịn cần nhiều sát thương hơn để phá.
- `Tool khai thác`:
  có thể dùng để chiến đấu,
  nhưng sát thương combat yếu hơn vũ khí chuyên dụng.
- Game hiện không có `stamina`.
- `Mỗi hit khai thác`:
  tốn thời gian và durability.
- Nếu dùng công cụ hỗ trợ bằng mana:
  tốn thêm mana.
- `Durability = 0`:
  tool gãy luôn hoặc biến mất.
- Hướng mong muốn:
  người chơi phải chú ý sửa đồ trước khi hỏng,
  và chi phí sửa nên rẻ hơn tạo mới.

## Ghi chú chốt tạm thêm: Inventory và Equipment

- `Inventory` hiện đi theo hướng:
  `hotbar + túi chính`,
  quản lý bằng `slot`,
  chưa dùng hệ `trọng lượng`.
- `Hotbar`:
  là khu đồ đang cầm hoặc dùng nhanh,
  chứa item, tool, weapon, consumable,
  và có thể đổi trực tiếp không cần mở túi.
- `Túi chính`:
  dùng cho phần lưu trữ chính.
- `Stack rule`:
  tài nguyên và consumable stack theo số riêng từng loại,
  tool, weapon và equipment thì không stack.
- `Auto pickup`:
  item mới ưu tiên vào `stack cũ trên hotbar`,
  rồi `stack cũ trong túi`,
  sau đó tới `ô trống trên hotbar`,
  rồi mới tới `ô trống trong túi`.
- Khi `túi chính` và `hotbar` đều đầy:
  item rơi lại đất.
- Có `equipment slot` riêng cho:
  `giáp`,
  `artifact`.
- `Artifact`:
  có thể vừa cộng chỉ số thụ động, vừa mở hiệu ứng đặc biệt, vừa tăng mana hoặc utility.
- Số ô `artifact` hiện tại:
  khoảng `4 ô`.
- Người chơi:
  tự chọn loadout artifact theo lối chơi.
- `Giáp`:
  có thể giảm sát thương,
  kháng hiệu ứng,
  và tự mang hiệu ứng riêng.
- `Set bonus của giáp`:
  tùy loại, có loại theo set và có loại mạnh theo từng món riêng.
- `Durability của giáp`:
  có hỏng dần và phải sửa,
  nhưng không vỡ.
- Khi giáp `hỏng`:
  món giáp trở thành vô tác dụng cho tới khi sửa.

## Ghi chú chốt tạm thêm: Combat nền

- `Combat` hiện đi theo hướng:
  kết hợp giữa `đọc chiêu`, `giữ vị trí` và `học cách né`.
  Người chơi cần đánh thử để hiểu pattern,
  rồi mới tối ưu cách né và trao đổi đòn.
- Combat nên đủ chiều sâu để tồn tại các thử thách kiểu `no-damage boss`.
- Hành vi tấn công của người chơi:
  chủ yếu dùng `vũ khí cận chiến`,
  có thêm một ít `tầm xa / utility`.
- `Skill active`:
  rất ít,
  thường chỉ 1 hoặc vài kỹ năng,
  và thiên về kỹ năng độc quyền của cây kỹ năng.
- Về di chuyển combat:
  hiện tại chỉ chốt `di chuyển thường`,
  `dash` vẫn đang là phương án cân nhắc chứ chưa khóa.
- Đòn đánh:
  mức độ commit hay khóa di chuyển là `tùy loại vũ khí`.
- Sát thương nhận vào:
  xử lý `tùy loại damage`.
- Tạm thời chỉ có `2 loại damage` chính:
  `vật lý`,
  `hiệu ứng môi trường`.
- `Ma thuật`:
  không là một loại damage riêng,
  mà sẽ quy đổi sang `vật lý`.
- `Hiệu ứng môi trường` hiện được gom theo `hazard`:
  `cháy / nóng`,
  `độc / khí độc`,
  `bẫy / hazard map`.
- `Giáp giảm sát thương vật lý`:
  theo công thức mềm để tránh bất tử sớm.
- `Crit`:
  để sau hoặc không có ở giai đoạn đầu.
- `Stagger`:
  có trong combat.
- `Quái nhỏ`:
  dễ bị stagger hơn.
- `Boss`:
  kháng mạnh hoặc chỉ stagger ở mốc đặc biệt.
- Sau khi người chơi trúng đòn:
  có `iframe rất ngắn` để tránh chết oan do hit chồng quá dày.
- `Block / đỡ đòn`:
  không là khả năng mặc định,
  chỉ có ở một số trang bị hoặc kỹ năng chuyên dụng.
- `Quái thường`:
  gây nguy hiểm bằng nhiều kiểu áp lực cùng lúc,
  chủ yếu là ép vị trí, ép thời gian xử lý và bào tài nguyên của người chơi.
- `Boss`:
  khác quái thường ở chỗ vừa bền hơn,
  vừa có phase,
  vừa có pattern riêng cần học,
  lại thường gắn với milestone hoặc gate.
- Phần thưởng chính sau khi hạ boss:
  `loot hiếm`,
  `mở gate hoặc mở tuyến đi ổn định`,
  `mở công thức hoặc vật liệu đặc biệt`.

## Ghi chú chốt tạm thêm: Crafting và Workstation

- `Crafting`:
  đồ đơn giản có thể craft tay,
  đồ cao hơn cần workstation.
- `Sửa đồ dã chiến`:
  làm được nhưng kém hiệu quả,
  cần `repair kit`.
- `Sửa ở workstation`:
  tốt hơn và rẻ hơn.
- `Thời gian chế tạo`:
  đồ nhỏ ra ngay.
- `Đồ lớn / đồ cao / đồ mana`:
  có thời gian craft.
- Hướng này giúp:
  đỡ rườm đầu game,
  giữ trọng lượng cho đồ lớn,
  và tạo nền cho tự động hóa cùng nguồn đốt mana.
- `Mở công thức` theo cấu trúc nhiều nguồn:
  đồ cơ bản mở khi thấy nguyên liệu hoặc có workstation,
  còn đồ cao mở qua blueprint, research hoặc milestone.
- `Nguồn nguyên liệu khi craft`:
  lấy từ inventory cá nhân
  và từ kho chung trong phạm vi quy định.
- Ví dụ phạm vi hiện tại:
  khoảng `10x10` tính từ bàn chế tạo.
- `Workstation`:
  có nâng cấp tier,
  nhưng cần hạn chế số loại để tránh quá nhiều bàn.
- Mỗi bước nâng cấp workstation nên tạo khác biệt đáng kể về:
  khả năng chế,
  kích cỡ vật cần chế,
  tốc độ chế.
- `Nâng cấp workstation`:
  theo kiểu đập bỏ làm mới.
- Khi đập bỏ workstation:
  hoàn lại một phần vật liệu,
  và lượng hoàn tùy theo công cụ dùng để đập.
- `Mana ở workstation`:
  cấp thấp thì không cần.
- `Workstation cấp cao`:
  dùng mana như nguồn năng lượng tự động.
- Khi không có mana:
  tùy loại bàn,
  một số bàn vẫn chạy tay rất chậm,
  một số bàn mana thì tắt hẳn.

## Ghi chú chốt tạm thêm: Gate Milestone và vận hành cổng

- `Mở gate ổn định` hiện được hiểu là `sửa gate`.
- `Boss` đứng ở khu gate để cản hoặc phá quá trình sửa.
- Ý đồ gameplay:
  nếu muốn yên ổn đứng sửa gate thì phải hạ boss trước.
- Khi `chưa giết boss`:
  người chơi vẫn có thể sửa gate từng phần,
  nhưng boss có thể phá tiến độ.
- Boss phá gate theo kiểu:
  `vỡ từng module`.
- Nếu người chơi vừa nhét tài nguyên vào sửa:
  boss có thể đập làm mất một phần tài nguyên vừa nhét vào.
- Khi gate đã `sửa ổn định`:
  gate mở vĩnh viễn.
- Mỗi lần dùng gate:
  vẫn tốn một ít năng lượng.
- Năng lượng gate ưu tiên lấy từ:
  `network mana`
  hoặc `năng lượng sẵn có của gate`.
- `Mana cá nhân`:
  có thể hỗ trợ bù khi thiếu.
- Nếu dịch chuyển tới hoặc qua một gate đang cạn năng lượng:
  sẽ trừ mạnh hơn vào người chơi.
- Nếu gate đã được nạp sẵn:
  dùng được lâu và ổn định hơn,
  tạo giá trị cho việc chuẩn bị logistics trước.
- `Gate cạn năng lượng`:
  vẫn dùng được nhưng rất đắt,
  có tỷ lệ lỗi,
  và có nguy cơ mất mana vô ích.
- `Lỗi gate`:
  không dịch chuyển,
  nhưng vẫn mất năng lượng.
- Gate được nạp sẵn bằng cách:
  `nhét vật phẩm nhiên liệu`.
- Nhiên liệu gate:
  dùng chung với `pin / bình / lõi mana`.
- Chi phí mỗi lần dùng gate:
  tính theo `khoảng cách / tầng / lần`.

## Ghi chú chốt tạm thêm: Mana cá nhân và nguồn mana

- `Mana cá nhân` ưu tiên dùng cho:
  `tool / trang bị / utility đặc biệt`,
  sau đó tới `kích hoạt skill`,
  và chỉ rất ít khi hỗ trợ máy móc hoặc gate khi thiếu.
- `Mana cho tool / utility`:
  là tùy loại.
- Với `búa, cuốc` và tool dùng theo phát:
  mana bị trừ theo mỗi lần dùng.
- Với utility duy trì như:
  `lọc khí`,
  `làm mát`,
  `tăng tốc`,
  `tăng sức mạnh`,
  mana bị trừ dần theo thời gian.
- `Utility duy trì`:
  hết mana là tắt ngay.
- `Mana cá nhân`:
  là lượng nhỏ, mang tính cơ động, giống `sạc dự phòng`.
- `Network mana` hoặc `kho mana ở base`:
  là nguồn lớn, giống `điện lưới`.
- Hướng chính:
  máy mana ở base nạp cho người chơi,
  chứ mana cá nhân không đáng để nuôi ngược lại cả hệ thống.
- `Nạp mana cá nhân` theo nhiều nguồn nhưng có phân vai rõ:
  nguồn chính là nạp ở base,
  nguồn cứu nguy là bình chứa dự trữ,
  còn nguồn cơ hội tại chỗ là quặng tinh khiết hoặc mana rơi từ sinh vật.
- `Nguồn chính`:
  nạp ở base bằng cách mang quặng mana về chiết xuất thành mana tích trữ.
- `Nguồn cứu nguy`:
  `bình chứa dự trữ`.
- `Nguồn tình huống / cơ hội`:
  `quặng tinh khiết`,
  `mana rơi từ sinh vật`.
- `Chiết xuất mana`:
  cần workstation hoặc máy chiết xuất.
- `Hiệu suất` và `tốc độ chiết xuất`:
  tùy theo cấp độ của máy.
- `Mana từ sinh vật`:
  tùy loài,
  nhưng nhìn chung không được thay thế vai trò của khai khoáng.
- `Quặng tinh khiết`:
  có thể dùng trực tiếp nhưng hiệu quả kém,
  nếu đem về base thì chiết xuất hiệu quả cao hơn nhiều.
- `Bình chứa dự trữ`:
  gồm cả `vật phẩm tiêu hao một lần`
  và `bình có thể sạc lại`.

## Ghi chú chốt tạm thêm: Boss gatekeeper và vòng farm

- `Boss lúc chưa aggro`:
  không chỉ đứng yên một chỗ,
  mà tùy loại có thể canh gate, tuần tra quanh khu hoặc phá gate theo nhịp riêng.
- `Ưu tiên hành vi của boss`:
  `đánh người chơi`
  > `phá gate định kỳ`
  > `đi loanh quanh`.
- `Phá gate định kỳ`:
  sau mỗi lần phá sẽ có cooldown.
- `Aggro của boss`:
  không có một rule cứng cho mọi boss,
  mà tùy hành vi boss từng tầng.
- Hướng thiết kế boss:
  rất đa dạng, từ ngu tới xảo quyệt,
  có thể có boss lừa người chơi,
  và thậm chí có boss thân thiện hoặc NPC bán đồ.
- Với `boss gatekeeper`:
  khi mất aggro thì tùy loại boss,
  có con quay lại gate,
  có con hồi máu, có con không.
- Nếu người chơi rời khỏi `hầm ngục / tầng`:
  boss sẽ reset phase hoặc reset hẳn.
- `Máu boss trong cùng một lần thám hiểm`:
  tùy loại boss.
- `Boss gatekeeper` chết rồi:
  chỉ hồi lại nếu người chơi chưa sửa gate xong.
- Người chơi có thể:
  phá cổng để gọi lại boss và farm tài nguyên.
- Khi phá cổng để gọi lại boss:
  gate chỉ hỏng một phần và sửa lại cho dễ.
- `Boss gọi lại để farm`:
  chỉ rơi một số vật liệu farm,
  không rơi lại milestone.
- `Vật liệu farm từ boss`:
  có hướng dùng khác nhau tùy loại boss.
- Nếu boss thiên chiến đấu:
  ưu tiên rơi vật chiến hoặc vật phục vụ combat.
- Nếu boss là dạng pháp sư hoặc ma thú:
  ưu tiên rơi vật phép, mana hoặc vật liên quan tới utility phép.
- Nếu boss là dạng người máy hoặc vật cổ:
  ưu tiên rơi đồ chế tạo và vật liệu công nghệ hay cấu phần đặc thù.

## Ghi chú chốt tạm thêm: Repair, durability và thu hồi đồ

- `Repair kit`:
  chủ yếu craft ở workstation.
- Ngoài ra:
  có thể mua nếu người chơi nhiều tiền hoặc loot ít.
- `Repair kit` được hiểu là:
  tạo một lần và dùng mãi mãi.
- Mỗi lần sửa bằng repair kit:
  tốn nguyên liệu sửa tùy món đồ.
- Sửa bằng `repair kit`:
  đắt hơn sửa ở máy chuyên dụng tại base.
- Hướng cân bằng đang mở:
  hoặc tốn nhiều nguyên liệu hơn,
  hoặc cùng giá nhưng hồi ít độ bền hơn.
- `Repair kit`:
  sửa được theo nhóm đồ và tier tương ứng,
  đồng thời bản thân repair kit cũng có `cấp độ`.
- `Repair kit cấp thấp`:
  không sửa được đồ cao tier.
- Hiện tại chốt:
  `repair kit có 4 cấp`,
  để scale tốt cho mục tiêu 100 tầng.
- `Máy sửa ở base`:
  cũng có tier,
  và số lượng tier sẽ cân bằng trong cây công nghệ.
- `Máy sửa base`:
  nhanh hơn, rẻ hơn và hồi full độ bền.
- `Tool`:
  khi độ bền về 0 thì gãy luôn hoặc biến mất.
- `Giáp`:
  không vỡ,
  nhưng khi hỏng thì vô tác dụng cho tới khi sửa.
- `Đồ hỏng`:
  vẫn mang được,
  vẫn chiếm slot như bình thường,
  nhưng vô tác dụng.
- `Tháo rã đồ`:
  tùy loại đồ.
- Lượng thu hồi từ tháo rã:
  ở các mức độ bền bình thường thì như nhau,
  luôn ít hơn chi phí chế mới,
  và nếu đồ đã `= 0 độ bền` thì thu hồi còn ít hơn nữa.
- `Rule tổng đã chốt`
  `Tool`: gãy luôn ở 0.
  `Giáp`: không vỡ, nhưng 0 thì vô tác dụng.
  `Đồ hỏng`: vẫn mang được, chiếm slot.
  `Repair kit`: 4 cấp, sửa dã chiến kém hiệu quả.
  `Máy sửa base`: nhanh hơn, rẻ hơn, full bền.

## Bản chốt tạm sau vòng hỏi 1-100

- `Player core`
  Có 3 thanh chính là `Máu`, `Thức ăn`, `Mana`.
  Chưa đưa `nước`, `tinh thần`, `bệnh tật` vào lõi hiện tại.
- `Thức ăn`
  `0 = kiệt đói`: trừ máu theo thời gian.
  `1-30 = đói`: giảm sát thương, không hồi máu tự nhiên.
  `30-70 = vừa`: trạng thái trung tính.
  `70-100 = no`: hồi máu dần nếu không bị đánh trong vài giây.
- `Mana`
  Không tự hồi.
  Chủ yếu dùng cho `tool / trang bị / utility đặc biệt`, sau đó mới tới `skill`.
  Nạp lại chủ yếu ở `base`, cứu nguy bằng `bình chứa`, cơ hội tại chỗ đến từ `quặng tinh khiết` hoặc `mana rơi từ sinh vật`.
- `Death và revive`
  `Solo`: chết ngay khi hết máu.
  `Co-op`: vào trạng thái `downed`.
  `Downed`: nằm im, không hành động, mặc định `60 giây`, có thể scale theo mode.
  Cứu cơ bản dùng `máu của đồng đội`.
  Cứu dậy mặc định với `50% máu`.
- `Gathering`
  Node cơ bản có thể dùng tay nhưng rất chậm.
  Node còn lại phải đúng tool.
  Sai tool chỉ vung như attack và không khai thác được.
  Khai thác là nhiều hit, hit cuối mới vỡ node và rơi loot.
  Đa số loot rơi ra đất.
- `Tool`
  Tool tier ảnh hưởng tới quyền khai thác, tốc độ và yield.
  Phần lớn được cân bằng qua `sát thương vật chất`.
  Tool có thể dùng đánh nhau nhưng yếu hơn vũ khí chuyên dụng.
  Tool mất `time + durability`, và có thể tốn thêm `mana` nếu là bản hỗ trợ bằng mana.
  Khi về `0 durability`, tool gãy luôn hoặc biến mất.
- `Inventory`
  Dùng mô hình `hotbar + túi chính`, theo `slot`, chưa dùng `weight`.
  Nhặt đồ ưu tiên vào `stack cũ trên hotbar`, rồi `stack cũ trong túi`, sau đó tới `ô trống trên hotbar`, rồi mới tới `ô trống trong túi`; full cả hai thì item ở lại đất.
  `Tài nguyên` và `consumable` có stack riêng.
  `Tool / weapon / equipment` không stack.
- `Equipment`
  Có slot riêng cho `giáp` và `artifact`.
  `Artifact` có khoảng `4 ô`, thiên về loadout theo lối chơi.
  `Giáp` có thể giảm sát thương, kháng hiệu ứng và mang hiệu ứng riêng.
  Giáp có thể theo set hoặc theo từng món, tùy loại.
- `Combat`
  Combat kết hợp giữa đọc chiêu, giữ vị trí và học né.
  Người chơi cần đánh thử để hiểu pattern rồi mới tối ưu cách né và trao đổi đòn.
  Chủ yếu dùng `vũ khí cận chiến`, có thêm một ít `tầm xa / utility`.
  `Skill active` rất ít.
  Chưa khóa `dash`, hiện tại lõi vẫn là di chuyển thường.
  Có `stagger`, `iframe ngắn`, và `block` không phải khả năng mặc định.
- `Damage model`
  Hiện có 2 nhóm damage chính:
  `vật lý`
  `hazard môi trường`
  Trong đó hazard tạm gom theo `cháy / nóng`, `độc / khí độc`, `bẫy / map hazard`.
  Ma thuật tạm quy đổi về vật lý.
- `Boss`
  Boss đa dạng mạnh, từ gatekeeper thù địch tới boss thân thiện hoặc NPC đặc biệt.
  Với boss gatekeeper:
  ưu tiên đánh người chơi, sau đó mới phá gate theo nhịp có cooldown.
  Boss có thể phá từng module sửa gate và làm mất một phần tài nguyên vừa nhét vào.
  Boss gọi lại để farm chỉ rơi vật liệu farm, không rơi lại milestone.
- `Gate`
  Gate được mở theo nghĩa `sửa ổn định`.
  Chưa hạ boss vẫn có thể sửa từng phần, nhưng boss có thể phá tiến độ.
  Khi sửa xong, gate mở vĩnh viễn.
  Mỗi lần dùng gate tốn năng lượng theo `khoảng cách / tầng / lần`.
  Gate ưu tiên dùng `network mana` hoặc năng lượng sẵn có của cổng, và khi thiếu có thể hút bù từ cả party đứng gần cổng.
  Gate thiếu năng lượng vẫn dùng được nhưng rất đắt, có tỷ lệ lỗi và có thể mất mana vô ích.
  Lỗi gate hiện chốt là `không dịch chuyển nhưng vẫn mất năng lượng`.
- `Crafting`
  Đồ đơn giản craft tay.
  Đồ cao hơn cần workstation.
  Đồ nhỏ ra ngay.
  Đồ lớn / đồ cao / đồ mana có thời gian craft.
  Công thức mở theo nhiều nguồn:
  đồ cơ bản mở từ `nguyên liệu` hoặc `workstation`,
  đồ cao mở qua `blueprint`, `research`, `milestone`.
- `Workstation`
  Có tier nhưng phải hạn chế số loại.
  Mỗi bước nâng cấp phải tạo nhảy vọt rõ về khả năng chế, kích cỡ vật chế và tốc độ.
  Nâng cấp theo kiểu `đập bỏ làm mới`.
  Đập bỏ chỉ hoàn lại một phần vật liệu, tùy công cụ dùng để đập.
- `Mana infrastructure`
  Workstation cấp thấp không cần mana.
  Workstation cấp cao có loại vẫn chạy tay chậm, có loại thiếu mana là tắt hẳn.
  Mana cá nhân nên được hiểu như `sạc dự phòng`.
  Mana ở base và network mới là `điện lưới`.
- `Repair`
  Có `repair kit` dùng dã chiến, nhưng kém hiệu quả hơn base.
  `Repair kit` có `4 cấp`.
  Kit thấp không sửa được đồ cao tier.
  `Máy sửa ở base` nhanh hơn, rẻ hơn và hồi full độ bền.
- `Salvage`
  Tùy loại đồ.
  Thu hồi luôn ít hơn chế mới.
  Nếu đồ đã về `0 độ bền`, lượng thu hồi còn ít hơn nữa.


## Mục 8: Edge case, xung đột và chống exploit

### Điều cần mô tả

- Những tình huống lạ nhưng chắc chắn sẽ xảy ra.
- Rule xử lý khi hai hệ hoặc hai người cùng chạm một đối tượng.
- Những đường exploit dễ xuất hiện nếu rule quá hở.

### Câu hỏi khung

- Inventory đầy khi nhặt hoặc khai thác thì xử lý ra sao.
- Hai người cùng nhặt một drop, cùng đào một node, cùng mở một gate thì ai thắng.
- Chết đúng lúc qua cổng, chết lúc boss đổi phase, hoặc hủy action giữa chừng thì outcome nào hợp lệ.
- Có cách nào lặp vô hạn để nhân tài nguyên, né chi phí hay bỏ qua milestone không.

### Đầu ra mong muốn

- Một đoạn `Edge Case and Conflict Resolution Rules`.

### Trả lời

Ở cấp này cần viết rõ các edge case dễ gây tranh cãi. Nếu inventory đầy khi khai thác, phần yield dư nên rơi ra đất hay bị mất phải được chốt trước. Nếu hai người cùng tương tác một drop hay node, rule phải nói rõ `first commit wins`, `chia phần`, hay `đóng góp chung`. Nếu gate activation bị hủy giữa chừng, cần chốt rõ là mất toàn bộ nguyên liệu, hoàn một phần hay chỉ mất charge. Nếu người chơi chết đúng lúc đạt milestone, đặc tả phải nói milestone có được giữ không và loot có bị rơi không. Các đường exploit như farm lại reward bằng việc hủy action ở frame cuối, spam bật tắt gate để né chi phí hoặc dùng utility vượt milestone đều nên được nêu tên và khóa bằng rule trước khi code.

## Mục 9: Data schema và mặt phẳng tuning

### Điều cần mô tả

- Những bảng dữ liệu nào cần có.
- Mỗi bảng cần những field lõi nào.
- Designer có thể tune game qua những biến nào mà không phải sửa logic.

### Câu hỏi khung

- Hệ nào nên đi vào data table, hệ nào nên giữ bằng rule cố định.
- Item, node, tool, enemy, boss, gate, workstation, status effect cần field gì.
- Những biến nào cần expose cho balancing.
- Một sheet dữ liệu tối thiểu cần đủ thông tin để ai đọc cũng hiểu object đó làm gì hay chưa.

### Đầu ra mong muốn

- Một đoạn `Data Schema and Tuning Surfaces`.

### Trả lời

Level 8 nên chốt được bộ bảng dữ liệu tối thiểu cho implementation và balance. `Items` cần biết type, stack, slot behavior, use case và sink. `Resource Nodes` cần biết tier, tool requirement, yield, respawn rule, danger context. `Tools and Weapons` cần biết action type, durability, speed, damage hoặc harvest modifier. `Enemies` cần biết role, state set, damage class, loot rule, phase marker nếu có. `Boss Milestones` và `Gates` cần biết điều kiện mở, chi phí, trạng thái, phần thưởng mở ra. `Status Effects` cần biết trigger, duration, tick rule, stack rule và cách giải. Những field này nên đủ để designer tune số và content team hiểu object dùng để làm gì, mà không phải đọc code mới biết hành vi.

## Mục 10: Test case chuẩn và bản đồ ưu tiên implementation

### Điều cần mô tả

- Những đặc tả nào phải viết xong trước khi đội bắt tay làm.
- QA cần những test case chuẩn nào để chạy lặp.
- Đặc tả nào là đủ sâu để giao việc, đặc tả nào còn đang là ý tưởng.

### Câu hỏi khung

- 5 đến 10 test case nào nếu chạy qua được thì hệ cơ bản đã đứng vững.
- Những sheet nào phải khóa trước để tránh code đè lên nhau.
- Sheet nào chỉ cần version 0.5, sheet nào cần version 1.0 ngay.
- Nếu phải cắt nửa sau, phần đặc tả nào vẫn phải còn để game làm được MVP.

### Đầu ra mong muốn

- Một danh sách `Implementation-ready Priority Map`.

### Trả lời

- `Phải khóa trước implementation`
  `Player Core State Sheet`: vì nó ảnh hưởng gần như mọi hệ khác.
  `Inventory and Load Rules`: vì gathering, loot, death và expedition đều chạm vào.
  `Gathering and Node Resolution`: vì đây là hành vi lặp lại rất thường xuyên.
  `Combat and Damage Resolution`: vì combat là nguồn áp lực chính của chiều sâu.
  `Survival and Mana Failure Rules`: vì fail state phải rõ từ đầu.
  `Crafting and Workstation Contract`: vì base là nơi đổi loot thành tiến triển.
  `Gate and Milestone Rules`: vì đây là chỗ nối exploration, boss và progression.

- `Vừa làm vừa làm rõ`
  `Boss Phase Detail`: có thể khóa khung trước, số và phase phụ chỉnh sau.
  `Ruins Interior Interaction`: chốt contract chính trước, puzzle detail bổ sung sau.
  `Mana Device Operating Rules`: chốt input-output trước, tuning chi phí chỉnh tiếp.
  `Status Effects`: chốt stack rule và duration trước, thêm loại effect sau.

- `Để sau`
  `Mutation Branch Detail`
  `Advanced Enchant Layer`
  `Heavy Automation Chain`
  `Weather Formula Deep Dive`

- `Bộ test case chuẩn nên có sớm`
  Người chơi đào node đúng tool, sai tool và với các mức durability khác nhau.
  Inventory đầy khi nhặt loot và khi harvest yield tràn.
  Người chơi chết khi đang mang nhiều loot và thử quay lại recovery.
  Người chơi cạn mana ở khu có quặng mana hoặc khi đang duy trì utility bằng mana.
  Hai người cùng tác động một node hoặc một drop.
  Boss bị hạ và gate chuyển đúng state.
  Crafting thất bại vì thiếu đúng một nguyên liệu.
  Utility hoặc consumable hết giữa chuyến đi.

## Điều kiện hoàn thành cấp 8

- Có một danh sách sheet cốt lõi đủ rõ để giao việc chi tiết.
- Mỗi sheet quan trọng đều có `state`, `transition`, `formula structure`, `cost`, `fail state`, `edge case`, `data field` và `test case`.
- Nhìn ra rõ phần nào đã sẵn sàng cho implementation, phần nào còn ở mức cần thử nghiệm.
- Không còn các chỗ mơ hồ kiểu “đến lúc code rồi tính”, ít nhất với các hệ sống trong core loop.

