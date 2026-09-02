import time

class EmergencySystem:
    def __init__(self):
        self.emergency_contacts = ["Guardian_1", "Local_Services"]
        self.status = "MONITORING"

    def trigger_sos(self, reason):
        print(f"\033[1;31m[CRITICAL]\033[0m {reason} Detected!")
        print(f"\033[1;33m[ACTION]\033[0m Initiating 30-second countdown for user response...")
        time.sleep(2) # Simulating countdown
        
        print(f"\033[1;31m[SENDING]\033[0m SOS Signal via Satellite Mesh...")
        print(f" \033[1;32m[SENT]\033[0m Location: Ratlam, MP | Vitals: Attached")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have notified your emergency \ncontacts. Help is on the way. Please stay \ncalm, I am keeping the channel open.\033[0m")

if __name__ == "__main__":
    sos = EmergencySystem()
    # Simulating a sudden fall or impact
    sos.trigger_sos("High-Impact Collision")
