import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = open("./1.txt", encoding="utf-8").read()  # 标明文本路径，打开

# 生成对象
wc = WordCloud(font_path="C:\Windows\Fonts\Microsoft YaHei UI\msyh.ttc", width=500, height=400, mode="RGBA",
               background_color=None).generate(text)
# 显示词云图
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

# 保存文件
wc.to_file("./good_link")