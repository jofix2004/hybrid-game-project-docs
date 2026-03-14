Project Code: HYBRID
Version: 0.9 (Draft)
Author: null
Date: 06/02/2026

# 10_QUESTIONS_LEVEL_6

Tài liệu này là khung câu hỏi cấp 6, dùng để xác định tiến trình dài hạn và kinh tế của game: người chơi tiến lên bằng cách nào, phải trả giá gì để tiến lên, và vì sao họ vẫn muốn chơi thêm nhiều giờ nữa.

## Mục tiêu của cấp độ này

- Làm rõ các trục tiến trình thật sự của game: đồ, căn cứ, utility, mana, chiều sâu, tuyến đi lại ổn định.
- Làm rõ kinh tế gameplay: tài nguyên chảy vào từ đâu, bị tiêu ra ở đâu, và thứ gì giữ cho economy không bị lạm phát quá sớm.
- Tránh tình trạng progression chỉ là tăng số, hoặc economy chỉ là farm thêm nguyên liệu mà không tạo quyết định.

## Nguyên tắc dùng tài liệu này

- Mỗi trục tiến trình hoặc lớp kinh tế phải được soi như một bài độc lập, không mặc định đúng chỉ vì các cấp trước đã nói tới nó.
- Có thể tham khảo loop, hệ thống và content đã chốt để lấy ngữ cảnh, nhưng không dùng chúng như bằng chứng cuối cùng.
- Nếu một trục progression không tạo được mục tiêu kế tiếp rõ ràng, hoặc một nhánh economy không tạo được quyết định đáng giá, phải gộp, cắt hoặc đẩy về sau.

## Tiêu chí cố định cho mọi trục tiến trình và kinh tế

1. Trục này tồn tại để thưởng cho hành vi gì của người chơi.
2. Người chơi chạm vào nó ở giai đoạn nào và lặp lại tới mức nào.
3. Nó ăn những đầu vào gì: thời gian, rủi ro, tài nguyên, boss, research hay phối hợp.
4. Nó tạo ra đầu ra gì: đồ mới, utility mới, tuyến đi mới, tầng sâu ổn định hơn hay chỉ số cao hơn.
5. Nó tạo ra quyết định gì đáng cân nhắc.
6. Nó thay đổi ra sao giữa đầu game, giữa game và giai đoạn sâu hơn.
7. Nếu cắt bớt một nửa số mốc mở khóa, xương sống của nó còn không.
8. Nó có nguy cơ gây lạm phát, snowball hoặc deadlock ở đâu.

## Mục 1: Chọn bản đồ trục tiến trình và kinh tế ứng viên

### Điều cần mô tả

- Những trục tiến trình nào đang được xem là bắt buộc.
- Những lớp economy nào là lõi của game.
- Những nhánh nào nghe hấp dẫn nhưng chưa chắc cần có sớm.

### Câu hỏi khung

- Người chơi mạnh lên chủ yếu qua đồ, utility, căn cứ, mana, chiều sâu hay tuyến đi lại ổn định.
- Tài nguyên được giữ như chiến lợi phẩm, nguyên liệu, nhiên liệu, chi phí dịch chuyển hay tất cả.
- Economy có xoay quanh tiêu hao chuyến đi, nâng cấp dài hạn hay cả hai.
- Nếu phải bỏ bớt vài nhánh progression, nhánh nào bỏ trước mà game ít mất hồn nhất.

### Đầu ra mong muốn

- Một danh sách `Progression and Economy Candidates` theo mức ưu tiên.

### Trả lời

- `Bắt buộc`: tiến trình đồ và công cụ, utility thám hiểm, căn cứ và workstation, mana như lớp năng lượng, chiều sâu hang mở, các mốc cổng dịch chuyển ổn định giữa tầng.
- `Quan trọng nhưng phải tiết chế`: nâng cấp tiện nghi căn cứ, economy tiêu hao chuyến đi, vài mốc research hoặc unlock qua nghiên cứu, chi phí vận hành các thiết bị mana.
- `Để sau`: kinh tế mua bán NPC dày, nhiều loại tiền tệ riêng, cây level nhân vật lớn, nhánh specialization cứng hoặc market xã hội.

## Mục 2: Cấu trúc giai đoạn tiến trình

### Điều cần mô tả

- Game có thể chia thành những chặng tiến trình nào.
- Mỗi chặng đổi mục tiêu chính của người chơi ra sao.
- Khi nào game thật sự bước sang “giữa game”.

### Câu hỏi khung

- Đầu game người chơi đang cố ổn định điều gì đầu tiên.
- Giữa game mở ra khi người chơi có công cụ tốt hơn, có căn cứ tốt hơn hay chạm tới mana.
- Cuối giai đoạn hiện tại của MVP nằm ở đâu: chạm tầng sâu, mở cổng ổn định, hay vận hành được hệ mana đầu tiên.
- Mỗi chặng có tín hiệu rõ để người chơi biết mình đã bước sang nấc mới không.

### Đầu ra mong muốn

- Một đoạn `Progression Stages` mô tả các chặng chính.

### Trả lời

Game nên chia thành 4 chặng rõ. `Chặng 1` là sống sót tay trắng: học thu nhặt, craft món cơ bản, dựng căn cứ tạm và chạm vào lớp hang nông. `Chặng 2` là ổn định: nâng công cụ, có nhịp mang loot về đều hơn, mở workstation và utility giúp đi xa hơn mà chưa cần đụng mạnh vào mana. `Chặng 3` bắt đầu khi người chơi đi tới các tầng 3+ và chạm quặng ma thuật; từ đây mana không còn là ý tưởng nền mà thành tài nguyên và năng lượng thật, mở utility, máy móc và chuẩn bị cho các mốc boss giữ cổng. `Chặng 4` là khai thác sâu ổn định hơn: người chơi không chỉ lách xuống được, mà bắt đầu mở các cổng dịch chuyển, thiết lập tuyến đi lại bền vững và biến chiều sâu thành nguồn tiến trình lặp lại lâu dài.

## Mục 3: Điều kiện mở khóa và cách game chỉ mục tiêu kế tiếp

### Điều cần mô tả

- Người chơi mở thứ mới bằng hành vi nào.
- Game cho họ thấy mục tiêu kế tiếp bằng cách nào.
- Boss, research và khám phá đóng vai trò ra sao trong unlock flow.

### Câu hỏi khung

- Unlock chủ yếu đến từ tài nguyên, khám phá, boss, research hay phối hợp.
- Người chơi nhìn thấy “mình còn thiếu gì” qua recipe, workstation, cổng tầng, công trình hay trải nghiệm thất bại.
- Boss có là cổng chặn bắt buộc, hay là mốc giúp tuyến đi ổn định hơn.
- Nếu bỏ một nửa số unlock phụ, trục mở khóa chính còn đọc được không.

### Đầu ra mong muốn

- Một đoạn `Unlock Logic and Signposting`.

### Trả lời

Unlock chính nên đến từ tài nguyên mang về và việc thật sự đi sâu khám phá. Người chơi nên nhìn thấy mục tiêu kế tiếp qua recipe còn khóa, workstation chưa dựng được, utility đang thiếu cho biome tiếp theo, hoặc cổng dịch chuyển ở tầng sâu mà mình biết là chưa thể khai thác ổn định. Boss không nên là cổng chặn tuyệt đối cho toàn bộ tiến trình; người chơi vẫn có thể lách xuống sâu hơn qua lối phụ nguy hiểm hơn, nhưng nếu muốn biến một mốc thành tuyến đi lại bền vững thì phải hạ boss giữ cổng. Research nên là lớp định hướng và gom tri thức, giúp những thứ đã nhặt được trở thành unlock có tổ chức hơn, chứ không thay thế hoàn toàn khám phá thật.

## Mục 4: Economy Faucets

### Điều cần mô tả

- Tài nguyên và giá trị đi vào economy từ đâu.
- Nguồn nào an toàn, nguồn nào rủi ro.
- Nguồn nào lặp lại được lâu dài và nguồn nào nên hiếm.

### Câu hỏi khung

- Người chơi lấy tài nguyên phổ thông, chiến lược, mana và milestone từ đâu.
- Nguồn nào ở gần căn cứ, nguồn nào buộc phải xuống sâu.
- Boss, POI, biome và quái đóng vai trò gì trong dòng chảy tài nguyên.
- Nếu một nguồn quá an toàn và quá giàu, economy có vỡ không.

### Đầu ra mong muốn

- Một đoạn `Economy Faucets`.

### Trả lời

Economy nên nhận đầu vào theo nhiều mức rủi ro. Tài nguyên sống còn và vật liệu cơ bản phải có nguồn lặp lại ở khu gần để người chơi luôn có đường phục hồi. Tài nguyên tiến trình như kim loại tốt hơn, vật liệu utility và loot công trình cần nằm sâu hơn hoặc ở các POI đáng để liều. Quặng mana nên là lớp faucet đặc biệt từ tầng 3+ trở đi: không quá hiếm tới mức chỉ là vật trưng bày, nhưng đủ nguy hiểm để mỗi chuyến lấy mana đều có trọng lượng. Boss drop, lõi cổ và vật liệu milestone không nên trở thành nguồn farm thường ngày; giá trị của chúng nằm ở chỗ mở mốc ổn định, mở utility lớn hoặc mở tuyến đi lại bền vững hơn.

## Mục 5: Economy Sinks và chi phí duy trì

### Điều cần mô tả

- Tài nguyên bị tiêu ra ở đâu.
- Chi phí nào là ngắn hạn, chi phí nào là dài hạn.
- Sink nào giữ cho economy có trọng lượng mà không tạo cảm giác hút máu vô lý.

### Câu hỏi khung

- Người chơi tiêu tài nguyên cho consumable, sửa đồ, base, utility, mana device hay dịch chuyển.
- Mỗi chuyến đi có “giá vé” rõ không.
- Cổng dịch chuyển hoặc utility mạnh có cần chi phí xây và chi phí vận hành không.
- Nếu sink quá yếu, economy có lạm phát không. Nếu sink quá nặng, người chơi có sợ đầu tư không.

### Đầu ra mong muốn

- Một đoạn `Economy Sinks`.

### Trả lời

Economy của game nên có ba lớp sink chính. `Sink ngắn hạn` là chi phí cho mỗi chuyến đi: thức ăn, đồ hồi phục, đuốc hoặc utility, sửa công cụ và vật tư dự phòng. `Sink dài hạn` là các nâng cấp căn cứ, workstation, thiết bị utility và hạ tầng để đi sâu ổn hơn. `Sink vận hành` nên xuất hiện rõ hơn từ lúc có mana, ví dụ một số máy hoặc cổng dịch chuyển cần chi phí xây ban đầu lớn và có chi phí kích hoạt hay nạp năng lượng khi dùng. Cách này giúp economy không bị vỡ quá sớm, đồng thời giữ cho mỗi lần đầu tư lớn đều là quyết định đáng cân nhắc chứ không chỉ là việc đủ nguyên liệu thì bấm xây.

## Mục 6: Resource Tiers và quy tắc chuyển đổi giá trị

### Điều cần mô tả

- Game có những tier tài nguyên nào.
- Mỗi tier dùng cho việc gì.
- Tài nguyên có thể đổi chéo hay nâng cấp lẫn nhau tới đâu.

### Câu hỏi khung

- Tier cơ bản, tier chiến lược, tier mana và tier milestone khác nhau ở đâu.
- Tài nguyên tier thấp còn giữ giá trị ở giữa game và sâu game không.
- Có công thức nào chuyển tài nguyên phổ thông thành tài nguyên hiếm không.
- Nếu cho đổi chéo quá dễ, tài nguyên hiếm còn đáng giá không.

### Đầu ra mong muốn

- Một đoạn `Resource Tier Structure`.

### Trả lời

Một cấu trúc tạm ổn là: `Tier 0` cho sinh tồn và vật liệu nền như thức ăn, gỗ, đá, sợi; `Tier 1` cho công cụ và căn cứ cơ bản; `Tier 2` cho kim loại tốt hơn và utility để đi sâu; `Tier 3` cho quặng mana, tinh thể năng lượng và các thành phần nuôi thiết bị ma thuật; `Tier 4` cho boss drop, lõi cổ hoặc vật liệu cực hiếm dùng cho mốc lớn. Tài nguyên tier thấp không nên mất giá hoàn toàn ở giữa game, vì chúng vẫn phải nuôi consumable, sửa chữa, base và các công thức trung gian. Việc đổi chéo nên có nhưng không quá thoải mái: người chơi có thể tinh luyện hoặc kết hợp nhiều nguyên liệu phổ thông để hỗ trợ một phần cho đồ cao hơn, nhưng không nên farm an toàn ở vùng nông rồi đổi thẳng sang mọi thứ quý hiếm.

## Mục 7: Điểm đầu tư và build variety

### Điều cần mô tả

- Người chơi có thể dồn tài nguyên vào đâu.
- Các hướng đầu tư khác nhau đổi cách chơi thật hay chỉ đổi chỉ số.
- Game có cho nhiều “kiểu mạnh lên” mà không khóa class quá sớm không.

### Câu hỏi khung

- Tài nguyên hiếm nên ưu tiên cho vũ khí, công cụ, utility, căn cứ hay mana infrastructure.
- Người chơi có thể mạnh lên theo hướng an toàn, hiệu quả, cơ động hay khai thác không.
- Các hướng đầu tư có cạnh tranh tài nguyên với nhau đủ để tạo quyết định không.
- Nếu mọi người đều luôn craft cùng một thứ theo một thứ tự, build variety có đang giả không.

### Đầu ra mong muốn

- Một đoạn `Investment Variety`.

### Trả lời

Build variety của game nên đến từ việc người chơi ưu tiên đầu tư vào đâu trước, không phải từ class bị khóa cứng quá sớm. Cùng một lượng tài nguyên hiếm, người chơi có thể chọn nâng vũ khí để xử lý mối nguy tốt hơn, nâng công cụ để lấy tài nguyên nhanh hơn, dựng utility giúp chuyến đi an toàn hơn, hoặc đầu tư vào hạ tầng mana để mở kiểu giải quyết mới. Điều quan trọng là các hướng này phải cạnh tranh tài nguyên thật với nhau; nếu mọi người luôn craft đúng cùng một thứ theo cùng một thứ tự, progression chỉ còn là checklist. Hướng đúng là để người chơi thấy mình đang chọn “mạnh lên theo cách nào trước”, trong khi lõi game vẫn là survival, đi sâu và mang thành quả về.

## Mục 8: Thất bại, phục hồi và chống deadlock

### Điều cần mô tả

- Thất bại làm người chơi mất gì trong economy.
- Họ có đường phục hồi nào sau một cú ngã lớn.
- Game chống vòng xoáy thua liên tiếp bằng cách nào.

### Câu hỏi khung

- Người chơi rơi đồ, mất tài nguyên, mất chi phí chuyến đi hay mất cả mốc tiến trình.
- Sau thất bại, họ còn nguồn nào để gượng dậy: căn cứ, recipe nền, tài nguyên gần, utility cũ.
- Có cơ chế nào khiến càng thua càng khó quay lại không.
- Nếu phục hồi quá dễ, rủi ro có mất trọng lượng không.

### Đầu ra mong muốn

- Một đoạn `Failure Recovery Economy`.

### Trả lời

Thất bại nên làm người chơi mất đau ở cấp chuyến đi, không phải mất sạch khả năng chơi tiếp. Mất hợp lý nhất là rơi đồ mang theo, tiêu tan vật tư expedition, bỏ lỡ một nhịp đẩy sâu hoặc phải tốn thêm tài nguyên để quay lại thu hồi. Nhưng căn cứ, recipe nền, nguồn farm gần và vài utility cơ bản phải còn để người chơi có đường gượng dậy. Nếu đã có cổng dịch chuyển hay mốc ổn định mở trước đó, chúng nên giữ giá trị thật sau thất bại và trở thành phần thưởng dài hạn giúp recovery bớt tuyệt vọng. Game nên tránh vòng xoáy “thua một lần là nghèo tới mức không thể đi tiếp”, nhưng cũng tránh hồi lại quá nhanh làm mọi quyết định mạo hiểm trở nên rẻ.

## Mục 9: Nhịp giữ người chơi lâu dài và chống lạm phát

### Điều cần mô tả

- Vì sao người chơi vẫn muốn chơi thêm 10 giờ nữa.
- Dấu hiệu nào cho thấy progression đang bị lạm phát hoặc cạn mục tiêu.
- Tier cũ, khu cũ và đồ cũ có còn vai trò không.

### Câu hỏi khung

- Người chơi luôn thấy mục tiêu kế tiếp bằng cách nào.
- Tài nguyên, đồ và unlock cũ còn giữ giá trị ở giữa game không.
- Có nguy cơ power creep khiến tầng cũ hoặc quặng cũ vô nghĩa không.
- Economy và progression có đang mở rộng đều giữa chiến đấu, utility, căn cứ và chiều sâu không.

### Đầu ra mong muốn

- Một đoạn `Long-term Retention and Anti-inflation`.

### Trả lời

Người chơi nên còn lý do chơi thêm nhiều giờ vì luôn có một nấc kế tiếp đủ cụ thể: tầng sâu hơn để thử, cổng dịch chuyển ổn định chưa mở, utility lớn chưa dựng, hoặc hướng đầu tư chưa dám ưu tiên. Progression không nên tăng theo kiểu mỗi tier mới xóa sạch giá trị của tier cũ; tài nguyên nền, khu nông và công cụ cũ vẫn phải còn vai trò trong hồi phục, vận hành base và chuẩn bị chuyến đi. Dấu hiệu xấu cần tránh là power creep quá nhanh: quặng cũ thành rác, biome cũ không ai muốn quay lại, mọi unlock mới chỉ cộng số và boss cũ mất sạch ý nghĩa. Hướng đúng là mỗi nấc mới vừa mạnh hơn, vừa mở ra quyết định mới và làm mạng lưới mục tiêu của game dày lên.

## Mục 10: Kết luận tiến trình và kinh tế

### Điều cần mô tả

- Trục progression nào là lõi bắt buộc.
- Lớp economy nào phải có để game có trọng lượng.
- Nhánh nào nên để sau để tránh phình scope.

### Đầu ra mong muốn

- Một danh sách `Progression and Economy Priority Map`.

### Trả lời

- `Bắt buộc`
  `Gear and Tool Progression`: Cần có vì đây là cách người chơi cảm nhận trực tiếp mình mạnh lên và đi sâu ổn hơn.
  `Utility Progression`: Cần có vì game sống bằng việc chuẩn bị cho chuyến đi, không chỉ bằng tăng sát thương.
  `Base and Workstation Progression`: Cần có vì căn cứ là nơi đổi loot thành khả năng đi tiếp.
  `Open Cave Depth Progression`: Cần có vì chiều sâu là trục tổ chức rủi ro, phần thưởng và lời hứa dài hạn.
  `Mana Economy`: Cần có từ các tầng 3+ vì mana là nền năng lượng thật của utility, máy móc và các mốc sâu hơn.
  `Expedition Economy`: Cần có để mỗi chuyến đi có giá vé, có đánh đổi và có hậu quả.
  `Stable Gate Milestones`: Cần có vì boss và cổng dịch chuyển là cách biến “đi được” thành “khai thác được lâu dài”.

- `Quan trọng nhưng phải tiết chế`
  `Research Layer`: Hữu ích để gom tri thức và định hướng unlock, nhưng không nên nặng hơn khám phá thật.
  `Operating Costs for Mana Devices`: Hữu ích để tránh lạm phát, nhưng nếu quá nặng sẽ làm người chơi sợ đầu tư.
  `Investment Variety`: Nên có để tạo lựa chọn, nhưng chưa nên phình thành class tree lớn.

- `Để sau`
  `NPC Trading Economy`: Dễ phình scope và làm lệch trọng tâm khỏi khám phá - mang về.
  `Character Level Tree`: Chưa cần nếu đồ, utility, depth và mana đã đủ dày.
  `Multiple Currencies`: Nghe có vẻ giàu hệ thống nhưng dễ làm economy khó đọc.
  `Heavy Automation Economy`: Chỉ nên mở rộng khi loop sinh tồn và đi sâu đã đủ chắc.

- `Nguy cơ cần canh`
  Progression chỉ tăng số mà không đổi cách chơi.
  Boss hoặc gate milestone xuất hiện quá dày làm content cost tăng mạnh.
  Tài nguyên tier thấp mất giá quá sớm.
  Mana trở thành nhánh sức mạnh tách riêng, lấn át survival và utility.

## Điều kiện để qua cấp 7

- Có bản đồ các trục tiến trình và economy đủ rõ để giải thích vì sao người chơi còn muốn chơi thêm nhiều giờ.
- Biết cái gì là faucet, cái gì là sink, và chúng đang giữ risk/reward ra sao.
- Biết boss, mana, chiều sâu và căn cứ gặp nhau ở đâu trong progression.
- Nhìn ra ít nhất 3 nguy cơ lạm phát, snowball hoặc deadlock.

