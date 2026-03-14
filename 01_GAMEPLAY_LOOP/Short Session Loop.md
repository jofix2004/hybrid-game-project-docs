Project Code: HYBRID
Version: 1.0 (Draft)
Author: null
Date: 02/03/2026

# Short Session Loop

Tài liệu này chốt hình dạng của một phiên chơi ngắn trong game: khi người chơi chỉ có khoảng 10-30 phút, họ phải vẫn làm được một việc nhỏ nhưng thật, thấy có tiến triển rõ ràng, và không bị buộc phải chờ tới một chuyến đi lớn mới cảm thấy phiên đó có giá trị.

## Mục tiêu

- Chốt tiêu chuẩn của một `phiên ngắn` đúng với game này.
- Làm rõ người chơi có thể hoàn thành những loại mục tiêu nào trong 10-30 phút.
- Chỉ ra vì sao phiên ngắn vẫn phải tạo ra tiến triển thật cho solo lẫn co-op.
- Xác định fail state, recovery và các anti-pattern khiến phiên ngắn trở nên vô nghĩa.

## Phạm vi

Tài liệu này tập trung vào:
- loop của một phiên chơi ngắn kéo dài khoảng 10-30 phút
- các loại mục tiêu hợp lệ của phiên ngắn
- cách một phiên ngắn nối vào `Core Gameplay Loop`
- giá trị của phiên ngắn đối với solo, co-op, căn cứ, chuẩn bị và tiến sâu
- dấu hiệu một phiên ngắn thành công, thất bại hoặc bị gãy nhịp

Tài liệu này không đi sâu vào:
- progression dài hạn nhiều phiên
- run sâu nhiều chặng hoặc boss run
- số balance thời lượng, lượng loot hay tỷ lệ lời/lỗ cụ thể

## Source Coverage

### Nguồn bắt buộc

- [06_QUESTIONS_LEVEL_2.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/06_QUESTIONS_LEVEL_2.md)
  - chốt `cấu trúc phiên chơi`, phân biệt `phiên ngắn` và `phiên dài`, xác định cuối phiên ngắn phải có cảm giác “mình đã tiến thêm được một phần rõ ràng”
- [07_QUESTIONS_LEVEL_3.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/07_QUESTIONS_LEVEL_3.md)
  - là nguồn chốt trực tiếp cho `Short Session Loop`, nhấn mạnh phiên ngắn phải đủ để làm xong một mục tiêu nhỏ nhưng thật, không mặc định cần co-op
- [08_QUESTIONS_LEVEL_4.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/12_QUESTION_FRAMEWORK/08_QUESTIONS_LEVEL_4.md)
  - xác nhận các hệ bắt buộc phải nuôi được phiên ngắn: survival, gathering, crafting/building, progression, multiplayer support

### Nguồn đối chiếu bắt buộc

- [Core Gameplay Loop.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/01_GAMEPLAY_LOOP/Core%20Gameplay%20Loop.md)
  - dùng để giữ cho phiên ngắn vẫn là một lát cắt hợp lệ của core loop, không biến thành loop ngoài lề
- [Target Experience.md](/d:/TrinhLaGiV2/document/GAME_PROJECT_DOCS/00_GAME_VISION/Target%20Experience.md)
  - dùng để xác nhận phiên ngắn phải luôn tạo ra `tiến triển thật`, không được để người chơi online xong mà thấy trôi mất thời gian

## Decision Status

- Trạng thái hiện tại: `Locked`
- Ghi chú:
  - Vai trò của phiên ngắn đã đủ rõ để làm nguồn cho các doc `Long Progression Loop`, `Survival System`, `Player Progression`, `Inventory System` và `Multiplayer Loop`.
  - Con số chính xác cho “ngắn” bao nhiêu phút vẫn là lớp balance/live tuning về sau, nhưng khoảng mục tiêu hiện tại là `10-30 phút`.

## Conflict Resolution

- `Level 2` mô tả phiên ngắn từ góc nhìn trải nghiệm: một mục tiêu nhỏ nhưng có ý nghĩa và kết thúc bằng cảm giác tiến thêm một phần rõ ràng.
- `Level 3` chuyển nó thành loop rõ ràng hơn: phiên ngắn không mặc định cần co-op, có thể là farm gần, chuẩn bị đồ, mở thêm một đoạn nhỏ hoặc hoàn thiện một mắt xích ở căn cứ.
- `Level 4` xác nhận phiên ngắn chỉ đứng vững khi survival, resource, crafting/building và progression đều cho phép tiến triển nhỏ nhưng thật.
- Không có xung đột cứng giữa các nguồn. Tài liệu này ưu tiên `Level 3` cho hình dạng loop và dùng `Level 2` để khóa cảm giác kết thúc phiên.

## Rule Summary

- Một phiên ngắn là một lát cắt ngắn nhưng hoàn chỉnh của core loop.
- Người chơi phải có thể bắt đầu với một mục tiêu cụ thể, hoàn thành nó trong khoảng 10-30 phút, rồi kết thúc phiên với tiến triển thật.
- Phiên ngắn không bắt buộc phải có cao trào lớn, nhưng bắt buộc phải có kết quả hữu hình.
- Phiên ngắn có thể là:
  - farm nguyên liệu gần
  - sửa đồ, craft đồ, nạp dự trữ và chốt loadout
  - hoàn thiện một utility hoặc một mắt xích ở căn cứ
  - mở thêm một đoạn đường hoặc một lớp tiếp cận ngắn
  - thử đẩy thêm một nhịp ngắn ở field rồi rút an toàn
- Co-op có thể làm phiên ngắn nhanh hơn, an toàn hơn hoặc vui hơn, nhưng phiên ngắn vẫn phải có giá trị ngay cả khi chơi solo.
- Một phiên ngắn thất bại không được khiến người chơi cảm thấy “phiên này coi như bỏ”, trừ khi họ đã chủ động liều một cách có ý thức.

## State List

### 1. Chọn Mục Tiêu Ngắn

Người chơi xác định một mục tiêu nhỏ, cụ thể và khả thi trong phiên hiện tại.

Ví dụ:
- lấy thêm một nhóm tài nguyên gần
- sửa và nạp lại đồ cho chuyến sau
- craft xong một món còn thiếu
- đẩy thêm một đoạn ngắn
- hoàn thiện một utility của căn cứ

### 2. Chuẩn Bị Tối Thiểu

Người chơi thực hiện phần chuẩn bị đủ dùng cho mục tiêu ngắn:
- cầm đúng tool
- mang đủ đồ ăn / hồi phục / utility cần thiết
- dọn bớt túi đồ nếu cần
- hoặc chia việc nhanh nếu là co-op

### 3. Thực Hiện Mục Tiêu

Người chơi đi ra ngoài field hoặc thao tác ở căn cứ để hoàn thành mục tiêu đã chọn.

### 4. Chốt Kết Quả

Người chơi quay về, cất đồ, hoàn tất craft/repair/build, hoặc xác nhận mình đã mở xong phần ngắn đã nhắm tới.

### 5. Thấy Tiến Triển

Phiên kết thúc với một kết quả đủ rõ để người chơi cảm thấy:
- mình có tiến thêm
- chuyến sau dễ hơn, giàu hơn hoặc rõ mục tiêu hơn

## Transition Rules

### Chọn Mục Tiêu Ngắn -> Chuẩn Bị Tối Thiểu

Xảy ra khi người chơi đã biết rõ:
- mình định làm gì trong phiên này
- cần mang gì
- và mốc “xong” của phiên là gì

### Chuẩn Bị Tối Thiểu -> Thực Hiện Mục Tiêu

Xảy ra khi người chơi:
- rời căn cứ để đi farm gần / mở thêm một đoạn / làm một nhịp ngắn
- hoặc bắt đầu thao tác trực tiếp vào phần tiến triển ở căn cứ

### Thực Hiện Mục Tiêu -> Chốt Kết Quả

Xảy ra khi:
- mục tiêu đã đạt
- hoặc người chơi quyết định dừng ở mức lời đủ an toàn
- hoặc tài nguyên của phiên ngắn không còn đáng để liều tiếp

### Chốt Kết Quả -> Thấy Tiến Triển

Xảy ra khi kết quả của phiên đã được chuyển thành:
- tài nguyên cất vào kho
- đồ được sửa / craft xong
- utility hoặc mắt xích căn cứ được dựng xong
- đường đi hoặc mức tiếp cận mới được mở ra
- hoặc chuyến sau được chuẩn bị tốt hơn thấy rõ

### Thực Hiện Mục Tiêu -> Failure and Recovery

Xảy ra khi:
- người chơi chết
- mất quá nhiều tài nguyên so với mục tiêu nhỏ đang theo
- hoặc phải bỏ ngang mục tiêu mà không chốt được giá trị chính

## Core Flows

### 1. Phiên Farm Gần

1. Chọn một nhóm tài nguyên hoặc vật tư đang thiếu.
2. Cầm đúng tool, dọn bớt túi, mang theo đồ tối thiểu.
3. Đi ra khu gần căn cứ hoặc khu đã quen.
4. Lấy đủ lượng tài nguyên mục tiêu.
5. Quay về trước khi chuyến đi bắt đầu chuyển từ “ngắn” sang “liều quá mức”.
6. Cất đồ và thấy rõ phiên này đã giải quyết được một thiếu hụt cụ thể.

### 2. Phiên Chuẩn Bị Và Hậu Cần

1. Người chơi vào game với mục tiêu không phải “đi sâu”, mà là làm chuyến sau tốt hơn.
2. Sửa đồ, craft đồ, nạp lại các vật phẩm tiêu hao, sắp xếp túi, chuẩn bị fuel hoặc mana item.
3. Nếu có đủ thời gian, đi thêm một nhịp nhỏ để lấp một món còn thiếu.
4. Kết thúc phiên với loadout tốt hơn và đường vào chuyến sau rõ hơn.

### 3. Phiên Mở Thêm Một Đoạn

1. Chọn một đoạn đường, một nhịp hang hoặc một mốc nhỏ chưa vượt.
2. Chuẩn bị vừa đủ để chạm vào nó.
3. Đi ra ngoài, mở thêm một phần không gian hoặc tiếp cận mới.
4. Khi đạt được tiến triển đã định, quay về ngay thay vì cố đẩy tiếp thành run dài.
5. Giá trị của phiên nằm ở việc “mở khóa thêm cho run sau”, không nhất thiết ở lượng loot lớn.

### 4. Phiên Co-op Hỗ Trợ

1. Một hoặc nhiều người vào với mục tiêu giúp cả nhóm chuẩn bị cho chuyến lớn hơn.
2. Chia nhau farm gần, sửa đồ, góp vật tư, hoàn thiện utility hoặc chốt loadout chung.
3. Kết thúc phiên với trạng thái chung của nhóm tốt hơn.
4. Phiên này vẫn phải có giá trị cá nhân cho từng người tham gia, không được là công việc vô hình.

## Cost / Reward

### Cost

Một phiên ngắn đúng vẫn có cost, nhưng cost phải nhỏ và kiểm soát được hơn so với run dài.

Các cost chính:
- thời gian chuẩn bị ngắn
- tiêu hao durability nhẹ
- tiêu hao một phần đồ ăn / hồi phục / fuel nếu rời căn cứ
- rủi ro mất lợi nhuận nhỏ nếu chủ quan

### Reward

Reward của phiên ngắn phải là reward thật, không phải reward “cho có cảm giác”.

Reward hợp lệ gồm:
- một lượng tài nguyên đủ dùng cho một nhu cầu cụ thể
- một món craft hoặc repair hoàn tất
- một mắt xích căn cứ / utility được dựng xong
- một đoạn đường / lớp tiếp cận được mở thêm
- một chuyến sau được chuẩn bị tốt hơn rõ ràng

### Anti-Reward

Những thứ không được xem là reward đủ tốt cho một phiên ngắn:
- chỉ tăng số rất nhỏ nhưng không giải quyết được nhu cầu cụ thể nào
- chỉ dọn UI hoặc sắp xếp vặt mà không đổi trạng thái thực của căn cứ / loadout / run sau
- chỉ “ngó qua” mà không cất được gì, mở được gì hoặc học được gì có ích

## Failure and Recovery

### Soft Failure

Phiên ngắn bị xem là soft failure khi:
- lời ít hơn kỳ vọng
- mất thời gian hơn dự kiến
- phải rút sớm
- hoặc hoàn thành được một nửa mục tiêu nhưng không trọn

Soft failure vẫn chấp nhận được nếu người chơi vẫn giữ lại:
- một phần tài nguyên
- một phần chuẩn bị
- hoặc một hiểu biết cụ thể giúp chuyến sau ngắn hơn, an toàn hơn

### Hard Failure

Phiên ngắn trở thành hard failure khi:
- chết
- mất nhiều tài nguyên hơn giá trị mục tiêu ban đầu
- hoặc buộc phải bỏ phiên mà không chốt được lợi ích nào có ý nghĩa

### Recovery

Một phiên ngắn sau thất bại phải vẫn cho phép người chơi:
- bật lại game ở phiên sau và làm lại nhanh
- không bị một cái chết nhỏ chặn luôn khả năng tiếp tục
- dùng chính phiên ngắn tiếp theo để phục hồi lại nền tối thiểu

Nếu một hard failure nhỏ làm người chơi cần quá lâu để đứng dậy, loop phiên ngắn đang quá nặng.

## Edge Cases

### 1. Chỉ Có 10 Phút

Vẫn phải có loại mục tiêu đủ nhỏ để người chơi:
- vào game
- làm xong một việc thật
- và thoát ra với cảm giác không phí phiên

### 2. Chỉ Ở Căn Cứ

Một phiên chỉ xoay quanh căn cứ vẫn được xem là phiên ngắn hợp lệ nếu nó:
- sửa đồ
- craft đồ
- sắp xếp và chuẩn bị cho chuyến sau
- hoàn thiện một utility cụ thể

Miễn là cuối phiên có thay đổi gameplay thật, không chỉ là việc vặt vô nghĩa.

### 3. Solo

Solo phải tận dụng được phiên ngắn mà không cần chờ party.
Phiên ngắn solo đúng là nơi người chơi:
- tự farm phần mình thiếu
- tự chỉnh loadout
- tự đẩy một bước nhỏ
- và không bị chặn vì thiếu co-op

### 4. Co-op Không Đủ Người

Nếu party không đủ đông hoặc chỉ online được ít phút, phiên ngắn vẫn phải hữu ích:
- góp tài nguyên
- sửa đồ
- chuẩn bị chuyến sau
- hoặc làm một run nhỏ an toàn hơn

### 5. Mục Tiêu Bị Lố

Nếu người chơi lỡ đẩy phiên ngắn thành một run dài hơn dự kiến, game phải để họ:
- quay đầu và chốt lời sớm
- thay đổi mục tiêu giữa chừng
- hoặc chấp nhận rủi ro tăng thêm một cách có ý thức

Phiên ngắn không được gãy chỉ vì mục tiêu ban đầu hơi lệch.

## Signs Of A Good Short Session

Một phiên ngắn được xem là tốt nếu người chơi thường có cảm giác:
- “vào một lúc mà vẫn làm xong được một việc”
- “mình đã giải quyết được đúng thứ đang thiếu”
- “lần sau vào là đi tiếp được”
- “không cần chuyến lớn mà vẫn thấy có tiến”

## Signs Of A Broken Short Session

Phiên ngắn đang hỏng nếu người chơi thường có cảm giác:
- “online ít thời gian là vô ích”
- “muốn làm gì meaningful cũng phải đợi phiên dài”
- “mỗi lần vào chỉ làm việc lặt vặt cho xong”
- “phiên ngắn không giúp run sau khác đi”

## Implementation Hooks

- Cần tag hoặc phân loại `session_goal_type` tối thiểu:
  - `nearby_farm`
  - `base_preparation`
  - `small_push`
  - `utility_completion`
  - `coop_support`
- Cần có cách đo `short_session_progress`:
  - tài nguyên thu về
  - craft/repair/build hoàn tất
  - đường hoặc mức tiếp cận mới
  - mức sẵn sàng cho chuyến sau
- Cần có phân biệt rõ giữa:
  - `short session success`
  - `short session partial success`
  - `short session failure`
- Cần telemetry cho các câu hỏi:
  - người chơi phiên ngắn có thường thoát game khi đang ở căn cứ hay ngoài field
  - tỷ lệ phiên ngắn kết thúc bằng lợi ích hữu hình là bao nhiêu
  - tỷ lệ người chơi online ngắn nhưng không chốt được gì có đang quá cao không

## Open Design Questions

- Mức tối thiểu nào để một thay đổi ở căn cứ được tính là “tiến triển thật” sẽ cần khóa kỹ hơn ở các doc `Building System` và `Crafting Economy`.
- Các loại mục tiêu ngắn theo từng phase tiến trình của game sẽ cần đặc tả sâu thêm trong `Player Progression`, `Dungeon Progression` và `Items`.

## Open Balance Variables

- Ngưỡng thời lượng thực tế để gọi là `phiên ngắn`
- Lượng reward tối thiểu để người chơi vẫn thấy đáng trong 10-15 phút
- Mức rủi ro tối đa chấp nhận được cho một mục tiêu ngắn
- Tỷ lệ phiên ngắn thiên về căn cứ so với phiên ngắn thiên về field
- Mức chênh hiệu quả giữa phiên ngắn solo và phiên ngắn co-op
