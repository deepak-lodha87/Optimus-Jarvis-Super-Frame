import time
import random

class PurityScanner:
    def __init__(self):
        self.location = "Ratlam, MP"
        self.status = "MONITORING"

    def scan_air_quality(self):
        print(f"\033[1;36m[SENSOR]\033[0m Activating Chemical & Dust Sensors...")
        time.sleep(1.5)
        
        # Simulating live AQI data
        aqi_value = random.randint(40, 160)
        
        print(f" \033[1;32m[RESULT]\033[0m Current AQI in {self.location}: {aqi_value}")
        
        if aqi_value <= 50:
            quality = "Excellent (Green)"
            advice = "The air is pure. Great time for a walk, Deepak sir."
        elif aqi_value <= 100:
            quality = "Satisfactory (Yellow)"
            advice = "Air quality is okay, but keep the windows closed."
        else:
            quality = "Unhealthy (Orange/Red)"
            advice = "High pollution detected. Avoid prolonged outdoor activity."

        print(f" \033[1;34m[STATUS]\033[0m Category: {quality}")
        print(f"\n\033[1;35m[VOICE] {advice}\033[0m")

if __name__ == "__main__":
    scanner = PurityScanner()
    scanner.scan_air_quality()
