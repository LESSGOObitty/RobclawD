# --- Termux Diamond State Sovereign Execution Surface -------------------------
import os
from datetime import datetime

def write_rob_witness(tag, energy, element):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    line = f"[{stamp}][{tag}][{energy}][{element}] DIAMOND-STATE-WITNESS"
    os.makedirs("robdoe_pulse", exist_ok=True)
    with open("robdoe_pulse/pulse.log", "a") as f:
        f.write(line + "\n")
    print(f">>> \033[33m{line}\033[0m")

def tetra(): write_rob_witness("TETRA", "IGNITION", "HYDROGEN (H)")
def cube(): write_rob_witness("CUBE", "STABILIZATION", "OXYGEN (O)")
def octa(): write_rob_witness("OCTA", "BALANCE", "NITROGEN (N)")
def icosa(): write_rob_witness("ICOSA", "EXPANSION", "CARBON (C)")
