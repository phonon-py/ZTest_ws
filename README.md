# Flask Notion API Integration

このプロジェクトはFlaskを使用して、特定のNotionページにMarkdown形式のテキストを送信するWebアプリケーションです。ユーザーはWebフォームを介してテキストを入力し、送信することで、Notionページが更新されます。

## セットアップ手順

このプロジェクトをローカルで実行するには、以下の手順に従ってください：

1. リポジトリをクローンする：
   ```bash
   git clone <リポジトリのURL>
   cd <クローンしたディレクトリ>

2. config.py ファイルを作成し、Notion APIトークンとページIDを設定する。

    使用方法
アプリケーションを起動するには、以下のコマンドを実行します：
    ```bash
    python app.py
    ```
    Webブラウザで http://127.0.0.1:5000/ にアクセスして、フォームを使用してNotionにMarkdownテキストを送信できます。

 ## アプリケーションのコード
以下にアプリケーションの主要な部分のコードを示します：
```python
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
        return f"リクエスト成功。レスポンス: {response.json()}"
    else:
        return f"リクエスト失敗。ステータスコード: {response.status_code} レスポンス: {response.json()}"

def create_notion_page(markdown_content):
    # ...コードの続き...

```   