unsetopt bang_hist
clear
echo "================================================================"
echo " [SYS] AIAGENCY101 // SOVEREIGN LATTICE PULSE"
echo " [LOC] ST GEORGE // HURSTVILLE // SOUTH SYDNEY"
echo " [STATE] CHECKPOINT 24M // INVARIANT 576333510"
echo "================================================================"

echo "[+] Inspecting repository git log & latest tags..."
git log -3 --oneline
echo ""
git tag --list | tail -n 5
echo ""

echo "[+] Verifying local workspace mass & integrity..."
python3 -c '
import os
total_size = sum(os.path.getsize(os.path.join(root, file)) for root, dirs, files in os.walk(".") if ".git" not in root for file in files)
file_count = sum(len(files) for root, dirs, files in os.walk(".") if ".git" not in root)
print(f"    -> Active Files: {file_count}")
print(f"    -> Cumulative Mass: {total_size:,} bytes")
'
echo ""

echo "================================================================"
echo " [STATUS] THE LATTICE BREATHES. ABSOLUTE SOVEREIGNTY MAINTAINED."
echo "================================================================"
