import time

class AssetArchive:
    def __init__(self):
        self.inventory = {
            "Brushless_Motor_A": {"Age": 850, "Limit": 1000, "Status": "Active"},
            "LiPo_Battery_01": {"Cycles": 45, "Limit": 50, "Status": "Critical"},
            "Phase_01_Core_Code": {"Version": "1.0", "Last_Update": "2026-01", "Status": "Legacy"}
        }

    def audit_assets(self):
        print("\033[1;36m[ARCHIVE]\033[0m Auditing all Project Assets...")
        time.sleep(1.5)
        
        for item, stats in self.inventory.items():
            status_color = "\033[1;32m" if stats["Status"] == "Active" else "\033[1;31m"
            print(f" \033[1;37m[ITEM]\033[0m {item:20} | Status: {status_color}{stats['Status']}\033[0m")
            
            if stats["Status"] == "Critical":
                print(f"    \033[1;33m[WARNING]\033[0m {item} is nearing end-of-life. Order replacement.")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am keeping a watch \non every nut, bolt, and line of code. \nNothing escapes the Archive. We won't be \ncaught off-guard by a failing part. \nOur foundation is solid and well-documented.\033[0m")

if __name__ == "__main__":
    archive = AssetArchive()
    archive.audit_assets()
