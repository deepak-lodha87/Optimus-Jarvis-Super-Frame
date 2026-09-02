import time

class UniversalMachineController:
    def __init__(self, machine_name):
        self.machine = machine_name
        self.steering_angle = 0 # Degrees
        self.sensor_pitch = 0
        self.swivel_angle = 0

    def track_steering_input(self, angle):
        self.steering_angle = angle
        print(f"\033[1;34m[UMC-OPTICS] Steering Input Detected: {angle}°\033[0m")
        # Direct link between steering and optics
        self.swivel_angle = angle * 0.85 
        return self.swivel_angle

    def execute_swivel_control(self):
        angle_to_move = self.swivel_angle
        print(f"\033[1;33m[ACTION] Activating Servo Motors for Headlights & LiDAR...\033[0m")
        time.sleep(0.8)
        
        if abs(angle_to_move) > 5:
            print(f"\033[1;35m[FOCUS] Swiveling Optical Pods to {angle_to_move:.1f}° for Cornering...\033[0m")
            return f"\033[1;32m[SUCCESS] Blind Spot Illuminated. Predictive Path Visible.\033[0m"
        return "\033[1;34m[STATUS] Centered Vision Active.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController("Optimus_Aero_Unit")
    
    print("-" * 50)
    print("   JARVIS UMC: ADAPTIVE OPTICS & SENSORS (P3216-17)")
    print("-" * 50)
    
    # Simulating a sharp right turn
    umc.track_steering_input(30)
    print(umc.execute_swivel_control())
    print("-" * 50)
