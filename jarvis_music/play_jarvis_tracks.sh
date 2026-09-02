#!/data/data/com.termux/files/usr/bin/bash

clear
echo -e "\033[1;32m============================================================\033[0m"
echo -e "\033[1;37;42m   OPTIMUS JARVIS SUPER-FRAME : PHASE 77 STREAM REPAIR     \033[0m"
echo -e "\033[1;32m============================================================\033[0m"

echo -e "\n\033[1;36m[REPAIR] Cleaning old buffer and testing live connections...\033[0m"
rm -f *.mp3 *.webm *.m4a 2>/dev/null

echo -e "\n\033[1;33m[1] नए एक्टिव गानों को हाई-स्पीड पर डाउनलोड किया जा रहा है...\033[0m"
# यहाँ हमने पूरी तरह से वर्किंग सिंगल ट्रैक्स और लाइव गानों के पैरामीटर्स सेट कर दिए हैं
yt-dlp --extract-audio --audio-format mp3 --max-downloads 20 --no-check-certificates "https://www.youtube.com/watch?v=k4yXQkG2E1w" || yt-dlp --extract-audio --audio-format mp3 --max-downloads 20 "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

if [ -f *.mp3 ]; then
    echo -e "\n\033[1;32m[SUCCESS] सभी एक्टिव गाने सफलतापूर्वक डाउनलोड हो चुके हैं!\033[0m"
    echo -e "\033[1;35m[INFO] अब आपके गाने बकायदा आवाज़ के साथ प्ले हो रहे हैं...\033[0m"
    echo -e "\033[1;36m[CONTROLS] अगला गाना: Enter | रोकना/चालू करना: Space | बंद करना: q\033[0m"
    echo -e "\033[1;32m============================================================\033[0m"
    mpv --no-video *.mp3
else
    echo -e "\n\033[1;31m[ERROR] नेटवर्क कनेक्शन या यूआरएल में दिक्कत है। डायरेक्ट स्ट्रीमिंग मोड चालू...\033[0m"
    # अगर डाउनलोड में कोई भी दिक्कत आए, तो यह डायरेक्ट इंटरनेट से गाना बजा देगा बिना डाउनलोड किए
    mpv --no-video "https://www.youtube.com/watch?v=k4yXQkG2E1w"
fi
