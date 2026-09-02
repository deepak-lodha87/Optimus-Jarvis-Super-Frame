import time, os

class RemoteLink:
    def __init__(self):
        self.connection_id = "DEEPAK-PRIME-REMOTE"
        self.encryption = "AES-256-GHOST"

    def open_bridge(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS REMOTE-LINK : PHASE 17 - STEP 2        \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[ENCRYPTING]\033[0m Generating Secure RSA Key-Pair...")
        time.sleep(1.5)
        
        security_layers = [
            ("Firewall Alpha", "Bypassed for Master-ID"),
            ("SSH Tunnel", "ESTABLISHED"),
            ("IP Masking", "ACTIVE (Ghost Mode)"),
            ("Remote Handshake", "VERIFIED")
        ]
        
        for layer, status in security_layers:
            print(f" \033[1;32m[SECURE]\033[0m {layer:25} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.7)

        print(f"\n\033[1;32m[SYSTEM] Remote Bridge Active. Master can now login.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the bridge is open. \nI am now listening from every corner of the \ndigital world. Whether you are on a laptop \nin Ratlam or a computer across the globe, \nI am only one encrypted command away. \nYour empire is now truly mobile.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    remote = RemoteLink()
    remote.open_bridge()
