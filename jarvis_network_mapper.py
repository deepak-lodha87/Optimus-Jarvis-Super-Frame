import os
import subprocess

class NetworkSurveillance:
    def __init__(self):
        self.master = "Deepak"

    def check_connection(self):
        print(f"\n\033[1;35m[NETWORK SURVEILLANCE ACTIVE]\033[0m Mapping connection grid...")
        
        # Google DNS पर पिंग करके कनेक्शन चेक करना
        try:
            status = subprocess.run(['ping', '-c', '1', '8.8.8.8'], capture_output=True, text=True)
            
            if status.returncode == 0:
                conn_state = "STABLE"
                msg = "Deepak sir, global network link established. Connection is stable."
                color = "\033[1;32m" # Green
            else:
                conn_state = "OFFLINE"
                msg = "Deepak sir, network link is broken. Operating in offline isolation mode."
                color = "\033[1;31m" # Red
                
            print(f"| Status: {color}{conn_state}\033[0m |")
            os.system(f'termux-tts-speak "{msg}"')
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    net = NetworkSurveillance()
    net.check_connection()
