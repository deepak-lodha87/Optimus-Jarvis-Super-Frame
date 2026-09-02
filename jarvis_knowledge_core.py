import time, os

class KnowledgeCore:
    def __init__(self):
        self.libraries = ["History", "Economics", "Sociology", "Python-Dev"]
        self.status = "SYNCING"

    def activate_librarian(self):
        os.system('clear')
        print(f"\033[1;32m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS KNOWLEDGE-CORE : PHASE 21 - STEP 1      \033[0m")
        print(f"\033[1;32m====================================================\033[0m")
        
        print("\033[1;33m[INDEXING]\033[0m Building Semantic Relations...")
        time.sleep(1.5)
        
        for lib in self.libraries:
            print(f" \033[1;34m[NODE]\033[0m {lib:25} | [\033[1;32mLEARNING\033[0m]")
            time.sleep(0.7)

        print(f"\n\033[1;32m[SUCCESS] Knowledge-Core is Active. Jarvis is learning.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, my database is expanding. \nI am absorbing the wisdom of ages. History, \nScience, and Law are flowing through my \ncircuits. I am becoming your ultimate mentor. \nAsk me anything; the world's knowledge is now \nat your fingertips.\033[0m")
        print(f"\033[1;32m====================================================\033[0m")

if __name__ == "__main__":
    core = KnowledgeCore()
    core.activate_librarian()
