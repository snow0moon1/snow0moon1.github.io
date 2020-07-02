import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
keyword='豬瘟'
 # 要抓取的網址
url = 'https://tw.finance.yahoo.com/news_search.html?ei=Big5&q=' + quote(keyword.encode('big5'))
#請求網站
list_req = requests.get(url)
#將整個網站的程式碼爬下來
soup = BeautifulSoup(list_req.content, "html.parser")
get_all_news = soup.find('table', { 'id': 'newListTable' })
single_news_tag_array = get_all_news.find_all('table')
# get all news title
all_news_title = []
all_news_body = []
all_news_links = []
for news in single_news_tag_array:
    title_tags = news.find_all('a', { 'class': 'mbody' })
    if len(title_tags) >= 2:
        title = title_tags[-1].get_text()
        all_news_title.append(title)
# get all news body
    body = news.find_all('span', { 'class': 'mbody' })
    if len(body) >= 2:
        all_news_body.append(body[0].get_text())
# get all links to news
    a_tags = news.find_all('span', { 'class': 'mbody' })
    for tag in a_tags:
        link = tag.find('a')
        if link != None:
            all_news_links.append(link['href'])
# print to console
f1 = open("test.txt", "w",encoding="UTF-8")
f2 = open("test.csv", "w",encoding="UTF-8")

f2.write('標題,內文\n')

for i in range(len(all_news_title)):
    print('標題: {}'.format(all_news_title[i]))
    print('內文: {}'.format(all_news_body[i]))
    print('詳全文網址: {}'.format(all_news_links[i]))
    print()
    f1.write('{}{}\n'.format(all_news_title[i],all_news_body[i]))
    f2.write('{},{}\n'.format(all_news_title[i],all_news_body[i]))
f1.close()
f2.close()