import time
import subprocess

class OptimusSecurity:
    def __init__(self):
        self.protocol_name = "Optimus Aegis-Level Defense"
        self.alert_status = False

    def trigger_alarm(self, threat_type):
        print(f"\n[!!!] ALERT: {threat_type.upper()} DETECTED!")
        self.alert_status = True
        
        # Voice Alert (Using Phase 322 Logic)
        alert_msg = f"Deepak, an emergency situation has been identified. Threat type: {threat_type}."
        try:
            subprocess.run(['termux-tts-speak', alert_msg])
            # Optional: Beep sound if available
            print("[SYSTEM] Security Protocol: Evasive Action Recommended.")
        except:
            print("[!] Audio System Offline. Visual Alert Only.")

    def monitor_environment(self, input_data):
        # Checking for danger keywords
        danger_keywords = ["attack", "intruder", "fail", "breach", "warning"]
        for word in danger_keywords:
            if word in input_data.lower():
                self.trigger_alarm(word)
                return
        print("[SAFE] System monitoring: No immediate threats detected.")

if __name__ == "__main__":
    security = OptimusSecurity()
    print(f"--- {security.protocol_name} Active ---")
    status_input = input("Enter system log/status update: ")
    security.monitor_environment(status_input)
