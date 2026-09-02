import os
import shutil

class FileArchitect:
    def __init__(self):
        self.target_dir = "/sdcard/Download" # आप इसे बदल सकते हैं
        self.extensions = {
            "Images": [".jpg", ".jpeg", ".png", ".gif"],
            "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
            "Videos": [".mp4", ".mkv"],
            "Code": [".py", ".sh", ".js"]
        }

    def organize(self):
        print(f"\n\033[1;34m[ARCHITECT MODE]\033[0m Scanning {self.target_dir}...")
        os.system('termux-tts-speak "Deepak sir, starting deep file organization."')
        
        count = 0
        for filename in os.listdir(self.target_dir):
            file_ext = os.path.splitext(filename)[1].lower()
            
            for folder, exts in self.extensions.items():
                if file_ext in exts:
                    dest_path = os.path.join(self.target_dir, folder)
                    if not os.path.exists(dest_path):
                        os.makedirs(dest_path)
                    
                    shutil.move(os.path.join(self.target_dir, filename), 
                                os.path.join(dest_path, filename))
                    count += 1
        
        print(f"\033[1;32m[SUCCESS]:\033[0m {count} files organized.")
        os.system(f'termux-tts-speak "Organization complete. {count} files sorted into categories."')

if __name__ == "__main__":
    architect = FileArchitect()
    architect.organize()
