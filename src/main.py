import cv2
from ultralytics import YOLO
import detect
import time

def init() -> tuple[YOLO, cv2.VideoCapture]:
    model: YOLO = YOLO("yolov8n.pt")  # モデルをロード
    cap: cv2.VideoCapture = cv2.VideoCapture(0)  # カメラデバイスを開く
    if not cap.isOpened():
        print("カメラが開けません。")
        exit(1)

    return model, cap


def main():
    print("start program")
    model, cap = init()
    while(True):
        if detect.detect_objects(model=model, cap=cap):
            print('OK')
        else:
            print('NG')
        time.sleep(0.5)
    cap.release()  # カメラデバイスを解放
    cv2.destroyAllWindows()  # 全てのOpenCVウィンドウを閉じる
    
    
if __name__ == "__main__":
    main()
    