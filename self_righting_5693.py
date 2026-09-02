import time, secrets, gc, math
from types import SimpleNamespace

class GyroSelfRighting:
    def __init__(self):
        self.gsl_id = f"GSL-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5689, "Inertial-Sync", "CALIBRATING 6-AXIS IMU SENSORS..."),
            (5690, "Angular-Correction", "COUNTERING UNWANTED ROTATION VECTORS..."),
            (5691, "CoG-Adjustment", "SHIFTING INTERNAL MASS FOR STABILITY..."),
            (5692, "Auto-Recovery", "PREPARING STABILIZING THRUST BURSTS..."),
            (5693, "Logic v351", "GSL-CORE: SELF-RIGHTING SYSTEM ACTIVE.")
        ]

    def calculate_tilt_angle(self, x, y):
        # Unique logic: Using hypotenuse to find the tilt magnitude
        return round(math.degrees(math.atan2(y, x)), 2)

    def activate_stabilizer(self):
        print(f"\033[1;37m--- GYROSCOPIC-SELF-RIGHTING-LOGIC ONLINE (ID: {self.gsl_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        # Simulating tilt sensor data
        telemetry = SimpleNamespace(x_axis=45.5, y_axis=12.2)
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            current_tilt = self.calculate_tilt_angle(telemetry.x_axis, telemetry.y_axis)
            print(f"\033[1;{colors[i]}m[TILT:{current_tilt}° | STABLE:NO] Phase {p_id}: {title} >> {status}\033[0m")
            # Simulating recovery
            telemetry.x_axis *= 0.5
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mGSL STATUS: SYSTEM RECOVERY COMPLETE. UPRIGHT POSITION SECURED.\033[0m")

if __name__ == "__main__":
    gsl = GyroSelfRighting()
    gsl.activate_stabilizer()
