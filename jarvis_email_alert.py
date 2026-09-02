import smtplib
import os
from email.message import EmailMessage

class EmailAlertSystem:
    def __init__(self):
        self.master_email = "your_email@gmail.com"  # यहाँ अपनी ईमेल डालें
        self.app_password = "xxxx xxxx xxxx xxxx"    # अपना 16-अंकों का ऐप पासवर्ड यहाँ डालें

    def send_intruder_report(self, image_path):
        print(f"\n\033[1;31m[SECURITY ALERT]\033[0m Unauthorized entity detected!")
        print("\033[1;33m[UPLINK]\033[0m Sending photo to Master Deepak...")

        msg = EmailMessage()
        msg['Subject'] = '⚠️ JARVIS ALERT: Intruder Detected'
        msg['From'] = self.master_email
        msg['To'] = self.master_email
        msg.set_content('Deepak sir, an unknown subject was detected by the Vision Engine. Attached is the visual data.')

        # फोटो को ईमेल में जोड़ना
        with open(image_path, 'rb') as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype='image', subtype='jpeg', filename='intruder.jpg')

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.master_email, self.app_password)
                smtp.send_message(msg)
                
            print("\033[1;32m[SUCCESS]\033[0m Intelligence report sent successfully.")
            os.system('termux-tts-speak "Deepak sir, the intruder report has been transmitted to your secure email."')
        except Exception as e:
            print(f"\033[1;31m[FAILED]\033[0m Could not send email: {e}")

if __name__ == "__main__":
    alert = EmailAlertSystem()
    # मान लीजिए जार्विस ने 'current_scan.jpg' ली है
    if os.path.exists("current_scan.jpg"):
        alert.send_intruder_report("current_scan.jpg")
    else:
        print("No image data found to send.")
