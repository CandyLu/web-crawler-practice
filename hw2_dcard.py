import requests
import re
from bs4 import BeautifulSoup

def main():
    # 從Dcard 的今日熱門文章區塊, 取得前十篇熱門文章的標題
    url = 'https://www.dcard.tw/f'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    articles = []
    # 利用 regex 找出所有 'PostList_entry_' 開頭的 div
    for div in soup.find_all('div', re.compile('PostList_entry_\w{6}')):
        articles.append({'title': div.h3.text.strip()})
    print('共%d篇' %len(articles))
    for a in articles[:10]:
        print(a)

if __name__ == '__main__':
    main()