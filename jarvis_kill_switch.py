import time
import sys

class RemoteKillSwitch:
    def __init__(self):
        self.system_lock = False

    def activate_kill_switch(self):
        print("\033[1;31m[CRITICAL] Initiating Emergency Remote Kill-Switch...\033[0m")
        time.sleep(1)
        # Bypassing machine's own shutdown delay
        self.system_lock = True
        return "\033[1;31m[LOCKED] All Machine Circuits Severed. System is now Dead-Locked.\033[0m"

class CommandOverride:
    def execute_force_command(self, command):
        print(f"\033[1;33m[OVERRIDE] Forcing External Machine to execute: {command}...\033[0m")
        time.sleep(1.2)
        # Advance Error-Resistant Logic
        return f"\033[1;32m[EXECUTED] Command '{command}' verified by Jarvis Core.\033[0m"

if __name__ == "__main__":
    ks = RemoteKillSwitch()
    cmd = CommandOverride()
    
    print("-" * 50)
    print("   JARVIS EMERGENCY CONTROL & KILL-SWITCH")
    print("-" * 50)
    
    # Testing Force Command
    print(cmd.execute_force_command("STOP ALL MOTORS"))
    
    # Simulating User Security Breach
    print("\n" + ks.activate_kill_switch())
    print("-" * 50)
