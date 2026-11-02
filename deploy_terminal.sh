#!/data/data/com.termux/files/usr/bin/bash
# ==============================================================================
# TERMUX SINGLE-CANVAS CONSOLED RADAR v23.0 (HYPER-STABLE LATENCY FIX)
# ==============================================================================

set -euo pipefail

# --- 1. PROVISIONING CONFIGURATION CHECK ---
pkg update -y
pkg install bc curl jq -y > /dev/null 2>&1

# --- 2. SINGLE SURFACE MONITOR LOOP ---
clear
while true; do
    # Instant raw canvas reset using ANSI terminal cursor homing
    printf "\033[H\033[J"
    
    echo -e "\e[90m┌──────────────────────────────────────────────────────────────────────────────────────┐\e[0m"
    echo -e "\e[90m│\e[0m \e[1;37mCHON INTEGRATED NETWORK SYSTEM v23.0\e[0m  \e[32m[ RUNTIME NOMINAL ]\e[0m                     \e[93m$(date +%H:%M:%S)\e[0m \e[90m│\e[0m"
    echo -e "\e[90m├──────────────────────────────────────────────────────────────────────────────────────┤\e[0m"

    # --- BLOCK 0: MULTI-KEY WALLET LEDGER & 4% ALLOCATION WEIGHTS ---
    echo -e "\e[90m│\e[0m \e[1;35m[ MULTI-CHAIN QUANT REGISTER: 96%% MATTER // 4%% ME ALLOCATION ]\e[0m                      \e[90m│\e[0m"
    
    # Linear stagger pacing avoids Etherscan public API rate-limit throttling
    res1=$(curl -s --max-time 1 'https://etherscan.io') || echo "{}"
    sleep 0.25
    res2=$(curl -s --max-time 1 'https://etherscan.io') || echo "{}"
    sleep 0.25
    res3=$(curl -s --max-time 1 'https://etherscan.io') || echo "{}"
    sleep 0.25

    # Safe validation parsing extraction guards
    b1=$(echo "$res1" | jq -r '.result' 2>/dev/null || echo "0")
    b2=$(echo "$res2" | jq -r '.result' 2>/dev/null || echo "0")
    b3=$(echo "$res3" | jq -r '.result' 2>/dev/null || echo "0")

    # Gracefully hold state instead of throwing structural shell errors
    [[ "$b1" == *"Max rate limit"* || -z "$b1" || "$b1" == "null" ]] && b1=0
    [[ "$b2" == *"Max rate limit"* || -z "$b2" || "$b2" == "null" ]] && b2=0
    [[ "$b3" == *"Max rate limit"* || -z "$b3" || "$b3" == "null" ]] && b3=0

    e1=$(echo "scale=4; $b1 / 1000000000000000000" | bc 2>/dev/null || echo "0.0000")
    e2=$(echo "scale=4; $b2 / 1000000000000000000" | bc 2>/dev/null || echo "0.0000")
    e3=$(echo "scale=4; $b3 / 1000000000000000000" | bc 2>/dev/null || echo "0.0000")
    
    cut1=$(echo "scale=4; $e1 * 0.04" | bc 2>/dev/null || echo "0.0000")
    cut2=$(echo "scale=4; $e2 * 0.04" | bc 2>/dev/null || echo "0.0000")
    cut3=$(echo "scale=4; $e3 * 0.04" | bc 2>/dev/null || echo "0.0000")
    
    printf "\e[90m│\e[0m  ┠ ACC_1 [..c2018]: \e[1;37m%8s ETH\e[0m │ 96%% Matter: \e[90m%8s\e[0m │ 4%% Me: \e[1;32m%8s ETH\e[0m  \e[90m│\e[0m\n" "$e1" "$(echo "scale=4; $e1 * 0.96" | bc 2>/dev/null)" "$cut1"
    printf "\e[90m│\e[0m  ┠ ACC_2 [..7Cffc]: \e[1;37m%8s ETH\e[0m │ 96%% Matter: \e[90m%8s\e[0m │ 4%% Me: \e[1;32m%8s ETH\e[0m  \e[90m│\e[0m\n" "$e2" "$(echo "scale=4; $e2 * 0.96" | bc 2>/dev/null)" "$cut2"
    printf "\e[90m│\e[0m  ┠ ACC_3 [..2D1D9]: \e[1;37m%8s ETH\e[0m │ 96%% Matter: \e[90m%8s\e[0m │ 4%% Me: \e[1;32m%8s ETH\e[0m  \e[90m│\e[0m\n" "$e3" "$(echo "scale=4; $e3 * 0.96" | bc 2>/dev/null)" "$cut3"
    echo -e "\e[90m├──────────────────────────────────────────────────────────────────────────────────────┤\e[0m"

    # --- BLOCK 1: FLOW EVM REAL-TIME INTEGRATION ---
    echo -e "\e[90m│\e[0m \e[1;32m[ INTEGRATED FLOW EVM REGISTRY ]\e[0m                                                      \e[90m│\e[0m"
    raw_hex=$(curl -s --max-time 1 -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBalance","params":["0x84CA4603B64b0b1C8EF90eC90Cc30e5A285c2018", "latest"],"id":1}' https://onflow.org | jq -r '.result' 2>/dev/null || echo "0x0")
    if [ -n "$raw_hex" ] && [ "$raw_hex" != "null" ] && [ "$raw_hex" != "0x" ]; then
        wei_val=$(printf "%d" "$raw_hex" 2>/dev/null || echo "0")
        flow_bal=$(echo "scale=4; $wei_val / 1000000000000000000" | bc 2>/dev/null || echo "0.0000")
    else
        flow_bal="0.0000"
    fi
    printf "\e[90m│\e[0m  ┠ ACC_1 Native Flow Vector State ➜ \e[1;32m%s FLOW\e[0m                                           \e[90m│\e[0m\n" "$flow_bal"
    echo -e "\e[90m├──────────────────────────────────────────────────────────────────────────────────────┤\e[0m"

    # --- BLOCK 2: SOVEREIGN DEED ARCHITECTURE ---
    echo -e "\e[90m│\e[0m \e[1;34m[ SOVEREIGN ENTRY REGISTRY ]\e[0m                                                          \e[90m│\e[0m"
    manifest="/data/data/com.termux/files/home/robdoerootauthority/atmospheric-truth-layer/icann_sovereign_tlds/tld_manifest.json"
    if [ -f "$manifest" ]; then
        jq -r '.deeds | to_entries[] | "  ┠ \(.key) ➜ \(.value)"' "$manifest" | paste - - - - | while read -r line; do
            printf "\e[90m│\e[0m %-84s \e[90m│\e[0m\n" "$line"
        done
    else
        echo -e "\e[90m│\e[0m  ┠ Synchronizing root anchor state..."
    fi
    echo -e "\e[90m├──────────────────────────────────────────────────────────────────────────────────────┤\e[0m"

    # --- BLOCK 3: QUAD-TARGET ECOSYSTEM FEED WITH UNIQUE TIME BOUNDS ---
    echo -e "\e[90m│\e[0m \e[1;33m[ INGESTION NETWORK LATENCY PARAMETERS ]\e[0m                                              \e[90m│\e[0m"
    
    # Target 1: Ethereum
    t1_s=$(date +%s%N)
    curl -s --max-time 1 'https://etherscan.io' > /dev/null || true
    t1_e=$(date +%s%N)
    l_eth=$(echo "scale=1; ($t1_e - $t1_s) / 1000000" | bc 2>/dev/null || echo "0.0")
    sleep 0.1

    # Target 2: Solana
    t2_s=$(date +%s%N)
    curl -s --max-time 1 -X POST -H 'Content-Type: application/json' -d '{"jsonrpc":"2.0","id":1,"method":"getHealth"}' https://solana.com > /dev/null || true
    t2_e=$(date +%s%N)
    l_sol=$(echo "scale=1; ($t2_e - $t2_s) / 1000000" | bc 2>/dev/null || echo "0.0")
    sleep 0.1

    # Target 3: Base
    t3_s=$(date +%s%N)
    curl -s --max-time 1 -X POST -H 'Content-Type: application/json' -d '{"jsonrpc":"2.0","id":1,"method":"eth_blockNumber"}' https://base.org > /dev/null || true
    t3_e=$(date +%s%N)
    l_base=$(echo "scale=1; ($t3_e - $t3_s) / 1000000" | bc 2>/dev/null || echo "0.0")
    sleep 0.1

    # Target 4: Arbitrum
    t4_s=$(date +%s%N)
    curl -s --max-time 1 -X POST -H 'Content-Type: application/json' -d '{"jsonrpc":"2.0","id":1,"method":"eth_blockNumber"}' https://arbitrum.io > /dev/null || true
    t4_e=$(date +%s%N)
    l_arb=$(echo "scale=1; ($t4_e - $t4_s) / 1000000" | bc 2>/dev/null || echo "0.0")

    printf "\e[90m│\e[0m  ETH Node: \e[1;36m%5.1fms\e[0m │ SOL Node: \e[1;36m%5.1fms\e[0m │ BASE Node: \e[1;36m%5.1fms\e[0m │ ARB Node: \e[1;36m%5.1fms\e[0m     \e[90m│\e[0m\n" "$l_eth" "$l_sol" "$l_base" "$l_arb"
    echo -e "\e[90m├──────────────────────────────────────────────────────────────────────────────────────┤\e[0m"

    # --- BLOCK 4: LOCAL SYSTEM EQUILIBRIUM ---
    echo -e "\e[90m│\e[0m \e[1;36m[ SYSTEM EQUILIBRIUM INVARIANT STATUS ]\e[0m                                              \e[90m│\e[0m"
    if [ -f live_liquidity_state.json ]; then
        inv=$(jq -r '.liquidity_data.invariant_base' live_liquidity_state.json)
        seal=$(jq -r '.hyper_seal[0:24]' live_liquidity_state.json)
        printf "\e[90m│\e[0m  Invariant Baseline :: \e[1;37m%-61s\e[0m \e[90m│\e[0m\n" "$inv"
        printf "\e[90m│\e[0m  Hyper Torque Seal  :: \e[1;30m%-61s\e[0m \e[90m│\e[0m\n" "$seal..."
    else
        printf "\e[90m│\e[0m  Equilibrium Formula :: \e[1;30m%-61s\e[0m \e[90m│\e[0m\n" "Z = Z² + eM²"
    fi
    echo -e "\e[90m└──────────────────────────────────────────────────────────────────────────────────────┘\e[0m"
    echo " [CTRL+C] to escape monitor loop and release terminal shell control down to bash."
    sleep 3
done
