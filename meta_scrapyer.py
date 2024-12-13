import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_metadata(url):
    try:
        # 發送請求獲取網頁內容
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # 解析 HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # 獲取網頁標題
        title = soup.title.string if soup.title else ""

        # 獲取 favicon
        icon = ""
        favicon = soup.find("link", rel=["icon", "shortcut icon"])
        if favicon and favicon.get("href"):
            icon = urljoin(url, favicon["href"])

        # 建立輸出字典
        metadata = {
            "title": title.strip(),
            "caption": "",  # 依照需求留空
            "url": url,
            "icon": icon,
        }

        return metadata

    except Exception as e:
        print(f"發生錯誤: {str(e)}")
        return None


# 使用範例
url = input("請輸入網址: ")
result = get_metadata(url)
if result:
    print(f"title = \"{result['title']}\"")
    print(f"caption = \"{result['caption']}\"")
    print(f"url = \"{result['url']}\"")
    print(f"icon = \"{result['icon']}\"")
