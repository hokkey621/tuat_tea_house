import asyncio
import cv2
from ultralytics import YOLO
import time


async def showbb(model: YOLO, cap: cv2.VideoCapture) -> None:
    """
    モデルとビデオキャプチャを使用してリアルタイムで境界ボックスを表示します。

    Args:
        model (YOLO): フレームを処理するために使用されるYOLOモデル。
        cap (cv2.VideoCapture): ビデオキャプチャオブジェクト。

    Returns:
        None
    """
    ret, frame = cap.read()
    if not ret:
        print("フレームが読み込めません。")
        return
    results = model(frame, show=True) # モデルでフレームを処理
    

async def detect_objects(model, cap, view) -> bool:
    """
    Detects objects in frames using the YOLOv8 model.

    Args:
        model: The YOLOv8 model used for object detection.
        cap: The video capture object used to read frames.

    Returns:
        bool: True if any of the specified objects ('wine glass', 'cup', 'bowl') are detected, False otherwise.
    """
    # フレームを読み込む
    ret, frame = cap.read()
    if not ret:
        print("フレームが読み込めません。")
        return
    
    # フレームをYOLOv8モデルに渡して検出を実行
    results = model(frame, conf=0.25)
    
    # 検出されたオブジェクトのクラスIDとラベルを取得
    object_exists = False
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)
            label = model.names[class_id]
            
            # 検出するオブジェクトのラベルが含まれているかどうかを確認
            if label in 'cup':
                object_exists = True
                break
        if object_exists:
            break
    
    if view:
        # フレームをウィンドウに表示
        cv2.imshow('YOLOv8 Real-Time Object Detection', frame)
        
    # 存在するかどうかを返す
    return True if object_exists else False