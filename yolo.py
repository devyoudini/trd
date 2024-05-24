from ultralytics import YOLO


class Model:
    def __init__(self, video_path):
        super().__init__(self)
        self.model = YOLO("yolov8n.pt")
