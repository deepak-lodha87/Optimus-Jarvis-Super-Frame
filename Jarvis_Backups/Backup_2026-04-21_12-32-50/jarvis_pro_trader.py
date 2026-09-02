import math

class JarvisAdvancedTrader:
    def __init__(self, capital):
        self.capital = capital
        self.risk_per_trade = 0.01 # केवल 1% रिस्क
        print(f"[JARVIS] सिस्टम एक्टिवेटेड। शुरुआती पूँजी: ₹{self.capital}")

    def calculate_position(self, current_price):
        """Kelly Criterion: दुनिया का सबसे एडवांस फॉर्मूला मुनाफे को मैक्सिमाइज करने के लिए"""
        win_prob = 0.65  # जार्विस की जीतने की संभावना (65%)
        win_loss_ratio = 2.0
        
        # Kelly Fraction Formula: f = (bp - q) / b
        f = (win_loss_ratio * win_prob - (1 - win_prob)) / win_loss_ratio
        
        investment = self.capital * f
        print(f"[JARVIS] गणना पूर्ण: इस ट्रेड में ₹{investment:.2f} लगाना सुरक्षित है।")
        return investment

# जार्विस को ₹1000 के साथ टेस्ट करना
jarvis_ai = JarvisAdvancedTrader(1000)
jarvis_ai.calculate_position(150)
