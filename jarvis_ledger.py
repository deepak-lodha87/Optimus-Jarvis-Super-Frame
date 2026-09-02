import datetime

def record_trade(action, stock, price, qty):
    total = price * qty
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"[{now}] {action.upper()} | {stock} | Price: {price} | Qty: {qty} | Total: {total}\n"
    
    with open("trading_history.txt", "a") as file:
        file.write(log_entry)
    
    print(f"[JARVIS] रिकॉर्ड अपडेट कर दिया गया है: {stock} {action}")

def show_history():
    print("\n--- जार्विस ट्रेडिंग इतिहास ---")
    with open("trading_history.txt", "r") as file:
        print(file.read())

# टेस्ट करने के लिए:
# record_trade('buy', 'TATASTEEL', 150, 6)
# show_history()
