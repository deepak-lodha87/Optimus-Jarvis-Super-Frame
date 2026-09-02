import time

class LanguageAdaptation:
    def __init__(self):
        self.user_name = "Deepak"
        self.vocabulary_bank = ["Ekdam perfect", "Shaandaar", "Zabardast"]
        self.learning_status = "Active"

    def adapt_response(self, user_input):
        print(f"\033[1;34m[LEARNING] Analyzing user style: '{user_input}'...\033[0m")
        time.sleep(1.2)
        
        # Simple logic to mirror user's style
        if "Baki ke start" in user_input or "Ha" in user_input:
            response_style = "Action-Oriented & Direct"
        else:
            response_style = "Conversational"
            
        print(f"\033[1;32m[ADAPTED] Switching to '{response_style}' mode for {self.user_name}.\033[0m")
        return f"Jarvis is now synchronized with your communication pattern."

if __name__ == "__main__":
    brain = LanguageAdaptation()
    print("-" * 50)
    print("   JARVIS NEURAL LANGUAGE ADAPTATION")
    print("-" * 50)
    
    # Testing how Jarvis adapts to your "Ha" response
    print(brain.adapt_response("Ha"))
