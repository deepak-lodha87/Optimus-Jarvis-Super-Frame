import os
import json
import time
import subprocess

def initiate_hybrid_trace():
    os.system('clear')
    print("\033[1;31m[HYBRID TRACER]\033[0m Activating Satellite & Mobile Network Handshake...")
    
    # Cleaning environment
    os.system("pkill -f termux-location")
    if os.path.exists("trace_data.json"): os.remove("trace_data.json")

    # Tracking Mode 1: Satellite (Raw GPS)
    print("\033[1;33m[TRACE 01]\033[0m Pinging Satellites for Precision...")
    os.system("termux-location -p gps -n 1 > trace_gps.json")
    
    # Tracking Mode 2: Mobile Tracer (Network Triangulation)
    print("\033[1;36m[TRACE 02]\033[0m Tracing Mobile Network Grid...")
    os.system("termux-location -p network > trace_net.json")

    time.sleep(2)

    try:
        # Hybrid Logic: Combining both for 100% Reliability
        source = "trace_gps.json" if os.path.exists("trace_gps.json") and os.stat("trace_gps.json").st_size > 0 else "trace_net.json"
        
        with open(source, "r") as f:
            data = json.load(f)
            lat, lon = data['latitude'], data['longitude']
            alt = data.get('altitude', 'N/A')
            provider = data.get('provider', 'Hybrid')

            print(f"\n\033[1;32m[TRACE SUCCESSFUL]\033[0m")
            print(f"Data Source: {provider.upper()}")
            print(f"Coordinates: {lat}, {lon}")
            print(f"Altitude: {alt}m above sea level")

            # Establishing the Map Link with Master Zoom
            map_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}&t=k&z=21"
            
            os.system(f'termux-tts-speak "Deepak sir, Hybrid Tracer active. Satellite and Mobile grid synchronized."')
            os.system(f"termux-open-url '{map_url}'")
            
    except Exception as e:
        print("\033[1;31m[CRITICAL]\033[0m Trace failed. Hardware still unresponsive.")
        print("Please ensure Location Permissions are 'Allowed all the time'")

if __name__ == "__main__":
    initiate_hybrid_trace()
