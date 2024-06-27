import cv2

def play_video(file_path):
    # 動画ファイルを読み込む
    cap = cv2.VideoCapture(file_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

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

# ビデオファイルのパスを指定する
video_file_path = 'path/to/your/video.mp4'
play_video(video_file_path)
