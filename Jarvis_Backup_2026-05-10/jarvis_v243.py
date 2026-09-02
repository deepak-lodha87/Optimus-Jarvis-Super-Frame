import os
import time
from datetime import datetime

def automated_weekly_report():
    print("\n" + "="*45)
    print("      JARVIS WEEKLY PERFORMANCE REPORT")
    print("="*45)
    
    msg_init = "Commander Deepak, generating your weekly performance summary..."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")
    
    report_file = f"Report_{datetime.now().strftime('%Y_%m_%d')}.txt"
    log_files = {
        "Academic Progress": "study_log.txt",
        "Financial Overview": "expense_log.txt",
        "System Commands": "command_log.txt"
    }
    
    with open(report_file, 'w') as report:
        report.write(f"--- OPTIMUS JARVIS WEEKLY REPORT ---\n")
        report.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        report.write(f"Commander: Deepak\n")
        report.write("-" * 35 + "\n\n")
        
        for category, file_name in log_files.items():
            if os.path.exists(file_name):
                with open(file_name, 'r') as f:
                    lines = f.readlines()
                    count = len(lines)
                    report.write(f"[{category}]: {count} entries recorded.\n")
                    print(f"[ANALYZING]: {category} data compiled.")
            else:
                report.write(f"[{category}]: No data available this week.\n")
        
        report.write("\n--- End of Report ---")
    
    time.sleep(1.5)
    success = f"Commander, the weekly report has been compiled as {report_file}."
    print(f"\n[SUCCESS]: {success}")
    os.system(f"termux-tts-speak '{success}'")
    print("\n" + "="*45)

if __name__ == "__main__":
    automated_weekly_report()
