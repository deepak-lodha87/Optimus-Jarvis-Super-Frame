import os

class IntegrityValidator:
    def __init__(self):
        self.master = "Deepak"
        # उन फाइलों की लिस्ट जिन्हें चेक करना है
        self.critical_files = [
            "jarvis_main_brain.py",
            "jarvis_stealth_security.py",
            "jarvis_resilient_monitor.py",
            "jarvis_logic_reader.py"
        ]

    def validate_core(self):
        print(f"\n\033[1;34m[INTEGRITY CHECK ACTIVE]\033[0m Scanning core components...")
        missing_files = []
        
        for file in self.critical_files:
            if os.path.exists(file):
                print(f"\033[1;32m[OK]:\033[0m {file} is secure.")
            else:
                print(f"\033[1;31m[MISSING]:\033[0m {file} not found!")
                missing_files.append(file)
        
        if not missing_files:
            msg = "Deepak sir, all core modules are intact. System integrity is one hundred percent."
        else:
            msg = f"Warning Deepak sir, {len(missing_files)} modules are missing from the frame."
            
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    validator = IntegrityValidator()
    validator.validate_core()
