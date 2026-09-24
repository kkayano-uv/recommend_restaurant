# Roboko Restaurant Recommender

Pythonで作成した対話型のレストラン推薦CLIアプリです。
ユーザーの名前を聞き、登録済みのレストラン候補をおすすめし、好みをもとに投票数をCSVへ保存します。

## Demo

```text
こんにちは、私はRoboko！あなたの名前は？
Taro
Taroさん、どこのレストランが好き？
japan
私のおすすめのレストランは、chineseです。
このレストランはお好きですか？[Yes/No]
No
... 
Taroさん。ありがとう！
良い1日を！
```

## Features

- 名前を入力して会話形式で開始
- 食べたいレストランを入力できる
- 保存済みのレストランを推薦し、Yes/Noでフィードバック
- 投票数をCSVに反映
- 追加されたレストランも自動で保存
- Python標準ライブラリのみで実装

## Tech Stack

- Python 3.14+
- CSV-based data persistence
- pathlib / os / csv

## Project Structure

```text
restaurant-app/
├── data/
│   └── restaurant.csv
├── src/
│   └── restaurant_app/
│       ├── __init__.py
│       ├── main.py
│       └── restaurant.py
├── pyproject.toml
├── README.md
└── .gitignore
```

## Data Format

データは `data/restaurant.csv` に保存されます。

```csv
NAME,COUNT
japan,2
chinese,3
```

## Quick Start

### 1. Clone

```bash
git clone https://github.com/your-name/restaurant-app.git
cd restaurant-app
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Run the app

```bash
uv run python src/restaurant_app/main.py
```

## How It Works

1. アプリがユーザー名を聞く
2. CSVから保存済みのレストラン候補を読み込む
3. おすすめレストランを表示し、好みを確認
4. 好きなレストラン名を入力
5. そのレストランの投票数を加算し、CSVへ保存

## Example Use Case

- 個人開発の小さなCLIアプリ
- PythonのCSV操作の練習
- GitHubに載せたポートフォリオ作品
- 自分用のレストラン選び補助ツール

## License

This project is licensed under the MIT License.

## Notes

このリポジトリは、GitHubに公開して作品として見せることを前提に作成しています。
READMEはそのままリポジトリの説明文として使えるように整理しています。

