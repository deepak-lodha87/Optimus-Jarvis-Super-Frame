import yfinance as yf
import time

# जार्विस के अपडेटेड कड़े नियम
PROFIT_LIMIT = 10.0  # हमने मुनाफा 10% कर दिया (₹1000 पर ₹100)
STOP_LOSS_LIMIT = 3.0 # 3% से ज्यादा नुकसान होने पर तुरंत बाहर

def jarvis_monitor(ticker, buy_price):
    print(f"\n[JARVIS] {ticker} पर नज़र रखी जा रही है...")
    print(f"[RULES] Target: {PROFIT_LIMIT}% | StopLoss: {STOP_LOSS_LIMIT}%")
    
    while True:
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period='1d')
            current_price = data['Close'][-1]
            
            change = ((current_price - buy_price) / buy_price) * 100
            
            print(f"Status: {ticker} @ {current_price:.2f} | Change: {change:.2f}%", end="\r")

            # मुनाफा बुक करना
            if change >= PROFIT_LIMIT:
                print(f"\n[EXECUTE] लक्ष्य प्राप्त! {PROFIT_LIMIT}% मुनाफा बुक किया गया।")
                break
            
            # नुकसान रोकना (सुरक्षा कवच)
            elif change <= -STOP_LOSS_LIMIT:
                print(f"\n[CRITICAL] सुरक्षा नियम सक्रिय! भारी नुकसान से बचने के लिए सेल किया।")
                break
                
            time.sleep(5) # हर 5 सेकंड में अपडेट
            
        except Exception as e:
            print(f"\nError: {e}")
            break

# यहाँ स्टॉक का नाम (जैसे RELIANCE.NS) और अपनी खरीदी कीमत डालें
# jarvis_monitor('TATAMOTORS.NS', 950) 
