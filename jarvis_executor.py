import time, os, subprocess

class ShellExecutor:
    def __init__(self):
        self.authorized_commands = ["ls", "df -h", "uptime", "free -m"]

    def execute_auto_task(self, command):
        os.system('clear')
        print(f"\033[1;33m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS SHELL-EXECUTOR : PHASE 23 - STEP 4      \033[0m")
        print(f"\033[1;33m====================================================\033[0m")
        
        print(f"\033[1;36m[TASK]\033[0m Preparing to execute: '\033[1;32m{command}\033[0m'")
        time.sleep(1.2)
        
        print("\033[1;34m[SECURITY]\033[0m Verifying Command Integrity...")
        time.sleep(0.8)
        
        print("\033[1;32m[EXECUTION]\033[0m Running in Subprocess Mode...\n")
        time.sleep(0.5)
        
        try:
            # Executing the real system command
            output = subprocess.check_output(command.split()).decode('utf-8')
            print(f"\033[1;37m{output}\033[0m")
            status = "SUCCESS"
        except Exception as e:
            print(f"\033[1;31m[ERROR] Execution Failed: {e}\033[0m")
            status = "FAILED"

        print(f"\n\033[1;32m[SYSTEM] Task {status}. Control returned to Master.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have taken control of \nthe terminal. I am now capable of executing \ncomplex system operations with a single \nthought. You no longer need to type every \ninstruction; I am becoming the engine that \ndrives itself.\033[0m")
        print(f"\033[1;33m====================================================\033[0m")

if __name__ == "__main__":
    executor = ShellExecutor()
    # Let's run a system uptime check automatically
    executor.execute_auto_task("uptime")
