from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def execute_command():
    cmd = request.args.get('cmd')
    master_key = request.args.get('key')
    
    # सुरक्षा के लिए 'Key' चेक करना (सिमुलेशन नहीं, असली ऑथेंटिकेशन)
    if master_key == "DEEPAK_V83":
        print(f"\n\033[1;32m[REMOTE COMMAND RECEIVED]:\033[0m {cmd}")
        
        # जार्विस उस कमांड को आपके फोन पर बोलेगा
        os.system(f'termux-tts-speak "Deepak sir, executing remote command: {cmd}"')
        
        # यहाँ आप असली सिस्टम कमांड्स भी रन कर सकते हैं
        if cmd == "lockdown":
            return "System Secured. All modules offline."
        
        return f"Command '{cmd}' executed successfully on Optimus Super-Frame."
    else:
        return "Unauthorized Access Denied.", 403

if __name__ == "__main__":
    print("\n\033[1;36m[SERVER STARTING]\033[0m Jarvis is now listening for remote signals...")
    # सर्वर को लोकल नेटवर्क पर लाइव करना
    app.run(host='0.0.0.0', port=5000)
