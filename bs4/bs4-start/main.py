import requests
from bs4 import BeautifulSoup
import lxml

# with open("website.html", encoding='utf8') as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title.string)
# all_anchor_tags = soup.find_all(name='a')
# # print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.getText())

response = requests.get("https://news.ycombinator.com/")

yc_wp = response.text

soup = BeautifulSoup(yc_wp, 'lxml')

titles = soup.find_all(name='a', attrs={'rel':'noreferrer'})
article_titles = []
for title in titles:
    # print(title.string)
    article_titles.append(title.string)
print(article_titles)
