import cv2
from ultralytics import YOLO


def init() -> tuple[YOLO, cv2.VideoCapture]:
    model: YOLO = YOLO("yolov8n.pt")  # モデルをロード
    cap: cv2.VideoCapture = cv2.VideoCapture(0)  # カメラデバイスを開く

    if not cap.isOpened():
        print("カメラが開けません。")

    return model, cap


def showbb() -> None:
    """
    モデルとビデオキャプチャを使用してリアルタイムで境界ボックスを表示します。

    Args:
        model (YOLO): フレームを処理するために使用されるYOLOモデル。
        cap (cv2.VideoCapture): ビデオキャプチャオブジェクト。

    Returns:
        None
    """
    # 初期化
    model, cap = init()
    
    # リアルタイムでバウンディングボックスを表示
    while True:
        ret, frame = cap.read()
        if not ret:
            print("フレームが読み込めません。")
            break
        results = model(frame, show=True) # モデルでフレームを処理
        if cv2.waitKey(1) == ord('q'):  # 'q'を押して終了
            break

    cap.release()  # カメラデバイスを解放
    cv2.destroyAllWindows()  # 全てのOpenCVウィンドウを閉じる
