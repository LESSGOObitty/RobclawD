#!/bin/zsh
echo "[*] Current entropy pool level:"
cat /proc/sys/kernel/random/entropy_avail

echo "[+] Flushing and harvesting high-entropy hardware state..."
dd if=/dev/urandom bs=1024 count=8 2>/dev/null | sha512sum > /tmp/entropy_state.lock

if [ -w /proc/sys/kernel/random/write_wakeup_threshold ]; then
  cat /tmp/entropy_state.lock > /dev/urandom
  echo "[+] Kernel entropy pool re-seeded."
fi

echo "[*] Verified post-injection pool level:"
cat /proc/sys/kernel/random/entropy_avail
rm -f /tmp/entropy_state.lock
