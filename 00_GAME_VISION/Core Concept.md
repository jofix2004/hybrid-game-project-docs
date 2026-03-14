Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 26/02/2026

# Core Concept

Tài liệu này chốt khái niệm cốt lõi của game ở cấp cao nhất: game này là gì, người chơi làm gì lặp đi lặp lại, vì sao hành trình đó hấp dẫn, và ranh giới nào không được vượt nếu muốn giữ đúng bản sắc đã khóa.

## Mục tiêu

- Viết ra một mô tả nhất quán, đủ ngắn để dùng làm câu trả lời gốc cho toàn bộ dự án.
- Tách rõ game này với các hướng dễ gây lệch như sandbox quá rộng, fantasy caster thuần hoặc action boss rush.
- Biến các câu trả lời ở `12_QUESTION_FRAMEWORK` thành một định nghĩa production có thể dùng để duyệt feature, viết pitch nội bộ và đối chiếu các doc sau.

## Phạm vi

Tài liệu này tập trung vào:
- game này là loại game gì
- bối cảnh nền của thế giới
- style hình ảnh và công nghệ của thế giới
- cấp độ công nghệ đang tồn tại
- người chơi bắt đầu ở đâu và đi tới đâu
- hành động lõi lặp lại là gì
- vì sao người chơi muốn tiếp tục chơi
- mana nằm ở đâu trong concept tổng thể
- ranh giới bản sắc không được vượt

Tài liệu này không đi sâu vào:
- công thức hệ thống
- số liệu balance
- schema data
- chi tiết implementation

## Source Coverage

### Nguồn bắt buộc

- [04_QUESTIONS_LEVEL_0.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/04_QUESTIONS_LEVEL_0.md)
  - chốt hạt giống của game: `survival co-op`, `tay trắng`, `đi sâu xuống lòng đất`, `mana là lớp năng lượng quan trọng`
- [05_QUESTIONS_LEVEL_1.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/05_QUESTIONS_LEVEL_1.md)
  - chốt mô tả game ở cấp identity, fantasy trung tâm, target experience sơ bộ, USP sơ bộ và giới hạn bản sắc
- [06_QUESTIONS_LEVEL_2.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/06_QUESTIONS_LEVEL_2.md)
  - chốt nhịp cảm xúc, nhịp chơi, cấu trúc phiên chơi và động lực quay lại

### Nguồn đối chiếu bắt buộc

- [Game Pillars.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/00_GAME_VISION/Game%20Pillars.md)
  - dùng để kiểm tra concept có còn bám đúng 5 pillar đã khóa hay không
- [Player Fantasy.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/00_GAME_VISION/Player%20Fantasy.md)
  - dùng để kiểm tra vai trò người chơi và hành trình biến đổi có nhất quán hay không
- [Target Experience.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/00_GAME_VISION/Target%20Experience.md)
  - dùng để kiểm tra concept có thật sự sinh ra đúng trải nghiệm đã hứa hay không

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - Đây là định nghĩa production của game ở cấp concept.
  - Nếu một doc sau này mô tả game theo cách mâu thuẫn với doc này, doc đó phải sửa theo `Core Concept` trước.

## Rule Summary

Game này là:
- một game `survival co-op theo chiều sâu`
- đặt trong bối cảnh `một đảo hoang còn sống được trên mặt đất`
- nhưng `giá trị thật nằm dưới lòng đất`
- mang style `low-tech steampunk magitech`
- nơi người chơi `bắt đầu tay trắng`
- cùng nhau `thu nhặt, khai thác, chịu áp lực sinh tồn, mang tài nguyên về`
- rồi dùng thứ mang về để `chuẩn bị cho chuyến đi sâu hơn tiếp theo`

Nền công nghệ của game là:
- `thủ công / tiền công nghiệp` ở đầu game
- sau đó mới mở dần `máy + mana`
- tri thức kỹ thuật nhìn chung dừng ở mức `cơ khí và điện sơ khai`, gần tinh thần thời kỳ mới phát minh ra bóng đèn dây tóc
- cảm giác thị giác và công cụ nên nghiêng về `steampunk thô`, không phải `steampunk trình diễn`

Mana trong game là:
- `nhiên liệu mới` gắn lên công cụ và máy móc
- được phát triển tiếp từ `tri thức nhân loại cũ`
- không phải phép thuật tách rời hoàn toàn khỏi kỹ thuật và vận hành

Điều game bán không phải là:
- sức mạnh anh hùng sẵn có
- sandbox ôm quá nhiều nhánh rời rạc
- hay fantasy caster thuần túy

Điều game bán là:
- cảm giác từ yếu và thiếu thành bài bản và lão luyện
- cảm giác mạo hiểm có chủ đích
- cảm giác mang chiến lợi phẩm về an toàn
- và lời hứa rằng bên dưới còn tầng sâu hơn, nguy hiểm hơn, đáng giá hơn

## 1. Định Nghĩa Một Câu

Đây là game survival co-op theo chiều sâu, lấy bối cảnh một đảo hoang nơi mặt đất vẫn còn sống được nhưng giá trị thật nằm dưới lòng đất. Thế giới mang chất `low-tech steampunk magitech`: công cụ, workshop và máy móc còn thô, nặng tính cơ khí, chưa high-tech, còn mana chỉ mới được gắn vào như một lớp năng lượng mới để khuếch đại khả năng khai thác, vận hành và đi sâu hơn.

## 2. Định Nghĩa Mở Rộng

Người chơi không vào game để làm anh hùng được chọn, cũng không vào chỉ để xây dựng sandbox rộng vô hạn. Họ vào game như những người sống sót trên một đảo hoang, nơi bề mặt đủ để bám trụ nhưng không phải nơi chứa giá trị lớn nhất. Giá trị thật, nguy hiểm thật và con đường tiến lên thật đều nằm dưới lòng đất.

Từ nền tảng yếu ớt đó, họ phải thu nhặt, khai thác, học nhịp nguy hiểm của thế giới, chịu áp lực đói, hồi phục, durability, mất mát và logistics, rồi mang thứ có giá trị về căn cứ để chuyển hóa thành khả năng đi tiếp.

Khái niệm cốt lõi của game là:
- `đi ra ngoài`
- `liều có chủ đích`
- `mang được thứ đáng giá về`
- `chuẩn bị tốt hơn`
- `đi sâu hơn lần sau`

Mana và ma thuật không thay lõi này. Chúng làm giàu cho nó bằng cách mở ra utility, vận hành, network, machine, gate và các công cụ khuếch đại sinh tồn, thay vì biến game thành một game spam phép. Về bản chất, mana ở đây là bước tiếp theo của một nền kỹ thuật cũ còn sơ khai: con người chưa đi tới công nghiệp hiện đại, nhưng đã biết gắn một nguồn năng lượng mới lên các công cụ và máy móc đang hình thành.

## 3. Bối Cảnh Nền Của Thế Giới

Thế giới của game đặt trên một `đảo hoang`.

Điều quan trọng của bối cảnh này là:
- `mặt đất còn sống được`
- người chơi vẫn có thể dựng chỗ bám trụ, tổ chức căn cứ và chuẩn bị chuyến đi
- nhưng `mặt đất không phải nơi chứa phần thưởng lớn nhất`
- mọi động lực khám phá, mở khóa và giàu lên thật sự đều kéo người chơi xuống `lòng đất`

Ở bản định hướng hiện tại:
- mặt đất của đảo tạm thời chỉ có các biome:
  - `rừng rậm`
  - `đồng bằng`
  - `bãi biển`
- phần dưới lòng đất được tổ chức thành `nhiều lớp hang`
- mỗi `tầng hang` mang một `biome đặc thù` riêng
- còn `hầm ngục` là các pocket nội dung đậm, công trình cổ hoặc khu đặc biệt nằm chen vào trong từng tầng hang, không phải toàn bộ cấu trúc dưới lòng đất

Bối cảnh này rất quan trọng cho concept vì nó giữ được cả hai nửa:
- có một nơi để `sống`, `chuẩn bị`, `xây nền`
- và có một nơi để `liều`, `kiếm lời`, `đi sâu`

Game không đi theo hướng:
- thế giới hậu tận thế đô thị nặng đổ nát công nghiệp
- hay fantasy thuần thần thoại xa rời kỹ thuật

Nó đi theo hướng:
- một thế giới còn đủ thô và hoang để survival có trọng lượng
- nhưng vẫn có đủ dấu vết tri thức cũ để công nghệ và mana phát triển thành một trục gameplay thật
- với cảm giác thẩm mỹ nghiêng về `low-tech steampunk magitech`, tức là cơ khí, vật liệu thật, máy móc sơ khai và năng lượng mana mới chớm được ứng dụng

## 4. Style Thế Giới

Style nền của game được chốt là `low-tech steampunk magitech`.

Điều này có nghĩa:
- có chất `steampunk` ở vật liệu, hình khối, máy móc, workshop và tinh thần phát minh cơ khí
- có chất `magitech` ở việc mana được gắn vào công cụ, máy và hạ tầng
- nhưng mọi thứ vẫn phải `low-tech`, thô, nặng tính thủ công và tiền công nghiệp

Style này không được hiểu là:
- thành phố công nghệ dày đặc
- máy móc bóng bẩy, tinh xảo như đồ trình diễn
- công nghệ áp đảo hoàn toàn đời sống sinh tồn
- hoặc ma thuật quá sạch, quá tiện, quá “thần kỳ”

Style này phải cho cảm giác:
- đồ nghề làm ra để sống và để đào sâu, không phải để khoe
- cơ khí, kim loại, gỗ, da, vải, kính, ống dẫn, van, đồng hồ, bóng đèn sơ khai
- máy móc đang trong giai đoạn hữu dụng nhưng chưa hoàn thiện
- mana giống một nguồn năng lượng mới còn đang được học cách khai thác

## 5. Cấp Độ Công Nghệ

Cấp độ công nghệ của game không phải trung cổ thuần, cũng chưa phải công nghiệp hiện đại.

Nền chung nên được hiểu là:
- `thủ công / tiền công nghiệp` là chính ở đầu game
- có `sắt thép, workshop, sửa chữa, chế tạo công cụ` ở mức cơ bản
- máy móc xuất hiện dần như một bước tiến có trọng lượng, không phải thứ mặc định sẵn có từ đầu

Mốc tham chiếu tinh thần phù hợp là:
- kỹ thuật ở mức `cơ khí và điện sơ khai`
- gần với thời kỳ nhân loại mới bước tới các phát minh nền tảng kiểu `bóng đèn dây tóc`
- nghĩa là đã có logic công cụ, máy, truyền năng lượng và workshop
- nhưng chưa có cảm giác công nghiệp hóa đại trà hoặc công nghệ hiện đại

Điều này giúp game giữ được:
- cảm giác thô ráp, làm bằng tay, tự xoay xở
- giá trị của mỗi bước nhảy công nghệ
- và vai trò rõ của mana như chất xúc tác cho một nền kỹ thuật còn non

Điểm rất quan trọng là:
- có thể dùng `steampunk` như nhãn thẩm mỹ
- nhưng không được hiểu thành `high-tech steampunk`
- chuẩn đúng là `low-tech steampunk`, tức máy hữu dụng, cũ, thô, nặng, còn giới hạn và luôn phải phục vụ survival

## 6. Quan Hệ Giữa Công Nghệ Và Mana

Mana không đứng ngoài công nghệ. Trong concept này, mana là `nhiên liệu mới` được gắn lên các công cụ và tri thức kỹ thuật cũ.

Quan hệ đúng giữa hai lớp này là:
- công cụ thường đi trước
- mana gắn vào để khuếch đại
- máy móc, automation, gate và utility cao hơn mới ngày càng phụ thuộc mana

Nói ngắn gọn:
- `công nghệ thường` xử lý lớp sinh tồn nền
- `mana` đẩy hiệu suất, utility, logistics và khả năng đi sâu lên tầng mới

Vì vậy mana trong game nên luôn có cảm giác:
- là một phát minh vận hành mới
- là nhiên liệu cho các hệ đang lớn dần
- và là cây cầu giữa survival thô sơ với infrastructure về sau

Nó không nên có cảm giác:
- là phép thuật tách hẳn khỏi kỹ thuật
- hay là bộ skill chiến đấu đứng riêng thành một game khác

## 7. Người Chơi Làm Gì Lặp Đi Lặp Lại

Ở cấp concept, hành động lõi của game là:

- chuẩn bị chuyến đi
- rời vùng an toàn
- quan sát, nhặt, khai thác và xử lý nguy hiểm
- quyết định `tham hay rút`
- mang loot về
- đổi loot thành khả năng sống sót và đi sâu hơn

Đây là một vòng lặp có nhịp rất rõ:
- `chuẩn bị`
- `mạo hiểm`
- `trở về`
- `nâng khả năng`
- `lặp lại ở lớp sâu hơn`

Nếu một feature mới không nuôi được ít nhất một mắt xích trong vòng này, nó không thuộc lõi concept.

## 8. Người Chơi Bắt Đầu Ở Đâu Và Đi Tới Đâu

Người chơi bắt đầu ở trạng thái:
- tay trắng
- thiếu thốn
- tò mò nhưng dè chừng
- sống bằng các tương tác rất cơ bản

Người chơi dần đi tới trạng thái:
- có chuẩn bị
- có phân vai
- có năng lực logistics
- có khả năng vận hành công cụ, mana, machine và tuyến đi
- đủ giỏi để xuống những lớp sâu hơn mà người chơi mới không chịu nổi

Concept đúng vì thế là hành trình:
- từ `yếu và thiếu`
- thành `có tổ chức`
- rồi thành `thám hiểm chiều sâu một cách bài bản`

## 9. Vì Sao Hành Trình Này Hấp Dẫn

Game này hấp dẫn vì nó luôn duy trì đồng thời 4 lực kéo:

### 9.1. Tò mò

Người chơi luôn thấy còn thứ mới để chạm, để thử, để mở và để đi sâu hơn.

### 9.2. Áp lực

Càng đi xa hoặc đi sâu, tài nguyên hồi phục mỏng hơn, đường lui đắt hơn, mất mát đau hơn.

### 9.3. Phần thưởng

Càng liều có chủ đích, người chơi càng có cơ hội đem về tài nguyên, mốc tiến trình, tầng mới và công cụ mới.

### 9.4. Tiến triển thật

Những gì mang về không chỉ là con số. Chúng phải đổi được thành khả năng đi tiếp, sống tốt hơn, vận hành tốt hơn hoặc tiếp cận chiều sâu mới.

## 10. Vai Trò Của Co-op Trong Concept

Co-op không phải chế độ phụ. Co-op là hình thái mạnh nhất của concept này.

Game đúng không phải là:
- nhiều người vào chung map rồi mỗi người tự lo phần mình

Game đúng là:
- cùng nhau chia việc
- cùng nhau gánh rủi ro
- cùng nhau đưa ra quyết định lớn
- cứu nhau, kéo nhau, và mang lợi nhuận về cùng nhau

Solo vẫn phải chơi được, nhưng concept trung tâm vẫn nghiêng rõ về:
- nhóm người sống sót đi bài bản hơn khi phối hợp tốt

## 11. Vai Trò Của Mana Trong Concept

Mana là lớp khác biệt quan trọng của game, nhưng không phải lõi duy nhất.

Trong concept tổng thể, mana phải là:
- lớp năng lượng của thế giới
- lớp utility và hậu cần
- lớp khuếch đại cho khai thác, sinh tồn, máy móc và gate

Mana cũng phải phản ánh đúng bối cảnh công nghệ:
- là thứ gắn lên công cụ được phát triển từ tri thức cũ
- đi từ ứng dụng sơ khai
- rồi mới thành nền cho machine, network và gate về sau
- và phải luôn giữ cảm giác `steampunk thô`, không biến thành năng lượng sci-fi sạch và vô hình

Mana không được làm game trượt sang:
- fantasy caster thuần
- combat power trip
- hoặc tài nguyên phép tự hồi vô nghĩa

Mana đúng là thứ khiến game có bản sắc riêng hơn trong khi vẫn giữ nguyên trục:
- survival
- co-op
- chiều sâu
- chuẩn bị
- và mạo hiểm có chủ đích

## 12. Trọng Tâm Khác Biệt Của Concept

Điểm khác biệt cốt lõi của game không nằm ở việc có nhiều biome, nhiều quái hay nhiều vật phẩm hơn người khác.

Điểm khác biệt cốt lõi nằm ở:
- `survival co-op theo chiều sâu`
- `mỗi chuyến đi là một vòng đánh đổi rõ giữa mạo hiểm và mang tài nguyên về`
- `mana là nền năng lượng khuếch đại sinh tồn, utility, khai thác và vận hành`
- `style low-tech steampunk magitech trên đảo hoang`

Nói cách khác:
- game này không bán `độ rộng`
- game này bán `độ sâu`
- cả ở nghĩa không gian chơi lẫn nghĩa tiến trình ra quyết định

## 13. Ranh Giới Bản Sắc

Game này không được trở thành:

### 13.1. Sandbox ôm quá nhiều thứ rời rạc

Mọi hệ thống thêm vào đều phải phục vụ trục survival co-op và khám phá chiều sâu.

### 13.2. Game hành động boss rush thuần

Combat có giá trị, nhưng không được nuốt toàn bộ nhịp chuẩn bị, khai thác, rút lui và mang về.

### 13.3. Fantasy caster thuần

Mana là lớp khuếch đại và vận hành, không phải identity duy nhất của người chơi.

### 13.4. Game tuyến tính nặng cốt truyện

NPC và milestone có thể định hướng, nhưng không được biến hành trình thành đường ray cứng làm mất trọng lượng của chuyến đi.

### 13.5. Steampunk bị đẩy quá tay

Không được để style đi thành:
- quá nhiều máy lòe loẹt
- quá nhiều thành phố và công nghệ sạch
- cảm giác tech show-off mạnh hơn survival

Steampunk của game này phải luôn phục vụ:
- bám trụ
- khai thác
- sửa chữa
- vận hành
- đi sâu

## 14. Dấu Hiệu Concept Đang Đúng

Concept được xem là đang đúng nếu người chơi thường có các cảm giác hoặc câu nói kiểu:

- “đi thêm một đoạn nữa thì lời thật, nhưng dễ mất hết”
- “mang được đống này về là thắng lớn”
- “chuẩn bị tốt hơn nên chuyến này đỡ căng hơn”
- “xuống sâu rõ ràng mở ra lớp chơi mới”
- “đi cùng nhau hiệu quả hơn hẳn”
- “đảo này chỉ là điểm bám, của ngon thật nằm ở dưới”
- “mana làm chuyến đi tiện và sâu hơn, chứ không biến game thành caster”
- “máy móc nhìn thô nhưng hữu dụng, đúng kiểu đồ để sống sót chứ không phải đồ diễn”

## 15. Cách Dùng Core Concept Để Duyệt Feature

Khi đánh giá một feature mới, phải trả lời được:

1. Feature này có phục vụ trục `chuẩn bị -> đi ra ngoài -> mạo hiểm -> mang về -> đi sâu hơn` không.
2. Nó làm co-op, survival, chiều sâu hay lớp mana mạnh hơn theo cách nào.
3. Nó có làm game rộng hơn nhưng nông hơn không.
4. Nó có đẩy game sang fantasy sai như sandbox builder thuần, hero tuyến tính hay caster thuần không.
5. Nó có tạo ra thêm quyết định thật cho chuyến đi hay chỉ thêm menu và hệ phụ.
6. Nó có giữ đúng chất `low-tech steampunk magitech`, hay đang kéo game sang high-tech hoặc city-tech quá mức.

Nếu không trả lời được các câu trên, feature đó chưa nên được xem là core.

## Open Design Questions

- Hiện chưa có câu hỏi mở bắt buộc ở cấp concept.
- Nếu sau này xuất hiện một hướng phát triển lớn mới như PvP, story campaign mạnh hoặc mode tách rời hầm ngục, phải rà lại doc này trước.

## Open Balance Variables

Ở cấp concept, chưa khóa số balance cụ thể.

Các doc sau phải cụ thể hóa concept này thành rule và data:
- `Game Pillars`
- `Player Fantasy`
- `Target Experience`
- `Core Gameplay Loop`
- `Risk and Reward`
- `Player Progression`
- `Survival System`
