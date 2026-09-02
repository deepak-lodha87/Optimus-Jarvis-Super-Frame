import os
from datetime import datetime

# UI Colors
C = {"G": "\033[92m", "R": "\033[91m", "Y": "\033[93m", "B": "\033[96m", "W": "\033[0m", "BOLD": "\033[1m"}

def get_time_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good Morning"
    elif 12 <= hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"

def color_print(text, color_code):
    print(f"{color_code}{text}{C['W']}")

def mission_entry():
    greeting = get_time_greeting()
    now = datetime.now().strftime("%d %b %Y | %H:%M")
    
    color_print("="*45, C['B'])
    color_print(f"      {greeting}, Commander Deepak", C['BOLD'])
    color_print(f"      System Date: {now}", C['W'])
    color_print("      PHASE 271: IDENTITY PROTOCOL", C['BOLD'])
    color_print

