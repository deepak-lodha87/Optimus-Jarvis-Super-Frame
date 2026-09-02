import os
import time
import math

def rotate_core():
    A, B = 0, 0
    chars = ".:-=+*#%@"
    char_len = len(chars) - 1 # अक्षरों की कुल संख्या
    
    print("\n\033[1;32m[SYSTEM REPAIR]\033[0m Fixing Neural Projection...")
    time.sleep(1)

    try:
        while True:
            z = [0] * 1760
            b = [' '] * 1760
            for j in range(0, 628, 7):
                for i in range(0, 628, 2):
                    ini = math.sin(i/100)
                    cosi = math.cos(i/100)
                    sinj = math.sin(j/100)
                    cosj = math.cos(j/100)
                    cosA = math.cos(A)
                    sinA = math.sin(A)
                    cosB = math.cos(B)
                    sinB = math.sin(B)

                    h = cosi + 2
                    D = 1 / (ini * h * sinA + sinj * cosA + 5)
                    t = ini * h * cosA - sinj * sinA

                    x = int(40 + 30 * D * (cosi * h * cosB - t * sinB))
                    y = int(12 + 15 * D * (cosi * h * sinB + t * cosB))
                    o = int(x + 80 * y)
                    
                    # सुरक्षा फ़िल्टर: N को chars की लिमिट के अंदर रखना
                    N = int(8 * ((sinj * sinA - ini * cosi * cosA) * cosB - ini * cosi * sinA - sinj * cosA - cosi * cosi * sinB))
                    
                    if 22 > y > 0 and 80 > x > 0 and D > z[o]:
                        z[o] = D
                        # यहाँ सुधार किया गया है: % char_len का उपयोग
                        idx = N if (N > 0 and N <= char_len) else (char_len if N > char_len else 0)
                        b[o] = chars[idx]

            os.system('clear')
            print("\033[1;36m      OPTIMUS JARVIS SUPER-FRAME | CORE FIXED\033[0m")
            print("".join(b))
            A += 0.04
            B += 0.02
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\n\033[1;31m[OFFLINE]\033[0m Core projection stopped.")

if __name__ == "__main__":
    rotate_core()
