import os

class ErrorHandler:
    def __init__(self):
        self.master = "Deepak"

    def execute_safe(self, function_name, action):
        print(f"\n\033[1;33m[SHIELD ACTIVE]:\033[0m Executing {function_name} in Safe-Mode...")
        try:
            # यहाँ जार्विस उस काम को करने की कोशिश करेगा
            action()
            print(f"\033[1;32m[SUCCESS]:\033[0m {function_name} executed without issues.")
        except Exception as e:
            # अगर एरर आता है, तो जार्विस उसे रिकॉर्ड करेगा और आपको बताएगा
            error_msg = f"Deepak sir, I encountered a minor glitch in {function_name}. Bypassing error to maintain system stability."
            print(f"\033[1;31m[BYPASS]:\033[0m {e}")
            os.system(f'termux-tts-speak "{error_msg}"')

if __name__ == "__main__":
    shield = ErrorHandler()
    
    # एक टेस्ट फंक्शन जिसमें जानबूझकर गलती है (1/0)
    def test_glitch():
        return 1 / 0
        
    shield.execute_safe("Test Module", test_glitch)
