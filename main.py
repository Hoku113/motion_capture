"""
Intel AI Global impact festivalに出展するためのプログラム
"""

# モジュールをインポートする
import cv2
import usd
import datetime


# 表示する画角の決定
HEIGHT = 720
WAITH = 1280

# カメラを読みこむ

cap = cv2.VideoCapture(0)

# カメラの画面を起動させる
while True:
    filename = "motion_{}.mp4".format(datetime.datetime.now())
    ret, img = cap.read()
    img = cv2.resize(img, (WAITH, HEIGHT), cv2.INTER_AREA)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # スペースキーを押して録画の開始

    # 録画したデータを保存


# ポーズ検出モデルに動画のデータを送りスケルトンデータの動画として返す

# スケルトンデータの動画をfunctionに送信してスケルトンアニメーションデータとして返す

# スケルトンアニメーションデータをusdファイル形式にして保存する
