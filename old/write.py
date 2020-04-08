a = ['登金陵鳳凰臺\n', '朝代：唐代\n', '作者：李白\n', '原文：\n', '鳳凰臺上鳳凰遊，鳳去臺空江自流。\n', '吳宮花草埋幽徑，晉代衣冠成古丘。\n', '三山半落青天外，二水中分白鷺洲。(二水 一作：一水)\n', '總爲浮雲能蔽日，長安不見使人愁。', '']

file = open("/Users/xiezhengqi/Desktop/travian.txt", "a+")
for i in a:
    file.write(i)
file.close()
