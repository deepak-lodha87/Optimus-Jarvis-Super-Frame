import time, secrets, random

class JarvisSentryCore:
    def __init__(self):
        self.sentry_id = f"NASe-{secrets.token_hex(2).upper()}"
        self.perimeter_status = "SECURED"

    def deploy_sentry(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-SENTRY V2 ACTIVE (ID: {self.sentry_id}) ---\033[0m")
        print("\033[1;36m[SENTRY] Activating perimeter scan via global nodes...\033[0m")
        time.sleep(2)
        
        # Simulating active monitoring
        objects_detected = random.randint(0, 5)
        print(f"\033[1;32m[SCAN] 360-Degree Sweep Complete. Objects Tracked: {objects_detected}\033[0m")
        
        if objects_detected > 0:
            print("\033[1;33m[ALERT] Unknown motion detected. Cross-referencing with Identity Core...\033[0m")
            time.sleep(1)
            print("\033[1;32m[VERIFIED] Authorized personnel only. Defense shields remaining passive.\033[0m")
        
        print(f"\033[1;35m[VOICE] Deepak, your physical and digital surroundings are now under my constant watch. Nothing passes the sentry line.\033[0m")

if __name__ == "__main__":
    sentry = JarvisSentryCore()
    sentry.deploy_sentry()
