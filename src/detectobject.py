import cv2
from ultralytics import YOLO


def detect():
    model = YOLO("yolov8n.pt")  # モデルをロード
    cap = cv2.VideoCapture(0)  # カメラデバイスを開く

    if not cap.isOpened():
        print("カメラが開けません。")
    else:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("フレームが読み込めません。")
                break
            results = model(frame, show=True)  # モデルでフレームを処理
            if cv2.waitKey(1) == ord('q'):  # 'q' を押すと終了
                break

    cap.release()  # カメラデバイスを解放
    cv2.destroyAllWindows()  # すべてのOpenCVウィンドウを閉じる
