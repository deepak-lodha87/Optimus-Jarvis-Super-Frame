def job_exit_status(current_savings, monthly_expenses, jarvis_profit):
    print("==================================================")
    print("        JARVIS: FINANCIAL FREEDOM TRACKER         ")
    print("==================================================")
    
    # कितने महीने आप बिना नौकरी के चल सकते हैं
    runway = current_savings / monthly_expenses if monthly_expenses > 0 else 0
    
    print(f"Monthly Expense: ₹{monthly_expenses}")
    print(f"Jarvis Monthly Profit: ₹{jarvis_profit}")
    print(f"Current Runway: {runway:.1f} Months")
    print("--------------------------------------------------")
    
    if jarvis_profit >= monthly_expenses:
        print("[JARVIS]: बधाई हो! आप पूरी तरह 'Financial Free' हैं।")
    else:
        gap = monthly_expenses - jarvis_profit
        print(f"[JARVIS]: हमें ₹{gap} और कमाने हैं ताकि हम सुरक्षित रहें।")
    print("==================================================")

# उदाहरण: बचत 5000, खर्चा 8000, जार्विस का मुनाफा 2000
# job_exit_status(5000, 8000, 2000)
