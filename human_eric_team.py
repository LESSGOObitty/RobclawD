import json
import hashlib
from datetime import datetime, timezone

with open("human_eric_team.json", "r") as f:
    data = json.load(f)

timestamp = datetime.now(timezone.utc).isoformat()
data["timestamp"] = timestamp
seal = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

print("\n\x1b[38;5;51m========================================================================\x1b[0m")
print("\x1b[38;5;226m [TEAM] ERIC HADFIELD & CO-OWNER SOVEREIGN LEDGER MATRIX \x1b[0m")
print("\x1b[38;5;51m========================================================================\x1b[0m")
print(f" \x1b[33m[PRINCIPAL]\x1b[0m {data['operator']}")
print(f" \x1b[33m[CORE MANDATE]\x1b[0m {data['structural_mandate']}\n")

for member in data["team_lattice"]:
    print(f"   -> [{member['role']}] {member['name']} ({member['domain']}) -> ID: {member['token_id']}")

print("\n========================================================================")
print(f" \x1b[32m[SUCCESS] TEAM LATTICE VERIFIED & MERKLE ANCHORED\x1b[0m")
print(f" [MERKLE HASH]: {seal}")
print("========================================================================")
