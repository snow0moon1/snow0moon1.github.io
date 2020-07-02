import jieba.analyse
import pandas as pd
import jieba
import numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
jieba.set_dictionary('dict.txt')
colrogroup = ['#427f8f','#4a8fa1','#559db0','#66a7b8','#77b1c0','#89bbc8','#9ac5d0','#bdd9e0','#cee3e8','#e0edf0']
colrogroup2 = ['#cd0003','#e60003','#ff0004','#ff1a1d','#ff3436','#ff4d4f','#ff6768','#ff8181','#ff9a9b','#ffb4b4']
# 無意義字元列表，可以自行新增
removeword = ['span','class','f3','https','imgur','h1','_   blank','href','rel',
              'nofollow','target','cdn','cgi','b4','jpg','hl','b1','f5','f4',
              'goo.gl','f2','email','map','f1','f6','__cf___','data','bbs'
              'html','cf','f0','b2','b3','b5','b6','原文內容','原文連結','作者'
              '標題','時間','看板','<','>','，','。','？','-','閒聊','・','/',
              ' ','=','\"','\n','」','「','！','[',']','：','‧','╦','╔','╗','║'
              ,'╠','╬','╬',':','╰','╩','╯','╭','╮','│','╪','─','《','》','_'
              ,'.','、','（','）',' ','*','※','~','○','"','"','～','@','＋','\r'
              ,'▁',')','(','-','═','?',',','!','…','&',';','『','』','#','＝'
              ,'\l']
#設定你關心的名稱
country = ['中國','澳洲','台灣','日本','非洲']
# 讀入爬蟲資料
pig=pd.read_csv('test.csv',encoding='utf-8',engine='python',error_bad_lines=False) #開啟檔案

#所有文章和標題都串在一起
thearticle = pig['標題'] + pig['內文']

# 移除無意義字元列
for word in removeword:
    thearticle = thearticle.replace(word,'')

#搜尋每個句子中，有出現該品牌的名稱，就+1
tatal_country = []
for mov in country:
    count = 0
    for art in thearticle:
        if mov in art:
            count = count +1
    tatal_country.append(count)
    
    
# 繪畫
plt.bar(country, tatal_country, color=colrogroup) #給予線標籤
plt.xticks(fontsize=15,rotation=90) 
plt.xlabel('名稱', fontsize=15)
plt.ylabel('聲量', fontsize=15)
plt.title('聲量分析', fontsize=20)
plt.show()