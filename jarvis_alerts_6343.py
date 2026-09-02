import time, secrets

class JarvisAlertSystem:
    def __init__(self):
        self.alert_id = f"ALT-{secrets.token_hex(2).upper()}"
        self.notification_log = []

    def send_notification(self, level, message):
        timestamp = time.strftime('%H:%M:%S')
        colors = {"CRITICAL": "\033[1;31m", "INFO": "\033[1;32m", "WARNING": "\033[1;33m"}
        color = colors.get(level, "\033[1;37m")
        
        print(f"\n{color}[{level}] {message}\033[0m")
        print(f"Time: {timestamp} | Dispatch ID: {self.alert_id}")
        
        # Simulating a system push to the mobile UI
        time.sleep(0.5)
        print("\033[1;35m[PUSH] Notification sent to Oppo Reno 12 Pro status bar.\033[0m")

    def monitor_vitals(self):
        # Example: Monitoring a simulated trade or system temp
        print("\n\033[1;37m--- MONITORING ACTIVE SECTORS ---\033[0m")
        time.sleep(1)
        self.send_notification("INFO", "GitHub Sync Successful. Data is secure.")
        time.sleep(1)
        self.send_notification("CRITICAL", "Unauthorized access attempt blocked by Ghost-Mode!")

if __name__ == "__main__":
    nas = JarvisAlertSystem()
    nas.monitor_vitals()
