Project Code: HYBRID
Version: 0.8 (Draft)
Author: null
Date: 26/01/2026

# 07_QUESTIONS_LEVEL_3

Tài liệu này là bản trả lời cấp 3, dùng để chốt khung gameplay cốt lõi sau khi bản sắc và trải nghiệm người chơi đã đủ chắc.

## Mục tiêu của cấp độ này

- Chốt người chơi làm gì lặp đi lặp lại ở từng nhịp chơi.
- Tách rõ vòng lặp hành động ngắn, vòng lặp phiên chơi và vòng lặp tiến trình dài hơn.
- Làm rõ điểm ra quyết định quan trọng nhất: đi tiếp hay quay về.

## Cách dùng tài liệu này

- Tài liệu này mô tả loop, không đi sâu vào công thức hay số liệu.
- Mỗi loop phải nối được về cảm giác đã chốt ở cấp 2.
- Nếu một hệ thống không nuôi được ít nhất một loop ở đây, cần xem lại vai trò của nó.

## Mục 1: Vòng lặp hành động ngắn

### Điều cần mô tả

- Trong 30 đến 60 giây, người chơi thường làm gì.
- Hành động nào lặp lại nhiều nhất khi ở ngoài hiện trường.
- Hành động nào tạo cảm giác “tay đang luôn bận”.

### Đầu ra mong muốn

- Một đoạn `Action Loop` ngắn, rõ, có thể hình dung ngay trên tay người chơi.

### Trả lời

Trong 30 đến 60 giây chơi điển hình, người chơi thường di chuyển qua khu vực gần, quan sát vật thể có thể tương tác, đập hoặc thu nhặt tài nguyên, né một mối nguy nhỏ, xử lý hoặc tránh kẻ địch vừa sức, rồi quyết định nên tiến thêm vài bước hay quay lại chỗ an toàn hơn. Tay người chơi nên luôn bận với những việc rất thực dụng: nhặt đồ, giữ để chặt cây, phá đá, di chuyển, sắp xếp kho đồ, nhìn lượng đồ mang theo, nhìn tình trạng của mình và ăn uống nếu cần. Vòng ngắn này phải tạo cảm giác thế giới luôn có thứ để sờ vào, nhưng mỗi tương tác nhỏ đều đẩy người chơi gần hơn tới một quyết định lớn hơn.

## Mục 2: Core Gameplay Loop

### Điều cần mô tả

- Vòng lặp lớn nhất mà game muốn người chơi lặp lại.
- Người chơi ra ngoài vì điều gì, quay về vì điều gì.
- Sau khi quay về, điều gì khiến họ mạnh hơn hoặc sẵn sàng hơn.

### Đầu ra mong muốn

- Một đoạn `Core Gameplay Loop` và một sơ đồ mũi tên ngắn.

### Trả lời

Core loop của game là chuẩn bị một chuyến đi, ra ngoài thu nhặt và khai thác, đẩy xuống sâu hơn để đổi lấy phần thưởng tốt hơn, rồi mang những gì kiếm được về căn cứ để biến thành khả năng sinh tồn và khả năng đi tiếp. Người chơi không ra ngoài chỉ để sống sót qua ngày, mà để lấy thứ mình chưa có, mở ra thứ mình chưa chạm tới và chuẩn bị cho một lần đi sâu hơn sau đó. Họ quay về vì túi đồ đã có giá trị, tài nguyên hồi phục đang mỏng dần, hoặc vì vừa chạm tới một mốc đủ lời để chưa cần liều thêm. Khi quay về, chiến lợi phẩm được đổi thành công cụ tốt hơn, chỗ ở ổn hơn, dự trữ dày hơn, utility mới hơn hoặc khả năng tiếp cận tầng sâu hơn.

`Vùng an toàn -> Chuẩn bị -> Đi ra ngoài -> Thu nhặt và khai thác -> Gặp nguy hiểm -> Quyết định tham hay rút -> Mang loot về -> Nâng khả năng sống sót và đi sâu -> Lặp lại`

## Mục 3: Short Session Loop

### Điều cần mô tả

- Một phiên ngắn 15 đến 30 phút nên đủ để hoàn thành điều gì.
- Người chơi online ít thời gian vẫn phải cảm thấy mình tiến được ra sao.
- Kết thúc phiên ngắn, điều gì còn đọng lại.

### Đầu ra mong muốn

- Một đoạn `Short Session Loop`.

### Trả lời

Một phiên ngắn nên cho người chơi đủ thời gian để chọn một mục tiêu cụ thể, làm xong nó và thấy phiên đó thật sự có tiến triển, kể cả khi chơi một mình. Họ có thể đi lấy một nhóm tài nguyên gần, chế xong một món đang thiếu, mở thêm một đoạn đường xuống, dựng thêm một utility ở căn cứ hoặc thử xuống sâu hơn một nhịp ngắn rồi quay về an toàn. Nếu đang chơi co-op, phiên ngắn cũng có thể là hỗ trợ đồng đội chuẩn bị cho chuyến đi dài hơn, nhưng đó nên là một lựa chọn thêm chứ không phải mặc định của loop này. Phiên ngắn không cần có cao trào lớn, nhưng phải kết thúc bằng cảm giác “mình đã tiến thêm được một nấc rõ ràng”.

## Mục 4: Long Progression Loop

### Điều cần mô tả

- Qua nhiều phiên chơi, người chơi đi từ trạng thái nào tới trạng thái nào.
- Điều gì mở ra từng lớp nội dung mới.
- Vì sao mỗi lần tiến lên lại đáng giá.

### Đầu ra mong muốn

- Một đoạn `Long Progression Loop`.

### Trả lời

Trong nhiều phiên chơi, người chơi đi từ chỗ chỉ biết đập, nhặt và ghép đồ cơ bản sang chỗ có thể chuẩn bị những chuyến đi bài bản hơn, mang về tài nguyên hiếm hơn và chủ động mở ra các tầng sâu hơn của thế giới ngầm. Mỗi lần tiến lên không chỉ là mạnh số hơn, mà là có thêm quyền tiếp cận: khu vực mới, loại tài nguyên mới, công cụ mới, cách vận hành căn cứ tốt hơn và biên an toàn lớn hơn cho lần đi kế tiếp. Vòng dài hạn đúng của game là càng tích lũy càng dám xuống sâu, và càng xuống sâu càng mang về thứ có thể đổi thành một mức sống sót và làm chủ mới.

## Mục 5: Risk and Reward Loop

### Điều cần mô tả

- Phần thưởng tăng lên như thế nào khi người chơi đi xa hơn hoặc sâu hơn.
- Rủi ro tăng lên như thế nào tương ứng.
- Khoảnh khắc “tham hay rút” được tạo ra bằng cách nào.

### Đầu ra mong muốn

- Một đoạn `Risk and Reward Loop`.

### Trả lời

Phần thưởng của game tăng lên theo độ sâu, độ xa căn cứ và mức độ người chơi dám vượt qua ranh giới an toàn quen thuộc. Đi sâu hơn đồng nghĩa với việc có cơ hội gặp quặng hiếm hơn, vật liệu tốt hơn, lối mở mới hơn hoặc một mốc tiến trình lớn hơn. Đổi lại, tài nguyên hồi phục mỏng dần, đường rút dài hơn, túi đồ giá trị hơn, sai lầm đắt hơn và việc cứu nhau trong co-op cũng khó hơn. Vì vậy, câu hỏi “đi tiếp hay quay về” phải luôn xuất hiện đúng lúc người chơi vừa cảm thấy lời nhất, thay vì chỉ tới khi họ đã hết sạch lựa chọn.

## Mục 6: Multiplayer Loop

### Điều cần mô tả

- Co-op làm loop chính khác đi như thế nào.
- Người chơi hỗ trợ nhau ở những điểm nào trong một chuyến đi.
- Cảm giác “đi cùng nhau thì lời hơn” đến từ đâu.

### Đầu ra mong muốn

- Một đoạn `Multiplayer Loop`.

### Trả lời

Trong co-op, loop chính không chỉ là mỗi người tự lo phần mình rồi cộng kết quả lại, mà là cùng nhau tạo ra một chuyến đi hiệu quả và đáng nhớ hơn. Một người có thể mở đường và khai thác, một người giữ nhịp an toàn, một người mang thêm đồ hoặc xử lý hậu cần, và khi tình huống xấu đi thì cả nhóm cùng bàn xem cứu, rút hay liều thêm. Co-op làm lời hơn vì chia tải công việc, tăng khả năng mang tài nguyên về và cho phép rút lui thông minh hơn; đồng thời nó cũng làm mọi quyết định nặng hơn vì lợi ích và rủi ro không còn là của riêng một người.

## Mục 7: Điểm nghẽn cần theo dõi

### Điều cần mô tả

- Loop nào có nguy cơ nhạt, lặp hoặc gãy nhịp.
- Khoảnh khắc nào dễ làm người chơi thấy mệt, rỗng hoặc bị phạt vô ích.
- Phần nào nếu thiết kế lệch sẽ làm hỏng toàn bộ vòng lặp.

### Đầu ra mong muốn

- Một đoạn `Loop Bottlenecks`.

### Trả lời

Các điểm nghẽn lớn nhất cần theo dõi là: pha chuẩn bị có thể kéo quá dài và làm mất hứng đi ra ngoài; phần thu nhặt đầu chuyến có thể trở nên máy móc nếu thế giới không phản hồi đủ đa dạng; câu hỏi `tham hay rút` có thể mất lực nếu phần thưởng không đủ sắc hoặc nếu quay về luôn là lựa chọn quá an toàn; và progression có thể bị gãy nếu xuống sâu mà không mở ra thứ mới đủ đáng kể. Ngoài ra, nếu việc thất bại chỉ gây khó chịu mà không để lại bài học hay động lực phục hồi, toàn bộ risk/reward loop sẽ nhanh chóng mất giá trị.

## Bản chốt cấp 3

- Vòng ngắn của game là quan sát -> tương tác -> nhặt hoặc xử lý nguy hiểm -> quyết định bước kế tiếp.
- Core loop của game là chuẩn bị -> đi ra ngoài -> khai thác và mạo hiểm -> mang loot về -> đổi loot thành khả năng đi sâu hơn.
- Phiên ngắn phải đủ để tạo ra tiến triển thật, dù chơi solo hay co-op; phiên dài phải đủ để tạo ra một chuyến đi đáng kể.
- Progression dài hạn đúng là tích lũy để dám xuống sâu hơn, rồi dùng thứ mang về để mở tiếp chiều sâu sau đó.
- Risk/reward và câu hỏi `tham hay rút` là trái tim của gameplay loop.
- Co-op phải làm chuyến đi vừa hiệu quả hơn vừa đáng nhớ hơn.
- Điểm nghẽn cần canh là: chuẩn bị quá dài, phần thưởng đi sâu không đủ sắc, quay về không đủ ý nghĩa và thất bại không để lại động lực làm lại.

## Điều kiện để qua cấp 4

- Viết được `Core Gameplay Loop` rõ bằng chữ và sơ đồ.
- Viết được `Short Session Loop` và `Long Progression Loop`.
- Viết được `Risk and Reward Loop`.
- Viết được `Multiplayer Loop`.
- Nhìn ra được các `Loop Bottlenecks` chính.
- Nhìn ra hệ thống nào bắt buộc phải tồn tại để nuôi các loop trên.

