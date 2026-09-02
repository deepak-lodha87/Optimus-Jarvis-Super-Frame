import os
import subprocess
import sys

def verify_fingerprint():
    # सुरक्षा जांच शुरू
    print("\033[1;31m[SECURITY]\033[0m Awaiting Biometric Authentication...")
    
    # एंड्रॉइड फिंगरप्रिंट सेंसर को कॉल करना
    result = subprocess.run(['termux-fingerprint'], capture_output=True, text=True)
    
    if '"auth_result": "AUTH_RESULT_SUCCESS"' in result.stdout:
        print("\033[1;32m[ACCESS GRANTED]\033[0m Welcome back, Deepak sir.")
        return True
    else:
        print("\033[1;31m[ACCESS DENIED]\033[0m Unauthorized Entry Attempt.")
        # गलत स्कैन पर तुरंत बाहर निकलें
        os.system('exit')
        return False

if __name__ == "__main__":
    if verify_fingerprint():
        # सफल पहचान के बाद डैशबोर्ड लोड करें
        os.system('python ~/jarvis_boot_dashboard.py')
