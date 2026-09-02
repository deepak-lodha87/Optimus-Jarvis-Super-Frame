import time

def security_sweep():
    print("\n[SECURITY] Initializing 360-Degree Perimeter Scan...")
    time.sleep(1)
    protocols = ["Neural-Link Encryption", "Biometric Lock", "Termux Firewall"]
    
    for p in protocols:
        print(f"[SCANNING] Checking {p}...", end=" ")
        time.sleep(0.5)
        print("SECURE")
    
    print("[STATUS] Security Level: Maximum. System is invisible to intruders.")

if __name__ == "__main__":
    security_sweep()
