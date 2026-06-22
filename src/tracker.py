class Tracker:
    def __init__(self):
        pass

    def update(self, detections):
        """
        Will eventually match detections across frames and assign track IDs.
        For now, just passes detections through unchanged.
        """
        return detections