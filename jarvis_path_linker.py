import os

class PathLinker:
    def __init__(self):
        self.master = "Deepak"
        # Android storage paths in Termux
        self.nav_points = {
            "Home": os.path.expanduser("~"),
            "Internal": "/sdcard",
            "Downloads": "/sdcard/Download",
            "Camera": "/sdcard/DCIM/Camera"
        }

    def map_directory(self):
        print(f"\n\033[1;33m[PATH LINKER ACTIVE]\033[0m Mapping navigation points...")
        os.system('termux-tts-speak "Deepak sir, establishing navigation links to the internal storage grid."')
        
        for name, path in self.nav_points.items():
            exists = os.path.exists(path)
            status = "\033[1;32m[LINKED]\033[0m" if exists else "\033[1;31m[OFFLINE]\033[0m"
            print(f"| {name.ljust(10)} : {status} Path: {path}")
            
        print("\033[1;36m[STATUS]:\033[0m Navigation map is now cached.")

if __name__ == "__main__":
    linker = PathLinker()
    linker.map_directory()
