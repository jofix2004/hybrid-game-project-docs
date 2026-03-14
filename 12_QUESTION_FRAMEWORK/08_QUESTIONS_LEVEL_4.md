Project Code: HYBRID
Version: 0.8 (Draft)
Author: null
Date: 29/01/2026

# 08_QUESTIONS_LEVEL_4

Tài liệu này là khung câu hỏi cấp 4, dùng để xác định các hệ thống chính của game và vai trò thật sự của từng hệ thống.

## Mục tiêu của cấp độ này

- Tách game thành các hệ thống rõ ràng để có thể thiết kế tiếp mà không bị mơ hồ.
- Xác định hệ thống nào là trục chính, hệ thống nào là hỗ trợ và hệ thống nào chưa cần có.
- Làm rõ quan hệ giữa các hệ thống bằng tiêu chí cố định, không để nội dung các cấp trước kéo lệch đánh giá.

## Nguyên tắc dùng tài liệu này

- Mỗi hệ thống phải được đọc như một bài độc lập, không mặc định đúng chỉ vì các cấp trước đã nói tới nó.
- Có thể tham khảo các cấp trước để lấy ngữ cảnh, nhưng không được dùng chúng như bằng chứng cuối cùng.
- Nếu một hệ thống không vượt qua các tiêu chí cố định bên dưới, phải sửa, hạ ưu tiên hoặc loại bỏ dù trước đó nghe rất hợp lý.

## Tiêu chí cố định cho mọi hệ thống

1. Hệ thống này tồn tại để phục vụ mục tiêu gì.
2. Người chơi chạm vào nó khi nào và thường xuyên tới đâu.
3. Nó nuôi loop nào trong game.
4. Nó thưởng gì và phạt gì.
5. Nó cần đầu vào gì và tạo ra đầu ra gì.
6. Nó phụ thuộc vào hệ thống nào khác.
7. Nó có còn giá trị khi tách khỏi các ý tưởng hấp dẫn xung quanh không.
8. Nếu bỏ hệ thống này đi, game mất gì.

## Mục 1: Chọn danh sách hệ thống ứng viên

### Điều cần mô tả

- Những hệ thống nào đang được xem là bắt buộc.
-> Hệ thống trạng thái sinh tồn, hệ thống thu nhặt/khai khoáng, hệ thống quái/mob, hệ thống chế tạo/cây công nghệ, hệ thống xây dựng, hệ thống mana hoặc năng lượng ma thuật, hệ thống chiều sâu hang mở...
- Những hệ thống nào chỉ là ứng viên.
-> Hệ thống thời gian/thời tiết, hệ thống trồng trọt/chăn nuôi, hệ thống tự động hóa, hệ thống thành tích/nhiệm vụ..
- Những hệ thống nào đang nghe hay nhưng chưa rõ vai trò.
-> Hệ thống pvp, hệ thống chỉ sổ sinh tồn nâng cao(nước, bệnh tật...), hệ thống cây kỹ năng nhân vật, hệ thống thuần hóa sinh vật, ...

### Đầu ra mong muốn

- Một danh sách `System Candidates` chia ba mức ưu tiên.

## Mục 2: Survival System

### Điều cần mô tả

- Survival tồn tại để tạo áp lực gì.
- Người chơi bị buộc phải quan tâm tới survival ở thời điểm nào.
- Nếu bỏ survival đi, loop nào hỏng.

### Câu hỏi khung

- Survival đang tạo ra căng thẳng, nhịp chuẩn bị hay giới hạn phiêu lưu.
-> nhịp chuẩn bị, giới hạn phưu lưu, đi xa được hay không còn tùy và vật tư và trang bị, trạng thái sinh tồn hiện tại
- Áp lực survival đến từ chỉ số, môi trường, vật tư hay cả ba.
-> cả 3
- Survival có tạo ra quyết định thú vị hay chỉ tạo việc lặt vặt.
-> Quyết định thú vị, tránh việc ăn bừa vài quả mọng để no là đủ, hoặc máu lúc nào cũng tự hồi full.
- Survival thưởng cho người chuẩn bị tốt bằng cách nào.
-> No-> sức mạnh không bị phạt, máu duy trong trạng thái đầy, ma lực dư dả để sử dụng, có thể được điểm cộng sức mạnh. Hạn chế hoặc không có các hình phạt về sức mạnh  
- Survival phạt thất bại ra sao để còn đáng sợ nhưng không gây chán.
-> phạt chỉ số sức mạnh, đói thì đánh yếu, cạn ma lực thì không dùng hỗ trợ được, máu thấp thì dễ chế, chết thì rơi đồ(hoặc gục nếu có cơ hội người khác đến cứu)

### Đầu ra mong muốn

- Một đoạn `Vai trò của Survival System` và một kết luận: `trục chính`, `trục phụ` hoặc `chưa cần`.

## Mục 3: Resource and Gathering System

### Điều cần mô tả

- Người chơi lấy tài nguyên bằng cách nào.
-> Thu nhặt/mở rương -> rơi từ sinh vật hoặc boss -> khai thác từ tài nguyên tự nhiên (cây cối, khoáng sản) -> trích xuất hoặc điều chế từ loại tài nguyên khác. Trao đổi với NPC, trồng trọt hoặc nhân giống chỉ nên là nhánh phụ về sau nếu chứng minh được giá trị thật cho loop chính.
- Tài nguyên có vai trò gì ngoài việc làm nguyên liệu craft.
-> Tài sản tích lũy, trao đổi hoặc làm nhiên liệu.
- Thu nhặt có đang nuôi khám phá hay chỉ là grind.
-> Cân bằng giữa cả 2.

### Câu hỏi khung

- Có bao nhiêu kiểu tài nguyên cốt lõi.
-> Thực phẩm, gỗ/đá/quặng, vật phẩm từ thực vật/động vật, đá quý/quặng ma thuật.....
- Người chơi phân biệt tài nguyên giá trị thấp và cao bằng gì.
-> Độ hiếm, giá trị sử dụng và giá thành
- Tài nguyên đến từ môi trường, kẻ địch, tầng sâu hay sự kiện nào.
-> Tất cả, phân bổ theo độ khó/hiếm
- Loop thu nhặt có đủ thay đổi theo khu vực và theo tiến trình không.
-> Có, thay đổ về độ hiếm cũng như độ khó/phức tạp để thu nhặt(ví dụ loại khoáng sản hiếm cần 1 công cụ chuyên dụng để thu thập)
- Nếu giảm một nửa số loại tài nguyên, game còn giữ được lõi không.
-> Không, hoặc khó

### Đầu ra mong muốn

- Một đoạn `Vai trò của Resource System` và danh sách câu hỏi còn mở.

## Mục 4: Crafting and Building System

### Điều cần mô tả

- Crafting và building đang phục vụ sinh tồn, tiện ích hay fantasy làm chủ.
- Người chơi craft vì cần sống sót, cần mở khóa hay cần tối ưu.
- Building là phần thưởng, công cụ hay mục tiêu dài hạn.

### Câu hỏi khung

- Crafting có tạo ra quyết định chọn lựa hay chỉ là bấm đủ nguyên liệu.
-> có
Người chơi phải cân nhắc.
Ví dụ:

dùng sắt để làm vũ khí hay nâng công cụ đào
craft đồ hồi máu hay mang vật liệu để đi sâu hơn
làm món rẻ dùng tạm hay để dành craft món mạnh hơn
- Building có thay đổi cách chơi thật hay chỉ đổi hình thức căn cứ.
->Thay đổi cách chơi thật:
Building tạo tác động gameplay rõ.
Ví dụ:

xây kho tốt hơn giúp mang và quản lý tài nguyên hiệu quả hơn
xây workstation mới mở recipe mới
xây phòng hồi phục giúp chuẩn bị chuyến đi nhanh hơn
xây công trình phòng thủ giúp sống sót tốt hơn khi có nguy cơ tấn công
bố trí căn cứ tốt làm nhịp quay về, hồi, craft, đi tiếp mượt hơn
- Người chơi quay về căn cứ để làm gì cụ thể.
-> Người chơi quay về căn cứ để cất loot, hồi phục, craft đồ mới, mở utility và đổi tài nguyên vừa kiếm được thành nâng cấp base, khả năng đi sâu hơn ở chuyến sau.
- Base có phải là nơi hồi phục, sản xuất, lưu trữ, phòng thủ hay tất cả.
-> tất cả
- Nếu bỏ building mà chỉ giữ crafting, game mất bao nhiêu phần bản sắc.
-> 30->40%

### Đầu ra mong muốn

- Một đoạn `Vai trò của Crafting and Building`.

## Mục 5: Combat System

### Điều cần mô tả

- Combat là trục chính, vật cản hay chất xúc tác cho khám phá.
- Người chơi đánh nhau để lấy gì, tránh gì và vượt gì.
- Combat cần sâu đến mức nào để không lấn át loop khác.

### Câu hỏi khung

- Combat xuất hiện với tần suất nào trong một phiên điển hình.
->Combat không diễn ra liên tục. Nó chủ yếu xuất hiện khi người chơi chạm vùng nguy hiểm, xuống sâu hơn hoặc gặp mốc chặn quan trọng.
- Combat đang kiểm tra điều gì: phản xạ, chuẩn bị, vị trí, phối hợp hay tài nguyên.
->Combat chủ yếu kiểm tra chuẩn bị, vị trí và quản lý tài nguyên; trong co-op thì thêm yếu tố phối hợp. Phản xạ có vai trò nhưng không nên là thứ quyết định tất cả.
- Kẻ địch làm chậm tiến trình, đổi nhịp hay mở ra cơ hội gì.
-> Làm chận tiến trình, khó để không có thể đánh là win, nhưng phải chuẩn bị đánh để lấy tài nguyên cho kẻ địch khác, xây dựng base, nâng trang bị.
- Nếu combat chiếm quá nhiều thời gian, loop nào sẽ chết trước.
-> khám phá và thu nhặt, rồi tới chuẩn bị -> đi sâu -> mang đồ về
- Nếu combat quá nhẹ, cảm giác đi sâu còn đủ trọng lượng không.
-> Không hoặc khó, vì nó cần đủ khó đề điều tiết tiến trình game, tránh đi quá nhanh và nhận về quá nhiều nội dung.

### Đầu ra mong muốn

- Một đoạn `Vai trò của Combat System`.

## Mục 6: Progression and Unlock System

### Điều cần mô tả

- Người chơi mạnh lên bằng những trục nào.
- Điều gì mở khóa khu vực, công cụ hoặc khả năng mới.
- Progression đang thưởng cho thời gian chơi hay cho việc chấp nhận rủi ro.

### Câu hỏi khung

- Progression có bao nhiêu lớp: đồ, căn cứ, utility, tầng sâu, công nghệ.
-> mạnh lên chủ yếu với trục đồ/trang bị, utility, căn cứ và tầng sâu; công nghệ là lớp mở rộng phía sau
- Mỗi bước mở khóa có đổi cách chơi hay chỉ tăng số.
->cả 2
- Người chơi nhìn thấy mục tiêu kế tiếp bằng cách nào.
-> cảm thấy giới hạn của bạn thân hiện tại, hiệu suất kém, sức mạnh chưa đủ, nghèo
- Điều kiện mở khóa đến từ tài nguyên, khám phá, boss, research hay phối hợp.
-> Chủ yếu đến từ tài nguyên và khám phá; research là lớp mở rộng về giữa game. Boss không nên là cổng chặn tuyệt đối, mà là mốc giữ cổng dịch chuyển ổn định giữa các tầng. Người chơi vẫn có thể lách xuống sâu hơn bằng các lối khó và nguy hiểm hơn, nhưng muốn mở đường đi lại bền vững thì vẫn phải vượt qua boss mốc.
- Nếu cắt bớt một nửa số unlock, xương sống progression còn không.
-> Có, vẫn giữ trục chính đồ cơ bản -> đồ tốt hơn -> xuống sâu hơn -> mở utility mới -> vào tầng mới là được

### Đầu ra mong muốn

- Một đoạn `Vai trò của Progression System`.

## Mục 7: Open Cave Depth Structure

### Điều cần mô tả

- Cấu trúc chiều sâu hang mở là một hệ thống riêng hay chỉ là world layout.
- Mỗi tầng sâu đổi điều gì trong luật chơi.
- Tầng sâu có đang thật sự nuôi risk/reward không.

### Câu hỏi khung

- Độ sâu làm thay đổi tài nguyên, kẻ địch, môi trường, visibility hay điều hướng ra sao.
-> quặng mới, quái mới thông minh và trâu hơn, cần nhiều trang bị hỗ trợ hơn (tối hơn, khắc nghiệt hơn), nhiều bẫy hơn, có đồ hiếm; từ tầng 3+ bắt đầu xuất hiện quặng ma thuật và nhu cầu dùng mana như một lớp năng lượng thật
- Người chơi biết mình đã sang một lớp sâu hơn bằng tín hiệu gì.
-> biome khác, màu sắc và ánh sáng khác, loại quái khác, tài nguyên khác và cảm giác môi trường đổi rõ
- Tầng sâu mới mang lại hứa hẹn gì ngoài việc quái mạnh hơn.
-> tài nguyên nhiều và quý hơn, biome mới, công thức chế tạo mới, quặng mana từ tầng 3+ và các mốc cổng dịch chuyển hoặc công trình lớn hơn
- Cấu trúc chiều sâu tạo ra quyết định quay về như thế nào.
-> Càng sâu giá trị kho đồ càng tăng nhưng đồ duy trì sinh tồn càng giảm. Người chơi vẫn có thể lách xuống tầng dưới bằng lối khó hoặc nguy hiểm hơn, nhưng nếu chưa hạ boss giữ cổng dịch chuyển thì việc quay lên, quay lại và khai thác ổn định sẽ cực hơn nhiều. Vì vậy quyết định quay về không chỉ là giữ loot, mà còn là chọn có nên cố chạm mốc boss để mở đường đi bền vững hay chưa.
- Nếu game không còn trục đi sâu, phần nào của game sẽ mất hồn trước tiên.
-> vòng khám phá -> mạo hiểm -> mang loot về -> chuẩn bị để xuống sâu hơn

### Đầu ra mong muốn

- Một đoạn `Vai trò của Open Cave Depth Structure`.

## Mục 8: Multiplayer Support Systems

### Điều cần mô tả

- Những hệ thống nào thật sự cần để co-op hoạt động tốt.
- Co-op đang cần chia vai, cứu nhau, chia đồ hay đồng bộ hành động ở mức nào.
- Phần nào là hệ thống hỗ trợ co-op, phần nào chỉ là hiệu ứng cộng thêm.

### Câu hỏi khung

- Nếu không có revive, ping, chia đồ hoặc đồng bộ tương tác, co-op còn vui không.
-> mất 50% niềm vui, vì nếu chỉ đi cùng nhau để trò chuyện thì hơi chán.
- Co-op đang tạo ra lợi thế về hiệu quả, an toàn hay cảm xúc.
-> cả 3 An toàn>Cảm xúc>Hiệu quả
- Hệ thống nào chỉ nên xuất hiện khi đã chứng minh được giá trị trong loop chính.
->combo skill cầu kỳ, quest riêng cho party, UI trade phức tạp,social feature nhiều lớp
- Hệ thống hỗ trợ co-op nào là bắt buộc cho trải nghiệm chuẩn.
-> chia hoặc đưa đồ cơ bản, downed/revive hoặc cơ chế cứu nhau, thấy được vị trí và trạng thái đồng đội, join/chơi cùng không quá vướng
- Nếu game phải solo tốt trước, hệ thống co-op nào vẫn cần được tách riêng.
-> save/progress của nhiều người, sync mở cửa, mở chest, khai thác tài nguyên, revive/downed state

### Đầu ra mong muốn

- Một đoạn `Vai trò của Multiplayer Support`.

## Mục 9: Kết luận hệ thống

### Điều cần mô tả

- Sau khi soi qua toàn bộ tiêu chí, hệ thống nào là lõi.
- Hệ thống nào quan trọng nhưng phải giữ mỏng.
- Hệ thống nào nên đẩy sang sau để tránh phình scope.

### Đầu ra mong muốn

- Một bảng hoặc danh sách `System Priority Map`.

### Trả lời

- `Bắt buộc`
  `Survival System`: Là trục chính vì nó tạo nhịp chuẩn bị, giới hạn chuyến đi và làm quyết định mang gì, đi bao xa, quay về lúc nào trở nên có trọng lượng.
  `Resource and Gathering System`: Là trục chính vì nó nuôi trực tiếp khám phá, crafting, progression và toàn bộ động lực đi ra ngoài.
  `Crafting System`: Là trục chính vì nó biến tài nguyên mang về thành khả năng sống sót, khả năng đi sâu hơn và mục tiêu rõ cho chuyến sau.
  `Combat System`: Là trục chính nhưng theo vai trò điều tiết. Nó cần đủ sức nặng để bảo vệ risk/reward loop và làm việc đi sâu có giá, nhưng không được nuốt hết phần khám phá.
  `Progression and Unlock System`: Là trục chính vì nó cho người chơi thấy mình đang đi lên theo các nấc rõ ràng, chủ yếu qua đồ, utility và tầng sâu.
  `Open Cave Depth Structure`: Là linh hồn của game vì nó tổ chức phần thưởng, nguy hiểm, tín hiệu khám phá và câu hỏi `tham hay rút`.
  `Mana or Magic System`: Là hệ bắt buộc vì từ các tầng sâu hơn, đặc biệt từ tầng 3+, mana và quặng ma thuật trở thành lớp năng lượng thật của progression, utility và vận hành hệ thống, thay cho logic điện truyền thống.

- `Quan trọng nhưng phải tiết chế`
  `Building System`: Quan trọng vì căn cứ là nơi cất loot, hồi phục, chế đồ và đổi thành quả thành tiến triển thật; nhưng nếu phình quá nhanh sẽ kéo game lệch sang base sim.
  `Multiplayer Support Systems`: Quan trọng vì co-op mất rất nhiều niềm vui nếu thiếu cứu nhau, chia đồ, sync tương tác và thấy được đồng đội; nhưng nên dừng ở bộ tối thiểu phục vụ loop chính trước.
  `Automation, Weather, Farming`: Có thể hữu ích về sau, nhưng chỉ nên giữ mỏng và chỉ phát triển khi chứng minh được rằng chúng làm mạnh hơn loop chuẩn bị -> đi ra ngoài -> mang loot về.

- `Chưa nên đưa vào`
  `PvP System`: Chưa phục vụ loop lõi hiện tại và rất dễ làm lệch trọng tâm khỏi survival co-op theo chiều sâu.
  `Chỉ số sinh tồn nâng cao`: Các lớp như nước, bệnh tật hoặc quá nhiều trạng thái phụ dễ biến survival thành việc vặt nếu đưa vào quá sớm.
  `Cây kỹ năng hoặc class cứng`: Chưa cần ở giai đoạn này vì dễ khóa vai người chơi trước khi loop và hệ thống lõi đủ chắc.
  `Thuần hóa sinh vật hoặc social feature nhiều lớp`: Nghe hấp dẫn nhưng chưa chứng minh được giá trị trực tiếp cho loop chính, rất dễ phình scope.

- `Nguy cơ scope cần canh`
  `Building` có nguy cơ ôm quá nhiều vai trò cùng lúc.
  `Resource System` có nguy cơ phình số loại tài nguyên quá mạnh.
  `Multiplayer Support` có nguy cơ trượt từ hỗ trợ loop sang một nhánh tính năng xã hội riêng.

## Điều kiện để qua cấp 5

- Có danh sách hệ thống chính và vai trò rõ ràng.
- Biết hệ thống nào nuôi loop nào.
- Biết hệ thống nào là lõi, hỗ trợ hay chưa cần.
- Nhìn ra được ít nhất 3 nguy cơ phình hệ thống hoặc lệch vai trò.

