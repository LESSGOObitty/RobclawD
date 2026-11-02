import cmath
import json
import hashlib
from datetime import datetime, timezone

def execute_formula():
    print("\n\x1b[38;5;51m========================================================================\x1b[0m")
    print("\x1b[38;5;226m [COMPLEX DYNAMICS] Z = z^2 + eM^2 MAPPING MATRIX \x1b[0m")
    print("\x1b[38;5;51m========================================================================\x1b[0m")
    
    z = complex(0.5, 0.5)
    e_val = cmath.e
    m = complex(1.2, 0.4)
    
    # Z = z^2 + e * M^2
    z_next = (z ** 2) + (e_val * (m ** 2))
    
    print(f" \x1b[33m[INITIAL Z]\x1b[0m {z}")
    print(f" \x1b[33m[OPERATOR M]\x1b[0m {m}")
    print(f" \x1b[32m[RESULTANT Z']\x1b[0m {z_next.real:.4f} + {z_next.imag:.4f}i")
    print(f" \x1b[33m[STATUS]\x1b[0m Non-linear feedback loop locked.")
    print("========================================================================")

if __name__ == "__main__":
    execute_formula()
