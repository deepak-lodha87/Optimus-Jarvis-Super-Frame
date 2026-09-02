def calculate_freedom(current_capital, daily_target_percent, dream_amount):
    print("==================================================")
    print("        JARVIS: FREEDOM & DREAMS CALCULATOR       ")
    print("==================================================")
    
    days = 0
    temp_capital = current_capital
    
    # 365 दिनों का प्रोजेक्शन (एक साल का अनुमान)
    while temp_capital < dream_amount and days < 365:
        temp_capital += temp_capital * (daily_target_percent / 100)
        days += 1
    
    print(f"Current Capital: ₹{current_capital}")
    print(f"Daily Target: {daily_target_percent}%")
    print(f"Dream Amount: ₹{dream_amount}")
    print("--------------------------------------------------")
    
    if days < 365:
        print(f"[JARVIS]: सर, इस रफ़्तार से आप {days} दिनों में अपने लक्ष्य तक पहुँच सकते हैं!")
    else:
        print(f"[JARVIS]: लक्ष्य बड़ा है, हमें अपनी 'Compounding' बढ़ानी होगी।")
    print("==================================================")

# टेस्ट के लिए: ₹1000 से शुरू, 2% रोज़ाना, लक्ष्य ₹1,00,000
# calculate_freedom(1000, 2, 100000)
