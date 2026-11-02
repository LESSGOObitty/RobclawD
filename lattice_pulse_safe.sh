unsetopt bang_hist
clear
echo "================================================================"
echo " [SYS] AIAGENCY101 // SOVEREIGN LATTICE PULSE (SAFE OS.WALK)"
echo " [LOC] ST GEORGE // HURSTVILLE // SOUTH SYDNEY"
echo " [STATE] CHECKPOINT 24M // INVARIANT 576333510"
echo "================================================================"

python3 -c '
import os

total_size = 0
file_count = 0
skip_dirs = {".git", "storage"}

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in skip_dirs]
    for file in files:
        filepath = os.path.join(root, file)
        try:
            if os.path.exists(filepath) and not os.path.islink(filepath):
                total_size += os.path.getsize(filepath)
                file_count += 1
        except Exception:
            pass

print(f"    -> Active Files (Excluding Storage): {file_count}")
print(f"    -> Cumulative Lattice Mass: {total_size:,} bytes")
'

echo "================================================================"
echo " [STATUS] BOUNDARY ENFORCED. LATTICE TRAVERSAL CLEAN."
echo "================================================================"
