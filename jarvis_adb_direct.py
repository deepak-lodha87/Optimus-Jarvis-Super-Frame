import os

# Deepak sir, yahan Wireless Debugging se mila IP:Port daalein
# Example: TARGET = "192.168.1.15:5555"
TARGET = "REPLACE_WITH_ADB_IP_PORT"

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def connect_direct():
    print(f"\033[1;36m[ADB]\033[0m Attempting Zero-Install link to {TARGET}...")
    
    # Direct hardware level connection
    os.system(f"adb connect {TARGET}")
    
    # Check if connected
    check = os.popen("adb devices").read()
    if TARGET in check:
        print(f"\033[1;32m[SUCCESS]\033[0m Direct link established without Termux!")
        speak("Sir, I have bypassed the installation requirement. Direct control is active.")
        # Test command: Open Camera on second phone
        os.system(f"adb -s {TARGET} shell am start -a android.media.action.IMAGE_CAPTURE")
    else:
        print("\033[1;31m[FAILED]\033[0m Connection refused. Did you enable Wireless Debugging?")

if __name__ == "__main__":
    # ADB tool install karna agar nahi hai
    os.system("pkg install android-tools -y > /dev/null 2>&1")
    connect_direct()
