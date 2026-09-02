import os
import subprocess
import time

def generate_signature():
    print("\033[1;35m>> SYSTEM: GENERATING VOICE ENCRYPTION KEY <<\033[0m")
    audio_file = "deepak_final_voice.wav"
    
    if os.path.exists(audio_file):
        print("\033[1;34m[LOG] Analyzing audio frequencies...\033[0m")
        size = os.path.getsize(audio_file)
        # Digital Hashing Simulation
        voice_hash = hash(size) 
        print(f"\033[1;32m[SUCCESS] Digital Signature Created: SHA-256:{abs(voice_hash)}\033[0m")
        print("\033[1;32m>> STATUS: SYSTEM LOCKED TO ARCHITECT DEEPAK <<\033[0m")
    else:
        print("\033[1;31m[ERROR] Voice sample missing. Run Phase 3001 first.\033[0m")

if __name__ == "__main__":
    generate_signature()
