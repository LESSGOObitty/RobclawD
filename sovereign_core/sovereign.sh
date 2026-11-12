#!/bin/bash
case "$1" in
    bridge)
        python3 "$HOME/sovereign_core/sovereign_unified_bridge.py"
        "$HOME/sovereign_core/sovereign_autocommit.sh"
        ;;
    hud)
        python3 "$HOME/sovereign_core/sovereign_hud.py"
        ;;
    backup)
        "$HOME/sovereign_core/sovereign_backup.sh"
        ;;
    *)
        echo "Usage: ./sovereign.sh {bridge|hud|backup}"
        ;;
esac
