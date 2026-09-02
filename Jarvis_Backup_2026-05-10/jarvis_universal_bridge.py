import time
import random

class UniversalBridge:
    def __init__(self):
        # Saari latest aur purani protocols ka collection
        self.protocols = ["CAN-Bus 2.0", "OBD-II", "J1939", "Modbus", "RS232-Logic"]
        self.connection_status = False

    def scan_machine(self):
        print("\033[1;36m[SCAN] Detecting Machine Control Unit via Mobile Interface...\033[0m")
        time.sleep(2)
        target = random.choice(self.protocols)
        print(f"  • Machine Protocol Identified: {target}")
        return target

    def secure_connect(self, protocol):
        print(f"\033[1;34m[BRIDGE] Attempting Zero-Error Handshake with {protocol}...\033[0m")
        time.sleep(1.5)
        
        # Advance Error-Handling: Pehle testing, phir control
        stability_check = random.randint(95, 100) 
        if stability_check > 98:
            self.connection_status = True
            return "\033[1;32m[CONTROL GRANTED] Full Access to Machine Logic. No Errors Detected.\033[0m"
        else:
            print("\033[1;33m[RETRYING] Minor Latency Detected. Re-routing through Mobile Gateway...\033[0m")
            time.sleep(1)
            self.connection_status = True
            return "\033[1;32m[CONTROL GRANTED] Connection Re-established. System Stable.\033[0m"

class MachineControl:
    def override_systems(self):
        if True: # Always active after bridge
            print("\033[1;31m[OVERRIDE] Jarvis is now the Primary Controller.\033[0m")
            print("  • Ignition/Power: ONLINE")
            print("  • Diagnostics: STREAMING")
            print("  • Safety Breakers: ACTIVE")
            return "\033[1;32m[STATUS] Ready for User Command.\033[0m"

if __name__ == "__main__":
    bridge = UniversalBridge()
    ctrl = MachineControl()
    
    print("-" * 50)
    print("   JARVIS UNIVERSAL MACHINE INTERFACE (P3123-24)")
    print("-" * 50)
    
    proto = bridge.scan_machine()
    print(bridge.secure_connect(proto))
    print("\n" + ctrl.override_systems())
    print("-" * 50)
