import cv2
import os
import time

def play_video(file_path: str) -> None:
    print(f"Trying to open video file: {file_path}")

    # ファイルの存在確認
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        return

    # 動画ファイルを読み込む
    cap = cv2.VideoCapture(file_path)

    if not cap.isOpened():
        print(f"Error: Could not open video file: {file_path}")
        return

    # ウィンドウを作成し、全画面表示に設定
    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while cap.isOpened():
        # フレームを一つずつ読み込む
        ret, frame = cap.read()
        
        if not ret:
            print("End of video or error reading frame.")
            break

        # フレームを表示する
        cv2.imshow('Video', frame)
        
        # 1ミリ秒ごとにキー入力を待つ
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # ビデオ再生が終了したら、ウィンドウを閉じる
    cap.release()
    cv2.destroyAllWindows()
    time.sleep(1) # 投影された映像による影響を避けるために1秒待機