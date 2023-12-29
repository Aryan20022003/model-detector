from .celery import app
from ultralytics import YOLO, settings
import requests
import cv2


def imageRead():
    # write path relative to app folder
    # "/home/aryan/Project/videoServer/app/static/image/sample.jpg"
    path = "../static/image/sample.jpg"
    image = cv2.imread(path)
    return image


# classes: https://docs.ultralytics.com/datasets/detect/coco/#dataset-yaml
detectionClass = [
    0,
    1,
    2,
    3,
    5,
    6,
    7,
    9,
    10,
    11,
    12,
    24,
    25,
    26,
    28,
    29,
    32,
    33,
    34,
    36,
    38,
    39,
    40,
    42,
    46,
    47,
    49,
    53,
    56,
    59,
    60,
    69,
    70,
    76,
    77,
]


@app.task
def backgroundCat():
    try:
        url: str = "https://cataas.com/cat"
        response = requests.get(url=url)
        data = response.json()
        print("cat two")
        print(data)
        return
    except Exception as e:
        print(e)
        return


@app.task
def backgroundBitCoin():
    try:
        url: str = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url=url)
        data = response.json()
        print("bitcoin two")
        # sleep for 10 seconds
        # time.sleep(100)
        print(data)
        return
    except Exception as e:
        print(e)
        return


@app.task
def staticMediaDetection():
    try:
        model = YOLO("yolov8n.pt")
        print("static analysis")
        # api request to get image central db but from now using local image form internet
        # source = "https://shorturl.at/ekDFV"
        source = imageRead()  # image of bus
        result = model(
            source=source,
            classes=detectionClass,
            # stream=True,
            save=True,
            stream=False,
            show=True,
            project="project",
            name="imageDetect",
            exist_ok=True,
        )

        return
        # will read and send the image to central db

    except Exception as e:
        print(e)
        return


@app.task
def liveStreamDetection():
    try:
        model = YOLO("yolov8n.pt")
        # api request to get live stream from central db
        source = "https://www.youtube.com/watch?v=5qap5aO4i9A"
        result = model(
            source,
            classes=detectionClass,
            save=True,
            project="project",
            name="liveDetect",
            exist_ok=True,
        )
        # will read and send the image to central db

    except Exception as e:
        print(e)
        return
