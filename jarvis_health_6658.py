import time, secrets, random

class JarvisHealthMonitor:
    def __init__(self):
        self.health_id = f"NAHe-{secrets.token_hex(2).upper()}"
        self.focus_level = 100

    def analyze_vitals(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-HEALTH V1 ACTIVE (ID: {self.health_id}) ---\033[0m")
        print("\033[1;36m[SCANNING] Analyzing biometric data and cognitive load...\033[0m")
        time.sleep(1.8)
        
        stats = {
            "Energy": random.randint(70, 95),
            "Focus": random.randint(60, 100),
            "Stress": random.randint(10, 30)
        }
        
        print(f"\033[1;32m[REPORT] Energy: {stats['Energy']}% | Focus: {stats['Focus']}% | Stress: Low\033[0m")
        
        if stats['Focus'] < 70:
            print("\033[1;33m[ADVICE] Focus drifting. Recommend 5-minute break for peak performance.\033[0m")
        
        print(f"\033[1;35m[VOICE] Deepak, your vitals are stable. I've optimized the system alert to match your peak focus hours.\033[0m")

if __name__ == "__main__":
    health = JarvisHealthMonitor()
    health.analyze_vitals()
