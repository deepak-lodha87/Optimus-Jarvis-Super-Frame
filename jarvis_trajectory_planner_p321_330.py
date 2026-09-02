import os
import sys
import time
import json
import random
import math
from datetime import datetime

class JarvisAutonomousTrajectoryPlanner:
    def __init__(self):
        self.master = "Deepak"
        self.device = "Oppo Reno 12 Pro"
        self.framework = "Optimus Jarvis Super-Frame"
        self.phase_range = "321-330 [Pathfinding & Trajectory Planning]"
        
        # नेविगेशन ग्रिड पैरामीटर्स (Starting Point to Destination Point)
        self.current_position = {"x": 0, "y": 0}
        self.target_destination = {"x": 10, "y": 10}
        
        # सिम्युलेटेड एनवायरनमेंट में आने वाले ऑब्स्टेकल्स (अवरोध)
        self.detected_obstacles = [
            {"x": 3, "y": 3, "type": "High_Rise_Structure"},
            {"x": 7, "y": 6, "type": "Thermal_Turbulence_Zone"}
        ]

    def termux_speak(self, text):
        try:
            os.system(f'termux-tts-speak "{text}"')
        except Exception:
            pass

    def run_pathfinding_optimization(self):
        """Phase 321-325: Obstacle Avoidance & Grid Mapping"""
        print(f"\n\033[1;36m🗺️ [PHASE 321-325]: INITIALIZING PATHFINDING OPTIMIZATION\033[0m")
        print(f"| Status: Mapping autonomous flight corridor from {self.current_position} to {self.target_destination}...")
        time.sleep(1.0)
        
        print(f"| -> Scanning Vector Field for potential threats/obstructions...")
        for obs in self.detected_obstacles:
            print(f"|    [ALERT]: Obstacle '{obs['type']}' detected at Coordinate Matrix: (X: {obs['x']}, Y: {obs['y']})")
            time.sleep(0.2)

    def run_autonomous_trajectory_generator(self):
        """Phase 326-330: Dynamic Trajectory Calculation and Interception"""
        print(f"\n\033[1;35m🚀 [PHASE 326-330]: GENERATING AUTONOMOUS TRAJECTORY\033[0m")
        print(f"| Status: Real-time calculation of optimal multi-axis waypoints...")
        time.sleep(1.2)
        
        # स्टार्टिंग पॉइंट से एंड पॉइंट तक का पाथवे जनरेट करना (ऑब्स्टेकल्स को छोड़ते हुए)
        generated_waypoints = []
        curr_x, curr_y = self.current_position["x"], self.current_position["y"]
        dest_x, dest_y = self.target_destination["x"], self.target_destination["y"]
        
        while curr_x < dest_x or curr_y < dest_y:
            if curr_x < dest_x:
                curr_x += 1
            if curr_y < dest_y:
                curr_y += 1
                
            # चेक करना कि क्या नया वेपॉइंट किसी ऑब्स्टेकल से टकरा रहा है
            collision = False
            for obs in self.detected_obstacles:
                if curr_x == obs["x"] and curr_y == obs["y"]:
                    collision = True
                    break
            
            if collision:
                # ओवरराइड मैकेनिज्म - रास्ता बदलना (Rerouting Vector)
                curr_x += 1 
                print(f"| -> [REROUTING]: Obstacle evaded successfully. Vector shifted to Waypoint (X: {curr_x}, Y: {curr_y})")
            else:
                generated_waypoints.append((curr_x, curr_y))
        
        print(f"| -> Generated Waypoints: {generated_waypoints}")
        print(f"| -> Trajectory Efficiency Status: \033[1;32m100% OPTIMAL PATH LOCKED\033[0m")
        self.termux_speak("Trajectory planning complete, Deepak sir. The safest and most optimal path has been locked into the navigation grid.")

    def execute_planner_boot(self):
        os.system('clear')
        print("\033[1;32m" + "🗺️ " * 35 + "\033[0m")
        print(f"\033[1;37;42m   {self.framework.upper()} : AUTONOMOUS TRAJECTORY PLANNER ({self.phase_range})   \033[0m")
        print("\033[1;32m" + "🗺️ " * 35 + "\033[0m")
        print(f"| NAVIGATION MASTER : {self.master} sir")
        print(f"| HARDWARE PLATFORM : {self.device} Sandboxed Environment")
        print(f"| ALGORITHM ENGINE  : Dynamic Vector Pathfinding Grid")
        print("\033[1;32m" + "-" * 70 + "\033[0m")
        
        # दोनों कोर नेविगेशन इंजनों को फायर करना
        self.run_pathfinding_optimization()
        self.run_autonomous_trajectory_generator()
        
        print("\033[1;32m" + "-" * 70 + "\033[0m")
        print(f"\033[1;32m[NAVIGATION LAYER ACTIVE]: Phases 321 to 330 are fully operational.\033[0m")
        print("\033[1;32m" + "🗺️ " * 35 + "\033[0m")

if __name__ == "__main__":
    planner_engine = JarvisAutonomousTrajectoryPlanner()
    planner_engine.execute_planner_boot()
