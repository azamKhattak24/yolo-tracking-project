from ultralytics import YOLO

class Detector:
    """Loads YOLOv8 and runs inference on frames."""

    def __init__(self, model_path="yolov8n.pt", conf_threshold=0.3):
        """
        model_path:     YOLOv8 weights to load (downloads automatically if not found).
        conf_threshold: Minimum confidence to keep a detection.
        """
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold

    def detect(self, frame):
        """
        Runs inference on a single BGR frame.
        Returns a list of dicts with bbox and class info.
        """
        results = self.model(frame, conf=self.conf_threshold, verbose=False)[0]

        detections = []
        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            detections.append({
                "bbox": (x1, y1, x2, y2),
                "confidence": float(box.conf[0]),
                "class_id": int(box.cls[0]),
                "class_name": self.model.names[int(box.cls[0])]
            })

        if detections:
            print(f"[Detector] {len(detections)} object(s) detected: " +
                  ", ".join(f"{d['class_name']} ({d['confidence']:.0%})" for d in detections))
        else:
            print("[Detector] No objects detected")

        return detections