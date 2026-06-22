import cv2
from src.video_processor import VideoProcessor
from src.detector import Detector
from src.tracker import Tracker

WEBCAM_INDEX = 0

def main():
    print("Starting...")
    detector = Detector()
    tracker = Tracker()

    print("Opening video processor...")
    with VideoProcessor(WEBCAM_INDEX) as vp:
        print("Opened. Entering frame loop...")
        for frame in vp.frames():
            print("Got a frame")
            detections = detector.detect(frame)
            tracked = tracker.update(detections)

            for obj in tracked:
                x1, y1, x2, y2 = obj["bbox"]
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            cv2.imshow("YOLO Tracking", frame)
            print("Called imshow")

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()