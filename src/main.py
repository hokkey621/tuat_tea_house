import asyncio
import cv2
from ultralytics import YOLO

from count import calculate_area_ratios
from detect import detect_objects
from showvideo import play_video


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
    detected = False
    
    while True:
        # コップがあるかどうかを検出
        is_object_exist = asyncio.run(detect_objects(model=model, cap=cap, view=False))
        # 白面積の割合を計算
        white_ratio = asyncio.run(calculate_area_ratios(cap=cap, view=False))
        
        # 結果を出力
        if is_object_exist:
            print("\033[92m", is_object_exist, white_ratio, "\033[0m")  # Green color for True
        else:
            print("\033[91m", is_object_exist, white_ratio, "\033[0m")  # Red color for False
            continue # Skip the rest of the loop
        
        if white_ratio > 40:
            # 満開の桜の動画を再生
            play_video('../movies/fullbloom.mov')
            detected = True
        elif white_ratio > 15:
            # 半開の桜の動画を再生
            play_video('../movies/scattering.mov')
            detected = True
        else:
            if detected:
                # 散るさくらの動画を再生
                play_video('../movies/scattered.mov')
                detected = False

        # 'q'キーが押されたら終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # リソースを解放
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
