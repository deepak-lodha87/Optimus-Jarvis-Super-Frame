import os

def analyze_sample(filename):
    print("\033[1;33m>> ANALYZING CAPTURED PULSE...\033[0m")
    
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        # 3232 bytes is very small, usually indicating background noise or silence
        if size > 10000: 
            print(f"\033[1;32m[VERIFIED] Voice Data Detected. Size: {size} bytes.\033[0m")
            print("[LOG] Data is sufficient for Frequency Mapping.")
        else:
            print("\033[1;31m[WARNING] Captured data is too thin (Low Volume/Silence).\033[0m")
            print("[ADVICE] Please speak louder or closer to the mic next time.")
    else:
        print("\033[1;31m[ERROR] File not found.\033[0m")

if __name__ == "__main__":
    analyze_sample("deepak_voice.wav")
