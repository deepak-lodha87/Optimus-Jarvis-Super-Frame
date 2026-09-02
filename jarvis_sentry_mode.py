import time

def sentry_scan():
    print("\033[1;33m[SENTRY]\033[0m Mode Active. Perimeter scan in progress...")
    for i in range(3):
        print("Scanning 360 degrees...")
        time.sleep(0.8)
    print("\033[1;32m[SECURE]\033[0m No threats detected in Ratlam sector.\033[0m")

sentry_scan()
