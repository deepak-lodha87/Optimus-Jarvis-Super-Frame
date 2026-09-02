import time
import os
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def render_bar(label, value, max_val, color_code):
    bar_length = 20
    filled_length = int(bar_length * value // max_val)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f"{label:<15} |{color_code}{bar}\033[0m| {value}%")

def data_visualizer_hud():
    os.system('clear')
    print("\033[1;35m" + "📊"*30)
    print("      OPTIMUS NEURAL SYSTEMS : DATA VISUALIZER (P362)")
    print("📊"*30 + "\033[0m")
    
    optimus_speak("Generating real-time visual telemetry. Rendering system analytics.")
    
    # Simulated Real-time Data
    metrics = [
        {"label": "CPU LOAD", "val": 42, "max": 100, "color": "\033[1;32m"},
        {"label": "RAM USAGE", "val": 68, "max": 100, "color": "\033[1;33m"},
        {"label": "UAV SIGNAL", "val": 94, "max": 100, "color": "\033[1;34m"},
        {"label": "BATTERY", "val": 86, "max": 100, "color": "\033[1;32m"},
        {"label": "THERMAL", "val": 38, "max": 100, "color": "\033[1;36m"}
    ]
    
    print("\n\033[1;37m[LIVE TELEMETRY STREAM]:\033[0m")
    print("-" * 45)
    for m in metrics:
        render_bar(m["label"], m["val"], m["max"], m["color"])
        time.sleep(0.3)
    print("-" * 45)
    
    optimus_speak("Visual data stream is stable. No anomalies detected in current cycle.")

if __name__ == "__main__":
    data_visualizer_hud()
