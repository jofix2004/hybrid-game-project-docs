Project Code: HYBRID
Version: 0.9 (Draft)
Author: null
Date: 15/03/2026

# Nghiên cứu Tín hiệu Thị giác và ứng dụng thiết kế tutorial game

## MỞ ĐẦU

### 1. Lý do chọn đề tài

Trong bối cảnh phát triển game hiện nay, tutorial không còn có thể được hiểu đơn thuần như một phần “chỉ dẫn cho người mới”, mà cần được xem như một cấu trúc tổ chức việc học cơ chế. Khi độ phức tạp của game gia tăng, đặc biệt ở các thể loại có nhiều lớp hành vi như survival, dungeon exploration, combat, quản lý tài nguyên và phối hợp co-op, khó khăn của người chơi không chỉ nằm ở thao tác điều khiển, mà còn nằm ở khả năng nhận ra điều gì quan trọng, hiểu điều đó có nghĩa gì trong ngữ cảnh hiện tại, rồi chuyển phần hiểu biết đó thành hành động đúng.

Song song với đó, tín hiệu thị giác ngày càng giữ vai trò nổi bật trong việc truyền đạt thông tin gameplay. Người chơi không tiếp cận cơ chế chỉ bằng văn bản hoặc lời nhắc trực tiếp; họ còn tiếp cận cơ chế thông qua việc quan sát thế giới game: đâu là vật thể có thể tương tác, đâu là mối nguy đang hình thành, đâu là lối đi hợp lệ, đâu là phản hồi cho biết hành động vừa rồi là đúng hay sai. Nói cách khác, thị giác không chỉ là lớp biểu diễn của thế giới game, mà còn là một kênh tổ chức thông tin và định hướng hành vi.

Tuy nhiên, trong thực tiễn thiết kế, tutorial và tín hiệu thị giác thường vẫn bị xử lý như hai lớp tách biệt. Tutorial thường được phát triển ở tầng logic trình tự, còn tín hiệu thị giác bị đặt ở tầng trình bày, polish hoặc readability bề mặt. Sự tách rời này dẫn tới một hệ quả đáng chú ý: người chơi có thể được “hướng dẫn” về mặt nội dung nhưng vẫn không nhìn ra tín hiệu cần chú ý, hoặc nhìn thấy tín hiệu nhưng không hiểu vì sao nó có ý nghĩa trong chuỗi hành động đang được học. Chính khoảng cách đó cho thấy nhu cầu cần có một mô hình lý thuyết đủ rõ để mô tả quan hệ cấu trúc giữa cấu hình tín hiệu thị giác và kiến trúc tutorial.

Đề tài này được lựa chọn trên cơ sở nhận diện khoảng trống nói trên. Thay vì coi tín hiệu thị giác là yếu tố minh họa hoặc hỗ trợ phụ, nghiên cứu hướng tới việc xác lập nó như một đơn vị mã hóa thông tin có chức năng trong quá trình học cơ chế. Từ đó, đề tài đề xuất một mô hình tích hợp giữa cấu hình tín hiệu thị giác và tổ chức tutorial, nhằm trả lời câu hỏi: bằng cách nào các quyết định thị giác có thể tham gia trực tiếp vào quá trình người chơi nhận diện, diễn giải và thực thi cơ chế.

Việc lựa chọn bối cảnh game `2D survival dungeon` cho nghiên cứu không nhằm thu hẹp giá trị của mô hình vào riêng một thể loại, mà nhằm xây dựng một trường hợp ứng dụng có mật độ tín hiệu và quyết định hành vi đủ cao để kiểm chứng giả thuyết nghiên cứu. Trong dạng game này, người chơi phải liên tục đọc không gian, xác định lối đi, phân biệt tài nguyên với nguy hiểm, hiểu telegraph của địch, quyết định khi nào nên tiến sâu và khi nào nên rút lui. Chính vì vậy, nó cung cấp một môi trường phù hợp để khảo sát mối quan hệ giữa tổ chức tín hiệu thị giác và hiệu quả tiếp thu cơ chế.

### 2. Tình hình nghiên cứu liên quan đến đề tài

Tình hình nghiên cứu liên quan đến đề tài có thể quy về ba cụm lớn.

Cụm thứ nhất là các nghiên cứu và tài liệu thiết kế về `tutorial`, `onboarding` và `sequencing` trong game. Nhóm này tập trung vào trình tự giới thiệu cơ chế, điều tiết độ phức tạp, kiểm soát nhịp độ tiếp thu, và tổ chức điều kiện thử - sai cho người chơi mới. Trong hướng này, tutorial thường được xem như một tiến trình dần dần đưa người chơi từ chỗ phụ thuộc vào hỗ trợ sang trạng thái tự chủ. Những vấn đề như quá tải chỉ dẫn, dồn quá nhiều cơ chế vào giai đoạn mở đầu, hoặc rút hỗ trợ quá sớm đã được mô tả tương đối rõ. Tuy nhiên, phần lớn các phân tích loại này thường dừng ở tầng tổ chức trình tự và phạm vi can thiệp của tutorial, hơn là đi sâu vào phương thức mã hóa thông tin bằng tín hiệu giác quan.

Cụm thứ hai là các nghiên cứu về `visual hierarchy`, `readability`, `affordance signaling`, `telegraphing` và thiết kế khả năng đọc hiểu trong không gian tương tác. Ở đây, mối quan tâm chính là làm thế nào để người chơi phân biệt được yếu tố quan trọng với nền, đọc được nguy hiểm trước khi nó xảy ra, nhận ra vật thể có thể tương tác, hoặc giải mã đúng phản hồi sau hành động. Nhóm nghiên cứu này rất mạnh trong việc phân tích cấu trúc thị giác của màn hình chơi, nhưng trong nhiều trường hợp, tín hiệu thị giác được xem như một vấn đề của clarity hoặc fairness, chứ chưa được đặt trong tiến trình hình thành tri thức cơ chế theo thời gian.

Cụm thứ ba là các cơ sở từ khoa học nhận thức và tâm lý học tri giác, đặc biệt liên quan tới chú ý chọn lọc, tương phản, cạnh tranh kích thích, phân biệt hình - nền, và các hiện tượng như inattentional blindness. Đây là nhóm tri thức cung cấp nền tảng để giải thích vì sao cùng một lượng thông tin, người chơi có thể nhìn thấy hoặc bỏ lỡ một tín hiệu tùy vào tổ chức của màn hình, trạng thái chú ý và tải nhận thức. Tuy nhiên, các tri thức này thường được sử dụng như cơ sở giải thích chung, chứ chưa được nối thành một mô hình thao tác trực tiếp cho tutorial trong game.

Từ ba cụm trên có thể nhận ra một khoảng trống nghiên cứu rõ ràng. Nghiên cứu về tutorial mạnh ở câu hỏi “giới thiệu cơ chế theo trình tự nào”, nghiên cứu về tín hiệu thị giác mạnh ở câu hỏi “thông tin nên được làm nổi như thế nào”, còn nghiên cứu tri giác mạnh ở câu hỏi “vì sao con người nhận ra hay bỏ sót tín hiệu”. Điều còn thiếu là một khung tích hợp đủ chặt để trả lời câu hỏi trung tâm của đề tài: bằng cách nào cấu hình tín hiệu thị giác có thể trở thành một phần trực tiếp của kiến trúc tutorial, thay vì chỉ là lớp hỗ trợ cho phần hướng dẫn đã được quyết định ở nơi khác.

Khoảng trống này biểu hiện rất rõ trong thực tiễn thiết kế. Chẳng hạn, một tutorial có thể yêu cầu người chơi né một đòn đánh, nhưng nếu telegraph của đòn đó không vượt qua được nhiễu thị giác hoặc không tách đủ khỏi nền, thì thất bại xảy ra không hoàn toàn vì người chơi “chưa học”, mà vì cấu trúc chú ý cần thiết cho việc học chưa được thiết kế đúng. Ở chiều ngược lại, một game có thể có tín hiệu rất rõ cho vật thể tương tác, nhưng nếu chúng xuất hiện dày đặc và không được gắn vào trình tự học có kiểm soát, người chơi vẫn có thể thử tương tác một cách ngẫu nhiên mà không hình thành được tri thức cơ chế ổn định.

Trên cơ sở nhận diện khoảng trống đó, đề tài hướng tới bốn nhiệm vụ có tính chất lý thuyết và ứng dụng: xác lập định nghĩa vận hành cho `Tín hiệu Thị giác`, xây dựng `taxonomy ba chiều`, mô hình hóa quan hệ giữa cue và tutorial thông qua `Visual-Integrated Tutorial Model (VITM)`, và kiểm chứng mô hình bằng một prototype game có đối chứng. Như vậy, đóng góp của nghiên cứu không nằm ở việc lặp lại các nguyên lý tri giác quen thuộc, mà ở việc tái tổ chức chúng thành một hệ khái niệm và một mô hình thao tác được cho thiết kế tutorial game.

### 3. Mục đích, nhiệm vụ nghiên cứu

Mục đích chung của đề tài là xây dựng một mô hình lý thuyết và ứng dụng nhằm tích hợp `tín hiệu thị giác` vào `kiến trúc tutorial`, từ đó giúp quá trình tiếp thu cơ chế trong game diễn ra hiệu quả, nhất quán và đo được.

Để đạt mục đích đó, đề tài đặt ra các nhiệm vụ nghiên cứu chính:

1. Xác lập cơ sở lý luận cho việc xem `Tín hiệu Thị giác` như một đơn vị mã hóa thông tin có chức năng trong thiết kế game.
2. Xây dựng hệ phân loại tín hiệu thị giác dựa trên ba chiều: `tồn tại`, `chức năng`, `thời gian`.
3. Làm rõ tutorial như một kiến trúc tổ chức học tập, gồm các bước nhận diện, diễn giải và thực thi.
4. Đề xuất mô hình `Visual-Integrated Tutorial Model (VITM)` để nối tutorial với cấu hình tín hiệu thị giác.
5. Ứng dụng mô hình vào bối cảnh game `2D survival dungeon` đang phát triển như một trường hợp thử nghiệm.
6. Đề xuất thiết kế thực nghiệm đối chứng để đánh giá hiệu lực của mô hình.

### 4. Đối tượng và phạm vi nghiên cứu

Đối tượng nghiên cứu của đề tài là `mối quan hệ giữa tín hiệu thị giác và thiết kế tutorial trong game`.

Phạm vi nghiên cứu được giới hạn như sau:

- Về lĩnh vực: tập trung trong `game design`, không mở rộng sang UX tổng quát ngoài game.
- Về nội dung: tập trung vào tín hiệu thị giác có ảnh hưởng trực tiếp tới quá trình nhận diện, diễn giải và thực thi cơ chế; không đi sâu vào yếu tố trang trí thuần thẩm mỹ.
- Về ứng dụng: sử dụng một game `2D survival dungeon` làm bối cảnh thử nghiệm, nhưng mô hình không bị giới hạn lý thuyết chỉ trong thể loại này.
- Về kiểm chứng: đề tài đề xuất và tổ chức kiểm chứng thông qua prototype và thực nghiệm có đối chứng; chưa tiến hành nghiên cứu sinh lý học tri giác mới mà kế thừa các nguyên lý đã được thừa nhận trong khoa học nhận thức và tâm lý học tri giác.

### 5. Phương pháp nghiên cứu

Đề tài sử dụng kết hợp các phương pháp sau:

- `Phương pháp phân tích - tổng hợp tài liệu`: dùng để tổng hợp các nghiên cứu và lý thuyết liên quan tới tutorial, readability, visual hierarchy, affordance, telegraphing và tri giác thị giác.
- `Phương pháp hệ thống hóa khái niệm`: dùng để xây dựng định nghĩa vận hành và taxonomy cho tín hiệu thị giác.
- `Phương pháp mô hình hóa`: dùng để đề xuất mô hình `VITM` và làm rõ các tầng cấu trúc của nó.
- `Phương pháp thiết kế ứng dụng`: dùng để đưa mô hình vào một game cụ thể dưới dạng prototype.
- `Phương pháp thực nghiệm đối chứng`: dùng để so sánh giữa các phiên bản tutorial khác nhau nhằm đánh giá vai trò của cấu hình thị giác.
- `Phương pháp quan sát hành vi và phân tích chỉ số`: dùng để đo thời gian tiếp thu, độ chính xác thực thi, tần suất lỗi và khả năng chuyển giao tri thức cơ chế.

### 6. Đóng góp mới của đề tài

Đóng góp mới của đề tài có thể xác định ở ba cấp:

1. `Cấp khái niệm`:
   - Chuẩn hóa cách hiểu `Tín hiệu Thị giác` như một đơn vị mã hóa thông tin trong game.

2. `Cấp mô hình`:
   - Xây dựng `taxonomy ba chiều` cho tín hiệu thị giác.
   - Đề xuất mô hình `Visual-Integrated Tutorial Model (VITM)` để tích hợp visual cue với tutorial.

3. `Cấp ứng dụng`:
   - Chuyển mô hình lý thuyết thành kế hoạch thiết kế và kiểm chứng trong một game 2D survival dungeon.
   - Chỉ ra cách mô hình có thể giúp giảm lệ thuộc vào text tutorial, tăng readability, tăng khả năng tiếp thu cơ chế và chuẩn hóa visual language cho sản phẩm game thực tế.

### 7. Ý nghĩa lý luận và thực tiễn

Về lý luận, đề tài góp phần nối lại hai mảng thường bị tách rời trong nghiên cứu và thực hành thiết kế game: `tutorial` và `tín hiệu thị giác`. Nó giúp xây dựng một cách nhìn mang tính cấu trúc hơn, trong đó visual cue không còn bị xem là lớp trang trí hay phụ trợ, mà trở thành một phần của kiến trúc học tập trong game.

Về thực tiễn, đề tài cung cấp:

- một khung thiết kế cue có thể dùng lại
- một mô hình tutorial tích hợp thị giác
- một quy trình kiểm chứng bằng prototype
- một nền tảng để cải thiện onboarding, readability, telegraphing và chuyển giao cơ chế trong game thật

Đặc biệt, với game hiện tại, đề tài còn có ý nghĩa trực tiếp ở mặt sản phẩm: nó giúp biến một phần nghiên cứu thành công cụ nâng chất lượng thiết kế game, thay vì chỉ dừng ở bình diện học thuật.

### 8. Kết cấu đề tài

Ngoài phần Mở đầu, Kết luận và tài liệu tham khảo, nội dung chính của đề tài gồm 3 chương:

- `Chương 1: Cơ sở lý luận và khái niệm chung`
- `Chương 2: Ứng dụng nghiên cứu và thiết kế`
- `Chương 3: Thiết kế game`

Ba chương này đi theo logic:

`xác lập nền lý thuyết -> chuyển thành mô hình ứng dụng -> triển khai thành thiết kế prototype`

---

## CHƯƠNG 1: CƠ SỞ LÝ LUẬN VÀ KHÁI NIỆM CHUNG

### 1.1. Cách tiếp cận lý luận của đề tài

Đề tài này được xây dựng trên một cách tiếp cận liên ngành, trong đó thiết kế game được xem là giao điểm của ba bình diện: thiết kế tương tác, tổ chức học tập và tri giác thị giác. Sự lựa chọn cách tiếp cận này xuất phát từ chính bản chất của vấn đề nghiên cứu. Nếu chỉ đứng từ phía mỹ thuật, tín hiệu thị giác sẽ dễ bị giản lược thành câu chuyện về hình ảnh “đẹp” hay “dễ nhìn”. Nếu chỉ đứng từ phía tutorial, vấn đề lại dễ bị giản lược thành trình tự hướng dẫn và lượng thông tin cần truyền đạt. Trong khi đó, khó khăn thực tế của người chơi nằm ở chỗ họ phải nhìn thấy, hiểu và hành động trong cùng một dòng trải nghiệm. Vì vậy, nghiên cứu cần một cấu trúc lý luận đủ rộng để giữ được đồng thời cả ba mặt này.

Về phương diện game studies và game design, đề tài kế thừa quan điểm cho rằng tri thức cơ chế trong game hình thành chủ yếu thông qua hành vi chơi, chứ không chỉ qua việc tiếp nhận lời giải thích. Một cơ chế chỉ thực sự được học khi người chơi có khả năng nhận ra điều kiện kích hoạt, dự đoán kết quả hành động và lặp lại hành động đó với mức ổn định nhất định. Điều này khiến tutorial trong game khác với truyền đạt thông tin thuần văn bản: tutorial phải tổ chức tình huống, chứ không chỉ cung cấp nội dung.

Về phương diện khoa học nhận thức, đề tài kế thừa các cơ sở liên quan tới chú ý, giới hạn xử lý thông tin, phân biệt hình - nền, cạnh tranh kích thích và cơ chế giải đoán tín hiệu trong môi trường nhiều yếu tố đồng thời. Những cơ sở này quan trọng vì chúng cho phép giải thích tutorial thất bại không chỉ như một lỗi nội dung, mà còn như một lỗi trong tổ chức chú ý và điều kiện tri giác.

Về phương diện thiết kế tutorial, đề tài tiếp nhận tinh thần của onboarding design nhưng không dừng lại ở việc xác định “dạy cái gì trước, dạy cái gì sau”. Điểm mở rộng của nghiên cứu là xem việc cấu hình tín hiệu thị giác cũng là một phần của tổ chức sư phạm trong game. Nói cách khác, sequencing và cue configuration không phải hai quyết định song song, mà là hai mặt của cùng một kiến trúc học tập.

Từ lập trường đó, `Cơ sở lý luận và khái niệm chung` của đề tài được tổ chức thành ba lớp:

- lớp khái niệm về `Tín hiệu Thị giác`
- lớp khái niệm về `tutorial như kiến trúc học tập`
- lớp mô hình hóa mối quan hệ giữa hai cấu phần trên

Ba lớp này tạo nền cho việc hình thành `Visual-Integrated Tutorial Model (VITM)` ở các phần sau. Điểm quan trọng là mô hình không được xây dựng như một tập mẹo thiết kế, mà như một khung liên kết giữa logic học tập, tổ chức tín hiệu và phản ứng của người chơi.

### 1.2. Tín hiệu thị giác trong thiết kế game

Trong môi trường game, người chơi luôn phải “đọc” thế giới để hành động. Họ đọc lối đi, đọc vật thể tương tác, đọc ý định của địch, đọc mức độ an toàn của khu vực, và đọc cả phản hồi sau khi mình tác động vào hệ thống. Vì vậy, về bản chất, gameplay không chỉ là vấn đề cơ chế ẩn sau hệ thống, mà còn là vấn đề cơ chế ấy được làm hiện ra như thế nào trong không gian cảm nhận.

Từ góc độ này, `Tín hiệu Thị giác` không thể bị giản lược thành “thứ gì đó nổi bật hơn nền”. Một yếu tố hình ảnh chỉ thực sự trở thành tín hiệu khi nó đồng thời thỏa mãn ba điều kiện: có chủ đích thiết kế, mang thông tin chức năng, và tác động được tới tiến trình người chơi nhận diện hoặc diễn giải tình huống. Điều đó có nghĩa là một ngọn đuốc lung linh trong hang có thể chỉ là yếu tố khí quyển, nhưng cũng có thể trở thành tín hiệu định hướng nếu luôn được đặt gần lối đi an toàn; một resource node sáng màu có thể là trang trí, nhưng cũng có thể là tín hiệu mời gọi tương tác nếu độ sáng ấy được giữ nhất quán như một quy ước xuyên suốt hệ thống.

Điểm quan trọng của khái niệm này nằm ở mối quan hệ giữa `độ nổi bật` và `ý nghĩa`. Độ nổi bật chỉ tạo điều kiện để tín hiệu được chú ý; nó không tự động bảo đảm việc tín hiệu được hiểu đúng. Ví dụ, một vật thể phát sáng mạnh trong góc nhìn người chơi có thể thu hút chú ý theo cơ chế bottom-up, nhưng nếu trước đó game chưa xây dựng được liên kết giữa kiểu phát sáng ấy với một hành vi cụ thể, người chơi có thể chỉ xem nó là điểm trang trí hoặc thử tương tác theo kiểu ngẫu nhiên. Điều này cho thấy visual cue không nên được định nghĩa bằng hiệu ứng thị giác đơn lẻ, mà bằng vai trò của nó trong chuỗi nhận diện - diễn giải - hành động.

Trong thực tế thiết kế game, tín hiệu thị giác thường xuất hiện dưới nhiều hình thức:

- màu sắc khác thường của một resource node để tách nó khỏi nền địa hình
- độ sáng hoặc tương phản cao hơn ở một lối ra để giữ hướng di chuyển
- silhouette riêng của vật thể có thể tương tác, giúp người chơi nhận ra chức năng ngay từ khoảng cách xa
- chuyển động báo trước của địch, cho phép người chơi dự đoán thay vì chỉ phản xạ sau khi bị đánh trúng
- bố cục không gian dẫn mắt người chơi đi từ mục tiêu chính sang mục tiêu phụ

Ở đây, giá trị của tín hiệu không nằm ở bản thân hình thức mã hóa, mà ở cách hình thức đó được đặt vào một hệ thống tổ chức thông tin. Cùng là màu sắc, nhưng màu chỉ là trang trí nếu nó không tham gia vào quyết định hành vi; cùng là chuyển động, nhưng chuyển động chỉ trở thành telegraph nếu người chơi có thể học được mối liên hệ giữa chuyển động đó và một hậu quả sắp tới. Chính vì vậy, nghiên cứu không xem tín hiệu thị giác như các thủ pháp hình ảnh rời rạc, mà như các đơn vị có chức năng bên trong cấu trúc gameplay.

Cũng cần phân biệt tín hiệu thị giác với `kể chuyện qua môi trường (environmental storytelling)`. Kể chuyện qua môi trường chủ yếu tổ chức chi tiết không gian để gợi ra lịch sử, bối cảnh, trạng thái xã hội hoặc diễn biến từng xảy ra trong thế giới game. Một căn phòng đổ nát, vết máu dẫn vào đường hầm, công cụ bỏ lại cạnh xác máy móc, hay cách một khu mỏ bị niêm phong có thể kể cho người chơi biết “điều gì đã xảy ra ở đây”. Ngược lại, tín hiệu thị giác theo nghĩa của đề tài tập trung vào việc giúp người chơi trả lời các câu hỏi mang tính chức năng như “đây là gì”, “có thể làm gì với nó”, “đi đâu”, “nguy hiểm nào sắp xảy ra”, hoặc “hành động vừa rồi đúng hay sai”.

Hai lớp này có thể giao nhau nhưng không đồng nhất. Một cánh cửa bị cào xước có thể là yếu tố kể chuyện nếu nó gợi ra việc từng có sinh vật lớn thoát ra từ bên trong; nhưng cánh cửa ấy chỉ trở thành tín hiệu thị giác trong phạm vi nghiên cứu nếu các vết cào đồng thời được quy ước như dấu hiệu cho biết khu vực phía sau là nguy hiểm hoặc có loại địch cụ thể. Việc không phân biệt hai lớp này sẽ làm khái niệm visual cue bị nới quá rộng, kéo nghiên cứu lệch từ cấu trúc thông tin và học cơ chế sang bình diện diễn giải tự sự.

### 1.3. Tutorial như kiến trúc tổ chức học tập

Trong nhiều trường hợp, tutorial vẫn bị hiểu theo nghĩa hẹp như một phân đoạn mở đầu gồm prompt, hộp thoại hoặc chỉ dẫn thao tác. Cách hiểu này có giá trị ở mức mô tả hiện tượng bề mặt, nhưng chưa đủ để phân tích tutorial như một cấu phần thiết kế. Về bản chất, tutorial nên được hiểu là một `kiến trúc tổ chức học tập`, tức một cách sắp xếp điều kiện để người chơi có thể hình thành tri thức cơ chế thông qua trải nghiệm.

Nếu coi tutorial là kiến trúc học tập, thì trọng tâm phân tích không chỉ còn là “thông tin nào được nói ra”, mà là toàn bộ cấu trúc điều kiện cho việc học: người chơi nhìn thấy gì trước, điều gì bị trì hoãn, nguy cơ nào được giảm tạm thời, hành động nào được yêu cầu lặp lại, phản hồi nào đủ rõ để xác nhận hiểu biết, và lúc nào hỗ trợ nên rút dần để người chơi chuyển sang tự chủ. Như vậy, tutorial không phải một gói nội dung, mà là một tiến trình điều phối mối quan hệ giữa chú ý, diễn giải và hành động.

Ở đây có thể phân biệt hai cách tiếp cận tutorial. Cách thứ nhất là tutorial như `truyền đạt chỉ dẫn`, trong đó trọng tâm nằm ở việc thông báo cho người chơi biết họ phải làm gì. Cách thứ hai là tutorial như `dàn dựng điều kiện học`, trong đó trọng tâm nằm ở việc tổ chức không gian, nguy cơ, tín hiệu và phản hồi sao cho người chơi có thể tự kết nối dấu hiệu với hành động. Đề tài lựa chọn cách tiếp cận thứ hai, bởi nó phù hợp hơn với bản chất của game như một hệ thống tương tác và cũng cho phép giải thích vì sao hai tutorial có cùng nội dung văn bản vẫn có thể cho ra kết quả học tập rất khác nhau.

Ví dụ, khi muốn dạy người chơi nhận biết telegraph của một quái vật, một tutorial theo kiểu truyền đạt chỉ dẫn có thể hiển thị dòng chữ “khi quái ngửa người ra sau thì hãy né”. Trong khi đó, một tutorial theo kiểu kiến trúc học tập sẽ giảm mật độ nguy hiểm cạnh tranh, đặt quái ở khoảng cách dễ quan sát, giữ nền đủ đơn giản để chuyển động báo trước tách ra rõ ràng, và cung cấp phản hồi đủ mạnh sau một lần né đúng. Hai trường hợp này cùng “dạy một cơ chế”, nhưng cơ chế học trong trường hợp thứ hai được tổ chức ngay trong cấu hình trải nghiệm, chứ không chỉ trong phần văn bản.

Chính vì tutorial có tính kiến trúc như vậy, nó không thể tách rời hệ thống tín hiệu thị giác. Nếu sequencing của tutorial xác định một cơ chế là trọng tâm, nhưng cấu hình thị giác lại không làm cho tín hiệu tương ứng đủ nổi, đủ rõ và đủ nhất quán, thì tutorial sẽ thất bại ngay từ bước đầu của tiếp thu. Nói cách khác, tutorial không chỉ cần một logic thời gian tốt, mà còn cần một logic tri giác tương thích với logic thời gian đó.

### 1.4. Cơ sở tri giác và nhận thức liên quan

Đề tài không tiến hành thí nghiệm sinh lý học mới, nhưng kế thừa những nền tảng đã được thừa nhận rộng rãi trong khoa học nhận thức và tâm lý học tri giác. Việc kế thừa này không nhằm biến nghiên cứu thành một công trình tâm lý học thực nghiệm, mà nhằm tạo cơ sở lý giải cho các tiêu chí thiết kế được sử dụng trong tutorial game.

Trước hết là các nguyên lý `Gestalt`, đặc biệt liên quan tới phân biệt hình - nền, nhóm hóa, tương cận và tương đồng. Những nguyên lý này cho thấy người chơi không tiếp nhận màn hình như tập hợp các điểm ảnh rời rạc, mà luôn có xu hướng tổ chức những gì mình thấy thành đơn vị có nghĩa. Vì vậy, một tín hiệu không thể được đánh giá chỉ bằng việc “đã có mặt trên màn hình” hay chưa; nó còn phải được xem xét ở khả năng tách khỏi nền, liên kết với nhóm thông tin phù hợp, và tránh bị hòa lẫn vào các nhóm nghĩa cạnh tranh. Ví dụ, một vật thể tương tác đặt giữa quá nhiều chi tiết trang trí có cùng shape language và cùng độ sáng sẽ khó được nhận ra như một thực thể chức năng, ngay cả khi bản thân sprite của nó được thiết kế riêng biệt.

Thứ hai là cơ chế chú ý `bottom-up` và `top-down`. Chú ý bottom-up bị hút bởi độ nổi bật vật lý như màu, tương phản, độ sáng hay chuyển động. Chú ý top-down lại chịu ảnh hưởng bởi mục tiêu hiện tại, kỳ vọng và tri thức có sẵn của người chơi. Trong thiết kế tutorial, hai cơ chế này luôn tương tác. Một tín hiệu có thể rất nổi bật về mặt thị giác nhưng vẫn không được giải đoán đúng nếu nó không khớp với mục tiêu mà người chơi đang theo đuổi. Ngược lại, một tín hiệu có thể ít nổi bật hơn nhưng vẫn được người chơi ưu tiên nếu nó phù hợp với nhiệm vụ họ đang cố hoàn thành. Đây là lý do vì sao tutorial không thể chỉ “làm mọi thứ sáng hơn”, mà phải đặt tín hiệu vào đúng thời điểm và đúng ngữ cảnh nhiệm vụ.

Thứ ba là vấn đề `cạnh tranh chú ý` trong không gian nhiều kích thích. Trong một game survival dungeon, người chơi thường phải xử lý đồng thời nền địa hình, kẻ địch, loot, hiệu ứng va chạm, thanh trạng thái, dấu hiệu nguy hiểm và các chỉ báo mục tiêu. Nếu mọi yếu tố cùng đòi quyền ưu tiên thị giác như nhau, tín hiệu cần học dễ bị nhấn chìm trong nhiễu. Một ví dụ điển hình là trường hợp game muốn dạy người chơi nhận biết đòn báo trước của quái, nhưng cùng thời điểm đó lại xuất hiện hiệu ứng lấp lánh từ loot, rung camera mạnh, và nhiều chỉ báo UI cạnh tranh. Khi ấy, thất bại học tập không chỉ là lỗi của telegraph, mà là lỗi của toàn bộ cấu hình cạnh tranh chú ý.

Thứ tư là hiện tượng `inattentional blindness`, cho thấy con người có thể bỏ sót một tín hiệu rõ ràng nếu chú ý đang bị huy động mạnh cho một nhiệm vụ khác. Trong ngữ cảnh game, điều này giải thích vì sao người chơi có thể không nhìn thấy một lối thoát sáng rõ, không nhận ra vật thể có thể tương tác ngay trước mặt, hoặc bỏ qua telegraph của địch trong lúc đang tập trung loot hoặc né một nguy hiểm khác. Việc ghi nhận khả năng này rất quan trọng về mặt lý luận, bởi nó chuyển câu hỏi từ “người chơi có chú ý hay không” sang “thiết kế đã tạo điều kiện để chú ý đúng đối tượng hay chưa”.

Từ bốn nền tảng trên có thể rút ra một hệ quả quan trọng cho nghiên cứu: trong tutorial game, cấu hình tín hiệu thị giác không phải là bước hoàn thiện mang tính thẩm mỹ sau cùng, mà là một thành phần trực tiếp của điều kiện học tập. Nói cách khác, nếu người chơi không thể thấy hoặc không thể phân biệt tín hiệu trong điều kiện chơi thực tế, thì bản thân cơ chế học cơ chế cũng không thể vận hành đúng như dự kiến.

### 1.5. Định nghĩa vận hành về Tín hiệu Thị giác

Để có thể phân tích, phân loại và mô hình hóa, đề tài cần một định nghĩa vận hành rõ ràng. Trong phạm vi nghiên cứu này, `Tín hiệu Thị giác` được xác định là:

`một đơn vị mã hóa thị giác mang thông tin chức năng, có ảnh hưởng đến quá trình nhận diện và diễn giải trong không gian tương tác.`

Định nghĩa này hàm chứa ba đặc tính cốt lõi.

Thứ nhất, tín hiệu là một `đơn vị mã hóa`, nghĩa là nó không phải sự xuất hiện ngẫu nhiên của hình ảnh, mà là một cấu phần được tổ chức có ý đồ. Điều này giúp phân biệt tín hiệu với sự nổi bật ngẫu nhiên do phong cách đồ họa hoặc do chồng chéo thị giác.

Thứ hai, tín hiệu mang `thông tin chức năng`, tức là nó phải gắn với một ý nghĩa liên quan tới hành vi, quyết định, nhận thức hoặc trạng thái. Một vật thể đẹp và nổi bật nhưng không làm thay đổi cách người chơi định hướng, dự đoán hay hành động thì chưa đủ điều kiện để được coi là visual cue theo nghĩa của nghiên cứu này.

Thứ ba, tín hiệu có ảnh hưởng tới `nhận diện và diễn giải`, nghĩa là nó không chỉ làm người chơi “thấy”, mà còn tác động đến khả năng họ hiểu điều đang được trình bày. Điểm này rất quan trọng, vì trong nhiều trường hợp người chơi có thể nhìn thấy một yếu tố thị giác nhưng không gán được ý nghĩa hành vi cho nó. Khi đó, yếu tố ấy có thể là vật thể nổi bật, nhưng chưa trở thành một tín hiệu vận hành được trong kiến trúc tutorial.

Từ đây, đề tài phân biệt tín hiệu thị giác với hai nhóm yếu tố dễ bị nhầm lẫn:

- `yếu tố trang trí`, là những thành phần tồn tại để làm giàu thẩm mỹ nhưng không giữ chức năng định hướng hành vi
- `yếu tố khí quyển`, là những thành phần giúp tạo mood, nhịp cảm xúc hoặc bản sắc không gian nhưng không trực tiếp tham gia vào cấu trúc thông tin của cơ chế đang được học
- `yếu tố kể chuyện qua môi trường`, là những thành phần giúp người chơi suy ra lịch sử, bối cảnh hoặc trạng thái thế giới, nhưng không nhất thiết trực tiếp hướng dẫn nhận diện, diễn giải hay thực thi cơ chế

Sự phân biệt này đặc biệt quan trọng, bởi nếu không làm rõ, mọi yếu tố “nổi bật” trong game đều có thể bị gán nhầm là visual cue, từ đó làm cho khái niệm mất giá trị phân tích. Chẳng hạn, một mảng sáng dùng để gợi cảm giác linh thiêng cho không gian có thể mang ý nghĩa thẩm mỹ rất mạnh, nhưng nó chỉ được xem là tín hiệu thị giác trong phạm vi nghiên cứu nếu người chơi có thể dựa vào nó để nhận biết một chức năng như lối đi, vùng an toàn, điểm tương tác hoặc cảnh báo nguy hiểm.

Việc bổ sung nhóm `kể chuyện qua môi trường` là cần thiết vì đây là lớp thường bị nhầm với visual cue trong các game có thế giới giàu chi tiết. Một dấu tích sụp đổ, một bàn thờ bị bỏ hoang hay một hành lang ngập xác thí nghiệm có thể rất giàu ý nghĩa tự sự, nhưng chúng không tự động là tín hiệu thị giác phục vụ tutorial. Chúng chỉ đi vào phạm vi của nghiên cứu khi được tổ chức sao cho người chơi có thể dùng chúng như dữ kiện chức năng để đưa ra hành vi hoặc giải đoán cơ chế.

Theo đó, định nghĩa vận hành của đề tài không nhằm bao quát toàn bộ giá trị thị giác trong game, mà nhằm khoanh đúng lớp yếu tố thị giác có khả năng tham gia vào việc hình thành tri thức cơ chế. Đây là điều kiện tiền đề để xây dựng taxonomy và để đánh giá hiệu quả của cue trong tutorial một cách nhất quán.

### 1.6. Hệ phân loại tín hiệu thị giác

#### 1.6.1. Cơ sở xây dựng hệ phân loại

Một trong những hạn chế phổ biến của thảo luận về visual cue là khái niệm thường được dùng theo lối trực giác: bất kỳ yếu tố nào “giúp dễ nhìn hơn” đều có thể bị gọi là tín hiệu thị giác. Cách dùng này thuận tiện cho trao đổi thiết kế ngắn hạn, nhưng không đủ để tiến hành phân tích học thuật hoặc đối chiếu giữa các prototype. Nếu không có hệ phân loại, sẽ rất khó trả lời các câu hỏi như: hai tín hiệu này khác nhau ở đâu, vì sao một tín hiệu thất bại còn tín hiệu kia thành công, hay khi thay đổi một cue thì thực chất ta đang thay đổi bình diện nào của hệ thống.

Vì vậy, đề tài xây dựng một `taxonomy ba chiều` nhằm đưa tín hiệu thị giác về một khung mô tả có thể sử dụng đồng thời trong nghiên cứu và ứng dụng thiết kế. Ba chiều được lựa chọn không phải ngẫu nhiên, mà nhằm bao phủ ba câu hỏi nền tảng của mọi tín hiệu:

- tín hiệu `hiện thân bằng gì`
- tín hiệu `được dùng để làm gì`
- tín hiệu `xuất hiện vào lúc nào` trong quan hệ với hành động và sự kiện

Khung ba chiều này cho phép mô tả cùng một tín hiệu ở nhiều mức: mức biểu hiện vật lý, mức vai trò chức năng và mức thời gian. Nhờ đó, nó hỗ trợ cả phân tích lý thuyết lẫn triển khai thiết kế.

#### 1.6.2. Chiều tồn tại

`Chiều tồn tại` trả lời câu hỏi: tín hiệu được hiện thân bằng phương tiện thị giác nào trong không gian game?

Trong đề tài này, chiều tồn tại gồm:

- `màu sắc (chromatic encoding)`
- `độ sáng và tương phản (luminance encoding)`
- `hình khối (geometric encoding)`
- `chuyển động (kinetic encoding)`
- `vị trí và bố cục (spatial encoding)`

Việc tách riêng chiều tồn tại là cần thiết vì cùng một chức năng có thể được mã hóa bằng nhiều phương tiện khác nhau, và mỗi phương tiện lại có ưu điểm, giới hạn riêng. Ví dụ, một tín hiệu cảnh báo có thể được xây bằng màu đỏ tương phản cao, bằng chuyển động giật lùi báo trước, bằng vùng sáng mở rộng trên mặt đất, hoặc bằng bố cục khiến vật thể nguy hiểm nằm ở vị trí trung tâm tầm nhìn. Mặc dù cùng thực hiện chức năng cảnh báo, bốn cách mã hóa này tác động lên chú ý theo những cơ chế khác nhau. Chuyển động thường mạnh trong việc thu hút chú ý tức thời; màu và độ sáng có lợi thế về tính ổn định; hình khối hữu ích cho nhận diện ở khoảng cách xa; trong khi bố cục lại đóng vai trò dẫn mắt ở cấp độ toàn cảnh.

Trong bối cảnh prototype của đề tài, một node tài nguyên đầu tiên có thể được làm nổi bằng màu lệch khỏi nền đá, trong khi lối ra của một đoạn hang lại phù hợp hơn với giải pháp tăng tương phản sáng - tối và bố cục dẫn mắt. Nhờ phân biệt chiều tồn tại, nghiên cứu có thể mô tả rõ không chỉ “có tín hiệu”, mà còn “tín hiệu được vật chất hóa như thế nào”.

#### 1.6.3. Chiều chức năng

`Chiều chức năng` trả lời câu hỏi: tín hiệu này được thiết kế để làm gì?

Các nhóm chức năng chính được xác lập gồm:

- `cảnh báo (warning)`
- `định hướng (directional)`
- `mời gọi tương tác (invitation)`
- `củng cố phản hồi (reinforcement)`
- `khởi phát trạng thái cảm xúc (emotional priming)`

Chiều chức năng đặc biệt quan trọng vì nó buộc nghiên cứu phải đánh giá tín hiệu dựa trên vai trò của nó, chứ không dựa trên mức độ bắt mắt đơn thuần. Một tín hiệu cảnh báo thành công khi nó giúp người chơi kịp điều chỉnh hành vi trước nguy hiểm; một tín hiệu định hướng thành công khi nó giúp người chơi không bị lạc mục tiêu; một tín hiệu mời gọi tương tác thành công khi nó khiến người chơi nhận ra khả năng can thiệp của mình vào hệ thống; một tín hiệu phản hồi thành công khi nó xác nhận hoặc hiệu chỉnh hiểu biết của người chơi về kết quả hành động.

Điều này cũng cho thấy vì sao tutorial không thể chỉ dạy “phải bấm nút gì”, mà còn phải dạy “nên chú ý dấu hiệu gì”. Trong một đoạn hướng dẫn khai thác tài nguyên, cue trọng tâm không phải là cảnh báo mà là mời gọi tương tác. Trong một đoạn dạy né đòn, cue trọng tâm lại chuyển sang cảnh báo và dự báo. Sự thay đổi này cho thấy tutorial và taxonomy phải được liên kết với nhau: khi cơ chế dạy thay đổi, loại tín hiệu được ưu tiên cũng thay đổi theo.

#### 1.6.4. Chiều thời gian

`Chiều thời gian` trả lời câu hỏi: tín hiệu tồn tại trong quan hệ thời điểm nào với hành động và sự kiện?

Đề tài chia chiều thời gian thành bốn loại:

- `liên tục (persistent)`
- `dự báo (predictive / telegraphing)`
- `kích hoạt theo sự kiện (triggered)`
- `phản ứng (reactive feedback)`

Việc thêm chiều thời gian là cần thiết vì cùng một tín hiệu về mặt hình thức và chức năng vẫn có thể tạo ra hiệu quả rất khác nhau tùy thời điểm xuất hiện. Một lối thoát luôn sáng nhẹ là tín hiệu liên tục; một vòng sáng mở rộng trước khi bẫy kích hoạt là tín hiệu dự báo; hiệu ứng sáng lên khi người chơi bước lại gần vật thể là tín hiệu kích hoạt; còn âm - hình phản hồi sau khi khai thác thành công là tín hiệu phản ứng. Nếu không phân biệt theo thời gian, nghiên cứu sẽ khó mô tả chính xác tín hiệu đang hỗ trợ bước nào trong vòng học cơ chế.

Trong tutorial, chiều thời gian đặc biệt quan trọng vì tri thức cơ chế thường được hình thành từ quan hệ trước - trong - sau hành động. Người chơi không chỉ cần nhận ra vật thể, mà còn cần hiểu rằng một tín hiệu xuất hiện trước nguy hiểm có ý nghĩa khác với một tín hiệu xuất hiện sau khi bị trúng đòn. Một prototype dạy né đòn chỉ thực sự kiểm tra năng lực đọc telegraph khi tín hiệu dự báo xuất hiện đủ sớm để người chơi có khả năng chuyển từ nhận diện sang thực thi.

#### 1.6.5. Giao điểm ba chiều

Theo mô hình của đề tài, một tín hiệu thị giác cụ thể không nên được xác định chỉ bằng một đặc tính đơn lẻ, mà phải được mô tả như giao điểm của ba chiều nói trên. Cách làm này cho phép phân tích chính xác hơn lý do một tín hiệu hoạt động hay thất bại. Ví dụ, một resource node đầu tiên trong prototype có thể được mô tả là:

- `Chiều tồn tại`: màu + độ sáng
- `Chiều chức năng`: mời gọi tương tác
- `Chiều thời gian`: liên tục

Trong khi một telegraph trước đòn đánh của quái có thể là:

- `Chiều tồn tại`: chuyển động + hình khối
- `Chiều chức năng`: cảnh báo
- `Chiều thời gian`: dự báo

Cách mô tả này cho phép tín hiệu được đưa vào mô hình nghiên cứu một cách rõ ràng hơn, đồng thời tạo nền cho việc ứng dụng vào thiết kế prototype. Nó cũng cho phép giải thích sai lệch thiết kế. Nếu người chơi không nhận ra resource node, lỗi có thể nằm ở chiều tồn tại; nếu người chơi nhìn thấy nhưng không thử khai thác, lỗi có thể nằm ở chiều chức năng; nếu người chơi chỉ nhận ra khi đã đi qua vật thể, lỗi có thể nằm ở chiều thời gian. Nhờ vậy, taxonomy không chỉ là công cụ mô tả, mà còn là công cụ chẩn đoán thiết kế.

### 1.7. Nguyên tắc phân cấp thị giác trong tutorial game

Trong điều kiện gameplay bình thường, không phải mọi thông tin trên màn hình đều có cùng giá trị. Những tín hiệu gắn với sống còn, nguy hiểm tức thời hoặc quyết định thao tác thường phải có ưu tiên cao hơn các tín hiệu phụ trợ. Tuy nhiên, trong tutorial, xuất hiện thêm một trục ưu tiên khác: `ưu tiên sư phạm`, tức ưu tiên dành cho tín hiệu cần thiết để người chơi học được cơ chế đang được giới thiệu.

Từ đó, đề tài xác lập rằng phân cấp thị giác trong tutorial game không phải là một cấu trúc tĩnh, mà là một `hệ phân cấp động` phụ thuộc vào `play state`. Có thể phân biệt:

- `Diegetic Priority`: ưu tiên nội tại của thế giới game, gắn với logic sống còn, đe dọa và giá trị sử dụng trong gameplay
- `Pedagogical Priority`: ưu tiên phục vụ cho việc học cơ chế, có thể tạm thời vượt lên trên logic sống còn thông thường

Việc phân biệt hai loại ưu tiên này có ý nghĩa quan trọng. Trong gameplay thường, một đòn đánh sắp tới của địch phải có mức ưu tiên cao hơn một node tài nguyên ở góc màn hình. Nhưng trong một đoạn tutorial dạy khai thác, môi trường có thể được dọn bớt mối nguy, và node tài nguyên đầu tiên có thể được đặt ở vị trí nổi bật hơn bình thường để người chơi buộc phải nhận ra nó. Khi đó, tutorial không phủ nhận logic của game, mà tạm thời điều chỉnh điều kiện tri giác để một cơ chế cụ thể có thể được học.

Về mặt thiết kế, `pedagogical priority` có thể được nâng lên bằng nhiều cách:

- giảm sát thương hoặc giới hạn loại nguy hiểm cạnh tranh
- giảm số lượng đối tượng có khả năng thu hút chú ý cùng lúc
- làm nổi bật mạnh hơn cue mục tiêu
- sắp xếp lại bố cục không gian để tín hiệu trọng tâm xuất hiện trước
- trì hoãn những tín hiệu phức tạp khác cho tới khi cơ chế đầu tiên đã ổn định

Nếu không làm rõ cơ chế phân cấp này, tutorial rất dễ thất bại theo hai hướng. Hướng thứ nhất là “dạy nhưng người chơi không thấy”, khi tín hiệu cần học bị chìm dưới các tín hiệu sống còn hoặc thẩm mỹ khác. Hướng thứ hai là “thấy nhưng hiểu sai”, khi cùng một cue phải đồng thời gánh quá nhiều chức năng và mất đi tính nhất quán. Do đó, phân cấp thị giác không chỉ là câu chuyện clarity, mà là câu chuyện tổ chức điều kiện học cơ chế.

### 1.8. Tutorial và ba cấp độ tiếp thu

Đề tài xem việc học cơ chế trong game là một quá trình diễn ra qua ba cấp độ:

1. `Nhận diện (recognition)`
2. `Diễn giải (interpretation)`
3. `Thực thi (execution)`

Ở cấp `nhận diện`, vấn đề trung tâm là người chơi có nhìn ra đúng đối tượng cần chú ý hay không. Đây là cấp chịu tác động trực tiếp nhất của cấu hình tín hiệu thị giác. Một node tài nguyên có thể tồn tại ngay giữa màn hình nhưng vẫn không được nhận ra nếu nó không đủ tách khỏi nền, bị cạnh tranh bởi UI, hoặc xuất hiện khi người chơi đang bị một nguy hiểm khác hút chú ý.

Ở cấp `diễn giải`, người chơi không chỉ thấy tín hiệu, mà còn phải hiểu tín hiệu đó có nghĩa gì. Đây là cấp mà tính nhất quán mã hóa trở nên quyết định. Nếu ánh sáng xanh lúc thì có nghĩa “an toàn”, lúc lại có nghĩa “có thể tương tác”, người chơi sẽ nhìn thấy nhưng không giải đoán ổn định. Một telegraph chỉ thực sự thành công khi người chơi không chỉ thấy địch chuyển động, mà hiểu được rằng chuyển động ấy báo trước một hậu quả cần phản ứng.

Ở cấp `thực thi`, tri thức được chuyển thành hành động. Đây là nơi tutorial cho thấy người chơi có thể biến dấu hiệu đã thấy và đã hiểu thành thao tác đúng hay không. Trong prototype dự kiến của đề tài, ví dụ về ba cấp này có thể được minh họa như sau:

- `Nhận diện`: người chơi thấy node tài nguyên đầu tiên nổi bật giữa nền hang
- `Diễn giải`: người chơi hiểu đó là vật thể có thể khai thác, không phải chi tiết trang trí
- `Thực thi`: người chơi tiến lại gần, dùng đúng công cụ hoặc đúng hành động để khai thác

Tương tự, với bài học né đòn:

- `Nhận diện`: người chơi thấy chuyển động báo trước của quái
- `Diễn giải`: người chơi hiểu đó là dấu hiệu nguy hiểm sắp xảy ra
- `Thực thi`: người chơi né đúng trong cửa sổ thời gian phù hợp

Ba cấp này tạo thành một chuỗi nối tiếp. Nếu thất bại ở cấp đầu, chuỗi học sẽ đứt trước khi bước vào diễn giải. Nếu thất bại ở cấp hai, người chơi có thể nhìn thấy mà vẫn hành động sai. Nếu thất bại ở cấp ba, bài học sẽ không chuyển thành năng lực thao tác. Vì vậy, tutorial hiệu quả phải được tổ chức sao cho tín hiệu, ngữ cảnh và phản hồi cùng lúc hỗ trợ cả ba cấp, thay vì chỉ tối ưu cho một cấp đơn lẻ.

### 1.9. Các dạng thất bại trong thiết kế tutorial

Từ cấu trúc lý luận trên, có thể xác định một số dạng thất bại điển hình trong thiết kế tutorial.

Thứ nhất là `quá tải chỉ dẫn (instruction overload)`. Quá tải không chỉ đến từ việc có quá nhiều câu chữ, mà còn có thể đến từ việc quá nhiều cue cùng lúc đòi hỏi chú ý. Một màn chơi đầu tiên vừa hiện prompt di chuyển, vừa nháy node tài nguyên, vừa tạo hiệu ứng nguy hiểm, vừa đưa nhiều icon UI mới vào cùng lúc sẽ khiến người chơi phải giải mã quá nhiều lớp thông tin trước khi họ kịp ổn định mục tiêu hành động.

Thứ hai là `chuyển giao tự chủ quá sớm (premature autonomy)`. Đây là tình huống tutorial rút hỗ trợ trước khi người chơi hình thành liên kết ổn định giữa tín hiệu và hành động. Người chơi khi đó có thể hoàn thành một lần do làm theo prompt hoặc do may mắn, nhưng không tái hiện được hành vi khi điều kiện thay đổi. Đây là khác biệt rất quan trọng giữa “làm theo trong tutorial” và “thật sự học được cơ chế”.

Thứ ba là `không nhất quán mã hóa thị giác (encoding inconsistency)`. Dạng thất bại này xảy ra khi cùng một loại thông tin được mã hóa bằng nhiều kiểu cue không liên hệ với nhau, hoặc cùng một cue lại mang nhiều ý nghĩa cạnh tranh. Ví dụ, nếu màu vàng lúc dùng cho loot, lúc dùng cho cảnh báo, lúc dùng cho điểm tương tác, thì người chơi khó xây dựng được một quy ước nhận thức ổn định.

Thứ tư là `xung đột giữa cơ chế (mechanic conflict)`. Điều này xảy ra khi tutorial cố dạy nhiều cơ chế có yêu cầu chú ý khác nhau trong cùng một thời điểm. Chẳng hạn, vừa dạy khai thác tài nguyên vừa dạy né đòn trong một không gian dày đặc nguy hiểm có thể khiến cue mời gọi tương tác và cue cảnh báo kéo người chơi theo hai hướng hành vi khác nhau. Trong trường hợp ấy, thất bại không nhất thiết do từng cơ chế riêng lẻ quá khó, mà do kiến trúc học tập không đủ tách bạch.

Thứ năm là `thất bại chú ý (attention failure)`, khi cue đã được đặt vào game nhưng không vượt qua được ngưỡng nhận diện hoặc bị chìm trong nhiễu cạnh tranh. Đây là dạng thất bại đặc biệt đáng chú ý đối với đề tài, vì nó cho thấy không thể đánh giá tutorial chỉ ở tầng nội dung; cần đánh giá cả khả năng tín hiệu thực sự được nhìn thấy trong hoàn cảnh chơi.

Việc nhận diện các dạng thất bại này có ý nghĩa phương pháp luận quan trọng. Nó cho phép nghiên cứu chuyển từ mô tả hiện tượng sang xác định điều kiện thiết kế có thể kiểm soát, và từ đó hình thành các nguyên tắc ràng buộc cho mô hình tích hợp ở phần sau.

### 1.10. Cơ sở hình thành mô hình Visual-Integrated Tutorial Model (VITM)

Trên nền của các khái niệm đã trình bày, có thể thấy rõ vì sao cần một mô hình tích hợp giữa tín hiệu thị giác và tutorial. Nếu tutorial chỉ được thiết kế ở tầng sequencing, còn tín hiệu thị giác chỉ được tối ưu ở tầng readability bề mặt, thì quá trình học cơ chế luôn có nguy cơ bị đứt đoạn giữa `thấy`, `hiểu` và `làm`. Một bài học có thể được sắp xếp hợp lý về mặt nội dung nhưng vẫn thất bại vì cue không đủ nổi, không nhất quán, hoặc xuất hiện sai thời điểm. Ngược lại, một hệ thống cue có thể rất rõ nhưng vẫn không giúp người chơi học nếu nó không được đặt trong một trình tự học có kiểm soát.

Từ đó, đề tài xác lập `Visual-Integrated Tutorial Model (VITM)` như một khung lý thuyết nhằm tổ chức có hệ thống mối quan hệ giữa cấu hình tín hiệu, trình tự học và vòng xử lý của người chơi. Mô hình gồm ba tầng:

1. `Cue Layer`
2. `Structuring Layer`
3. `Interpretive Loop`

Trong đó:

- `Cue Layer` chịu trách nhiệm cấu hình tín hiệu: tín hiệu nào tồn tại, dùng loại mã hóa nào, có độ nổi bật ra sao, và được phân cấp như thế nào
- `Structuring Layer` chịu trách nhiệm tổ chức tutorial: dạy cơ chế nào trước, giảm áp lực ở mức nào, cue nào được ưu tiên trong từng bước, khi nào rút hỗ trợ
- `Interpretive Loop` mô tả vòng xử lý thực tế của người chơi khi tiếp xúc với cue và yêu cầu hành động

Vòng lặp trung tâm của mô hình được xác định là:

`Trình bày tín hiệu -> Thu hút chú ý -> Diễn giải ý nghĩa -> Thử nghiệm hành động -> Phản hồi -> Cập nhật tri thức`

Điểm cốt lõi của mô hình này là không giả định việc “đưa tín hiệu lên màn hình” sẽ tự động dẫn đến học tập. Mỗi bước trong vòng lặp đều có thể thất bại: tín hiệu có thể không được chú ý, được chú ý nhưng bị hiểu sai, được hiểu đúng nhưng không chuyển thành thao tác ổn định, hoặc thao tác được thực hiện nhưng phản hồi không đủ rõ để củng cố. Bằng cách đặt các khả năng thất bại đó vào cùng một khung, VITM cho phép xem tutorial như một hệ thống có điều kiện, thay vì một tuyến chỉ dẫn một chiều.

Với cách hiểu như vậy, VITM không phải là một kỹ thuật “trang trí tutorial”, mà là một mô hình tái cấu trúc tutorial trên nền của tín hiệu thị giác. Giá trị của mô hình nằm ở chỗ nó nối được ba cấp đang thường bị tách rời trong thực tiễn: cấu hình thị giác, kiến trúc dạy học và hành vi giải đoán của người chơi. Đây cũng là cơ sở để chương sau chuyển từ nền tảng lý luận sang phần ứng dụng trong bối cảnh game cụ thể.

---

## CHƯƠNG 2: ỨNG DỤNG NGHIÊN CỨU VÀ THIẾT KẾ

### 2.1. Bối cảnh ứng dụng

Bối cảnh ứng dụng của nghiên cứu là một game `2D survival dungeon` đang được phát triển, trong đó người chơi khởi đầu trên một đảo hoang, thiết lập điểm trú ẩn ban đầu, rồi dần dần đi xuống các tầng hang tự nhiên nằm dưới lòng đất. Trên mặt đất, không gian hiện gồm các vùng `rừng rậm`, `đồng bằng` và `bãi biển`; phía dưới là nhiều lớp hang, trong đó mỗi tầng hang mang một biome đặc thù và có thể chứa các pocket nội dung đậm như hầm ngục, tàn tích hoặc khu vực sự kiện. Về phong cách, game được định hướng theo chất `low-tech steampunk magitech`, tức một thế giới chưa đạt tới ngưỡng công nghệ cao, nơi công cụ, máy móc và năng lượng mana tồn tại trong trạng thái cơ khí - kỹ thuật sơ khai.

Việc lựa chọn bối cảnh này không chỉ nhằm tìm một ví dụ minh họa thuận tiện, mà dựa trên các tiêu chí phù hợp với mục tiêu kiểm chứng của đề tài.

Thứ nhất, đây là kiểu game có `mật độ đọc tín hiệu cao`. Người chơi buộc phải liên tục phân biệt vật thể tương tác, lối đi, vùng nguy hiểm, nhịp đòn của địch, trạng thái an toàn tương đối, và giá trị của việc tiếp tục tiến sâu hay quay về. Điều đó khiến việc nhận diện và diễn giải tín hiệu thị giác không còn là yếu tố phụ trợ, mà trở thành điều kiện trực tiếp của hành vi chơi.

Thứ hai, đây là kiểu game có `nhu cầu tutorial nội sinh`. Các cơ chế cốt lõi của game không tự bộc lộ hoàn toàn qua thao tác thử - sai ngắn hạn. Người chơi phải học cách nhận biết tài nguyên, đọc không gian hang, hiểu nguy hiểm báo trước, và hình thành nhịp “đi - lấy - quay về”. Do đó, tutorial trong bối cảnh này không thể chỉ dựa vào lời nhắc văn bản, mà cần gắn trực tiếp với ngôn ngữ thị giác của thế giới game.

Thứ ba, đây là kiểu game `thuận lợi cho đối chứng thực nghiệm`. Cùng một nội dung cơ chế có thể được triển khai thành nhiều phiên bản tutorial khác nhau mà không cần thay đổi bản sắc cơ bản của trò chơi. Chẳng hạn, cùng một bài học về khai thác tài nguyên hoặc né đòn có thể được tổ chức dưới dạng lệ thuộc nhiều vào văn bản, dưới dạng có cue thị giác nhưng thiếu cấu trúc, hoặc dưới dạng tutorial tích hợp đầy đủ theo VITM. Khả năng tạo nhiều biến thể như vậy là điều kiện cần để thiết kế nghiên cứu có đối chứng.

Thứ tư, game hiện tại cho phép cô lập một `lát cắt nghiên cứu` đủ nhỏ nhưng vẫn có ý nghĩa thật đối với sản phẩm. Điều này rất quan trọng, vì nếu sử dụng toàn bộ game làm nền kiểm chứng, số lượng biến nhiễu sẽ tăng cao và khó xác định chính xác mô hình tác động vào đâu. Ngược lại, nếu chọn một lát cắt quá nghèo nàn, nghiên cứu sẽ mất đi tính đại diện đối với gameplay thật.

Từ các tiêu chí trên, có thể xem game này như một `trường hợp ứng dụng khả thi` cho đề tài. Nó vừa đủ phức tạp để đặt ra vấn đề nghiên cứu thật về tín hiệu thị giác và tutorial, vừa đủ cụ thể để các khái niệm ở Chương 1 có thể được chuyển hóa thành hệ thống thiết kế và tiêu chí đo lường ở các mục tiếp theo.

### 2.2. Mục tiêu ứng dụng vào game hiện tại

Việc ứng dụng nghiên cứu vào game hiện tại không nên được hiểu đơn thuần như “đem lý thuyết gắn vào một sản phẩm”, mà cần được xác định như một quá trình kiểm chứng hai chiều: dùng game để kiểm tra mô hình, đồng thời dùng mô hình để tái cấu trúc một phần thiết kế game. Trên cơ sở đó, mục tiêu ứng dụng của đề tài có thể được chia thành ba lớp, với `mục tiêu nghiên cứu` giữ vị trí ưu tiên.

Trước hết là `mục tiêu nghiên cứu`. Mục tiêu này nhằm kiểm tra xem việc tổ chức tutorial theo VITM có tạo ra khác biệt quan sát được trong quá trình người chơi tiếp thu cơ chế hay không. Nói cụ thể hơn, đề tài không chỉ muốn biết người chơi “thích” phiên bản nào hơn, mà muốn kiểm tra các câu hỏi sâu hơn: người chơi có nhận ra cue nhanh hơn không, có diễn giải đúng chức năng của cue hơn không, có thực thi cơ chế với số lỗi thấp hơn không, và khi cue hỗ trợ giảm đi thì họ có còn giữ được tri thức cơ chế hay không.

Thứ hai là `mục tiêu thiết kế`. Ở lớp này, đề tài hướng tới việc xây dựng cho game một ngôn ngữ tín hiệu thị giác có thể tái sử dụng, đủ nhất quán để phục vụ tutorial mà không phụ thuộc quá nhiều vào text. Điều này có nghĩa là phần ứng dụng không chỉ dừng ở việc “gắn thêm cue” cho một đoạn mở đầu, mà phải thử chứng minh một hướng thiết kế trong đó tín hiệu thị giác tham gia trực tiếp vào onboarding, readability, telegraphing và phản hồi hành động.

Thứ ba là `mục tiêu sản phẩm`. Dù nghiên cứu giữ ưu tiên trước, prototype được tạo ra không nên chỉ là một demo học thuật tách rời khỏi game hiện tại. Nó cần đồng thời là một `vertical slice` có giá trị thực đối với dự án, nghĩa là phần được xây để kiểm chứng cũng phải có khả năng tái sử dụng trong pipeline phát triển sau này. Yêu cầu này giúp đề tài tránh rơi vào tình trạng mô hình có vẻ đúng trong phòng thí nghiệm nhưng khó chuyển hóa thành quy tắc thiết kế cho sản phẩm thật.

Từ ba lớp mục tiêu trên, có thể diễn đạt gọn mục tiêu ứng dụng của chương này như sau: `chuyển VITM từ một khung lý thuyết thành một cấu trúc tutorial có thể kiểm chứng trong prototype, đồng thời tạo ra lợi ích thiết kế trực tiếp cho game hiện tại`. Cách xác lập này giúp giữ cân bằng giữa yêu cầu học thuật và yêu cầu phát triển sản phẩm, đồng thời chuẩn bị nền cho việc lựa chọn lát cắt thử nghiệm ở mục tiếp theo.

### 2.3. Chọn lát cắt thử nghiệm

Một yêu cầu phương pháp luận quan trọng của đề tài là không sử dụng toàn bộ game như một đơn vị kiểm chứng duy nhất. Nếu ôm toàn bộ hệ thống đang phát triển, số lượng biến nhiễu sẽ tăng quá lớn: áp lực sinh tồn, combat, quản lý tài nguyên, tiến trình dài hạn, base building, mana, machine, gate và co-op đều có thể đồng thời tác động lên hành vi học của người chơi. Trong tình huống đó, sẽ rất khó xác định phần thay đổi trong kết quả xuất phát từ mô hình tutorial hay từ những hệ khác của trò chơi.

Vì vậy, nghiên cứu cần một `lát cắt thử nghiệm` hẹp nhưng vẫn đại diện được cho logic cốt lõi của game. Tiêu chí để lựa chọn lát cắt này gồm:

- có đủ mật độ tín hiệu để kiểm tra quá trình `nhận diện - diễn giải - thực thi`
- có thể tổ chức thành một chuỗi tutorial ngắn, rõ mục tiêu
- có thể tạo phiên bản đối chứng mà không làm thay đổi bản sắc cơ bản của gameplay
- có giá trị thực đối với sản phẩm, tức phần xây ra cho nghiên cứu vẫn có thể tái sử dụng trong game sau này

Trên cơ sở các tiêu chí đó, lát cắt phù hợp nhất là `phần đầu game`, cụ thể nằm ở vùng:

- `khu gần base`
- `cửa vào hang đầu tiên`
- `đoạn hang đầu tiên`

Đây là vùng phù hợp vì nó hội tụ ba nhóm cơ chế đầu tiên mà người chơi buộc phải học:

1. `nhận ra và khai thác resource cơ bản`
2. `nhận ra cảnh báo nguy hiểm và phản ứng đúng`
3. `hiểu logic đi ra ngoài rồi quay về an toàn`

Ba nhóm cơ chế này có vai trò đặc biệt quan trọng đối với nghiên cứu. Chúng vừa là cơ chế nền của game, vừa là những cơ chế có thể biểu hiện rõ qua không gian và tín hiệu thị giác. Nếu chọn một phần gameplay quá trừu tượng hoặc phụ thuộc nhiều vào số liệu ẩn, nghiên cứu sẽ khó quan sát được tác động thực sự của cue. Ngược lại, trong lát cắt được đề xuất, gần như mọi hành vi cốt lõi đều gắn với việc người chơi nhìn thấy một dấu hiệu, giải đoán nó, rồi hành động tương ứng.

Việc giới hạn prototype vào lát cắt này cũng có ý nghĩa về mặt kiểm soát độ phức tạp. Ở giai đoạn đầu, nghiên cứu chưa cần đưa vào các hệ như `mana network`, `gate milestone`, `machine / automation` hay `co-op nhiều vai`. Không phải vì các hệ đó không quan trọng, mà vì chúng mở rộng phạm vi biến số quá nhanh và khiến việc đọc kết quả thực nghiệm trở nên kém minh bạch. Những hệ sâu hơn có thể được xem như giai đoạn mở rộng sau khi hiệu lực cơ bản của mô hình đã được kiểm chứng.

Theo nghĩa đó, lát cắt thử nghiệm không phải là một lựa chọn mang tính tiện lợi, mà là một quyết định phương pháp luận. Nó cho phép nghiên cứu giữ được sự cân bằng giữa hai yêu cầu: một mặt phải đủ đơn giản để kiểm chứng mô hình, mặt khác phải đủ giàu để phản ánh đúng cấu trúc hành vi của game thật.

### 2.4. Mapping từ taxonomy sang hệ thống game

Mục tiêu của phần này không chỉ là liệt kê các loại cue có thể dùng trong game, mà là chuyển `taxonomy ba chiều` ở Chương 1 thành một hệ tín hiệu có thể triển khai, quan sát và so sánh trong prototype. Nói cách khác, phần mapping phải trả lời được câu hỏi: khi bước từ lý thuyết sang thiết kế, mỗi chiều của taxonomy sẽ trở thành quyết định cụ thể nào trong tutorial slice.

Về nguyên tắc, việc mapping này phải tuân theo ba yêu cầu:

- mỗi cue phải có `vị trí phân loại` rõ trong taxonomy
- mỗi cue phải gắn với `một chức năng học tập` cụ thể trong tutorial
- mỗi cue phải tránh nhầm lẫn với yếu tố trang trí, khí quyển hoặc kể chuyện qua môi trường nếu các yếu tố đó không trực tiếp phục vụ hành vi học cơ chế

Do đó, phần mapping không nên được hiểu là “trang trí thêm cho màn chơi”, mà là tổ chức một `hệ tín hiệu chức năng` phục vụ các bài học đầu tiên của prototype.

#### 2.4.1. Ứng dụng chiều tồn tại

Trong prototype, `chiều tồn tại` quyết định cue được vật chất hóa bằng phương tiện thị giác nào. Đây là lớp thiết kế đầu tiên, vì nếu tín hiệu không hiện thân bằng một hình thức đủ rõ, các chiều còn lại sẽ khó phát huy tác dụng.

Các hướng hiện thực hóa chính trong game gồm:

- `màu sắc`
  - dùng để tách resource đầu tiên ra khỏi nền đất đá hoặc thảm thực vật
  - dùng để tạo quy ước cảnh báo cơ bản cho trạng thái nguy hiểm
- `độ sáng và tương phản`
  - dùng để làm rõ lối đi, cửa hang, vùng quay về hoặc object cần chú ý
  - đặc biệt hữu ích ở các khu vực tối, nơi màu sắc đơn thuần có thể chưa đủ để tách nền
- `hình khối / silhouette`
  - dùng để phân biệt resource, hazard, lootable object và địch ngay từ khoảng cách nhìn đầu tiên
  - có vai trò mạnh trong game 2D, nơi người chơi thường nhận dạng vật thể trước qua silhouette
- `chuyển động`
  - dùng cho telegraph của địch, cue nhắc tương tác hoặc những báo hiệu cần phản ứng nhanh
  - là lớp mã hóa đặc biệt hiệu quả cho các cue có tính thời điểm
- `vị trí và bố cục`
  - dùng để đặt object tutorial vào đường nhìn tự nhiên của người chơi
  - dùng để sắp xếp không gian sao cho mục tiêu chính xuất hiện trước mục tiêu phụ

Ở đây, điều quan trọng không phải là sử dụng càng nhiều phương tiện càng tốt, mà là chọn phương tiện phù hợp với từng nhiệm vụ học. Ví dụ, resource đầu tiên nên ưu tiên `màu + silhouette + vị trí`, vì mục tiêu là người chơi nhận ra khả năng tương tác. Trong khi đó, đòn báo trước của địch nên ưu tiên `chuyển động + hình khối + tương phản`, vì mục tiêu là tạo khả năng phản ứng theo thời gian ngắn.

#### 2.4.2. Ứng dụng chiều chức năng

Nếu chiều tồn tại trả lời câu hỏi cue “trông như thế nào”, thì `chiều chức năng` trả lời câu hỏi cue “phục vụ điều gì” trong quá trình học. Đây là phần quyết định cue có thực sự tham gia vào tutorial hay chỉ tồn tại như một lớp hình ảnh.

Trong prototype, các nhóm chức năng có thể được map như sau:

- `warning`
  - telegraph trước đòn đánh của quái
  - dấu hiệu bẫy hoặc hazard sắp kích hoạt
  - chỉ báo cho vùng mà người chơi không nên đứng lại
- `directional`
  - chỉ hướng đi xuống hang đầu tiên
  - chỉ lối quay về base hoặc vùng an toàn
  - làm rõ đâu là tuyến tiến chính trong lát cắt thử nghiệm
- `invitation`
  - resource đầu tiên nên khai thác
  - object đầu tiên nên nhặt hoặc thử tương tác
  - chỗ mở lối hoặc vật cản mà người chơi được kỳ vọng chú ý
- `reinforcement`
  - hit confirm khi khai thác đúng
  - phản hồi khi né đúng, nhặt đúng hoặc quay về đúng lúc
  - phản hồi fail khi hành động sai để người chơi hiệu chỉnh hiểu biết
- `emotional priming`
  - cảm giác an toàn và ổn định quanh base
  - cảm giác dè chừng khi bước vào khu vực hang đầu tiên
  - cảm giác áp lực tăng nhẹ khi người chơi ở xa điểm quay về

Điểm quan trọng ở đây là cùng một object có thể mang nhiều chức năng, nhưng trong từng đoạn tutorial cần xác định `chức năng trội`. Một quái vật ở đoạn đầu có thể vừa là mối nguy chiến đấu, vừa góp phần tạo cảm giác căng thẳng cho không gian. Tuy nhiên, nếu bài học trọng tâm của đoạn đó là “đọc telegraph để né”, thì chức năng trội của cue liên quan đến quái phải là `warning`, không phải `emotional priming`.

#### 2.4.3. Ứng dụng chiều thời gian

`Chiều thời gian` là phần giúp chuyển một cue từ trạng thái “thông tin tĩnh” sang trạng thái “thông tin gắn với tiến trình hành động”. Trong prototype tutorial, đây là chiều đặc biệt quan trọng, vì bài học không chỉ nằm ở việc người chơi nhìn thấy một vật thể, mà ở việc họ hiểu tín hiệu xuất hiện khi nào và phải phản ứng vào lúc nào.

Trong game hiện tại, có thể chia như sau:

- `cue liên tục`
  - safe zone quanh base
  - exit hoặc đường lui
  - resource / object quan trọng cần được nhận ra trong suốt bài học
- `cue dự báo`
  - telegraph trước đòn đánh
  - dấu hiệu nguy hiểm xuất hiện ngay trước khi hazard kích hoạt
  - nhịp rung, co người hoặc đổi pose của địch
- `cue kích hoạt theo sự kiện`
  - object bắt đầu sáng hơn khi người chơi tới gần
  - cue xuất hiện khi người chơi bước vào vùng học mới
  - nhắc quay về khi người chơi đạt ngưỡng risk nhất định
- `cue phản ứng`
  - feedback sau khi khai thác đúng
  - phản hồi sau khi né thành công hoặc thất bại
  - chỉ báo cho thấy hành động vừa rồi đã làm thay đổi trạng thái hệ thống

Điểm đáng chú ý là cùng một object có thể tham gia nhiều lớp thời gian khác nhau. Ví dụ, một resource node có thể có silhouette liên tục để người chơi nhận ra từ xa, nhưng chỉ phát hiệu ứng sáng nhẹ khi người chơi lại gần để chuyển từ “nhìn thấy” sang “thử tương tác”. Một quái vật có thể vừa hiện diện liên tục như mối nguy, vừa tạo ra cue dự báo ngay trước đòn đánh, rồi sau đó sinh cue phản ứng khi người chơi né trúng hoặc bị đánh trúng. Vì vậy, mapping theo chiều thời gian giúp nghiên cứu tách rõ từng thời điểm mà cue hỗ trợ việc học.

#### 2.4.4. Từ taxonomy tới gói cue cho prototype

Để phần mapping không dừng ở mức khái quát, có thể chuyển toàn bộ taxonomy thành ba `gói cue` trung tâm của prototype:

- `Gói cue khai thác`
  - trọng tâm học tập: nhận ra resource đầu tiên và thực hiện tương tác đúng
  - thành phần chính: màu sắc, silhouette, vị trí đặt object, phản hồi sau khai thác
- `Gói cue cảnh báo`
  - trọng tâm học tập: nhận ra telegraph nguy hiểm và phản ứng đúng
  - thành phần chính: chuyển động báo trước, pose của địch, tương phản nguy hiểm, feedback sau né hoặc trúng đòn
- `Gói cue định hướng quay về`
  - trọng tâm học tập: hiểu nhịp đi - lấy - quay về an toàn
  - thành phần chính: độ sáng / bố cục của lối quay về, cảm giác an toàn quanh base, chỉ báo ngưỡng risk tăng dần

Ba gói cue này không chỉ là giải pháp thiết kế, mà còn là đơn vị phân tích cho thực nghiệm ở phần sau. Nhờ đó, nghiên cứu có thể quan sát xem từng gói cue hỗ trợ mạnh nhất cho cấp `nhận diện`, `diễn giải` hay `thực thi`, đồng thời xác định được nơi mô hình phát huy hiệu lực rõ nhất hoặc nơi còn xảy ra thất bại.

### 2.5. Tutorial như cấu trúc học tập trong game

Trong khuôn khổ đề tài này, tutorial của prototype không nên được tổ chức như một chuỗi chỉ dẫn rời rạc, mà phải được xem là một `cấu trúc học tập có điều kiện`. Điều đó có nghĩa là mỗi đoạn tutorial không chỉ có nhiệm vụ “nói cho người chơi biết phải làm gì”, mà phải tạo ra một tiến trình trong đó người chơi:

1. `nhìn thấy` đúng đối tượng cần chú ý
2. `hiểu` đúng ý nghĩa chức năng của đối tượng đó
3. `thực hiện` đúng hành động tương ứng
4. nhận được `phản hồi` đủ rõ để củng cố tri thức vừa hình thành

Từ cách hiểu này, prototype cần được xây thành các `micro-learning sequence`, tức các chuỗi học nhỏ, mỗi chuỗi chỉ tập trung vào một bài học trung tâm, nhưng vẫn nằm trong dòng chơi tự nhiên của game. Đây là điểm phân biệt quan trọng giữa tutorial tích hợp và tutorial chèn ngoài gameplay. Người chơi không rời khỏi game để học; chính gameplay được tổ chức lại để việc học xảy ra có kiểm soát hơn.

#### 2.5.1. Cấu trúc ba cấp trong từng bài học

Mỗi bài học trong prototype cần được tổ chức qua ba cấp tiếp thu đã xác lập ở Chương 1.

Ở cấp `nhận diện`, thiết kế phải bảo đảm rằng đối tượng hoặc tình huống cần học đủ nổi bật để lọt vào trọng tâm chú ý. Trong bài học khai thác tài nguyên, điều này có nghĩa resource đầu tiên phải đủ tách khỏi nền, nằm trên đường đi hợp lý, và không bị cạnh tranh bởi quá nhiều tín hiệu khác. Trong bài học né đòn, điều này có nghĩa chuyển động báo trước của quái phải xuất hiện trong một bối cảnh đủ sạch để người chơi thực sự nhìn thấy nó.

Ở cấp `diễn giải`, thiết kế phải tạo điều kiện để người chơi gắn tín hiệu vừa thấy với một ý nghĩa hành vi cụ thể. Một node khác màu nền chỉ thực sự có giá trị tutorial nếu người chơi hiểu nó là đối tượng nên thử tương tác. Một telegraph chỉ thực sự phát huy tác dụng nếu người chơi hiểu nó là dấu hiệu nguy hiểm sắp xảy ra, chứ không phải một animation trang trí. Do đó, cue ở cấp này phải được đặt trong ngữ cảnh đủ rõ và đủ nhất quán.

Ở cấp `thực thi`, bài học phải cho phép người chơi chuyển phần hiểu biết vừa có thành hành động đúng. Đây là giai đoạn tutorial chứng minh rằng cue không chỉ được thấy và hiểu, mà còn dẫn tới thao tác ổn định. Nếu người chơi nhận ra resource nhưng không biết phải đến gần hay dùng hành động nào để khai thác, hoặc nhìn thấy telegraph nhưng không đủ thời gian để né, thì chuỗi học vẫn bị đứt.

#### 2.5.2. Ba chuỗi học trung tâm của prototype

Dựa trên lát cắt đã chọn, có thể tổ chức prototype thành ba chuỗi học chính.

Chuỗi thứ nhất là `chuỗi học khai thác`. Trọng tâm ở đây là đưa người chơi từ việc nhận ra một object nổi bật trong không gian tới việc hiểu đó là resource và thực hiện đúng tương tác khai thác. Chuỗi này kiểm tra rõ nhất nhóm cue `invitation` và `reinforcement`.

Chuỗi thứ hai là `chuỗi học cảnh báo`. Ở đây, đối tượng học không phải là vật thể tĩnh mà là một tình huống có tính thời gian. Người chơi phải nhìn thấy telegraph, hiểu đó là nguy hiểm báo trước, và phản ứng kịp bằng né, lùi hoặc đổi vị trí. Chuỗi này là nơi nhóm cue `warning` và `predictive` được kiểm tra mạnh nhất.

Chuỗi thứ ba là `chuỗi học định hướng quay về`. Mục tiêu không chỉ là tìm đường, mà là hình thành nhịp quyết định đặc trưng của game: đi ra ngoài, lấy được một lượng giá trị nhất định, rồi quay lại khi rủi ro tăng lên. Chuỗi này gắn chặt với cue `directional`, `emotional priming` và các cue thời gian dạng kích hoạt theo sự kiện.

Ba chuỗi này nên được đặt kế tiếp nhau, nhưng không hoàn toàn tách rời. Chúng cần liên kết thành một nhịp trải nghiệm thống nhất: từ chỗ học nhìn ra resource, sang học đọc nguy hiểm, rồi học đánh giá khi nào nên quay về. Như vậy, tutorial vừa có tính phân đoạn, vừa giữ được logic của gameplay thật.

#### 2.5.3. Nguyên tắc giảm dần hỗ trợ

Một tutorial chỉ thực sự hoàn thành vai trò học tập khi nó có khả năng `rút hỗ trợ` mà không làm mất hoàn toàn khả năng thực thi của người chơi. Vì vậy, prototype không nên giữ nguyên mức nổi bật và mức hỗ trợ ở mọi lần lặp lại.

Ở lượt đầu, cue có thể được làm rõ hơn bình thường, không gian được dọn sạch hơn, và mức áp lực được hạ xuống. Ở lượt sau, thiết kế nên bắt đầu giảm bớt hỗ trợ: cue bớt lộ hơn, tín hiệu cạnh tranh tăng nhẹ, hoặc người chơi phải tự xác định thời điểm hành động thay vì được dắt quá rõ. Mục đích của giai đoạn này là kiểm tra xem tri thức cơ chế đã hình thành hay mới chỉ tồn tại dưới dạng làm theo chỉ dẫn.

Trong khuôn khổ nghiên cứu, nguyên tắc này đặc biệt quan trọng vì nó gắn trực tiếp với bài kiểm tra `transfer`. Nếu một cue chỉ có tác dụng khi được làm quá nổi và đặt trong không gian quá đơn giản, thì hiệu lực của tutorial có thể chỉ dừng ở mức ngắn hạn. Ngược lại, nếu người chơi vẫn thực hiện đúng khi hỗ trợ giảm xuống, có thể xem tri thức cơ chế đã được củng cố ở mức sâu hơn.

#### 2.5.4. Biểu hiện thất bại ở từng cấp

Để tutorial được xem như cấu trúc học tập chứ không chỉ là flow thiết kế, cần chỉ rõ biểu hiện thất bại tương ứng với từng cấp tiếp thu.

`Thất bại ở cấp nhận diện` xảy ra khi người chơi không nhìn ra object hoặc không nhận ra cue quan trọng, dù cue đã được đặt trong không gian. Dấu hiệu quan sát có thể là đi lướt qua resource đầu tiên, không nhìn về phía telegraph, hoặc luôn bỏ qua lối quay về dù nó đã được đánh dấu.

`Thất bại ở cấp diễn giải` xảy ra khi người chơi thấy cue nhưng gán sai ý nghĩa cho nó. Chẳng hạn, họ nhìn thấy một vật thể nổi bật nhưng không hiểu đó là thứ có thể khai thác; hoặc họ quan sát thấy quái đổi pose nhưng không hiểu đó là báo trước cho một đòn đánh.

`Thất bại ở cấp thực thi` xảy ra khi người chơi đã hiểu tín hiệu nhưng không chuyển hóa được thành thao tác đúng. Ví dụ, họ biết phải né khi telegraph xuất hiện nhưng né sai hướng hoặc sai nhịp; họ biết object là resource nhưng dùng sai hành động hoặc bỏ dở tương tác.

Việc phân tách ba dạng thất bại này là nền tảng để giai đoạn thực nghiệm ở mục sau không chỉ đo “thành công hay thất bại”, mà đo được tutorial đang thành công hoặc thất bại ở chính xác mắt xích nào của chuỗi học tập.

### 2.6. Đề xuất thiết kế thực nghiệm

Trong điều kiện thực tế của dự án, nghiên cứu không hướng tới một mô hình thí nghiệm phòng lab với kiểm soát tuyệt đối, mà phù hợp hơn với một `thực nghiệm đối chứng dạng prototype thực địa`. Nói cách khác, game sẽ được phát hành thử nghiệm miễn phí cho cộng đồng game indie, và việc kiểm chứng mô hình sẽ diễn ra trên một lát cắt gameplay ngắn, có cấu trúc rõ, nhưng trong điều kiện chơi gần với bối cảnh phân phối thực tế hơn là điều kiện phòng thí nghiệm.

Từ đặc điểm đó, thiết kế phù hợp nhất là `thiết kế so sánh ba nhóm theo kiểu between-subject`, trong đó mỗi người chơi chỉ tiếp xúc với một phiên bản tutorial. Cách chọn này có lợi thế thực tế ở ba điểm:

- tránh hiệu ứng học lặp lại nếu một người chơi trải qua nhiều phiên bản
- phù hợp với cách phát hành build miễn phí qua cộng đồng
- giảm gánh nặng triển khai so với thiết kế chéo phức tạp hơn

Ba nhóm thực nghiệm được đề xuất như sau:

- `Nhóm A - Baseline Visual`
  - game có tín hiệu thị giác, nhưng chúng chưa được tổ chức chặt theo logic VITM
  - đây là nhóm dùng để kiểm tra trường hợp “có visual nhưng chưa có cấu trúc”
- `Nhóm B - Structured Visual (VITM)`
  - tutorial được tổ chức đầy đủ theo logic VITM
  - cue được phân cấp, nhất quán và gắn trực tiếp với chuỗi học
- `Nhóm C - Text-dominant control`
  - tutorial dựa nhiều hơn vào văn bản và chỉ dẫn trực tiếp
  - visual cue vẫn tồn tại ở mức tối thiểu cần thiết cho gameplay, nhưng không đóng vai trò cấu trúc trung tâm

Trong cả ba nhóm, các yếu tố sau phải được giữ cố định:

- cùng `lát cắt thử nghiệm`
- cùng `bố cục không gian`
- cùng `nhiệm vụ gameplay`
- cùng `object`, `enemy`, `reward` và `input`
- cùng `độ dài phiên chơi` ở mức mục tiêu

Biến độc lập chính của nghiên cứu sẽ nằm ở:

- `cấu hình cue`
- `mức độ nhất quán mã hóa`
- `cách tutorial tổ chức chuỗi học`

Trong điều kiện khả thi của dự án, người tham gia nên được tuyển từ `cộng đồng game indie` và tiếp cận prototype dưới hình thức `phát hành miễn phí`. Đây là cách triển khai phù hợp với nguồn lực hiện có, đồng thời tương thích với mục tiêu của đề tài là kiểm tra tính khả dụng của mô hình trong bối cảnh phát triển game độc lập. Tuy nhiên, vì đây là nguồn mẫu tiện lợi, nghiên cứu cần ghi nhận rõ rằng mẫu có thể không đại diện cho toàn bộ quần thể người chơi game nói chung. Giá trị chính của đợt kiểm chứng đầu tiên vì thế nằm ở việc xác lập `hiệu lực ban đầu` của mô hình, chứ chưa phải khẳng định khả năng khái quát tuyệt đối.

Về quy trình, mỗi người tham gia sẽ:

1. nhận một phiên bản prototype duy nhất
2. chơi qua lát cắt tutorial đã xác định
3. hoàn thành một chuỗi nhiệm vụ ngắn tương ứng với ba bài học trung tâm
4. cung cấp dữ liệu hành vi trong lúc chơi, kết hợp với phản hồi sau phiên chơi

Trong điều kiện dự án nhỏ và phát hành miễn phí, việc thu dữ liệu nên ưu tiên các phương án nhẹ nhưng đáng tin cậy:

- log thời gian thực hiện các mốc hành vi
- đếm số lỗi thao tác và số lần bỏ qua cue
- ghi nhận việc hoàn thành hay thất bại ở từng chuỗi học
- thu phản hồi ngắn sau phiên chơi để hỗ trợ giải thích dữ liệu hành vi

Điểm quan trọng về phương pháp là nghiên cứu này không chỉ so sánh “phiên bản nào dễ hơn”, mà phải so sánh `phiên bản nào giúp người chơi hình thành tri thức cơ chế rõ hơn`. Vì vậy, phần thiết kế thực nghiệm phải luôn bám vào ba cấp tiếp thu đã xác lập ở mục 2.5.

### 2.7. Tiêu chí đánh giá

Để tương thích với cấu trúc lý luận của đề tài, tiêu chí đánh giá không nên chỉ dừng ở mức “hoàn thành hay không hoàn thành”, mà phải được tổ chức theo các cấp độ tiếp thu và theo điều kiện thực tế của prototype.

Trước hết là `chỉ số nhận diện`. Nhóm chỉ số này nhằm trả lời câu hỏi người chơi có nhìn ra đúng cue hay không. Trong prototype, có thể sử dụng các chỉ báo như:

- thời gian nhận ra object đầu tiên cần tương tác
- số lần đi ngang qua resource hoặc exit mà không chú ý
- số lần bỏ lỡ telegraph trước khi bị trúng đòn

Thứ hai là `chỉ số diễn giải`. Nhóm này nhằm đo người chơi có hiểu đúng ý nghĩa của cue hay không. Trong điều kiện dự án nhỏ, việc đo lường không nên quá nặng về khảo sát dài, mà có thể kết hợp giữa hành vi và phản hồi ngắn sau phiên chơi. Những chỉ báo phù hợp gồm:

- số lần người chơi nhìn thấy object nhưng không thử tương tác
- số lần phản ứng sai loại hành vi trước cue cảnh báo
- câu trả lời ngắn sau phiên chơi về việc người chơi nghĩ cue đó dùng để làm gì

Thứ ba là `chỉ số thực thi`. Đây là lớp chỉ số gần gameplay nhất, dùng để đo việc người chơi chuyển phần hiểu biết thành thao tác đúng. Những chỉ báo cần thiết gồm:

- thời gian thực hiện đúng cơ chế lần đầu
- số lỗi thao tác trước khi thực hiện đúng
- số lần dính hit trong phần học né / cảnh báo
- thời gian hoàn thành vòng nhỏ của lát cắt thử nghiệm

Thứ tư là `chỉ số chuyển giao`. Đây là nhóm chỉ số đặc biệt quan trọng nếu nghiên cứu muốn chứng minh tutorial không chỉ tạo ra hành vi làm theo. Trong điều kiện thực tế của dự án, bài kiểm tra chuyển giao có thể được thiết kế nhẹ nhưng vẫn có giá trị, chẳng hạn:

- lặp lại cùng cơ chế trong bối cảnh ít hỗ trợ hơn
- thay đổi nhẹ bố cục không gian nhưng giữ nguyên logic cue
- yêu cầu người chơi thực hiện lại hành vi sau khi cue trực tiếp đã giảm bớt

Nếu người chơi vẫn thực hiện đúng trong các điều kiện này, có thể suy ra tri thức cơ chế đã vượt qua mức bắt chước tức thời.

Thứ năm là `chỉ số ghi nhớ muộn`, nhưng phần này cần được xử lý phù hợp với nguồn lực thực tế. Với một prototype phát miễn phí trong cộng đồng game indie, việc tổ chức bài kiểm tra ghi nhớ muộn nhiều ngày sau là khả thi nhưng không nên quá tham. Một phương án thực tế hơn là:

- mời một phần người chơi quay lại chơi một thử thách ngắn tương tự sau một khoảng thời gian
- hoặc kiểm tra lại cùng cơ chế ở một đoạn sau mà không nhắc lại trực tiếp

Nếu không triển khai được đầy đủ, nghiên cứu cần ghi rõ đây là giới hạn phương pháp, không nên giả định mức kiểm soát cao hơn khả năng thực có của dự án.

Ngoài các chỉ số trung tâm trên, có thể sử dụng `chỉ số hỗ trợ diễn giải` như:

- mức độ rõ ràng tự báo cáo của tutorial
- mức độ người chơi cảm thấy bị dạy bằng chữ hay bằng thế giới game
- mức độ tự tin của người chơi khi lặp lại cơ chế

Tuy nhiên, các chỉ số tự báo cáo chỉ nên đóng vai trò bổ trợ. Trọng tâm đánh giá của đề tài vẫn phải đặt ở dữ liệu hành vi, vì mục tiêu chính là kiểm tra hiệu lực của cấu hình tín hiệu và cấu trúc tutorial, chứ không chỉ đo cảm nhận chủ quan.

Từ các tiêu chí trên, có thể thấy phần đánh giá của nghiên cứu không hướng tới việc tìm ra “phiên bản dễ nhất”, mà hướng tới việc xác định phiên bản nào hỗ trợ tốt hơn cho quá trình nhận diện, diễn giải, thực thi và chuyển giao cơ chế. Đây mới là thước đo phù hợp với bản chất của mô hình VITM.

---

## CHƯƠNG 3: THIẾT KẾ GAME

Chương này hiện được giữ ở trạng thái `khung triển khai đang xây dựng`. Mục tiêu của chương không phải là trình bày một bản thiết kế game đã hoàn thiện, mà là xác lập trước cấu trúc nghiên cứu - thiết kế dự kiến để chuyển mô hình ở Chương 1 và Chương 2 thành một prototype có thể thực hiện được trong dự án thật.

Do game hiện vẫn đang trong quá trình phát triển, nhiều chi tiết hệ thống, content và pipeline sản xuất chưa đủ ổn định để coi như dữ liệu cuối cùng. Vì vậy, Chương 3 được hiểu như một `khung thiết kế dự kiến`, có chức năng:

- ghi lại phần nào của game sẽ được dùng làm prototype nghiên cứu
- xác định các cấu phần thiết kế cần xây để phục vụ kiểm chứng
- dự kiến quy trình triển khai, log dữ liệu và đánh giá
- chỉ ra cách kết quả nghiên cứu có thể quay trở lại phục vụ sản phẩm

### 3.1. Vai trò của game trong giai đoạn hiện tại

Ở giai đoạn hiện tại, game không được xem là một sản phẩm đã hoàn chỉnh dùng để “gắn thêm nghiên cứu”, mà là một hệ đang xây dựng, trong đó một phần lõi sẽ được tách ra thành `prototype nghiên cứu`. Theo đó, game đồng thời giữ ba vai trò:

- `bối cảnh triển khai`
- `phương tiện kiểm chứng`
- `nguồn giá trị ứng dụng cho sản phẩm`

Việc xác định ba vai trò này có ý nghĩa quan trọng. Nếu chỉ xem game là ví dụ minh họa, nghiên cứu sẽ khó tạo ra giá trị quay ngược cho dự án. Nếu chỉ xem game là sản phẩm, nghiên cứu lại dễ bị hòa tan vào tiến độ làm game thông thường. Vì vậy, trong giai đoạn hiện tại, cần giữ nguyên tắc: phần nào phục vụ kiểm chứng mô hình phải được ưu tiên rõ ràng về chức năng nghiên cứu, nhưng vẫn phải đủ tương thích để sau này nhập trở lại pipeline sản phẩm.

### 3.2. Khung prototype dự kiến

Trên cơ sở các mục trước, prototype dự kiến hiện được xác định ở mức khung như sau:

- một `khu an toàn gần base`
- một `resource node đầu tiên`
- một `lối vào hang đầu tiên`
- một `đoạn hang đầu tiên` với nguy hiểm nhẹ
- một `điểm hoặc tuyến quay về an toàn`

Khung này chưa được hiểu là thiết kế scene cuối cùng, mà là `bộ điều kiện tối thiểu` để nghiên cứu có thể diễn ra. Cấu trúc không gian cần đủ để người chơi đi qua trọn một vòng học:

`nhìn thấy -> hiểu ý nghĩa -> thử hành động -> nhận phản hồi -> lặp lại trong điều kiện giảm hỗ trợ -> quay về`

Ở giai đoạn hiện tại, phần cần tiếp tục nghiên cứu sâu không phải là chi tiết mỹ thuật hay bố cục map cuối cùng, mà là liệu cấu trúc không gian nào sẽ cho phép quan sát rõ nhất ba chuỗi học trung tâm đã xác lập ở Chương 2.

### 3.3. Các cấu phần thiết kế cần được xây tiếp

Dựa trên mục tiêu nghiên cứu hiện tại, có thể xác định trước các cấu phần mà prototype bắt buộc phải có, dù chi tiết triển khai vẫn còn để mở:

- `Cue Bible` ở mức tối thiểu
  - cue cho resource đầu tiên
  - cue cho hướng đi chính
  - cue cho vùng an toàn và vùng rủi ro
  - cue cho telegraph của mối nguy đầu tiên
  - cue cho phản hồi đúng / sai sau hành động
- `tutorial flow` cho ba nhóm thực nghiệm
  - baseline visual
  - structured visual theo VITM
  - text-dominant
- `hệ log hành vi`
  - ghi thời điểm nhận diện
  - ghi lỗi thao tác
  - ghi thời điểm hoàn thành từng chuỗi học
  - ghi dấu hiệu chuyển giao ở điều kiện ít hỗ trợ hơn
- `lớp thu phản hồi ngắn`
  - dùng để hỗ trợ giải thích dữ liệu hành vi

Ở thời điểm hiện tại, các cấu phần này mới được xác định ở cấp `khung nghiên cứu dự kiến`. Chúng chưa phải hạng mục đã hoàn thành, và việc triển khai thực tế sẽ phụ thuộc vào tiến độ phát triển của bản game thử nghiệm.

### 3.4. Hướng nghiên cứu - thiết kế tiếp theo

Từ trạng thái hiện tại, Chương 3 cần tiếp tục được phát triển theo ba nhánh song song.

Nhánh thứ nhất là `hoàn thiện prototype nghiên cứu`. Đây là nhánh ưu tiên trước, gồm việc chốt lát cắt thử nghiệm, khóa các cue trung tâm, và xác định phiên bản đối chứng có thể build được với nguồn lực hiện có.

Nhánh thứ hai là `hoàn thiện công cụ thu dữ liệu`. Một prototype phục vụ luận văn không chỉ cần chơi được, mà cần log được những chỉ số tương ứng với ba cấp tiếp thu. Nếu thiếu lớp log và ghi nhận hành vi, việc kiểm chứng mô hình sẽ rất khó đi tới kết luận có giá trị.

Nhánh thứ ba là `nối kết quả quay trở lại game`. Ngay cả khi nghiên cứu mới ở giai đoạn đầu, cần chuẩn bị trước cách các cue, nguyên tắc phân cấp và logic tutorial của prototype có thể được tái sử dụng về sau trong onboarding, combat readability, hazard design và world signaling của game.

### 3.5. Ghi chú trạng thái hiện tại của Chương 3

Tại thời điểm hiện tại, `Chương 3` chưa phải là chương báo cáo thành quả triển khai xong, mà là chương ghi nhận `khung thiết kế đang được chuẩn bị`. Điều này cần được nêu rõ để tránh tạo cảm giác rằng nghiên cứu đã có prototype hoàn chỉnh và dữ liệu thực nghiệm hoàn tất.

Có thể xem trạng thái hiện tại của chương như sau:

- `đã có`: khung lý thuyết, logic ứng dụng, lát cắt thử nghiệm đề xuất, cấu trúc đối chứng sơ bộ, nhóm chỉ số đánh giá
- `đang xây`: prototype thử nghiệm, cue bible tối thiểu, tutorial flow từng nhóm, hệ log hành vi, kế hoạch phát hành miễn phí cho cộng đồng game indie
- `chưa có kết quả cuối`: dữ liệu thực nghiệm, phân tích so sánh ba nhóm, kết luận hiệu lực cuối cùng của mô hình

Việc giữ Chương 3 ở dạng mở như vậy phù hợp hơn với thực trạng của dự án, đồng thời giúp đề tài trung thực về mặt phương pháp.

---

## KẾT LUẬN ĐỊNH HƯỚNG

Ở trạng thái hiện tại, đề tài `Nghiên cứu Tín hiệu Thị giác và ứng dụng thiết kế tutorial game` đã hình thành được khung lý luận tương đối rõ về mối quan hệ giữa `tín hiệu thị giác`, `tutorial` và `quá trình tiếp thu cơ chế`. Trên nền đó, đề tài cũng đã bước đầu xác định được bối cảnh ứng dụng phù hợp, lát cắt thử nghiệm khả thi, cùng các tiêu chí đánh giá có thể triển khai trong điều kiện thực tế của một dự án game indie.

Tuy nhiên, ở thời điểm này, nghiên cứu vẫn đang ở giai đoạn `xây dựng khung và chuẩn bị triển khai`, chưa đi tới giai đoạn có thể rút ra kết luận cuối cùng về hiệu lực của mô hình. Prototype thử nghiệm, cue bible tối thiểu, hệ log hành vi và kế hoạch phát hành miễn phí cho cộng đồng game indie hiện vẫn là các hạng mục đang được tiếp tục hoàn thiện.

Vì vậy, phần kết luận ở giai đoạn này chỉ nên xác nhận ba điểm:

- đề tài đã xác lập được nền lý luận và cấu trúc nghiên cứu đủ rõ để tiếp tục triển khai
- game hiện tại là một trường hợp ứng dụng có tiềm năng thực sự cho việc kiểm chứng mô hình
- kết luận cuối cùng về hiệu lực của VITM cần chờ kết quả từ quá trình xây prototype, phát hành thử nghiệm và thu thập dữ liệu đối chứng

Theo đó, hướng đi tiếp theo phù hợp nhất không phải là đóng lại vấn đề bằng một kết luận khẳng định, mà là tiếp tục chuyển từ `khung nghiên cứu` sang `giai đoạn kiểm chứng thực tế`, với các bước ưu tiên gồm:

- hoàn thiện prototype thử nghiệm
- hoàn thiện cue bible và tutorial flow cho ba nhóm
- triển khai log dữ liệu hành vi
- phát hành bản thử nghiệm miễn phí cho cộng đồng game indie
- và chỉ sau đó mới tiến hành phân tích, so sánh, kết luận

Nói cách khác, ở giai đoạn hiện tại, giá trị của đề tài nằm ở việc đã xây được một `khung nghiên cứu khả thi`, còn giá trị kiểm chứng cuối cùng vẫn là phần đang mở.
