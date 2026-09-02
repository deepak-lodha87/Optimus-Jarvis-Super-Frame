#!/data/data/com.termux/files/usr/bin/bash

# ==============================================================================
# PROJECT: OPTIMUS JARVIS SUPER-FRAME
# MODULE: CONTROLLER INTERFACE TO UTILISED THE CORE PACKAGE
# OWNER: MASTER DEEPAK
# ==============================================================================

# पहले कोड (कोर पैकेज) को इस कंट्रोलर के भीतर लोड करना
if [ -f ./jarvis_core.sh ]; then
    source ./jarvis_core.sh
else
    echo -e "\033[1;31m[ERROR] मुख्य फाइल 'jarvis_core.sh' नहीं मिली! पहले उसे बनाएं।\033[0m"
    exit 1
fi

clear
while true
do
    echo -e "\n\033[1;34m====================================================================\033[0m"
    echo -e "\033[1;37;44m     OPTIMUS JARVIS SUPER-FRAME : UNIFIED INTERFACE PANEL         \033[0m"
    echo -e "\033[1;34m====================================================================\033[0m"
    echo -e " दीपक सर, आप इस मुख्य पैकेज से किस मॉड्यूल का उपयोग करना चाहते हैं?"
    echo -e " \033[1;36m[1]\033[0m अंतरिक्ष और हाइपर-स्पीड डेटा (Space Core)"
    echo -e " \033[1;35m[2]\033[0m स्पाइडरमैन नैनो टेक्नोलॉजी (Spiderman Nano-Tech)"
    echo -e " \033[1;33m[3]\033[0m हाइपर सस्पेंशन मैकेनिक्स (Hyper Suspension Core)"
    echo -e " \033[1;32m[4]\033[0m ओप्पो मोबाइल का असली सेंसर डेटा (Real Hardware Telemetry)"
    echo -e " \033[1;31m[5]\033[0m सिस्टम से बाहर निकलें (Exit Control Panel)"
    echo -e "\033[1;34m====================================================================\033[0m"
    
    read -p " अपना विकल्प चुनें (1-5): " CHOICE
    
    case $CHOICE in
        1) clear; get_space_intel ;;
        2) clear; get_nanotech_intel ;;
        3) clear; get_suspension_intel ;;
        4) clear; get_hardware_status ;;
        5) echo -e "\n\033[1;32m[INFO] कंट्रोल पैनल बंद हो रहा है। कोर पैकेज सुरक्षित है।\033[0m"; exit ;;
        *) echo -e "\n\033[1;31m[INVALID] गलत विकल्प! कृपया 1 से 5 के बीच चुनें।\033[0m" ;;
    esac
    
    echo -e "\n\033[1;34m====================================================================\033[0m"
    read -p " मुख्य मेनू पर वापस जाने के लिए ENTER दबाएं..." KEY
    clear
done
