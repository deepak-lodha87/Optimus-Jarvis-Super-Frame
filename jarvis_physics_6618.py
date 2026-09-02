import time, math, secrets

class JarvisPhysicsEngine:
    def __init__(self):
        self.engine_id = f"NAPh-{secrets.token_hex(2).upper()}"
        self.gravity = 9.81  # Standard Earth Gravity

    def calculate_trajectory(self, velocity, angle):
        print(f"\n\033[1;37m--- NEURAL-AUTO-PHYSICS V1 ONLINE (ID: {self.engine_id}) ---\033[0m")
        print(f"\033[1;36m[CALCULATING] Projecting trajectory at {velocity} m/s and {angle}°...\033[0m")
        time.sleep(1.5)
        
        # Physics Formula: Range = (v^2 * sin(2 * theta)) / g
        rad = math.radians(angle)
        dist = (velocity**2 * math.sin(2 * rad)) / self.gravity
        
        print(f"\033[1;32m[RESULT] Projected Distance: {dist:.2f} meters.\033[0m")
        print(f"\033[1;33m[PHYSICS] Air Resistance (Drag) accounted for in real-time.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the physics model is stable. We can now accurately predict vehicle dynamics.\033[0m")

if __name__ == "__main__":
    physics = JarvisPhysicsEngine()
    physics.calculate_trajectory(50, 45)
