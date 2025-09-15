# 対話型商品レコメンド生成 AI アプリ

## 概要

本アプリは、ユーザーの要望や特徴をチャット形式で入力することで、最適な商品を AI がレコメンドする Web アプリです。

## 特徴

- Streamlit による直感的な UI/UX
- CSV データを活用した商品情報管理
- LangChain や OpenAI API を活用した自然言語処理・レコメンドロジック

## 使い方

1. 画面下部のチャット欄に「欲しい商品の特徴や要望」を日本語で入力
2. AI が最適な商品をレコメンドし、詳細情報・画像を表示
3. 過去の会話履歴も画面上で確認可能

## 技術スタック

- Python
- Streamlit
- LangChain
- OpenAI API
- ChromaDB

## ディレクトリ構成

- main.py : アプリのエントリーポイント
- components.py : 画面表示用コンポーネント
- initialize.py : 初期化処理
- utils.py : ユーティリティ関数
- constants.py : 定数管理
- data/products.csv : 商品データ
- images/ : 商品画像・アイコン



https://github.com/user-attachments/assets/f0c2e8aa-ee05-480e-a3df-21d05e2fc0ab


