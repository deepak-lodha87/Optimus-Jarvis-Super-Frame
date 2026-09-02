import threading
import time

class SubconsciousBrain:
    def __init__(self):
        self.user_habit = "Evening_Drone_Flight"
        self.prediction_ready = False

    def subconscious_loop(self):
        while True:
            current_hour = time.localtime().tm_hour
            # Predicting flight if it's evening (e.g., after 5 PM / 17:00)
            if current_hour >= 17:
                print("\033[1;34m[SUBCONSCIOUS]\033[0m Pattern matched: Evening routine.")
                print(" \033[1;33m[PREDICTIVE]\033[0m Pre-warming Drone Sensors & GPS...")
                time.sleep(2)
                self.prediction_ready = True
                print(" \033[1;32m[READY]\033[0m Readiness report stored in Cache.")
            time.sleep(10) # Checks patterns every 10 seconds

    def main_interaction(self):
        print("\033[1;36m[SYSTEM]\033[0m Active Interaction Thread started.")
        time.sleep(5)
        if self.prediction_ready:
            print(f"\n\033[1;35m[VOICE] Deepak... sir, I noticed it's evening. \nI've already calibrated the drone and \nchecked the wind for you. Are we taking \noff today?\033[0m")
        else:
            print("\033[1;35m[VOICE] Waiting for your command, sir.\033[0m")

if __name__ == "__main__":
    brain = SubconsciousBrain()
    
    # Running prediction in background
    t_sub = threading.Thread(target=brain.subconscious_loop, daemon=True)
    t_main = threading.Thread(target=brain.main_interaction)

    t_sub.start()
    t_main.start()
