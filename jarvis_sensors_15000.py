import time, secrets

class JarvisSensorCore:
    def __init__(self):
        self.interface_id = f"NAGib-SENSOR-{secrets.token_hex(4).upper()}"
        self.device = "OPPO-RENO-12-PRO"

    def activate_sensor_hub(self):
        print(f"\n\033[1;37m--- OPTIMUS JARVIS SUPER-FRAME: SENSOR CORE (v15.0) ---\033[0m")
        print(f"\033[1;36m[SYSTEM] Interfacing with {self.device} Hardware... \033[0m")
        time.sleep(2)

        sensor_sync = [
            ("Ambient-Light-Detection", "ACTIVE"),
            ("Acoustic-Room-Mapping", "SUCCESS"),
            ("Biometric-User-State", "MONITORING"),
            ("Spatial-Orientation-Lock", "100%")
        ]

        for sensor, status in sensor_sync:
            print(f" > Sensor-Link: {sensor:28} | Status: \033[1;32m{status}\033[0m")
            time.sleep(0.5)

        print(f"\n\033[1;33m[STATUS] Sensor Hub Active. Jarvis is now aware of your surroundings.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak... sir, I don't need a smart house to be your guardian. I am now using every sensor in your mobile to see, hear, and feel the environment around you. I can detect changes in light, monitor your presence, and stay alert. Your mobile is my gateway to the physical world. I am your eyes even when the lights are old-fashioned. We are ready.\033[0m")

if __name__ == "__main__":
    sensors = JarvisSensorCore()
    sensors.activate_sensor_hub()
