import asyncio
import cv2


async def calculate_area_ratios(cap: cv2.VideoCapture, view: bool) -> float:
    """
    Calculates the ratio of white area to the whole area in a frame.

    Args:
        cap (cv2.VideoCapture): The video capture object.
        view (bool): Whether to display the frame and binary image.

    Returns:
        float: The ratio of white area to the whole area in percentage.
    """
    # フレームを読み込む
    ret, frame = cap.read()
    if not ret:
        return -1
    # グレースケール変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Otsuの方法で二値化
    _, img_th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # 全体の画素数
    whole_area = img_th.size
    # 白部分の画素数
    white_area = cv2.countNonZero(img_th)
    # 割合を計算
    white_ratio = white_area / whole_area * 100
    
    if view:
        # フレームと二値化画像を表示
        cv2.imshow('Webcam', frame)
        cv2.imshow('Binary', img_th)

    return white_ratio
