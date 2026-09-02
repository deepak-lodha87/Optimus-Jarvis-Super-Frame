import numpy as np

def calculate_alpha(prices):
    """
    Alpha ही वह जादुई नंबर है जो बताता है कि 
    आपका एल्गोरिदम मार्केट से कितना बेहतर है।
    """
    returns = np.diff(prices) / prices[:-1]
    # जार्विस यहाँ 'Sharpe Ratio' कैलकुलेट करेगा
    # जो रिस्क और रिटर्न का बैलेंस बताता है
    avg_return = np.mean(returns)
    std_dev = np.std(returns)
    
    sharpe_ratio = avg_return / std_dev if std_dev != 0 else 0
    print(f"[JARVIS] Sharpe Ratio: {sharpe_ratio:.4f}")
    
    if sharpe_ratio > 1.5:
        return "HIGH CONFIDENCE: ट्रेड लें"
    else:
        return "LOW CONFIDENCE: इंतज़ार करें"

# जार्विस खुद तय करेगा कि कब एंट्री लेनी है
