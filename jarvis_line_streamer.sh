#!/data/data/com.termux/files/usr/bin/bash

# ==============================================================================
# PROJECT: OPTIMUS JARVIS SUPER-FRAME
# LINE-BY-LINE DEEP ARCHIVE STREAMER
# OWNER: MASTER DEEPAK
# ==============================================================================

clear
echo -e "\033[1;33m====================================================================\033[0m"
echo -e "\033[1;37;43m   OPTIMUS JARVIS SUPER-FRAME : LINE-BY-LINE CORE CODE STREAMER    \033[0m"
echo -e "\033[1;33m====================================================================\033[0m"

echo -e "\n\033[1;36m[SEARCHING ARCHIVE...] Scanning Termux home directory for all source codes...\033[0m"
sleep 1

# ढूंढें कि क्या कोई स्क्रिप्ट फाइल मौजूद है या नहीं
FILES_FOUND=$(find . -maxdepth 1 -type f \( -name "*.sh" -o -name "*.py" \) ! -name "jarvis_line_streamer.sh")

if [ -z "$FILES_FOUND" ]; then
    echo -e "\n\033[1;31m[ERROR] कोई भी पुरानी .sh या .py फाइल डायरेक्टरी में नहीं मिली।\033[0m"
    echo -e "\033[1;35m[SUGGESTION] कृपया सुनिश्चित करें कि आप उसी फोल्डर में हैं जहाँ फाइलें सेव थीं।\033[0m"
    exit 1
fi

# हर एक फाइल को एक-एक करके पकड़ना और उसके अंदर का कोड लाइन बाय लाइन प्रिंट करना
for file in $FILES_FOUND; do
    echo -e "\n\033[1;34m====================================================================\033[0m"
    echo -e "\033[1;37;44m OPENING FILE: $file \033[0m"
    echo -e "\033[1;34m====================================================================\033[0m"
    sleep 0.5
    
    LINE_COUNT=1
    # फाइल को लाइन बाय लाइन पढ़ना
    while IFS= read -r line; do
        printf "\033[1;30m[Line %03d]:\033[0m %s\n" "$LINE_COUNT" "$line"
        ((LINE_COUNT++))
        # थोड़ा सा डिले ताकि आप स्क्रीन पर कोड को आसानी से चलते हुए देख सकें
        usleep 20000
    done < "$file"
    
    echo -e "\n\033[1;32m[END OF FILE] Finished reading $file successfully.\033[0m"
    echo -e "\033[1;34m--------------------------------------------------------------------\033[0m"
    echo -e "Press [ENTER] to stream the next file..."
    read -r
done

echo -e "\n\033[1;33m====================================================================\033[0m"
echo -e "\033[1;32m[SUCCESS] All old files have been streamed line by line.\033[0m"
echo -e "\033[1;33m====================================================================\033[0m"
