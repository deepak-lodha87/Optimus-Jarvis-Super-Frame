import time

class FusionEye:
    def __init__(self):
        self.drone_camera = "Top-Down View"
        self.rover_camera = "Forward-Facing View"

    def process_fusion(self):
        print("\033[1;36m[VISION-SYNC]\033[0m Receiving visual streams...")
        time.sleep(1.0)
        
        print(f" \033[1;37m[AIR]\033[0m Capturing {self.drone_camera}")
        print(f" \033[1;37m[GROUND]\033[0m Capturing {self.rover_camera}")
        
        print("\n\033[1;33m[PROCESSING]\033[0m Stitching images into 3D Depth Map...")
        time.sleep(2.0)
        
        print(" \033[1;32m[SUCCESS]\033[0m 360-Degree Situational Awareness Active.")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have merged the sight \nof the Sky and the Earth. Nothing can hide \nfrom us now. I can see behind walls and \nover mountains. Our vision is absolute.\033[0m")

if __name__ == "__main__":
    eye = FusionEye()
    eye.process_fusion()
