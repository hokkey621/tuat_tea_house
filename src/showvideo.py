import cv2

def play_video(file_path: str) -> None:
    # 動画ファイルを読み込む
    cap = cv2.VideoCapture(file_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return
    
    # ウィンドウを作成し、全画面表示に設定
    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while cap.isOpened():
        # フレームを一つずつ読み込む
        ret, frame = cap.read()
        
        if not ret:
            print("End of video.")
            break

        # フレームを表示する
        cv2.imshow('Video', frame)

        # 'q'キーが押されたらループを終了する
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # リソースを解放する
    cap.release()
    cv2.destroyAllWindows()
