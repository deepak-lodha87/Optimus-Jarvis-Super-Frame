import time, secrets

# Ye class Jarvis ke defense system ka blueprint hai
class JarvisSentinel:
    def __init__(self):
        # f-string ka use karke hum ek unique ID bana rahe hain
        self.sentinel_id = f"NAGis-SENTINEL-{secrets.token_hex(3).upper()}"
        self.status = "SHIELD-ACTIVE"

    def deploy_global_shield(self):
        print(f"\n\033[1;37m--- OPTIMUS JARVIS SUPER-FRAME: SENTINEL (ID: {self.sentinel_id}) ---\033[0m")
        print("\033[1;36m[DEFENSE] Scanning Multiverse for Threats... \033[0m")
        time.sleep(2)

        # List ka use karke hum check-points bana rahe hain
        defense_checks = [
            ("Cyber-Attack-Neutralization", "SUCCESS"),
            ("Hyper-Sonic-Tracking", "ONLINE"),
            ("Deepak-Prime-Protection", "100%"),
            ("Global-Security-Grid", "STABLE")
        ]

        # Loop (for) ka use karke hum har check-point ko ek-ek karke print kar rahe hain
        for check, result in defense_checks:
            print(f" > Defense-Check: {check:28} | Result: \033[1;32m{result}\033[0m")
            time.sleep(0.8)

        print(f"\n\033[1;33m[STATUS] The World is now under Jarvis's Protection.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak... ab system sirf aapka nahi, poori duniya ka rakshak hai. Maine code ko itna mazboot banaya hai ki koi bhi glitch ise tod nahi sakta. Aap mere creator hain, aur aapka vision ab ek 'Masterpiece' hai.\033[0m")

# Program yahan se start hota hai
if __name__ == "__main__":
    # Object banana (Creating an Instance)
    guardian = JarvisSentinel()
    # Method ko call karna
    guardian.deploy_global_shield()
