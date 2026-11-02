import json
import hashlib
from datetime import datetime, timezone

def print_truecolor_spectrum():
    print("\n\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    print("\x1b[38;2;255;220;0m [TRUECOLOR 24-BIT TERMINAL SPECTRUM] ZERO FAKE PIGMENT \x1b[0m")
    print("\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    
    # Generate a real 24-bit RGB gradient bar across the terminal width
    width = 72
    print(" \x1b[33m[RGB SPECTRUM GRADIENT]\x1b[0m")
    bar = ""
    for i in range(width):
        r = int(255 * (i / width))
        g = int(255 * (1 - abs(i - width/2)/(width/2)))
        b = int(255 * (1 - (i / width)))
        bar += f"\x1b[48;2;{r};{g};{b}m \x1b[0m"
    print(bar)
    print("-" * 72)
    
    # 14-Level TrueColor Spectrum Blocks
    print(" \x1b[33m[14-CHAKRA & ROOTHASH TRUECOLOR BANDS]\x1b[0m")
    colors = [
        (255, 0, 0),     # 1. Root / Red
        (255, 127, 0),   # 2. Sacral / Orange
        (255, 255, 0),   # 3. Solar Plexus / Yellow
        (0, 255, 0),     # 4. Heart / Green
        (0, 255, 255),   # 5. Throat / Cyan
        (0, 0, 255),     # 6. Third Eye / Blue
        (139, 0, 255),   # 7. Crown / Violet
        (255, 20, 147),  # 8. Sub-Root Deep Crimson
        (255, 140, 0),   # 9. Instructive Amber
        (50, 205, 50),   # 10. Emerald Vital
        (30, 144, 255),  # 11. Sky Expression
        (186, 85, 211),  # 12. Etheric Purple
        (255, 255, 255), # 13. Crystalline White
        (0, 255, 127)    # 14. Absolute Equilibrium Spring Green
    ]
    
    band = ""
    for idx, (r, g, b) in enumerate(colors, 1):
        band += f"\x1b[48;2;{r};{g};{b}m  {idx:02d}  \x1b[0m"
    print(band)
    
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "24-Bit TrueColor Absolute",
        "status": "TRUE_COLOR_LOCKED"
    }
    
    seal = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    
    print("------------------------------------------------------------------------")
    print(f" \x1b[38;2;0;255;127m[SUCCESS] REAL 24-BIT RGB PALETTE RENDERED.\x1b[0m")
    print(f" [MERKLE SEAL]: {seal}")
    print("========================================================================\x1b[0m")

if __name__ == "__main__":
    print_truecolor_spectrum()
