unsetopt bang_hist
clear
echo "================================================================"
echo " [SYS] AIAGENCY101 // GIT BRANCH & PUSH RECOVERY"
echo " [LOC] ST GEORGE // HURSTVILLE // SOUTH SYDNEY"
echo "================================================================"

# Check current branch
CURRENT_BRANCH=$(git branch --show-current)
echo "[+] Current local branch: $CURRENT_BRANCH"

# If no branch or empty commit history, create initial commit
if [ -z "$CURRENT_BRANCH" ]; then
    echo "[+] Initializing repository and making first commit..."
    git checkout -b main
    git add .
    git commit -m "feat(init): sovereign initial lattice anchor"
else
    echo "[+] Ensuring branch is committed before pushing..."
    git add .
    git commit -m "feat(sync): synchronize local lattice state" || echo "[INFO] No changes to commit."
fi

# Push using the active branch name or default to main/master dynamically
ACTIVE_BRANCH=$(git branch --show-current)
echo "[+] Pushing active branch '$ACTIVE_BRANCH' to remote..."
git push -u origin "$ACTIVE_BRANCH" || git push -u origin HEAD

echo "================================================================"
echo " [STATUS] GIT PUSH RECOVERY SEQUENCE EXECUTED."
echo "================================================================"
