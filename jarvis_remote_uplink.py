import imaplib
import email
import os

class NeuralUplink:
    def __init__(self):
        self.master = "Deepak"
        self.mail_user = "YOUR_EMAIL@gmail.com"
        self.mail_pass = "YOUR_APP_PASSWORD"

    def listen_remote(self):
        print("\n\033[1;35m[NEURAL UPLINK ACTIVE]\033[0m Scanning encrypted commands...")
        try:
            mail = imaplib.IMAP4_SSL("imap.gmail.com")
            mail.login(self.mail_user, self.mail_pass)
            mail.select("inbox")

            # केवल अनरीड (Unseen) ईमेल चेक करना
            _, data = mail.search(None, 'UNSEEN')
            
            for num in data[0].split():
                _, msg_data = mail.fetch(num, '(RFC822)')
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        subject = msg['subject'].lower()
                        
                        if "status" in subject:
                            print("\033[1;32m[REMOTE CMD]:\033[0m Status Request Received.")
                            os.system("python jarvis_social_sync.py")
                        elif "battery" in subject:
                            os.system("python jarvis_power_guardian.py")
            
            mail.logout()
        except Exception as e:
            print(f"\033[1;31m[UPLINK ERROR]:\033[0m {e}")

if __name__ == "__main__":
    uplink = NeuralUplink()
    uplink.listen_remote()
