import os
import platform

class KernelInterface:
    def __init__(self):
        self.master = "Deepak"

    def identify_environment(self):
        print(f"\n\033[1;33m[KERNEL INTERFACE ACTIVE]\033[0m Mapping system architecture...")
        
        # सिस्टम की जानकारी निकालना
        system_info = platform.uname()
        node_name = platform.node()
        
        print(f"\033[1;36m[OS]:\033[0m {system_info.system}")
        print(f"\033[1;36m[NODE]:\033[0m {node_name}")
        print(f"\033[1;36m[ARCH]:\033[0m {system_info.machine}")
        
        msg = f"Deepak sir, Kernel Interface is linked. Operating on {system_info.system} architecture. Systems are steady."
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    kernel = KernelInterface()
    kernel.identify_environment()
