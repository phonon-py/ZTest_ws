from flask import Flask, request, render_template
import requests
from datetime import datetime
from config import NOTION_TOKEN, NOTION_PAGE_ID  

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    markdown_content = request.form['markdown_content']
    response = create_notion_page(markdown_content)
    if response.status_code == 200:
        message = f"リクエスト成功。レスポンス: {response.json()}"
    else:
        message = f"リクエスト失敗。ステータスコード: {response.status_code} レスポンス: {response.json()}"
    return render_template('response.html', message=message)

def create_notion_page(markdown_content):
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    title_content = f"{current_time} Python 3 Data Analyst"

    data = {
        "parent": {"page_id": NOTION_PAGE_ID},
        "properties": {
            "title": {
                "title": [
                    {
                        "text": {
                            "content": title_content
                        }
                    }
                ]
            }
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": markdown_content,
                                "link": None
                            }
                        }
                    ]
                }
            }
        ]
    }

    return requests.post('https://api.notion.com/v1/pages', headers=headers, json=data)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
