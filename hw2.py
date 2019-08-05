import requests
import re
from bs4 import BeautifulSoup

def main():
    resp = requests.get('http://blog.castman.net/web-crawler-tutorial/ch2/blog/blog.html')
    soup = BeautifulSoup(resp.text, 'html.parser')
    # 找出範例網頁一 總共有幾篇 blog 貼文
    blogs = soup.find_all('div', 'card card-blog')
    print('總共有%d篇blog貼文' %len(blogs))

    # 找出範例網頁一 總共有幾張圖片網址含有 ‘crawler’ 字串
    imgs = soup.find_all('img', {'src': re.compile('crawler')})
    print('總共有%d張圖片網址含有\'crawler\'字串' %len(imgs))

    # 找出範例網頁二 總共有幾堂課程
    resp = requests.get('http://blog.castman.net/web-crawler-tutorial/ch2/table/table.html')
    soup = BeautifulSoup(resp.text, 'html.parser')
    courses = soup.find('table', 'table').tbody.find_all('tr')
    print('總共有%d堂課程' %len(courses))

if __name__ == '__main__':
    main()