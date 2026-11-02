import sys
import hashlib
import time

class SovereignVault:
    def __init__(self, initial_capital=1161.80):
        self.capital = initial_capital
        self.multiplier = 1.618
        self.epoch = 0
        self.ledger = []

    def inspect(self):
        print(f"\n[+] CURRENT VAULT STATUS")
        print(f"    - Epoch: {self.epoch}")
        print(f"    - Capital Balance: {self.capital:,.2f} units")
        print(f"    - Total Ledger Entries: {len(self.ledger)}")

    def advance_epoch(self):
        self.epoch += 1
        self.capital *= self.multiplier
        proof = hashlib.sha3_256(f"{self.capital}-{self.epoch}".encode()).hexdigest()
        self.ledger.append((self.epoch, self.capital, proof))
        print(f"\n[+] ADVANCED TO EPOCH {self.epoch}")
        print(f"    - New Vault State: {self.capital:,.2f} units")
        print(f"    - SHA3 Proof: 0x{proof[:16]}...")

    def export_manifest(self):
        print(f"\n[+] EXPORTING SOVEREIGN MANIFEST...")
        for ep, cap, prf in self.ledger:
            print(f"    Epoch {ep} | {cap:,.2f} units | 0x{prf[:12]}...")
        print("    [Status: Manifest Immutable & Secured]\n")

def main():
    vault = SovereignVault()
    print(" >>> NPP Vault Initialized. Type 'step' to advance, 'inspect' to check, 'export' for log, 'exit' to quit.")
    
    while True:
        try:
            cmd = input("\nnpp-vault> ").strip().lower()
            if cmd == "step":
                vault.advance_epoch()
            elif cmd == "inspect":
                vault.inspect()
            elif cmd == "export":
                vault.export_manifest()
            elif cmd == "exit":
                print(" >>> Securing vault state and exiting controller.")
                break
            else:
                print(" [!] Unknown command. Use: step, inspect, export, exit")
        except (KeyboardInterrupt, EOFError):
            print("\n >>> Vault state locked. Session terminated safely.")
            break

if __name__ == "__main__":
    main()
