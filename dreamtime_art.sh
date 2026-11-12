#!/data/data/com.termux/files/usr/bin/bash
# ==============================================================================
# NGAPUHI SPIRAL TANNE & KORI DREAMTIME TELEMETRY ART MATRIX (V2)
# z = z^2 + e^(M_2) with Julia-Mandelbrot Hallet Expansion
# ==============================================================================

clear

C_RED="\033[1;31m"
C_GOLD="\033[1;33m"
C_CYAN="\033[1;36m"
C_GREEN="\033[1;32m"
C_MAGENTA="\033[1;35m"
C_RESET="\033[0m"

echo -e "${C_GOLD}"
echo '     ,ad8888ba,     88                                           88  '
echo '    d8"    `"8b    88                                           88  '
echo '   d8'              88                                           88  '
echo '   88              88  ,adPPYba,  88   ,adPPYba,   88   ,adPPYba,  '
echo '   88              88 a8"     "8a 88  a8"     "8a  88  a8"     "8a '
echo '   Y8,              88 8b       d8 88  8b       d8  88  8b       d8 '
echo '    Y8a.    .a8P    88 "8a,   ,a8" 88  "8a,   ,a8"  88  "8a,   ,a8" '
echo '     `"Y8888Y"'     88  `"YbbdP"'  88   `"YbbdP"'   88   `"YbbdP"'  '
echo -e "${C_RESET}"

echo -e "${C_CYAN}[*] Initializing Ngāpuhi Spiral & Kori Dreamtime State Matrix...${C_RESET}"
echo -e "${C_GREEN}[*] Complex Equation: Z = Z^2 + e^(M_2) + Julia Hallet${C_RESET}"
echo -e "${C_RED}[*] Rendering Fractal Torus & Hallet Field...${C_RESET}\n"

sleep 1

rows=18
cols=64
center_x=32
center_y=9

for ((y=0; y<rows; y++)); do
    line=""
    for ((x=0; x<cols; x++)); do
        dx=$((x - center_x))
        dy=$((y - center_y))
        dist=$(( (dx*dx + dy*dy) ))
        
        # Mandelbrot-Julia Hallet perturbation calculation
        hallet=$(( (dx * dx * 3 - dy * dy * 2 + x * y) % 13 ))
        
        if [ $dist -lt 10 ]; then
            line+="${C_MAGENTA}o${C_RESET}"
        elif [ $dist -lt 25 ] && [ $((hallet % 2)) -eq 0 ]; then
            line+="${C_GOLD}*${C_RESET}"
        elif [ $dist -lt 55 ] && [ $((hallet % 3)) -eq 0 ]; then
            line+="${C_RED}#${C_RESET}"
        elif [ $dist -lt 95 ]; then
            line+="${C_CYAN}~${C_RESET}"
        elif [ $(( (dx * dx + dy * dy + hallet) % 7 )) -eq 0 ]; then
            line+="${C_GREEN}.${C_RESET}"
        else
            line+=" "
        fi
    done
    echo -e "$line"
    sleep 0.04
done

echo -e "\n${C_GOLD}[+] Kori Dreamtime & Julia-Mandelbrot Hallet Matrix Locked.${C_RESET}"
