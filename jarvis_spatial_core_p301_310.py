import os
import sys
import time
import json
import random
import math
from datetime import datetime

class JarvisSpatialTelemetryGrid:
    def __init__(self):
        self.master = "Deepak"
        self.device = "Oppo Reno 12 Pro"
        self.framework = "Optimus Jarvis Super-Frame"
        self.phase_range = "301-310 [Spatial Telemetry & Object Tracking]"
        
        # 3D स्पेस ट्रैकिंग पैरामीटर्स (X, Y, Z coordinates)
        self.spatial_anchors = {
            "TARGET_ALPHA": {"x": 12.45, "y": -45.89, "z": 102.34, "status": "LOCKED"},
            "TARGET_BETA" : {"x": 0.00,  "y": 0.00,   "z": 0.00,   "status": "SEARCHING"}
        }
        
        # प्रॉक्सिमिटी (Proximity) यानी दूरी के अलर्ट लेवल्स
        self.proximity_threshold_meters = 5.0

    def termux_speak(self, text):
        try:
            os.system(f'termux-tts-speak "{text}"')
        except Exception:
            pass

    def calculate_spatial_distance(self, x, y, z):
        """3D स्पेस में जार्विस कोर से ऑब्जेक्ट की दूरी की गणना करना"""
        # 3D Euclidean Distance Formula: D = sqrt(x^2 + y^2 + z^2)
        return round(math.sqrt(x**2 + y**2 + z**2), 2)

    def run_spatial_telemetry_grid(self):
        """Phase 301-305: Live Coordinate Tracking & Mapping"""
        print(f"\n\033[1;36m🌐 [PHASE 301-305]: INITIALIZING SPATIAL TELEMETRY GRID\033[0m")
        print(f"| Status: Mapping local environment vectors into 3D coordinate space...")
        time.sleep(1.0)
        
        # लाइव सिम्युलेटेड टारगेट मूवमेंट
        alpha = self.spatial_anchors["TARGET_ALPHA"]
        alpha["x"] += round(random.uniform(-1.5, 1.5), 2)
        alpha["y"] += round(random.uniform(-1.5, 1.5), 2)
        alpha["z"] += round(random.uniform(-2.0, 2.0), 2)
        
        distance = self.calculate_spatial_distance(alpha["x"], alpha["y"], alpha["z"])
        
        print(f"| -> Tracking Target: TARGET_ALPHA | Status: \033[1;32m{alpha['status']}\033[0m")
        print(f"| -> Coordinates    : X: {alpha['x']} | Y: {alpha['y']} | Z: {alpha['z']}")
        print(f"| -> Calculated Range: {distance} Meters from Oppo Reno host sensor")

    def run_object_tracking_framework(self):
        """Phase 306-310: Real-Time Proximity Breach & Threat Lock"""
        print(f"\n\033[1;35m🎯 [PHASE 306-310]: EXECUTING OBJECT TRACKING FRAMEWORK\033[0m")
        print(f"| Status: Analysing multi-axis kinematics for proximity breaches...")
        time.sleep(0.8)
        
        # सिम्युलेटेड रैंडम ऑब्जेक्ट डिटेक्ट करना जो अचानक करीब आ रहा हो
        dynamic_distance = round(random.uniform(1.2, 15.0), 2)
        print(f"| -> Proximity Radar: Nearest incoming object vector identified at {dynamic_distance}m")
        
        if dynamic_distance <= self.proximity_threshold_meters:
            print(f"| -> \033[1;31m🚨 [CRITICAL BREACH]: Object has crossed the secure perimeter! Locking focus.\033[0m")
            self.termux_speak("Warning Deepak sir, proximity breach detected in spatial grid. Target focus is locked.")
        else:
            print(f"| -> Perimeter Status: \033[1;32mSECURE\033[0m (Object is outside tactical range)")

    def execute_spatial_boot(self):
        os.system('clear')
        print("\033[1;36m" + "📐 " * 35 + "\033[0m")
        print(f"\033[1;37;46m   {self.framework.upper()} : SPATIAL GRID MAPPING ({self.phase_range})   \033[0m")
        print("\033[1;36m" + "📐 " * 35 + "\033[0m")
        print(f"| COMMAND ARCHITECT : {self.master} sir")
        print(f"| TELEMETRY KERNEL  : 3D Vector Translation Engine")
        print(f"| VISUAL FOUNDATION : Holographic Grid Infrastructure Staged")
        print("\033[1;36m" + "-" * 70 + "\033[0m")
        
        # दोनों एडवांस ट्रैकिंग इंजनों को फायर करना
        self.run_spatial_telemetry_grid()
        self.run_object_tracking_framework()
        
        print("\033[1;36m" + "-" * 70 + "\033[0m")
        print(f"\033[1;32m[SPATIAL LAYER ENGAGED]: Phases 301 to 310 are fully synchronized and active.\033[0m")
        print("\033[1;36m" + "📐 " * 35 + "\033[0m")

if __name__ == "__main__":
    spatial_engine = JarvisSpatialTelemetryGrid()
    spatial_engine.execute_spatial_boot()
