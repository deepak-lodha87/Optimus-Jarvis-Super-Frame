import os
import json

class SensorHub:
    def __init__(self):
        self.status = "Monitoring Sensors"

    def get_location_data(self):
        print("Accessing GPS data via Termux API...")
        # termux-location command extracts real-time coordinates
        os.system("termux-location > location.json")
        return "Location data captured successfully."

    def capture_vision_feed(self):
        print("Accessing Mobile Camera...")
        # Capturing a snapshot for visual analysis
        os.system("termux-camera-photo -c 0 vision_input.jpg")
        return "Visual feed secured."

if __name__ == "__main__":
    hub = SensorHub()
    print(hub.get_location_data())
    print(hub.capture_vision_feed())
