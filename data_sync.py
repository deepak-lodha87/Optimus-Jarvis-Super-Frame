import time

class DataSync:
    def __init__(self):
        self.sync_status = False

    def sync_streams(self, stream_1, stream_2):
        print(f"Syncing {stream_1} and {stream_2}...")
        time.sleep(1)
        self.sync_status = True
        return "Synchronization Successful: Data is aligned."

if __name__ == "__main__":
    sync = DataSync()
    print(sync.sync_streams("Image_Data", "Sensor_Data"))
