unsetopt bang_hist
clear
echo "================================================================"
echo " [SYS] AIAGENCY101 // GIT PUSH RECOVERY"
echo " [LOC] ST GEORGE // HURSTVILLE // SOUTH SYDNEY"
echo "================================================================"

echo "[+] Checking local git status and commit log..."
git status -s
git log -1 --oneline
echo ""

echo "[+] Pushing master with explicit upstream tracking..."
git push --set-upstream origin master --tags

echo "================================================================"
echo " [STATUS] RECOVERY SEQUENCE EXECUTED."
echo "================================================================"
