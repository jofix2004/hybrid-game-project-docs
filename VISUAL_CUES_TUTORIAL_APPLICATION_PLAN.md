Project Code: HYBRID
Version: 0.8 (Draft)
Author: null
Date: 13/03/2026

# Kế hoạch ứng dụng đề tài Visual Cues Tutorial vào game hiện tại

Tài liệu này dùng để nối trực tiếp đề tài `Nghiên cứu Tín hiệu thị giác và ứng dụng thiết kế tutorial game` với game hiện tại đang được xây trong `GAME_PROJECT_DOCS`.

Mục tiêu của tài liệu không phải là tóm tắt lại toàn bộ luận văn, mà là:

- xác định game hiện tại sẽ được dùng như `sản phẩm thử nghiệm` theo cách nào
- chỉ ra phần nào của game phù hợp nhất để kiểm chứng mô hình
- lập kế hoạch phát triển prototype nghiên cứu
- chỉ ra kết quả nghiên cứu sẽ giúp thiết kế game hiện tại ở đâu

## 1. Tóm tắt ngắn đề tài nghiên cứu

Theo bản thảo `Visual Cues Tutorial V12`, trục nghiên cứu nằm ở mối quan hệ giữa hai lớp thường bị tách rời trong thiết kế game:

- `Tín hiệu thị giác`
- `Tutorial`

Đề tài coi tutorial không chỉ là chuỗi text hay prompt hướng dẫn, mà là một kiến trúc tổ chức học tập. Trong kiến trúc đó, tín hiệu thị giác phải trở thành một phần cấu trúc của quá trình:

`Cấu hình tín hiệu thị giác -> Nhận diện -> Diễn giải -> Thực thi cơ chế -> Hình thành tri thức cơ chế`

Đóng góp cốt lõi của đề tài gồm:

- định nghĩa vận hành cho `Tín hiệu Thị giác`
- xây dựng `taxonomy ba chiều`
- đề xuất mô hình `Visual-Integrated Tutorial Model (VITM)`
- kiểm chứng bằng prototype có đối chứng

## 2. Vì sao game hiện tại phù hợp để làm sản phẩm thử nghiệm

Game hiện tại rất phù hợp với đề tài vì nó có đầy đủ các điều kiện cần để kiểm chứng VITM:

### 2.1. Game có không gian đọc tín hiệu rõ ràng

Game là:

- `2D`
- `survival`
- `co-op`
- `dungeon theo chiều sâu`

Trong kiểu game này, người chơi liên tục phải đọc:

- vật thể nào tương tác được
- đường nào nên đi
- chỗ nào nguy hiểm
- quái sắp làm gì
- lúc nào nên rút
- đâu là resource đáng lấy

Đây chính là môi trường lý tưởng để nghiên cứu `visual cue configuration`.

### 2.2. Game có nhu cầu tutorial tự nhiên

Game hiện tại không phải dạng nhấn nút đơn giản là hiểu ngay. Nó có nhiều lớp cần học:

- nhặt và khai thác
- survival pressure
- đường đi xuống hang
- phân biệt an toàn / nguy hiểm
- đọc telegraph của quái
- hiểu giá trị của việc quay về
- về sau là mana, machine, gate

Điều này khiến tutorial trở thành một vấn đề thiết kế thật, không phải phần phụ.

### 2.3. Game có lợi thế cho thực nghiệm có đối chứng

Có thể tạo nhiều phiên bản tutorial cho cùng một nội dung cơ chế mà không cần đổi bản sắc game:

- bản dựa nhiều vào text
- bản có visual cue nhưng không theo cấu trúc chặt
- bản tích hợp đầy đủ theo VITM

Vì vậy game này phù hợp để làm `prototype thực nghiệm`, không chỉ là ví dụ minh họa.

## 3. Cách đặt lại mục tiêu ứng dụng vào game hiện tại

Trong ngữ cảnh dự án game, đề tài này nên được hiểu là:

`Xây một hệ visual tutorial có cấu trúc, giúp người chơi học cơ chế bằng nhìn - hiểu - làm, thay vì phụ thuộc chủ yếu vào chữ hoặc trial-and-error mù.`

Mục tiêu ứng dụng vào game hiện tại gồm 3 lớp:

### 3.1. Mục tiêu nghiên cứu

- kiểm chứng mô hình VITM trong một bối cảnh game 2D survival dungeon
- đo xem cấu trúc cue tốt hơn có giúp người chơi học cơ chế nhanh hơn, ít lỗi hơn và nhớ lâu hơn không

### 3.2. Mục tiêu thiết kế

- xây một ngôn ngữ tín hiệu thị giác dùng được thật cho game
- giảm phụ thuộc vào text tutorial
- giảm onboarding friction
- tăng readability khi chơi thật

### 3.3. Mục tiêu sản phẩm

- tạo ra một vertical slice vừa đủ để đem test
- slice này không cần đại diện toàn bộ game, nhưng phải đại diện đúng trục lõi của game

## 4. Phạm vi prototype đề xuất

Không nên dùng toàn bộ game hiện tại để kiểm chứng đề tài ngay lập tức. Phạm vi prototype nên hẹp, đo được và bám sát loop lõi.

### 4.1. Nên chọn một `tutorial slice` rất rõ

Prototype đề xuất nên chỉ dạy 3 nhóm cơ chế đầu tiên:

1. `Nhận ra vật thể tương tác được và thực hiện khai thác cơ bản`
2. `Nhận ra nguy hiểm và phản ứng đúng với telegraph / cue cảnh báo`
3. `Hiểu nhịp đi - lấy - quay về an toàn`

Đây là lựa chọn tốt vì:

- nó chạm đúng lõi game
- không cần chờ toàn bộ machine / mana / gate hoàn chỉnh
- vẫn đủ giàu để đo tác dụng của visual cues

### 4.2. Bối cảnh thử nghiệm phù hợp nhất

Slice nên đặt ở:

- `surface gần base`
- `cửa vào hang đầu tiên`
- `đoạn hang đầu tiên`

Đây là vùng tốt nhất để kiểm chứng vì:

- vừa có không gian an toàn tương đối
- vừa có tài nguyên tương tác
- vừa có nguy hiểm nhẹ
- vừa có ý nghĩa thật trong loop game

### 4.3. Không nên nhét quá nhiều hệ vào prototype đầu

Prototype nghiên cứu ban đầu không nên ôm:

- mana network đầy đủ
- gate milestone đầy đủ
- machine / automation
- co-op sâu nhiều vai

Những phần này có thể là `extension phase`, không phải lõi của đợt kiểm chứng đầu tiên.

## 5. Mapping trực tiếp từ đề tài sang game

## 5.1. Taxonomy ba chiều áp vào game

### A. Chiều tồn tại

Trong game hiện tại, tín hiệu có thể được mã hóa qua:

- `Màu sắc`
  - tài nguyên khác màu nền
  - vật thể quan trọng có palette nổi hơn
  - trạng thái nguy hiểm dùng màu cảnh báo rõ
- `Độ sáng và tương phản`
  - lối đi, cửa hang, vật tương tác hoặc điểm quan trọng có độ tách nền tốt hơn
- `Hình khối`
  - vật thể có thể khai thác, lootable, hazard, exit có silhouette khác nhau
- `Chuyển động`
  - rung nhẹ, phát sáng, blink, telegraph trước đòn, chuyển động định hướng
- `Vị trí và bố cục`
  - đặt vật thể học cơ chế ở nơi người chơi không thể bỏ lỡ trong nhịp đầu

### B. Chiều chức năng

Trong game hiện tại, cue có thể chia theo chức năng:

- `Cảnh báo`
  - quái sắp đánh
  - hazard sắp kích hoạt
  - vùng nguy hiểm
- `Định hướng`
  - đường xuống hang
  - lối quay về
  - mục tiêu tutorial hiện tại
- `Mời gọi tương tác`
  - node khai thác đầu tiên
  - vật thể nhặt được
  - chỗ mở lối
- `Củng cố phản hồi`
  - hit confirm khi khai thác đúng
  - feedback khi né hoặc rút đúng
  - phản hồi khi nhặt đúng vật
- `Khởi phát trạng thái cảm xúc`
  - làm người chơi thấy an toàn, dè chừng, hoặc biết “đây là mốc đáng chú ý”

### C. Chiều thời gian

Trong game hiện tại, cue nên được chia rõ:

- `Liên tục`
  - exit, safe zone, resource silhouette
- `Dự báo`
  - telegraph đòn đánh
  - rung / sáng trước nguy cơ
- `Kích hoạt theo sự kiện`
  - vật thể bắt đầu sáng khi vào gần
  - cue nhắc quay về khi người chơi đạt ngưỡng risk nhất định
- `Phản ứng`
  - hit feedback
  - loot feedback
  - fail feedback khi làm sai

## 5.2. Tutorial như kiến trúc học tập áp vào game

Prototype nên dạy theo 3 cấp tiếp thu đúng như đề tài:

1. `Nhận diện`
   - người chơi nhìn ra thứ gì là quan trọng
2. `Diễn giải`
   - người chơi hiểu tín hiệu đó có nghĩa gì
3. `Thực thi`
   - người chơi làm đúng hành động

Với game hiện tại, điều này có thể chuyển thành:

- thấy node khác thường
- hiểu node này là thứ cần tương tác
- dùng tool đúng để khai thác

hoặc:

- thấy quái / hazard phát telegraph
- hiểu đây là dấu hiệu nguy hiểm
- né hoặc rút đúng

## 6. Đề xuất Visual-Integrated Tutorial Model cho prototype game

## 6.1. Cue Layer

Xây thư viện cue nhỏ nhưng nhất quán cho prototype:

- cue cho `resource interactable`
- cue cho `đường đi chính`
- cue cho `safe / unsafe`
- cue cho `enemy telegraph`
- cue cho `return / extraction`

## 6.2. Structuring Layer

Tổ chức tutorial thành chuỗi ngắn:

1. thấy thứ cần làm
2. làm thử trong điều kiện an toàn hơn bình thường
3. nhận feedback rõ
4. lặp lại một lần trong bối cảnh hơi khác
5. bỏ bớt hỗ trợ và kiểm tra người chơi có tự làm lại được không

## 6.3. Interpretive Loop

Vòng lặp trung tâm trong prototype cần đọc được:

`trình bày cue -> người chơi chú ý -> người chơi diễn giải -> người chơi hành động -> game phản hồi -> người chơi cập nhật tri thức`

Nếu thất bại ở bước nào, thiết kế phải có cơ chế điều chỉnh:

- tăng độ nổi bật
- giảm nhiễu
- hạ áp lực
- lặp lại tình huống ở điều kiện dễ hơn

## 7. Thiết kế thực nghiệm đề xuất cho game hiện tại

## 7.1. Ba nhóm thử nghiệm

Giữ đúng tinh thần bản thảo đề tài:

### Nhóm A. Baseline Visual

- có dùng visual cues
- nhưng cue chưa có phân cấp rõ
- chưa nhất quán
- chưa có logic hỗ trợ / rút hỗ trợ đúng kiểu VITM

### Nhóm B. Structured Visual - VITM

- cue được thiết kế theo taxonomy và nguyên tắc VITM
- có cấu trúc nhận diện -> diễn giải -> thực thi -> feedback -> chuyển giao

### Nhóm C. Text-dominant

- dựa nhiều vào chữ hoặc prompt văn bản
- visual cue chỉ đóng vai trò phụ

## 7.2. Những gì phải giữ cố định giữa các nhóm

Để so sánh có ý nghĩa, phải giữ cố định:

- cùng một không gian
- cùng một mục tiêu cơ chế
- cùng một loại quái / hazard / resource
- cùng nhịp nhiệm vụ
- cùng input
- cùng reward

Khác biệt chính chỉ nên nằm ở:

- cách cấu hình cue
- cách tổ chức tutorial

## 7.3. Chỉ số đo phù hợp với game hiện tại

Các chỉ số nên đo:

- thời gian người chơi nhận ra vật tương tác đầu tiên
- thời gian hoàn thành hành động đúng lần đầu
- số lỗi thao tác
- số lần bỏ qua cue
- số lần dính hit trong phần học né / cảnh báo
- thời gian từ lúc vào scene tới lúc rút về đúng điểm an toàn
- khả năng lặp lại hành động trong bối cảnh ít hỗ trợ hơn

Nếu có điều kiện, nên thêm:

- test chuyển giao sang một room khác
- test ghi nhớ muộn ở buổi sau

## 8. Lộ trình phát triển đề tài bằng game hiện tại

## Giai đoạn 1. Khóa phạm vi nghiên cứu ứng dụng

Đầu ra cần có:

- chọn 3 cơ chế cho prototype
- khóa không gian thử nghiệm
- khóa nhóm biến độc lập và biến phụ thuộc

Đề xuất chốt:

- cơ chế 1: nhận ra và khai thác resource cơ bản
- cơ chế 2: nhận ra cảnh báo nguy hiểm và né
- cơ chế 3: hiểu logic quay về an toàn

## Giai đoạn 2. Xây `Cue Bible` cho prototype

Đầu ra cần có:

- bảng cue theo taxonomy
- rule màu sắc
- rule độ sáng / tương phản
- rule silhouette
- rule chuyển động
- rule feedback

Đây là bước rất quan trọng vì nếu không có `Cue Bible`, nhóm A và nhóm B sẽ khó tách ra đúng nghĩa nghiên cứu.

## Giai đoạn 3. Thiết kế 3 phiên bản tutorial

Đầu ra cần có:

- bản A
- bản B
- bản C

Mỗi bản phải dạy đúng cùng một cơ chế, chỉ khác ở cấu trúc trình bày.

## Giai đoạn 4. Tích hợp vào vertical slice của game

Đầu ra cần có:

- một build ngắn chơi được
- có vào scene
- có học cơ chế
- có thử lại
- có đoạn chuyển giao
- có kết thúc một vòng nhỏ

## Giai đoạn 5. Playtest và thu dữ liệu

Đầu ra cần có:

- log thời gian
- log lỗi
- quan sát hành vi
- câu hỏi phản hồi sau test

## Giai đoạn 6. Phân tích và quay ngược lại GDD

Kết quả nghiên cứu không chỉ dùng cho luận văn, mà phải quay lại cải thiện game:

- sửa onboarding
- sửa world signal
- sửa combat telegraph
- sửa readability của interactable
- sửa rule giảm hỗ trợ theo tiến trình

## 9. Đề tài này giúp game hiện tại như thế nào?

## 9.1. Giúp onboarding bớt phụ thuộc chữ

Game hiện tại có khá nhiều lớp để học. Nếu chỉ dựa vào text, người chơi dễ:

- bỏ qua
- đọc nhưng không nhớ
- hoặc hiểu mà không làm được

Nghiên cứu này giúp chuyển tutorial sang dạng:

- thấy
- hiểu
- làm

## 9.2. Giúp survival và dungeon dễ đọc hơn

Game sống bằng:

- risk / reward
- đi sâu
- quyết định tham hay rút

Nếu tín hiệu thị giác yếu, người chơi sẽ không phân biệt rõ:

- đâu là tài nguyên đáng lấy
- đâu là nguy hiểm thật
- lúc nào đang lời to nhưng cũng đang sắp chết

Ứng dụng đề tài giúp tăng readability ở chính lõi game.

## 9.3. Giúp combat và hazard công bằng hơn

Một combat khó vẫn được chấp nhận nếu tín hiệu rõ.

Nghiên cứu này giúp:

- chuẩn hóa telegraph
- giảm chết vì không đọc ra game muốn nói gì
- tăng cảm giác “mình sai” thay vì “game chơi bẩn”

## 9.4. Giúp game giữ immersion tốt hơn

Nếu tutorial được tích hợp vào world, người chơi học cơ chế mà không bị cảm giác “bị kéo ra khỏi game”.

Điều này đặc biệt hợp với game hiện tại vì bối cảnh `đảo hoang + hang sâu + low-tech steampunk magitech` rất cần cue diegetic và grounded.

## 9.5. Giúp về lâu dài cho content pipeline

Khi đã có framework cue rõ, nhóm content về sau có thể dùng lại cho:

- biome mới
- resource mới
- quái mới
- hazard mới
- machine và mana cue
- gate và boss milestone

Nói cách khác, đề tài không chỉ giúp `tutorial đầu game`, mà có thể trở thành `ngôn ngữ đọc game` cho toàn bộ sản phẩm.

## 10. Kết luận định hướng

Game hiện tại không nên chỉ được dùng như một ví dụ minh họa cho đề tài. Nó nên được dùng như:

- `prototype nghiên cứu có đối chứng`
- `vertical slice kiểm chứng VITM`
- và đồng thời là `bước đầu chuẩn hóa visual language` cho chính sản phẩm game

Hướng làm đúng là:

- không ôm toàn bộ game
- chọn một lát cắt thật đúng lõi
- đo bằng ba nhóm rõ ràng
- rồi dùng kết quả để quay ngược trở lại nâng chất lượng onboarding, readability và combat của game hiện tại
