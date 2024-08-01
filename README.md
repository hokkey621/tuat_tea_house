# tuat_tea_house

## 概要
`tuat_tea_house`は，画像認識技術（YOLO V8 & Open CV）を用いて，飲み物が入ったコップにプロジェクタ動画を投影するプログラムです．このプロジェクトは，チームラボのEN TEA HOUSEに触発されて開発しました．

## デモ

https://github.com/hokkey621/tuat_tea_house/assets/70475604/ff8e2fe4-01e6-4f0e-a494-e3d321879fc7

## 特徴
- **画像認識技術の利用**: YOLO V8とOpenCVを組み合わせて，リアルタイムで容器に最適な画像を投影します．
- **インタラクティブ体験**: 飲み物の入った容器に動画を投影することで，視覚的な楽しみを提供します．

## 必要条件
このプロジェクトはRyeを使用して依存関係を管理しています．以下のパッケージが必要です:

- Python==3.12
- pip==24.0
- ultralytics==8.2.10
- opencv-python==4.9.0.80

## 使い方
リポジトリをクローンし，必要な依存関係をインストールしてプロジェクトを実行します:

```bash
git clone https://github.com/hokkey621/tuat_tea_house.git
cd tuat_tea_house/src
python main.py
```

## ライセンス
`tuat_tea_house`は[MITライセンス](https://en.wikipedia.org/wiki/MIT_License)のもとで公開されています．
