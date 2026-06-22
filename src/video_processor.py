import cv2


class VideoProcessor:
    """Handles reading frames from a webcam (or video file later)."""

    def __init__(self, source=0):
        """
        source: int = webcam index (0 is usually the default/built-in camera).
        """
        self.source = source
        self.cap = None

    def open(self):
        self.cap = cv2.VideoCapture(self.source)
        if not self.cap.isOpened():
            raise IOError(f"Cannot open webcam (source={self.source})")
        return self

    def get_fps(self):
        return self.cap.get(cv2.CAP_PROP_FPS)

    def frames(self):
        """Generator that yields frames one at a time until stopped."""
        if self.cap is None:
            self.open()

        while True:
            ret, frame = self.cap.read()
            if not ret:
                # Webcam dropped a frame/disconnected — stop the loop
                break
            yield frame

    def release(self):
        if self.cap is not None:
            self.cap.release()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()