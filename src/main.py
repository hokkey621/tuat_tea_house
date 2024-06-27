import asyncio
import cv2
from ultralytics import YOLO
import detect
import time
from count import calculate_area_ratios


def init() -> tuple[YOLO, cv2.VideoCapture]:
    model: YOLO = YOLO("yolov8n.pt")  # モデルをロード
    cap: cv2.VideoCapture = cv2.VideoCapture(0)  # カメラデバイスを開く
    if not cap.isOpened():
        print("カメラが開けません。")
        exit(1)

    return model, cap


def main():
    # モデルとカメラデバイスを初期化
    model, cap = init()
    while True:
        # コップがあるかどうかを検出
        is_object_exist = asyncio.run(detect.detect_objects(model=model, cap=cap, view=False))
        # 白面積の割合を計算
        white_ratio = asyncio.run(calculate_area_ratios(cap=cap, view=True))
        
        # 結果を出力
        print(is_object_exist, white_ratio)

        # 'q'キーが押されたら終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        time.sleep(0.5)

    # リソースを解放
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
