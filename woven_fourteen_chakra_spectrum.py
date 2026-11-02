import json
import hashlib
from datetime import datetime, timezone

def weave_chakras():
    print("\n\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    print("\x1b[38;2;255;220;0m [WOVEN 14-CHAKRA SPECTRUM] TRUECOLOR TENSION & WEAVE MATRIX \x1b[0m")
    print("\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    
    # 14 Chakras with exact RGB TrueColor definitions & woven alignment tags
    chakra_spectrum = [
        (1, "Patala (Deep Sub-Root)", 15, 0, 30, "Obsidian Root Anchor"),
        (2, "Rasatala (Underworld)", 75, 0, 130, "Deep Crimson Foundation"),
        (3, "Mahatala (Nether Base)", 139, 0, 0, "Burnt Orange Matrix"),
        (4, "Talatala (Subterranean)", 204, 85, 0, "Amber Gold Drive"),
        (5, "Sutala (Lower Region)", 218, 165, 32, "Bright Yellow Willpower"),
        (6, "Vitala (Nether Realm)", 0, 100, 0, "Emerald Vital Force"),
        (7, "Atala (Sub-Earth)", 0, 139, 139, "Sky Blue Expression"),
        (8, "Muladhara (Root)", 255, 0, 0, "Vibrant Red Grounding"),
        (9, "Svadhisthana (Sacral)", 255, 127, 0, "Pure Orange Flow"),
        (10, "Manipura (Solar Plexus)", 255, 255, 0, "Golden Yellow Power"),
        (11, "Anahata (Heart)", 0, 255, 0, "Emerald Lattice Balance"),
        (12, "Vishuddha (Throat)", 0, 255, 255, "Bright Blue Resonance"),
        (13, "Ajna (Third Eye)", 75, 0, 130, "Indigo Vision & Perception"),
        (14, "Sahasrara (Crown / Beyond)", 255, 255, 255, "Crystalline White Equilibrium")
    ]
    
    print(" \x1b[33m[WOVEN TRUECOLOR STRANDS]\x1b[0m")
    for idx, name, r, g, b, function in chakra_spectrum:
        # Render a truecolor block for each woven strand
        block = f"\x1b[48;2;{r};{g};{b}m    \x1b[0m"
        print(f" {block} \x1b[38;2;{r};{g};{b}m[Chakra {idx:02d}]\x1b[0m {name:<30} -> {function}")
        
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "system": "Woven 14-Chakra TrueColor Spectrum",
        "total_strands": 14,
        "status": "WOVEN_EQUILIBRIUM_LOCKED"
    }
    
    seal = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    
    print("------------------------------------------------------------------------")
    print(f" \x1b[38;2;0;255;127m[SUCCESS] 14 CHAKRAS WOVEN INTO UNBREAKABLE TRUECOLOR LATTICE.\x1b[0m")
    print(f" [MERKLE SEAL]: {seal}")
    print("========================================================================\x1b[0m")

if __name__ == "__main__":
    weave_chakras()
