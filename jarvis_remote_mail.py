import imaplib
import email
import os
import time

class RemoteOverlord:
    def __init__(self):
        self.master_email = "your_email@gmail.com"
        self.app_password = "your_app_password" # यहाँ अपना 16-अंकों का ऐप पासवर्ड डालें
        self.imap_url = 'imap.gmail.com'

    def listen_for_commands(self):
        print("\n\033[1;36m[REMOTE UPLINK]\033[0m Scanning for encrypted commands...")
        try:
            mail = imaplib.IMAP4_SSL(self.imap_url)
            mail.login(self.master_email, self.app_password)
            mail.select('inbox')

            # सिर्फ बिना पढ़े (Unseen) ईमेल चेक करना
            result, data = mail.search(None, '(UNSEEN)')
            mail_ids = data[0].split()

            if mail_ids:
                latest_id = mail_ids[-1]
                result, data = mail.fetch(latest_id, '(RFC822)')
                raw_email = data[0][1]
                msg = email.message_from_bytes(raw_email)
                
                subject = msg['subject'].lower()
                sender = msg['from']

                if self.master_email in sender:
                    print(f"\033[1;32m[AUTHORIZED]:\033[0m Command Received: {subject}")
                    
                    if "status" in subject:
                        os.system("python jarvis_system_health.py")
                    elif "photo" in subject:
                        os.system("termux-camera-photo -c 1 remote_capture.jpg")
                        print("Remote snapshot taken.")
                    elif "brief" in subject:
                        os.system("python jarvis_daily_brief.py")
                    
                    os.system(f'termux-tts-speak "Remote command {subject} executed, Deepak sir."')
            else:
                print("\033[1;33m[CLEAN]\033[0m No remote instructions found.")
            
            mail.logout()
        except Exception as e:
            print(f"Connection Failed: {e}")

if __name__ == "__main__":
    remote = RemoteOverlord()
    # इसे आप लूप में चला सकते हैं या हर 5 मिनट में चेक कर सकते हैं
    remote.listen_for_commands()
