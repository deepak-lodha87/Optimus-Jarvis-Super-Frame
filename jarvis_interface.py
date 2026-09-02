import time
import sys

class CommandCenter:
    def __init__(self):
        self.admin = "Deepak"
        self.is_active = True

    def display_status(self):
        print("\n\033[1;34m[COMMAND CENTER]\033[0m Initializing Interface...")
        time.sleep(1)
        print(f"--- Welcome, Sir. Admin: {self.admin} ---")
        print("1. System Health Check (Phase 45)")
        print("2. Security Status (Phase 46)")
        print("3. Predictive Analytics (Phase 47)")
        print("4. Exit System")

    def execute_command(self, choice):
        if choice == '1':
            print("\033[1;32m[HEALTH]\033[0m All modules are stable. No repairs needed.")
        elif choice == '2':
            print("\033[1;31m[SECURITY]\033[0m Ghost Protocol is active. No threats detected.")
        elif choice == '3':
            print("\033[1;36m[ORACLE]\033[0m Predicted outcome for today: 98% Success.")
        elif choice == '4':
            print("\033[1;35m[VOICE] Shutting down, Deepak sir. Sleep well.\033[0m")
            self.is_active = False
        else:
            print("Invalid command, sir.")

if __name__ == "__main__":
    center = CommandCenter()
    while center.is_active:
        center.display_status()
        # Simulating a user choice for the final phase
        user_choice = '3' 
        print(f"\nUser Input: {user_choice}")
        center.execute_command(user_choice)
        time.sleep(2)
        break # Breaking loop for demonstration
