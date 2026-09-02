import os
import socket
import psutil
import json

class OptimusJarvis:
    def __init__(self):
        self.user_name = "Deepak"
        self.project_name = "Optimus Jarvis Super-Frame"
        
        # Phase 2: Blueprints Database
        self.blueprints = {
            "Iron Man Suit": {"Model": "Mark 85", "Power": "Arc Reactor", "Material": "Nanotech"},
            "Iron Man Weapons": {"Primary": "Nano Repulsors", "Ultimate": "Lightning Refocuser"},
            "Spider-Man Suit": {"Model": "Iron Spider", "Features": "Web-Shooters, Waldo Arms"},
            "Fighter Jet": {"Model": "F-35", "Speed": "1,960 km/h"},
            "Truck": {"Model": "Tesla Semi", "Range": "800 km"},
            "Submarine": {"Model": "DeepFlight Dragon", "Depth": "120m"}
        }

    def speak(self, text):
        """Voice Output"""
        print(f"Jarvis: {text}")
        os.system(f"termux-tts-speak '{text}'")

    def self_diagnosis(self):
        """Phase 1 Check"""
        print("\n[SYSTEM SELF-DIAGNOSIS...]")
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=2)
            net = "ONLINE"
        except:
            net = "OFFLINE"
        
        battery = psutil.sensors_battery()
        batt = f"{battery.percent}%" if battery else "Desktop"
        print(f"Network: {net} | Power: {batt}")

    def wish_me(self):
        """Aapko Boss bulayega"""
        self.speak(f"System Online. Kya kar rahe ho Boss? Main aapki kaise madad kar sakta hoon?")

    def get_data(self, query):
        """Data Search"""
        query = query.title()
        if query in self.blueprints:
            info = str(self.blueprints[query])
            self.speak(f"Data found for {query}.")
            print(f"Details: {info}")
        else:
            self.speak(f"Sorry Boss, {query} is not in my database.")

    def listen_and_act(self):
        """Voice Commands"""
        print("\nListening...")
        try:
            cmd = os.popen("termux-speech-to-text").read().strip().lower()
            if not cmd:
                return True
            
            print(f"Boss: {cmd}")
            
            if "exit" in cmd or "stop" in cmd:
                self.speak("Shutting down. Goodbye Boss.")
                return False
            elif "kya kar rahe ho" in cmd:
                self.speak("Aapke orders ka intezar kar raha hoon, Boss!")
            else:
                self.get_data(cmd)
            return True
        except:
            return True

# --- EXECUTION ---
if __name__ == "__main__":
    jarvis = OptimusJarvis()
    jarvis.self_diagnosis()
    jarvis.wish_me()
    
    running = True
    while running:
        running = jarvis.listen_and_act()
    def perform_action(self, command):
        """Boss ke bolte hi action lene ke liye"""
        if "whatsapp" in command:
            self.speak("Opening WhatsApp for you, Boss.")
            os.system("termux-open-url https://wa.me/")
        elif "youtube" in command:
            self.speak("Launching YouTube.")
            os.system("termux-open-url https://www.youtube.com")
        elif "time" in command:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M")
            self.speak(f"Boss, the time is {now}")

# Ab listen_and_act function ke andar elif section mein ye line add kar dena jab fursat mile:
# self.perform_action(cmd)
    def execute_mobile_task(self, voice_input):
        """Awaaz sunkar mobile apps kholne ke liye"""
        cmd = voice_input.lower()
        
        if "open" in cmd:
            app = cmd.replace("open", "").strip()
            self.speak(f"Sure Boss, opening {app}")
            # Termux can open URLs and some deep links
            if "whatsapp" in app:
                os.system("termux-open-url https://wa.me/")
            elif "youtube" in app:
                os.system("termux-open-url https://www.youtube.com")
            elif "google" in app:
                os.system("termux-open-url https://www.google.com")
            else:
                # Common way to search for other apps
                os.system(f"termux-open-url https://www.google.com/search?q={app}")

        elif "kaun ho" in cmd or "who are you" in cmd:
            self.speak("Main Jarvis hoon, aapka personal AI assistant.")

        elif "kya kar rahe ho" in cmd:
            self.speak("Main aapke agle command ka intezar kar raha hoon, Boss.")
    def jarvis_power_update(self):
        """Battery Permission Error fix karne ke liye"""
        try:
            # Termux API se battery check karna (No Permission Error)
            battery_info = os.popen("termux-battery-status").read()
            if battery_info:
                data = json.loads(battery_info)
                print(f"Jarvis Power: {data['percentage']}%")
        except Exception as e:
            print("System Check: Local Mode Active")

    def open_mobile_app(self, app_name):
        """Awaaz sunkar mobile apps kholne ke liye"""
        self.speak(f"Opening {app_name}, Boss.")
        # Isse aapka phone browser ke zariye apps trigger karega
        os.system(f"termux-open-url https://www.google.com/search?q={app_name}")
    def auto_progress_display(self):
        """Screen par automatic coding aur progress dikhane ke liye"""
        import time
        import random
        
        stages = [
            "Scanning Mobile Directory...",
            "Loading Spider-Man Suit Blueprints...",
            "Checking Arc Reactor Stability...",
            "Syncing with Satellite...",
            "System Integrity: 98% Optimized"
        ]
        
        self.speak("Initiating automatic sequence, Boss.")
        for stage in stages:
            print(f"[PROGRESS]: {stage}")
            time.sleep(random.uniform(0.5, 1.5)) # Asli coding jaisa feel dene ke liye
        
        self.speak("All systems are operational. Ready for your command.")

# Is function ko execute karne ke liye while loop ke upar jarvis.auto_progress_display() likh dein.
    def background_monitor(self):
        """Jarvis khud se check karega aur update dega"""
        import time
        import random
        
        # Automatic phrases jo Jarvis beech mein bolega
        updates = [
            "Boss, internal systems are 100% stable.",
            "Scanning for new updates in the Super-Frame.",
            "I am monitoring the background processes, everything looks good.",
            "Boss, should I initiate a deep scan of the Spider-Man suit blueprints?"
        ]
        
        # Ek chota sa automatic progress bar
        print("\n[AUTO-SYNC ACTIVE]")
        for i in range(1, 6):
            time.sleep(0.5)
            print(f"Progress: [{'#'*i}{'-'*(5-i)}] {i*20}% Syncing...")
            
        self.speak(random.choice(updates))

    def live_listening_mode(self):
        """Hamesha sunne aur turant jawab dene ke liye"""
        self.speak("System is in Live Mode. Just speak, Boss.")
        while True:
    def verify_boss(self, voice_input):
        """Sirf Deepak ki awaaz pehchanne ke liye"""
        # Abhi ke liye hum 'Name' base authentication use karenge
        # Taki koi aur command na de sake
        boss_name = "deepak"
        
        if boss_name in voice_input.lower():
            self.speak("Voice Identity Confirmed. Welcome back, Boss.")
            return True
        else:
            self.speak("Unauthorized voice detected. System Locked.")
            return False

# Isse use karne ke liye listen_and_act mein ye shart (condition) lagani hogi.
            # Termux se seedha voice command lena
            cmd = os.popen("termux-speech-to-text").read().strip().lower()
            if cmd:
                print(f"Detected: {cmd}")
                if "kya kar rahe ho" in cmd:
                    self.speak("Aapke frame ko analyze kar raha hoon, Boss. Sab perfect hai.")
                elif "exit" in cmd:
                    self.speak("Going to sleep. Good luck, Boss.")
                    break
                else:
                    self.perform_action(cmd) # Purana function call karega
