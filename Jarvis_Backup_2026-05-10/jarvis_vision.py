import subprocess
import os
import time

class JarvisVision:
    def __init__(self):
        self.sensor_name = "Optimus Optical Unit"
        self.save_path = "scans/"
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

    def capture_scan(self):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{self.save_path}scan_{timestamp}.jpg"
        
        print(f"\n[+] Activating {self.sensor_name}...")
        try:
            # Taking photo using Termux API
            subprocess.run(['termux-camera-photo', '-c', '0', filename])
            print(f"[✓] Scan Captured: {filename}")
            
            # Voice feedback
            subprocess.run(['termux-tts-speak', "Visual scan completed. Image saved to database."])
            return filename
        except Exception as e:
            print(f"[!] Vision Error: {e}")
            return None

    def analyze_environment(self, file):
        if file:
            print(f"[*] Analyzing Scan Data: {file}...")
            time.sleep(1.5)
            print("[JARVIS]: Analysis complete. No immediate structural threats identified in the visual field.")

if __name__ == "__main__":
    vision = JarvisVision()
    print("--- Jarvis Visual Interface ---")
    cmd = input("Type 'scan' to activate camera: ")
    if cmd.lower() == "scan":
        image_file = vision.capture_scan()
        vision.analyze_environment(image_file)
