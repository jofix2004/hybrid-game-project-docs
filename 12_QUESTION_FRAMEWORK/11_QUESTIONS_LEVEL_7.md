Project Code: HYBRID
Version: 0.9 (Draft)
Author: null
Date: 10/02/2026

# 11_QUESTIONS_LEVEL_7

Tài liệu này là khung câu hỏi cấp 7, dùng để xác định các ràng buộc vận hành và kỹ thuật của game: game chạy theo mô hình phiên nào, multiplayer được chống lưng bởi mức networking nào, save được giữ ra sao, content được sản xuất bằng pipeline nào, và scope kỹ thuật nên dừng ở đâu để còn làm được.

## Mục tiêu của cấp độ này

- Làm rõ giả định nền cho multiplayer, networking, save, chunk simulation, content pipeline và công cụ nội bộ.
- Chốt những ràng buộc sản xuất thật: game này vận hành được tới đâu trong MVP, và cái gì chưa nên ôm.
- Tránh tình trạng ý tưởng design rất hay nhưng technical cost, tool cost hoặc maintenance cost vượt quá sức của dự án.

## Nguyên tắc dùng tài liệu này

- Mỗi mảng vận hành hoặc kỹ thuật phải được soi như một bài độc lập, không mặc định đúng chỉ vì các cấp trước đã cần nó về mặt fantasy hay gameplay.
- Có thể tham khảo loop, hệ thống và content đã chốt để lấy ngữ cảnh, nhưng không dùng chúng như bằng chứng cuối cùng.
- Nếu một yêu cầu kỹ thuật chỉ làm game “nghe xịn hơn” mà không mở ra giá trị thật cho trải nghiệm chuẩn hoặc production, phải hạ ưu tiên hoặc đẩy về sau.

## Tiêu chí cố định cho mọi mảng vận hành và kỹ thuật

1. Mảng này tồn tại để phục vụ trải nghiệm hay quy trình nào.
2. Nó ảnh hưởng trực tiếp tới người chơi, designer hay programmer ở đâu.
3. Nó có bắt buộc cho MVP không, hay chỉ bắt buộc cho scale lớn hơn.
4. Nó tiêu tốn chi phí gì: code, QA, content authoring, vận hành hay support.
5. Nó có điểm nghẽn, failure mode hoặc rủi ro desync nào.
6. Nếu cắt nó đi, game mất trải nghiệm gì hoặc production mất công cụ gì.
7. Nó có thể được thay bằng bản mỏng hơn trong giai đoạn đầu không.
8. Nó có rủi ro kéo scope ra khỏi khả năng thực hiện của đội ngũ không.

## Mục 1: Bản đồ ràng buộc vận hành và kỹ thuật ứng viên

### Điều cần mô tả

- Những mảng kỹ thuật nào đang được xem là bắt buộc.
- Những mảng nào quan trọng nhưng có thể giữ mỏng.
- Những mảng nào nghe hấp dẫn nhưng chưa nên làm sớm.

### Câu hỏi khung

- Game cần chốt gì trước giữa: session model, authority, save, chunk streaming, content pipeline, debug tools.
- Những thứ nào là “muốn có” nhưng không phải điều kiện để gameplay chuẩn hoạt động.
- Nếu phải bỏ bớt một nửa các tính năng kỹ thuật, phần lõi nào vẫn phải còn.

### Đầu ra mong muốn

- Một danh sách `Operational and Technical Candidates`.

### Trả lời

- `Bắt buộc`: session model rõ ràng, network authority đủ chặt, save world và player state, chunk hoặc streaming cho hang mở, content pipeline data-driven, bộ debug tool nội bộ, quy tắc recovery cơ bản.
- `Quan trọng nhưng phải tiết chế`: dedicated server, host migration, analytics gameplay, telemetry hiệu năng, bản đồ công cụ cho designer.
- `Để sau`: crossplay, matchmaking công cộng lớn, mod support, replay system, live event backend, cloud service dày.

## Mục 2: Trải nghiệm phiên chơi chuẩn và mô hình kết nối

### Điều cần mô tả

- Một phiên co-op chuẩn bắt đầu, tham gia và kết thúc như thế nào.
- Game đang nghiêng về listen server, dedicated server hay mô hình khác.
- Solo và co-op có đi cùng một đường kỹ thuật không.

### Câu hỏi khung

- Người chơi vào game qua world save chung, lobby, invite hay matchmaking.
- MVP nên hỗ trợ bao nhiêu người chơi trong một world.
- Host có đang là máy giữ world, authority và save không.
- Solo có dùng chung hệ mô phỏng với co-op để tránh tách nhánh không.

### Đầu ra mong muốn

- Một đoạn `Session Model and Player Count Assumptions`.

### Trả lời

MVP nên giả định một mô hình `1 host + 1-3 client`, tức thế giới được mở bởi một người chơi làm host và những người còn lại tham gia qua invite hoặc lobby đơn giản. Host nên là điểm giữ authority và save của world trong giai đoạn đầu, vì như vậy giảm bớt chi phí backend và giúp team tập trung vào core loop. Solo nên đi chung một đường mô phỏng với co-op càng nhiều càng tốt, chỉ khác ở chỗ không cần đồng bộ qua mạng. Điều này giúp giảm số nhánh code và làm cho balancing giữa solo với co-op dễ kiểm soát hơn. Dedicated server là hướng hợp lý về sau, nhưng chưa nên là điều kiện bắt buộc để gameplay chuẩn hoạt động.

## Mục 3: Networking Model và quyền quyết định trạng thái

### Điều cần mô tả

- Dữ liệu nào cần độ trễ thấp.
- Dữ liệu nào phải do server hoặc host quyết định.
- Phần nào có thể chấp nhận dự đoán cục bộ, phần nào tuyệt đối không.

### Câu hỏi khung

- Di chuyển, combat, quái, inventory, crafting, loot, khai thác và mở cổng tầng được quyết định ở đâu.
- Có cần tách kênh low-latency và reliable không.
- Có cần snapshot hoặc delta cho world state không.
- Nếu desync xảy ra, hệ nào đau nhất trước.

### Đầu ra mong muốn

- Một đoạn `Networking and Authority Rules`.

### Trả lời

Mạng của game nên tách rõ hai lớp. `Lớp phản hồi nhanh` gồm di chuyển, combat và trạng thái tức thời gần người chơi, nơi client có thể được hỗ trợ bằng prediction hoặc nội suy để cảm giác điều khiển không ì. `Lớp quyết định thật` phải thuộc về host hoặc server-authority, gồm inventory, crafting, rơi đồ, khai thác tài nguyên, boss state, mở cổng dịch chuyển, thay đổi công trình và mọi thứ ảnh hưởng tới economy hoặc progression. Nên tách kênh reliable và low-latency, đồng thời dùng snapshot hoặc delta cho entity state và chunk state để giảm băng thông. Hệ đau nhất nếu desync là loot, inventory, gate milestone và trạng thái boss, nên đây phải là vùng bị khóa authority chặt nhất.

## Mục 4: Save, persistence và quyền sở hữu thế giới

### Điều cần mô tả

- World save lưu những gì.
- Player save lưu những gì.
- Khi rời phiên hoặc reconnect, trạng thái nào được giữ lại.

### Câu hỏi khung

- World save có giữ căn cứ, công trình, boss milestone, cổng tầng, chunk state và resource depletion không.
- Player save có giữ inventory, equipment, vị trí, trạng thái ngắn hạn và dấu mốc cá nhân không.
- Save được ghi khi nào: định kỳ, khi ngủ, khi rời phiên hay khi chạm milestone.
- Nếu host crash hoặc save lỗi, có backup hay versioning không.

### Đầu ra mong muốn

- Một đoạn `Save and Persistence Model`.

### Trả lời

Game nên có `world save` và `player save` tách nhau. World save cần giữ những thứ tạo ra tiến trình chung như căn cứ, workstation, công trình, cổng dịch chuyển đã mở, trạng thái boss milestone, thay đổi chunk đáng kể và một phần depletion của thế giới. Player save cần giữ inventory, equipment, vị trí an toàn hợp lệ hoặc điểm quay lại, cùng một số trạng thái cá nhân ngắn hạn. Autosave nên có chu kỳ rõ và thêm save tại các mốc lớn như dựng công trình quan trọng hoặc mở cổng ổn định. Hệ save cũng nên có bản backup hoặc version slot cơ bản, vì world shared progression là thứ đau nhất nếu hỏng.

## Mục 5: Chunk, streaming và ranh giới mô phỏng

### Điều cần mô tả

- Game mô phỏng thế giới hang mở theo đơn vị nào.
- Khi người chơi tách xa nhau, hệ thống chịu được tới đâu.
- Nội dung nào vẫn cần sống khi không có người ở gần.

### Câu hỏi khung

- World chia theo chunk, room, zone hay cụm biome.
- AI, quái, resource node, machine mana và trap được simulate đầy đủ hay simplified khi ở xa.
- Có giới hạn mềm cho việc người chơi tách quá xa nhau không.
- Nếu không có streaming rõ, cost hiệu năng sẽ vỡ ở đâu trước.

### Đầu ra mong muốn

- Một đoạn `World Streaming and Simulation Boundary`.

### Trả lời

Hang mở nên được chia theo chunk hoặc zone đủ rõ để stream theo vị trí người chơi, còn các interior như ruins có thể là cụm nhỏ hoặc scene riêng dễ kiểm soát hơn. Mô phỏng đầy đủ chỉ nên diễn ra quanh người chơi hoặc quanh những điểm thực sự quan trọng; những vùng xa nên dùng simplified simulation cho resource respawn, machine state hoặc world time thay vì giữ AI và combat hoạt động đầy đủ. Co-op vẫn nên cho phép tách nhau ở mức nào đó, nhưng MVP không nên giả định cả đội sẽ phân tán khắp bản đồ quá mạnh cùng lúc. Nếu không đặt ranh giới mô phỏng rõ, hiệu năng, băng thông và bug tái hiện sẽ vỡ trước cả khi content đủ dày.

## Mục 6: Content pipeline và cách designer author game

### Điều cần mô tả

- Designer tạo biome, POI, interior, quái, loot và gate milestone bằng pipeline nào.
- Nội dung nào nên data-driven, nội dung nào nên hand-made.
- Một thay đổi design sẽ đi qua các bước tool nào.

### Câu hỏi khung

- Biome, enemy family, resource spawn, POI, gate và boss được cấu hình bằng data table, prefab, script hay code tay.
- Content có tái tổ hợp được không hay mỗi thứ đều cần code riêng.
- Designer có thể đổi spawn rule, loot rule, gate cost, mana cost mà không chờ programmer quá nhiều không.
- Nếu không có pipeline đủ dữ liệu, bottleneck sản xuất nằm ở đâu.

### Đầu ra mong muốn

- Một đoạn `Content Production Pipeline`.

### Trả lời

Pipeline của game nên data-driven ở mức đủ mạnh để designer chỉnh được phần lớn content mà không phải chờ code cho từng thay đổi nhỏ. Spawn quái, phân bố tài nguyên, loot table, gate cost, mana cost, POI frequency và rule của biome nên nằm ở data table hoặc preset có thể chỉnh được. Các đối tượng gameplay nên đi qua prefab hoặc template thống nhất, còn nội dung milestone như boss lớn, ruins đặc biệt hoặc gate mốc có thể hand-made hơn. Mục tiêu của pipeline không phải là “không cần programmer”, mà là giảm số lần phải đụng code cho những thay đổi lặp lại hàng ngày của design và content team.

## Mục 7: Scope kỹ thuật, đội ngũ và ranh giới MVP

### Điều cần mô tả

- MVP kỹ thuật nên dừng ở đâu.
- Những gì nghe hợp lý nhưng chưa nên cam kết.
- Hướng cắt scope nào ít đau nhất nếu production chậm.

### Câu hỏi khung

- MVP có thực sự cần dedicated server, host migration, crossplay, cloud save hay matchmaking công cộng không.
- Nếu đội nhỏ, phần nào nên lấy giải pháp đơn giản nhưng chắc.
- Nếu phải cắt bớt một lớp kỹ thuật, lớp nào cắt trước mà vẫn giữ được trải nghiệm chuẩn.
- Chi phí QA của từng lựa chọn lớn nằm ở đâu.

### Đầu ra mong muốn

- Một đoạn `MVP Technical Boundary`.

### Trả lời

Ranh giới MVP nên được giữ khá rõ: một world shared progression, mô hình host-authoritative listen server, 1-4 người chơi, save bền vững đủ tốt và một pipeline content đủ để team sản xuất đều tay. Dedicated server, host migration mượt, crossplay hoặc cloud service nặng đều là những thứ có thể rất đáng giá về sau, nhưng chưa nên là tiêu chí sống còn cho vòng đầu. Nếu phải cắt scope, nên cắt những thứ liên quan scale, platform và service trước; không nên cắt authority đúng chỗ, save recovery hay debug tools, vì đó là các lớp giữ game chạy ổn thật sự.

## Mục 8: Debug, QA và công cụ quan sát nội bộ

### Điều cần mô tả

- Team cần những công cụ gì để test, tái hiện lỗi và balance game.
- Designer và QA có cách nào kiểm tra nhanh content, gate, loot và economy không.
- Multiplayer có công cụ nào để bắt desync, lag và save lỗi không.

### Câu hỏi khung

- Có cần console spawn item, teleport, reveal map, force gate state, spawn boss, set mana, set weather không.
- Có cần log authority, log save, log inventory delta, log gate milestone không.
- Có cần network simulation cho ping, packet loss, disconnect, reconnect không.
- Nếu không có bộ tool này, khâu test sẽ đau ở đâu.

### Đầu ra mong muốn

- Một đoạn `Internal Debug and QA Toolkit`.

### Trả lời

Game này rất cần bộ công cụ nội bộ tốt ngay từ sớm vì bug đau nhất của nó nằm ở giao điểm giữa progression, save, multiplayer và world state. Tối thiểu nên có console hoặc tool panel cho spawn item, teleport, mở chunk nhanh, đặt gate state, spawn boss, chỉnh mana, chỉnh loot và giả lập ping hoặc packet loss. Cũng nên có log hoặc inspector cho inventory delta, save snapshot, gate milestone và các thay đổi world quan trọng. Nếu không có bộ tool này, mỗi lần test sâu tới tầng 3+, mở cổng hoặc tái hiện desync sẽ tốn quá nhiều vòng đời phát triển.

## Mục 9: Reliability, recovery và ranh giới vận hành sau phát hành

### Điều cần mô tả

- Game phụ thuộc vào dịch vụ online tới mức nào.
- Khi host rớt, mất mạng, save lỗi hoặc version lệch, người chơi bị đau ở đâu.
- Team có đang cam kết một gánh support quá lớn không.

### Câu hỏi khung

- Core loop có còn chơi được nếu không có backend nặng không.
- Host crash, client rớt mạng, save corrupt và update version mismatch được xử lý ra sao.
- Có cần migration tool, backup slot, world versioning hay compatibility layer không.
- Sau phát hành, đội ngũ có đủ sức support các promise kỹ thuật đã hứa không.

### Đầu ra mong muốn

- Một đoạn `Reliability and Service Boundary`.

### Trả lời

Core loop của game nên còn chơi được mà không cần một backend nặng hoặc live service liên tục, vì điều đó giảm áp lực vận hành và giúp đội tập trung vào chất lượng gameplay. Những failure mode thật sự cần chăm từ sớm là host crash, save hỏng, version lệch và desync dẫn đến mất loot hoặc mất milestone. World save nên có backup slot hoặc versioning cơ bản, còn reconnect và recover nên có hành vi rõ ràng thay vì “cầu mong không lỗi”. Đội ngũ không nên hứa quá sớm những tính năng vận hành tốn support như migration hoàn hảo, cross-version compatibility rộng hoặc online dependency liên tục nếu chưa có năng lực giữ lời.

## Mục 10: Kết luận vận hành và kỹ thuật

### Điều cần mô tả

- Mảng kỹ thuật nào là lõi bắt buộc.
- Mảng nào quan trọng nhưng phải giữ mỏng.
- Mảng nào nên để sau để tránh nổ scope.

### Đầu ra mong muốn

- Một danh sách `Operational and Technical Priority Map`.

### Trả lời

- `Bắt buộc`
  `Session Model`: Cần có vì nếu không chốt mô hình phiên chơi, mọi quyết định multiplayer và save phía sau đều mơ hồ.
  `Network Authority Rules`: Cần có vì loot, progression, gate milestone và inventory không chịu được authority lỏng.
  `Save and Persistence`: Cần có vì shared world progression là phần thưởng dài hạn lớn nhất của game.
  `Chunk or Streaming Boundary`: Cần có vì hang mở và co-op sẽ làm hiệu năng, băng thông và bug vỡ rất nhanh nếu không có ranh giới mô phỏng.
  `Content Pipeline`: Cần có vì game sống nhờ nhiều lớp content và không thể phụ thuộc code tay cho mọi chỉnh sửa nhỏ.
  `Debug and QA Toolkit`: Cần có vì đây là lớp giúp team thật sự làm chủ bug network, save, gate và economy.
  `Reliability Basics`: Cần có vì save hỏng hoặc desync milestone sẽ phá niềm tin của người chơi rất mạnh.

- `Quan trọng nhưng phải tiết chế`
  `Dedicated Server Support`: Có giá trị nếu game chứng minh được nhu cầu world sống lâu, nhưng chưa nên là điều kiện MVP.
  `Host Migration`: Hữu ích cho trải nghiệm mượt hơn, nhưng cost QA và failure mode cao.
  `Telemetry and Analytics`: Hữu ích để cân bằng và bắt lỗi, nhưng nên giữ ở mức giúp ra quyết định chứ không thành dự án riêng.
  `Designer-facing Authoring Tools`: Có giá trị lớn, nhưng nên phát triển đúng điểm nghẽn thật chứ không làm editor quá sớm.

- `Để sau`
  `Crossplay`: Dễ nhân mạnh cost QA và support.
  `Public Matchmaking`: Không phải lõi của fantasy nhóm bạn co-op trong world shared progression.
  `Mod Support`: Hấp dẫn nhưng kéo thêm compatibility, tooling và support cost lớn.
  `Replay or Spectator Systems`: Không phải nhu cầu lõi của vòng gameplay hiện tại.
  `Heavy Live Ops Backend`: Dễ kéo dự án sang bài toán dịch vụ thay vì game loop.

- `Nguy cơ cần canh`
  Network authority quá lỏng làm vỡ loot, gate và progression.
  Save world quá chi tiết nhưng không có recovery tốt.
  Co-op cho phép tách quá xa mà không có ranh giới mô phỏng rõ.
  Pipeline content phụ thuộc quá nhiều vào programmer.
  Tool nội bộ quá yếu khiến chi phí debug cao hơn chi phí làm tính năng.

## Điều kiện để qua cấp 8

- Có bản đồ ràng buộc vận hành và kỹ thuật đủ rõ để biết game MVP nên chạy theo mô hình nào.
- Biết authority, save, chunk, pipeline và debug tool gặp nhau ở đâu trong thực tế sản xuất.
- Biết cái gì nên giữ chắc cho MVP và cái gì tuyệt đối không nên hứa sớm.
- Nhìn ra ít nhất 3 failure mode hoặc production bottleneck lớn cần xử lý trước khi vào đặc tả chi tiết.

