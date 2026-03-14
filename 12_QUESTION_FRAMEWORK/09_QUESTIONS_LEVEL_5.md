Project Code: HYBRID
Version: 0.8 (Draft)
Author: null
Date: 02/02/2026

# 09_QUESTIONS_LEVEL_5

Tài liệu này là khung câu hỏi cấp 5, dùng để xác định game cần những nhóm nội dung nào để nuôi loop trong nhiều giờ chơi mà không bị cạn nhanh.

## Mục tiêu của cấp độ này

- Xác định game cần những loại nội dung gì ở cấp cao: biome, lớp chiều sâu hang mở, kẻ địch, boss, tài nguyên, POI hoặc công trình đặc biệt, room nội thất và sự kiện.
- Làm rõ từng nhóm nội dung phục vụ loop nào và khác nhau ở điểm nào.
- Tránh tình trạng nội dung nhiều nhưng trùng vai trò, hoặc nghe hấp dẫn nhưng không nuôi được gameplay thật.

## Nguyên tắc dùng tài liệu này

- Mỗi nhóm nội dung phải được soi như một bài độc lập, không mặc định đúng chỉ vì các cấp trước đã nói tới nó.
- Có thể tham khảo loop và hệ thống đã chốt, nhưng không dùng chúng để ép phải có một loại content cụ thể.
- Nếu một nhóm nội dung không vượt qua tiêu chí cố định bên dưới, phải gộp, cắt hoặc đẩy về sau.

## Tiêu chí cố định cho mọi nhóm nội dung

1. Nhóm nội dung này tồn tại để phục vụ cảm giác hoặc loop nào.
2. Người chơi gặp nó ở giai đoạn nào của game.
3. Nó khác gì với nhóm nội dung cùng vai trò.
4. Nó tạo ra rủi ro gì và phần thưởng gì.
5. Nó có tín hiệu nhận biết đủ rõ không.
6. Nó mở ra quyết định mới hay chỉ đổi lớp hình ảnh.
7. Nó có đủ biến thể để không cạn quá nhanh không.
8. Nếu bỏ nhóm nội dung này đi, game mất gì.

## Mục 1: Chọn bản đồ nội dung ứng viên

### Điều cần mô tả

- Những nhóm nội dung nào đang được xem là bắt buộc.
- Những nhóm nội dung nào là ứng viên mở rộng.
- Những nhóm nội dung nào nghe hay nhưng chưa rõ vai trò.

### Đầu ra mong muốn

- Một danh sách `Content Candidates` theo mức ưu tiên.

### Trả lời

- `Bắt buộc`: Biome và lớp môi trường hang mở, lớp chiều sâu hang mở, họ tài nguyên, họ kẻ địch, POI hoặc công trình cốt lõi, boss hoặc major encounter theo mốc tiến trình.
- `Mở rộng hợp lý`: Event hiếm, sub-biome, elite variant, room nội thất đặc biệt trong công trình, lore POI, resource pocket đặc thù theo biome.
- `Để sau`: Seasonal content, chuỗi nhiệm vụ dài, biome thiên về trang trí, social space, minigame hoặc content chỉ để kể chuyện mà không nuôi loop chính.
- Bản đồ nội dung này nên được hiểu là khung cấp cao. Chưa cần quyết định số lượng chính xác từng món nhỏ, nhưng phải biết game sống nhờ những họ nội dung nào trước.

## Mục 2: Biome and Environment Content

### Điều cần mô tả

- Game cần bao nhiêu loại biome hoặc lớp môi trường thật sự khác nhau.
- Mỗi biome đổi điều gì trong cảm giác chơi.
- Biome khác nhau ở gameplay hay chỉ khác hình ảnh.

### Câu hỏi khung

- Mỗi biome đổi tài nguyên, điều hướng, tầm nhìn, mối nguy hay nhịp chơi ra sao.
- Người chơi nhận ra biome mới bằng tín hiệu gì.
- Biome mới mang lại hứa hẹn gì ngoài việc đổi màu nền và quái mạnh hơn.
- Biome có tạo ra quyết định chuẩn bị khác đi không.
- Nếu giảm một nửa số biome, game còn đủ đa dạng không.

### Đầu ra mong muốn

- Một đoạn `Vai trò của Biome Content`.

### Trả lời

Game nên có một số biome đủ ít để quản lý scope nhưng đủ khác nhau để mỗi lần đi sâu hoặc đi xa đều tạo cảm giác đổi luật chơi. Một bộ khung mẫu có thể là: `bề mặt an toàn tương đối`, `hang ẩm hoặc nấm`, `vùng tinh thể`, `hồ ngầm hoặc vực tối`, `khu nhiệt hoặc dung nham`, và `vùng mana lõi hoặc vực sâu`. Mỗi biome không chỉ khác màu nền mà phải đổi ít nhất ba thứ: loại tài nguyên đáng săn, loại nguy hiểm chính, và cách chuẩn bị trước khi vào. Ví dụ hang ẩm có thể khiến visibility thấp và tăng nguy cơ độc hoặc nấm, vùng tinh thể có tài nguyên quý nhưng địa hình sắc nhọn và quái phản ứng nhanh hơn, còn vùng nhiệt buộc người chơi mang theo utility chịu nóng hoặc tính toán đường đi kỹ hơn. Nếu phải cắt bớt số biome, game vẫn nên giữ lại ít nhất các nhóm đủ khác nhau về cảm giác chơi: một biome nền dễ học, một biome tối hoặc khó nhìn, một biome tài nguyên giá trị cao nhưng nhiều rủi ro, và một biome sâu mang tính milestone.

## Mục 3: Open Cave Depth Content

### Điều cần mô tả

- Cấu trúc chiều sâu hang mở có đang là nguồn nội dung thật hay chỉ là thang độ khó.
- Mỗi lớp sâu đổi điều gì trong luật chơi.
- Người chơi được hứa hẹn gì khi xuống thêm.

### Câu hỏi khung

- Mỗi lớp sâu của hang mở có thay đổi về tài nguyên, quái, điều hướng, visibility, trap hay tín hiệu môi trường không.
- Tín hiệu nào báo người chơi đã sang một lớp sâu khác.
- Tầng sâu mới mở ra phần thưởng gì ngoài chỉ số cao hơn.
- Cấu trúc chiều sâu tạo ra quyết định `tham hay rút` bằng cách nào.
- Nếu bỏ trục đi sâu, game còn giữ được bản sắc không.

### Đầu ra mong muốn

- Một đoạn `Vai trò của Open Cave Depth Content`.

### Trả lời

Cấu trúc chiều sâu hang mở nên là nguồn nội dung thật, không chỉ là một thang tăng máu quái. Mỗi lớp sâu hơn cần đổi tài nguyên, nhịp điều hướng, chất lượng phần thưởng và giá của việc quay về. Một mẫu hợp lý là tầng đầu dạy người chơi cách sống sót và thu nhặt, tầng giữa mở ra tài nguyên quý hơn nhưng bắt đầu thêm visibility kém, bẫy hoặc đường lui rối hơn, còn từ tầng 3+ bắt đầu xuất hiện quặng mana, công trình đáng chú ý hơn và ở một số mốc chiều sâu mới có guardian hoặc boss giữ cổng dịch chuyển ổn định giữa các tầng. Người chơi vẫn có thể lách xuống sâu hơn bằng giếng sụt, lối phụ hoặc các đường nguy hiểm hơn, nhưng nếu chưa vượt qua boss mốc thì việc đi lên, quay lại và khai thác ổn định tầng đó sẽ cực hơn nhiều. Người chơi phải biết mình vừa sang lớp sâu mới bằng các tín hiệu rõ như ánh sáng khác, vật liệu nền khác, âm thanh khác, quái khác và loot table khác. Giá trị lớn nhất của open cave depth content là tạo lời hứa “bên dưới còn thứ đáng để liều”, đồng thời làm câu hỏi `tham hay rút` ngày càng nặng hơn vì đồ trong túi giá trị hơn, đường lui đắt hơn và cám dỗ chạm tới cổng dịch chuyển ngày càng lớn.

## Mục 4: Resource Family Content

### Điều cần mô tả

- Game cần những họ tài nguyên nào để nuôi loop.
- Mỗi họ tài nguyên phục vụ việc gì.
- Tài nguyên được phân tầng hay phân vai ra sao.

### Câu hỏi khung

- Có bao nhiêu họ tài nguyên cốt lõi là đủ.
- Họ tài nguyên nào là phổ thông, họ nào là chiến lược, họ nào là hiếm.
- Mỗi họ tài nguyên đến từ đâu: môi trường, quái, boss, tầng sâu hay sự kiện.
- Tài nguyên có kéo người chơi đi khám phá thêm không hay chỉ tạo grind.
- Nếu cắt bớt nhiều loại tài nguyên, xương sống content còn không.

### Đầu ra mong muốn

- Một đoạn `Vai trò của Resource Families`.

### Trả lời

Game nên có một số họ tài nguyên rõ vai trò thay vì quá nhiều loại lẻ. Một mẫu khung ổn là: `tài nguyên sinh tồn tiêu hao` như thực phẩm và vật hồi phục, `tài nguyên phổ thông` như gỗ, đá, sợi để xây và chế cơ bản, `tài nguyên tiến trình` như kim loại hoặc quặng đặc biệt để nâng đồ và mở utility, `tài nguyên năng lượng hoặc thành phần đặc thù` như tinh thể mana, bột rune hoặc lõi năng lượng để nuôi mana, utility và máy móc, và `tài nguyên milestone` như lõi cổ, boss drop hoặc vật liệu cực hiếm để mở cổng dịch chuyển, utility lớn hơn hoặc các mốc sâu ổn định hơn. Mỗi họ tài nguyên nên kéo người chơi đi theo một hướng: thứ phổ thông đến từ khu gần và dùng hằng ngày, thứ chiến lược nằm sâu hơn hoặc nguy hiểm hơn, còn thứ hiếm gắn với các mốc khám phá hoặc chạm trán lớn. Nếu một loại tài nguyên chỉ tồn tại để tăng số lượng recipe mà không kéo thêm quyết định hay khám phá, nên gộp hoặc cắt.

## Mục 5: Enemy Family Content

### Điều cần mô tả

- Game cần bao nhiêu họ kẻ địch thật sự khác nhau.
- Mỗi họ kẻ địch kiểm tra điều gì ở người chơi.
- Kẻ địch khác nhau ở hành vi, bối cảnh hay chỉ khác chỉ số.

### Câu hỏi khung

- Mỗi họ kẻ địch đổi nhịp combat hoặc nhịp khám phá ra sao.
- Người chơi nhận ra họ kẻ địch khác bằng tín hiệu gì.
- Kẻ địch mở ra rủi ro hoặc cơ hội loot nào.
- Có họ nào chỉ trùng vai trò với họ khác nhưng khoác skin mới không.
- Nếu cắt một nửa số họ kẻ địch, combat còn đủ sắc không.

### Đầu ra mong muốn

- Một đoạn `Vai trò của Enemy Families`.

### Trả lời

Game không cần quá nhiều họ kẻ địch, nhưng mỗi họ phải đổi cách người chơi đọc tình huống. Một khung mẫu nên gồm: `quái áp lực nhỏ` để làm nhiễu và đuổi người chơi khỏi vùng an toàn, `quái giữ vị trí hoặc tanker` để chặn đường và buộc đổi vị trí, `quái tầm xa hoặc phá nhịp` để ép người chơi quan sát kỹ địa hình, `quái phục kích hoặc săn mồi` để khiến việc đi sâu có cảm giác bị rình rập, `quái gắn biome` với cơ chế riêng theo môi trường, và `elite hoặc guardian` để canh tài nguyên quý, shortcut hoặc mốc tầng sâu. Các họ này nên khác nhau ở hành vi, cách xuất hiện và thứ chúng bảo vệ hoặc đe dọa, không chỉ khác máu và sát thương. Nếu cắt một nửa số họ kẻ địch mà combat vẫn giữ được các vai trò trên, số còn lại đủ dùng; còn nếu nhiều họ hiện tại chỉ là reskin, nên gộp sớm.

## Mục 6: Boss and Major Encounter Content

### Điều cần mô tả

- Game có cần boss hay mốc chạm lớn không.
- Boss đang phục vụ progression, cảm xúc hay kiểm tra kỹ năng gì.
- Major encounter khác combat thường ở đâu.

### Câu hỏi khung

- Boss xuất hiện theo tầng sâu, theo biome hay theo milestone nào.
- Boss mở khóa gì ngoài loot hiếm.
- Encounter lớn có tạo ra ký ức và cao trào thật không.
- Nếu bỏ boss, phần progression nào sẽ yếu đi.
- Có cần nhiều boss khác nhau hay chỉ cần ít nhưng thật rõ vai trò.

### Đầu ra mong muốn

- Một đoạn `Vai trò của Boss Content`.

### Trả lời

Boss hoặc major encounter nên là các mốc hiếm nhưng nhớ lâu, dùng để khóa milestone chứ không phải rải đều như quái mạnh bình thường. Một hướng mẫu là ở một số vùng sâu chính hoặc tại các mốc dịch chuyển quan trọng mới có boss hoặc guardian encounter đủ khác nhau về cách chuẩn bị và cách đọc trận. Boss nên kiểm tra chuẩn bị, quản lý tài nguyên và vị trí trước khi kiểm tra phản xạ thuần, vì như vậy sẽ đúng chất survival hơn. Giá trị của boss không chỉ nằm ở loot hiếm mà còn ở việc mở cổng dịch chuyển ổn định giữa các tầng, giúp hành trình đi lên và quay lại khai thác về sau bền vững hơn. Người chơi vẫn có thể lách xuống tầng dưới bằng các lối phụ nguy hiểm hơn khi chưa hạ boss, nhưng nếu muốn biến một mốc sâu thành tuyến đi lại có thể khai thác lâu dài thì boss vẫn là cửa ải lớn cần vượt qua. Tốt hơn là có ít boss nhưng mỗi boss gắn với một thay đổi thật trong game, thay vì nhiều boss chỉ khác skin và số.

## Mục 7: POI, Structure and Interior Room Content

### Điều cần mô tả

- Trong một chuyến đi ở hang mở, người chơi có thể gặp những loại điểm nội dung nào.
- POI hoặc công trình đặc biệt khác gì với biome mở xung quanh.
- Room type bên trong công trình khác gì với không gian hang mở.

### Câu hỏi khung

- Có những loại POI hoặc công trình nào là cốt lõi trong hang mở.
- Mỗi loại POI hoặc công trình khiến người chơi làm khác đi như thế nào.
- Khi vào bên trong công trình, room type nào là đủ để tạo nhịp khám phá, loot, bẫy, mê cung đơn giản hoặc boss.
- Nội dung ngẫu nhiên ở hang mở khác gì với nội dung cố định trong công trình.
- Nếu bỏ POI hoặc công trình đặc biệt, chuyến đi có trở nên quá phẳng và thiếu mục tiêu không.

### Đầu ra mong muốn

- Một đoạn `Vai trò của POI, Structure and Interior Room Content`.

### Trả lời

Với cấu trúc game này, phần lớn chuyến đi nên diễn ra trong không gian hang mở, nơi người chơi gặp biome, tài nguyên, sinh vật, khoáng sản và các mối nguy tự nhiên giống kiểu DST caves hơn là đi từ phòng này sang phòng khác. Vì vậy, `room type` không nên được hiểu là cấu trúc của toàn bộ hang, mà chỉ là lớp nội dung bên trong các công trình hoặc khu ruins xuất hiện ngẫu nhiên trong hang. Ở lớp giữa, game nên có các `POI hoặc công trình` đủ khác nhau để làm mục tiêu khám phá, ví dụ ruins cổ, altar, mỏ bị bỏ hoang, ổ quái lớn, cổng dịch chuyển tầng hoặc khu canh giữ loot quý. Khi người chơi bước vào một công trình như ruins, lúc đó mới cần `room type` nội thất như phòng loot, phòng bẫy, đoạn mê cung đơn giản, phòng giao tranh, phòng khóa hoặc phòng boss. Cách tổ chức này giúp hang mở vẫn giữ cảm giác thám hiểm tự do, còn công trình đặc biệt đóng vai trò các “nút nội dung đậm” nơi nhịp chơi được nén lại, phần thưởng tăng lên và có thể chứa vật phẩm hiếm, boss hoặc thử thách đặc biệt.

## Mục 8: Content Variety and Reuse

### Điều cần mô tả

- Game đang tạo đa dạng bằng số lượng nội dung mới hay bằng tổ hợp thông minh.
- Nội dung nào cần handmade, nội dung nào có thể tái tổ hợp.
- Độ đa dạng tối thiểu để loop không cạn nhanh là bao nhiêu.

### Câu hỏi khung

- Loại nội dung nào cần độc nhất, loại nào chấp nhận reuse.
- Reuse đang giữ chất lượng hay làm nội dung loãng đi.
- Có tổ hợp nào giúp nhân độ đa dạng mà không phình scope quá mạnh.
- Dấu hiệu nào cho thấy content đang cạn nhanh hơn tốc độ progression.
- Nếu phải cắt scope, cắt ở đâu thì ít đau nhất.

### Đầu ra mong muốn

- Một đoạn `Content Variety Strategy`.

### Trả lời

Game nên tạo đa dạng chủ yếu bằng tổ hợp thông minh giữa biome hang mở, enemy family, resource placement, POI hoặc công trình đặc biệt và event, thay vì cố biến toàn bộ thế giới thành mạng lưới room liên tục. Những thứ cần handmade rõ ràng thường là biome chủ chốt, boss, ruins hoặc POI ký ức và một số interior room đặc trưng theo mốc sâu. Những thứ có thể tái tổ hợp là vị trí công trình, phân bố tài nguyên, tổ hợp quái, modifier môi trường, layout interior đơn giản và event ngắn. Chiến lược đúng là giữ hang mở làm nền khám phá chính, còn công trình đặc biệt là nơi nén content đậm hơn. Nếu phải cắt scope, nên cắt biến thể trang trí, skin lặp, POI phụ và room nội thất phụ trước; không nên cắt các content family đang giữ vai trò gameplay riêng. Dấu hiệu content cạn nhanh là người chơi đoán được gần hết loại POI tiếp theo, ruins nào cũng giống nhau, loot không còn tạo quyết định mới, và biome mới chỉ cho cảm giác “khoác áo khác”.

## Mục 9: Kết luận nội dung

### Điều cần mô tả

- Nhóm nội dung nào là lõi bắt buộc để game còn đúng chất.
- Nhóm nội dung nào nên có nhưng phải giữ mỏng.
- Nhóm nội dung nào nên để sau để tránh nổ scope.

### Đầu ra mong muốn

- Một bảng hoặc danh sách `Content Priority Map`.

### Trả lời

- `Bắt buộc`
  `Biome and Environment Content`: Cần có vì đây là lớp thay đổi cảm giác chơi, chuẩn bị và tín hiệu khám phá rõ nhất.
  `Open Cave Depth Content`: Cần có vì đây là trục tổ chức phần thưởng, rủi ro và tiến trình chính của game.
  `Resource Family Content`: Cần có vì nó nuôi trực tiếp gathering, crafting, progression và lý do đi ra ngoài.
  `Enemy Family Content`: Cần có vì nó tạo nhịp áp lực, chặn đường và làm các khu vực khác nhau có tính cách riêng.
  `POI, Structure and Interior Room Content`: Cần có vì nó tạo các nút nội dung đậm trong hang mở, đổi nhịp chuyến đi và là nơi đặt loot hiếm, bẫy, mê cung đơn giản hoặc boss.
  `Boss and Major Encounter Content`: Cần có ở mức milestone vì nó tạo cao trào và giữ các cổng dịch chuyển hoặc mốc đi lại ổn định giữa các tầng.

- `Quan trọng nhưng phải tiết chế`
  `Sub-biome và event hiếm`: Hữu ích để tăng bất ngờ, nhưng dễ phình nếu làm trước khi các họ nội dung lõi đủ chắc.
  `Elite variant và special modifier`: Hữu ích để tăng đa dạng mà không cần làm quái mới hoàn toàn, nhưng nên dùng để bổ sung chứ không che thiếu hụt ở enemy family gốc.
  `Lore POI và room nội thất thưởng đặc biệt`: Có giá trị giữ ký ức cho chuyến đi, nhưng nên đến sau khi các công trình lõi và interior room cơ bản đã rõ vai trò.

- `Để sau`
  `Seasonal content`: Không cần để chứng minh loop chính.
  `Biome thiên về trang trí`: Không nên làm sớm nếu chưa mang khác biệt gameplay thật.
  `Chuỗi event dài hoặc narrative chain`: Dễ tiêu tốn content production nhưng chưa chắc nuôi loop lõi.
  `Nội dung social hoặc side activity riêng`: Chưa nên xuất hiện trước khi khung content phiêu lưu đã đủ mạnh.

- `Nguy cơ content cần canh`
  Biome chỉ khác hình ảnh mà không đổi gameplay.
  Tài nguyên quá nhiều loại nhưng không thêm quyết định.
  Quái và room nhiều biến thể ngoài da nhưng trùng vai trò thật.

## Điều kiện để qua cấp 6

- Có bản đồ nhóm nội dung cấp cao đủ nuôi loop trong nhiều giờ.
- Biết nhóm nội dung nào là lõi, hỗ trợ hay để sau.
- Biết mỗi nhóm nội dung đang phục vụ loop nào.
- Nhìn ra được ít nhất 3 nguy cơ cạn content hoặc phình content.

