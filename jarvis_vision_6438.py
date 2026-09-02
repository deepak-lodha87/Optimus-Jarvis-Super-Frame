import time, secrets

class JarvisVision:
    def __init__(self):
        self.vision_id = f"NAV-{secrets.token_hex(2).upper()}"
        self.ar_mode = "ENABLED"

    def scan_object(self, obj_name):
        print(f"\n\033[1;37m--- NEURAL-AUTO-VISION V2 ONLINE (ID: {self.vision_id}) ---\033[0m")
        print(f"\033[1;36m[CAMERA] Initializing AR Overlay for: {obj_name}...\033[0m")
        time.sleep(1.5)
        
        # Simulating Object Identification and Data Retrieval
        print(f"\033[1;32m[IDENTIFIED] Target: {obj_name}\033[0m")
        print("\033[1;33m[AR-DATA] Specs: Genuine Part | Status: Optimal | Lifespan: 85%\033[0m")
        
        self.display_hud_info(obj_name)

    def display_hud_info(self, obj):
        print(f"\033[1;35m[VOICE] Deepak, I've mapped the {obj}. All parameters are within safety limits.\033[0m")

if __name__ == "__main__":
    vision = JarvisVision()
    # Simulating scanning a bike engine or a spare part
    vision.scan_object("Hero-HF-Deluxe-Engine-Core")
