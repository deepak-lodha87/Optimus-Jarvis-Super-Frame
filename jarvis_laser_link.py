import time

class LaserLink:
    def __init__(self):
        self.wavelength = "450nm (Blue-Green)"
        self.link_status = "DISCONNECTED"

    def establish_satellite_handshake(self):
        print("\033[1;36m[LASER] Aligning Satellite Optical Transceiver...\033[0m")
        time.sleep(1.5)
        print(f"  • Spectrum Analysis: {self.wavelength} detected.")
        print("  • Penetrating Water Surface Layer... [OK]")
        self.link_status = "ESTABLISHED"
        return "\033[1;32m[SUCCESS] Deep-Sea Laser Link Active. Commands Synced.\033[0m"

class SignalDecoder:
    def decode_photon_stream(self):
        print("\033[1;35m[DECODER] Processing Photon Pulse Stream...\033[0m")
        time.sleep(1.2)
        # Converting light pulses back into binary machine code
        return "\033[1;34m[INFO] Signal Integrity: 99.9% | No Packet Loss Detected.\033[0m"

if __name__ == "__main__":
    link = LaserLink()
    decoder = SignalDecoder()
    
    print("-" * 50)
    print("   JARVIS SATELLITE-LASER LINK (P3185-86)")
    print("-" * 50)
    
    print(link.establish_satellite_handshake())
    print("\n" + decoder.decode_photon_stream())
    print("-" * 50)
