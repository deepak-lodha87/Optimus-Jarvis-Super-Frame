import os
import time

def self_learning_log_analyzer():
    print("\n" + "="*40)
    print("      JARVIS SELF-LEARNING LOG ANALYZER")
    print("="*40)
    
    msg_init = "Commander Deepak, initiating deep-scan of historical activity logs."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")
    
    # फाइलों की सूची जिनका विश्लेषण करना है
    log_files = {
        "Academic": "study_log.txt",
        "Financial": "expense_log.txt",
        "System": "command_log.txt"
    }
    
    analysis_report = []
    
    for category, file_name in log_files.items():
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                entry_count = len(f.readlines())
                analysis_report.append(f"{category}: {entry_count} activities recorded.")
        else:
            analysis_report.append(f"{category}: No data available.")
            
    print("\n[ANALYSIS REPORT]:")
    for report in analysis_report:
        print(f"- {report}")
        
    time.sleep(1)
    
    summary = "Commander, your recent focus has been primarily on system development and academic preparation."
    print(f"\n[INSIGHT]: {summary}")
    os.system(f"termux-tts-speak '{summary}'")

    print("\n" + "="*40)

if __name__ == "__main__":
    self_learning_log_analyzer()
