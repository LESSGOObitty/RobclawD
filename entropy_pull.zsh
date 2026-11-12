#!/bin/zsh
if [ "$EUID" -ne 0 ]; then
  echo "[-] Drop into termux-chroot or run with proper privileges for full device entropy hooks."
fi
echo "[+] Tapping hardware entropy and jitter sources..."
ENTROPY_SEED=$(dd if=/dev/urandom bs=64 count=1 2>/dev/null | sha512sum | awk '{print $1}')
echo "[+] Entropy pool seeded successfully."
echo "[*] Master Hash: $ENTROPY_SEED"
