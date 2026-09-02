import os
import time

class TerminalMultiplexer:
    def __init__(self):
        self.master = "Deepak"

    def create_split_session(self):
        print(f"\n\033[1;36m[OPTIMIZING WORKSPACE]\033[0m Splitting Termux Core for {self.master}...")
        time.sleep(1)
        
        # असली Tmux कमांड्स जो स्क्रीन को दो हिस्सों में बांट देंगे
        # एक हिस्सा कोडिंग के लिए, दूसरा हिस्सा गिटहब और एरर मॉनिटरिंग के लिए
        os.system("tmux new-session -d -s JarvisWorkspace")
        os.system("tmux split-window -h")
        os.system("tmux send-keys -t JarvisWorkspace:0.0 'ls -la' C-m")
        os.system("tmux send-keys -t JarvisWorkspace:0.1 'python jarvis_integrity_check.py' C-m")
        
        msg = "Deepak sir, I have split your workspace. You can now monitor code and GitHub errors simultaneously."
        os.system(f'termux-tts-speak "{msg}"')
        
        print("\033[1;32m[SUCCESS]\033[0m Session 'JarvisWorkspace' is active. Type 'tmux attach' to enter.")

if __name__ == "__main__":
    work = TerminalMultiplexer()
    work.create_split_session()
