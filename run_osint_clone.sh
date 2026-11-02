unsetopt bang_hist
clear
echo "================================================================"
echo " [SYS] AIAGENCY101 // MOTOTERMUX OSINT INJECTION PIPELINE"
echo " [LOC] ST GEORGE // HURSTVILLE // SOUTH SYDNEY"
echo "================================================================"

# Corrected target configuration (Example target placeholder)
WORKSPACE="$HOME/Matrix/OSINT_Lab"
TARGET_REPO="https://github.com/backupsonbackupsrobby-cyber/robdoerootauthority.git"

REPO_NAME=$(basename "$TARGET_REPO" .git)
TARGET_FOLDER="$WORKSPACE/$REPO_NAME"

echo "[INIT] Target Repo: $TARGET_REPO"
echo "[INIT] Target Folder: $TARGET_FOLDER"

if [ -d "$TARGET_FOLDER" ]; then
    echo "[CLEAN] Wiping legacy tracking database block: $REPO_NAME"
    rm -rf "$TARGET_FOLDER"
fi

mkdir -p "$WORKSPACE"
cd "$WORKSPACE"

echo "[ROBDOISNT] Injecting git clone instruction..."
git clone --quiet "$TARGET_REPO"

if [ -d "$TARGET_FOLDER" ]; then
    echo "[SUCCESS] Data block fully cloned to local storage."
    echo "[HYBRID LOCK] Matrix directory anchored: $TARGET_FOLDER"
else
    echo "[FATAL] Transmission completed but target path mapping failed."
    exit 1
fi
