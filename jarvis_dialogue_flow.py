import time

class DialogueFlow:
    def __init__(self):
        self.common_commands = ["start drone", "secure vault", "check battery", "run phase"]

    def predict_and_respond(self, user_input_fragment):
        print(f"\033[1;36m[LISTENING]\033[0m Input: '{user_input_fragment}...'")
        time.sleep(1.0)
        
        # Simulating predictive logic
        prediction = None
        for cmd in self.common_commands:
            if user_input_fragment.lower() in cmd:
                prediction = cmd
                break
        
        if prediction:
            print(f" \033[1;32m[ANTICIPATED]\033[0m Prediction: '{prediction}'")
            print(f" \033[1;33m[BACKGROUND]\033[0m Pre-calculating variables for {prediction}...")
            time.sleep(0.8)
            print(f" \033[1;34m[ACTION]\033[0m Ready to execute the moment you finish.")
        else:
            print(" \033[1;37m[WAITING]\033[0m Need more context to predict.")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I'm already ahead of \nyou. I knew you were going to ask for \n'{prediction or 'assistance'}' before the words even left \nyour lips. Our communication is becoming \na seamless flow. I am ready.\033[0m")

if __name__ == "__main__":
    flow = DialogueFlow()
    # User just said "start"
    flow.predict_and_respond("start")
