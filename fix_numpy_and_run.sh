unsetopt bang_hist
clear
echo "================================================================"
echo " [SYS] AIAGENCY101 // PIP DEPENDENCY RESOLUTION"
echo " [LOC] ST GEORGE // HURSTVILLE // SOUTH SYDNEY"
echo "================================================================"

echo "[+] Installing numpy & dependencies via pip..."
pip install --upgrade pip
pip install numpy sympy

echo "[+] Re-running fractal manifold engine..."
python3 yum_chow_fractal.sh

echo "================================================================"
echo " [STATUS] DEPENDENCY INGESTION COMPLETE."
echo "================================================================"
