## 概要
このプロジェクトは、商品在庫データベースへのデータ登録、更新、取得、削除を行うための簡易的なAPIを実装することを目的としています。

## プロジェクトの目的
- APIの仕組みや動作について理解を深める
- FastAPIフレームワークを使用したAPI開発の基礎を学ぶ

## 機能
1. 在庫の更新、作成:	指定した商品について在庫を追加し、商品名と追加した個数のペアをレスポンスとして返すAPI
2. 在庫チェック:	商品について、商品名と現状の在庫の数のペアを返すAPI。商品名を指定した場合は（在庫の有無に関わらず）指定した商品の在庫数を返し、指定しない場合は在庫があるすべての商品のものを返す。
3. 販売	指定した商品について、在庫の数を減らして売上として加算するAPI
4. 売り上げチェック:	これまで((5)の全削除API実行以降)に(3)の販売のAPI実行により売り上げた総売上を確認するAPI
5. 全削除:	在庫及び売り上げをすべて削除するAPI

## 使用方法
1. リポジトリをローカルにclone: ```git clone git@github.com:ANS0025/inventory-management-api.git```
2. ディレクトリを移動: ```cd inventory-management-api```
3. 必要パッケージのインストール: ```docker-compose run --entrypoint "poetry install --no-root" demo-app```
4. コンテナの起動: ```docker-compose build --no-cache```
5. APIをテスト: http://localhost:8000/docs#/default/

## 実行例
```
//(1) 在庫の更新、作成
$ curl -v -d '{"name": "xxx", "amount": 100}' -H 'Content-Type: application/json' http://xx.xx.xx.xx/v1/stocks
{"name":"xxx","amount":100}

//(2) 在庫チェック
//URI が /v1/stocks/xxx の場合の実行例
$ curl http://xx.xx.xx.xx/v1/stocks/xxx
{"xxx":100}

//URI が /v1/stocks の場合の実行例
$ curl http://xx.xx.xx.xx/v1/stocks
{"YYY":100,"xxx":96,"yyy":100}

//(3) 販売
$ curl -v -d '{"name": "xxx", "amount": 4}' -H 'Content-Type: application/json' http://xx.xx.xx.xx/v1/sales
{"name":"xxx","amount":4}

//(4) 売り上げチェック
$ curl http://xx.xx.xx.xx/v1/sales
{"sales":400.0}

//(5) 全削除
$ curl -d '{"name": "YYY", "amount": 100}' -H 'Content-Type: application/json' http://xx.xx.xx.xx/v1/stocks
{"name":"YYY","amount":100}

$ curl http://xx.xx.xx.xx/v1/stocks
{"YYY":100,"xxx":96,"yyy":100}
```

## 参考資料
- [FastAPI入門](https://zenn.dev/sh0nk/books/537bb028709ab9)
