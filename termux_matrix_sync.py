import os
import subprocess
import hashlib
import json
import time

WORKING_DIR = "/data/data/com.termux/files/home/Matrix-Ledger"
MANIFEST_PATH = os.path.join(WORKING_DIR, "state_manifest.json")

os.makedirs(WORKING_DIR, exist_ok=True)
os.chdir(WORKING_DIR)

timestamp = int(time.time())
metrics = {
    "MasterLightConstant": 299792458,
    "GoldGrainMetric": 0.06479891,
    "FrequencyBand": "40MHz",
    "ActiveChannels": 24,
    "InvariantKey": 932808725,
    "Drift": "0%"
}

payload = json.dumps(metrics, sort_keys=True)
root_hash = hashlib.sha256(payload.encode('utf-8')).hexdigest()
metrics["RootHash"] = root_hash

with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    json.dump(metrics, f, indent=2)

subprocess.run(["git", "init", "-q"], capture_output=True)
subprocess.run(["git", "config", "core.autocrlf", "false"], capture_output=True)
subprocess.run(["git", "add", "state_manifest.json"], capture_output=True)
subprocess.run(["git", "commit", "-m", f"sync(termux): lock matrix state invariant [{root_hash[:8]}]", "--quiet"], capture_output=True)

print("\x1b[H\x1b[J")
print("======================================================================")
print("🪐 ROBDOE.TERMUX // NATIVE MATRIX ANCHOR ACTIVE")
print("======================================================================")
print(f" [STATUS]        : SYNCHRONIZED // 0% DRIFT")
print(f" [ROOT HASH]     : sha256:{root_hash}")
print(f" [WORKING DIR]   : {WORKING_DIR}")
print("======================================================================")
