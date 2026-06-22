class Detector:
    def __init__(self):
        pass

    def detect(self, frame):
        """
        Will eventually run YOLO on `frame` and return a list of detections,
        e.g. [{"bbox": (x1, y1, x2, y2), "class": "person", "conf": 0.91}, ...]
        For now, returns an empty list so main.py runs end-to-end.
        """
        return []