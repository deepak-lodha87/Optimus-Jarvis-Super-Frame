import os

class AppCommander:
    def __init__(self):
        self.master = "Deepak"
        # ऐप्स के पैकेज नाम या शॉर्टकट
        self.apps = {
            "instagram": "com.instagram.android",
            "whatsapp": "com.whatsapp",
            "youtube": "com.google.android.youtube",
            "chrome": "com.android.chrome"
        }

    def launch_app(self, app_name):
        app_name = app_name.lower()
        if app_name in self.apps:
            print(f"\n\033[1;32m[LAUNCHING]:\033[0m Opening {app_name.capitalize()}...")
            os.system(f'termux-tts-speak "Opening {app_name}, Deepak sir."')
            # Android intent के जरिए ऐप खोलना
            os.system(f"am start --user 0 -n {self.apps[app_name]}/.MainActivity || am start --user 0 {self.apps[app_name]}")
        else:
            print(f"\033[1;31m[ERROR]:\033[0m App '{app_name}' not configured in Jarvis Core.")
            os.system(f'termux-tts-speak "Deepak sir, I do not have the protocol for {app_name} yet."')

if __name__ == "__main__":
    commander = AppCommander()
    # उदाहरण के लिए आप यहाँ इनपुट ले सकते हैं
    target = input("Which app should I open, Deepak sir? ").lower()
    commander.launch_app(target)
