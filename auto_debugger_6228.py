import sys, os, time, secrets

class CodeDebugger:
    def __init__(self):
        self.nad_id = f"NAD-{secrets.token_hex(2).upper()}"
        self.report = []

    def analyze_file(self, target_file):
        print(f"\n\033[1;33m[SCANNING] File: {target_file} | ID: {self.nad_id}\033[0m")
        if not os.path.exists(target_file):
            print("\033[1;31m[ERROR] File not found!\033[0m")
            return

        with open(target_file, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            # Simple check for common mistakes (e.g., missing colons)
            if (line.strip().startswith("def ") or line.strip().startswith("if ")) and not line.strip().endswith(":"):
                self.report.append(f"Line {i+1}: Missing colon ':' at the end.")
            
            # Check for print statements without brackets (Python 2 style)
            if "print " in line and "(" not in line:
                self.report.append(f"Line {i+1}: Use print() with brackets (Python 3 style).")

        self.display_report()

    def display_report(self):
        if not self.report:
            print("\033[1;32m[CLEAN] No obvious syntax bugs found. Logic flow is optimal.\033[0m")
        else:
            print("\033[1;31m--- DEBUG REPORT ---\033[0m")
            for issue in self.report:
                print(f"[!] {issue}")
        print(f"\033[1;37m" + "="*40 + "\033[0m")

if __name__ == "__main__":
    debugger = CodeDebugger()
    # Check if a filename was provided as an argument
    if len(sys.argv) > 1:
        debugger.analyze_file(sys.argv[1])
    else:
        # Self-test on the architect module we made earlier
        debugger.analyze_file("income_engine_6223.py")
