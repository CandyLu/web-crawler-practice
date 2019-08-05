import requests
from bs4 import BeautifulSoup

def main():
    # 取出範例網頁的標題 (title) 與段落文字
    # 讓程式試著取出範例網頁中不存在的標籤文字 (如 button.text), 並且在標籤不存在時, 程式能正常結束
    title = get_head_text('http://blog.castman.net/web-crawler-tutorial/ch1/connect.html', 'title')
    print(title)
    p = get_head_text('http://blog.castman.net/web-crawler-tutorial/ch1/connect.html', 'p')
    print(p)
    button = get_head_text('http://blog.castman.net/web-crawler-tutorial/ch1/connect.html', 'button')
    print(button)

def get_head_text(url, head_tag):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            return soup.find(head_tag).text
    except Exception as e:
        return None

if __name__ == '__main__':
    main()
