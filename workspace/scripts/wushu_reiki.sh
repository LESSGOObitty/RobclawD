#!/data/data/com.termux/files/usr/bin/sh
echo "=== 🥋 WUSHU REIKI: SYSTEM CHI & TELEMETRY PULSE ==="
echo "[*] Timestamp: $(date)"
echo "[*] Engine Status:"
tmux has-session -t robclaw-engine 2>/dev/null && echo "  -> robclaw-engine: ACTIVE [RUNNING]" || echo "  -> robclaw-engine: OFFLINE [STOPPED]"

echo "[*] Thermal & Battery Flow:"
if command -v termux-battery-status >/dev/null 2>&1; then
    termux-battery-status 2>/dev/null | grep -E "temperature|percentage|status" | sed 's/^/  -> /'
else
    echo "  -> Battery telemetry unavailable"
fi

echo "[*] Memory & Storage Vitality:"
free -h | awk 'NR==2{printf "  -> RAM Used: %s / %s (%.2f%%)\n", $3, $2, $3/$2 * 100}'
df -h /data/data/com.termux/files/home | awk 'NR==2{printf "  -> Storage: %s used (%s free)\n", $3, $4}'
echo "====================================================="
