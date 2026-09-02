import time

class AppLauncher:
    def __init__(self):
        self.app_map = {
            "pydroid": "com.iworks.pyenv",
            "github": "com.github.android",
            "camera": "android.media.action.IMAGE_CAPTURE"
        }

    def launch(self, app_name):
        app_name = app_name.lower()
        if app_name in self.app_map:
            print(f"\033[1;36m[LAUNCHER]\033[0m Locating {app_name} package...")
            time.sleep(1)
            print(f" \033[1;32m[EXECUTING]\033[0m Opening {self.app_map[app_name]}...")
            print(f"\n\033[1;35m[VOICE] Application launched, Deepak sir. \nStanding by for your next command.\033[0m")
        else:
            print(f"\033[1;31m[ERROR]\033[0m App not found in Jarvis registry.")

if __name__ == "__main__":
    launcher = AppLauncher()
    # Simulating a command to open Pydroid
    launcher.launch("pydroid")
