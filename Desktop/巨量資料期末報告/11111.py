
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import jieba
import numpy as np
from collections import Counter

# 如果檔案內有一些編碼錯誤，使用 errors='ignore' 來忽略錯誤
with open("test.txt", encoding="UTF-8", errors='ignore') as f:
    text = f.read()
# 設定斷詞
jieba.set_dictionary('dict.txt')
wordlist = jieba.cut(text)
words = " ".join(wordlist)

# 從 Google 下載的中文字型
font = 'SourceHanSansTW-Regular.otf'

#背景顏色預設黑色，改為白色、使用指定圖形、使用指定字體
my_wordcloud = WordCloud(background_color='white',font_path=font).generate(words)

#產生圖片

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
#存檔
wordcloud.to_file('word_cloud.png')