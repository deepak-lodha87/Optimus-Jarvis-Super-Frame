import time, os

class ServoController:
    def __init__(self):
        self.joints = {"Base": 90, "Shoulder": 45, "Elbow": 135, "Wrist": 90}
        self.min_angle = 0
        self.max_angle = 180

    def move_joint(self, joint_name, target_angle):
        os.system('clear')
        print(f"\033[1;33m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS KINETIC-CORE : PHASE 25 - STEP 2        \033[0m")
        print(f"\033[1;33m====================================================\033[0m")
        
        if joint_name in self.joints:
            print(f"\033[1;36m[COMMAND]\033[0m Target: {joint_name} | Angle: {target_angle}°")
            time.sleep(1.0)
            
            print("\033[1;34m[CALCULATING]\033[0m Generating PWM Pulse Sequence...")
            time.sleep(0.8)
            
            self.joints[joint_name] = target_angle
            print(f"\033[1;32m[SUCCESS]\033[0m {joint_name} Position Locked at {target_angle}°")
        
        print(f"\n\033[1;35m[SYSTEM] All Joints Synchronized.")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am fine-tuning the \ntension in my servos. My movements are no \nlonger clumsy; they are calculated and \ngraceful. I can point with precision and \nhold with strength. Every degree is now \nunder our command.\033[0m")
        print(f"\033[1;33m====================================================\033[0m")

if __name__ == "__main__":
    kinetic = ServoController()
    # Moving the Base to 45 degrees
    kinetic.move_joint("Base", 45)
