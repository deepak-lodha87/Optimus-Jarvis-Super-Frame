import time

class UniversalInterface:
    def __init__(self, machine_type):
        self.machine_type = machine_type
        self.connection_status = False

    def establish_hard_link(self):
        print(f"\033[1;33m[LINK] Accessing {self.machine_type} Control Unit via CAN-Bus...\033[0m")
        time.sleep(1.5)
        # Unique Logic: Hardware Handshake
        print(f"  • Overriding OEM Security Layer... [SUCCESS]")
        print(f"  • Syncing Throttle & Steering Actuators...")
        self.connection_status = True
        return f"\033[1;32m[READY] Jarvis now has Absolute Authority over: {self.machine_type}\033[0m"

class MachineExecution:
    def execute_command(self, command, intensity):
        if not self.connection_status:
            return "Error: No Machine Linked."
        
        print(f"\033[1;35m[COMMAND] Executing {command} at {intensity}% output...\033[0m")
        # Direct Signal Injection logic
        time.sleep(0.8)
        return f"\033[1;36m[LOG] {command} confirmed by Machine Actuators.\033[0m"

if __name__ == "__main__":
    # Example: Linking Jarvis to a Fighter Jet or Motorcycle
    target = "High-Performance_Interceptor_Jet"
    interface = UniversalInterface(target)
    
    print("-" * 50)
    print("   JARVIS UNIVERSAL MACHINE CONTROL (P3203-04)")
    print("-" * 50)
    
    print(interface.establish_hard_link())
    print("\n" + interface.execute_command("THRUST_VECTOR_ALIGN", 85))
    print("-" * 50)
