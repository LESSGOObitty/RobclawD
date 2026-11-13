#!/usr/bin/env python3
import sys
import json
import statistics

BLOCK_DATA = [
    {"block": 26405078, "tx": 233, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405079, "tx": 300, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405080, "tx": 265, "miner": "0x396343362be2a4da1ce0c1c210945346fb82aa49"},
    {"block": 26405081, "tx": 94,  "miner": "0x155a59fd6bd7839a0c9b1d3f56fdd4d8784897ac"},
    {"block": 26405082, "tx": 386, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405083, "tx": 334, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405084, "tx": 128, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405085, "tx": 191, "miner": "0xfb74767c1ce1aada0a0e114441173b57f8c1571b"},
    {"block": 26405086, "tx": 461, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405087, "tx": 242, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405088, "tx": 222, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405089, "tx": 300, "miner": "0x396343362be2a4da1ce0c1c210945346fb82aa49"},
    {"block": 26405090, "tx": 102, "miner": "0x4231b2f83cb7c833db84cec0ceaaa9959f051374"},
    {"block": 26405091, "tx": 360, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405092, "tx": 316, "miner": "0x396343362be2a4da1ce0c1c210945346fb82aa49"},
    {"block": 26405093, "tx": 222, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405094, "tx": 447, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405095, "tx": 163, "miner": "0xf22e098cb0d6c24d88ab79c1ce87b73ea26e608f"},
    {"block": 26405096, "tx": 418, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405097, "tx": 232, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405098, "tx": 262, "miner": "0x396343362be2a4da1ce0c1c210945346fb82aa49"},
    {"block": 26405099, "tx": 298, "miner": "0x396343362be2a4da1ce0c1c210945346fb82aa49"},
    {"block": 26405100, "tx": 232, "miner": "0xdadb0d80178819f2319190d340ce9a924f783711"},
    {"block": 26405101, "tx": 85,  "miner": "0x33209ffd1e01930b24ab50015eacb911c7fa7aa3"},
    {"block": 26405102, "tx": 148, "miner": "0x388c818ca8b9251b393131c08a736a67ccb19297"},
    {"block": 26405103, "tx": 503, "miner": "0x396343362be2a4da1ce0c1c210945346fb82aa49"},
    {"block": 26405104, "tx": 283, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405105, "tx": 205, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405106, "tx": 70,  "miner": "0xfb74767c1ce1aada0a0e114441173b57f8c1571b"},
    {"block": 26405107, "tx": 475, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405108, "tx": 378, "miner": "0x396343362be2a4da1ce0c1c210945346fb82aa49"},
    {"block": 26405109, "tx": 142, "miner": "0x5535d0da686a6dd8e64059c367e2e1062bc327ce"},
    {"block": 26405110, "tx": 125, "miner": "0x512ba2e9c4f2f4842af667137dd14a98181d97f6"},
    {"block": 26405111, "tx": 333, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405112, "tx": 415, "miner": "0xdadb0d80178819f2319190d340ce9a924f783711"},
    {"block": 26405113, "tx": 259, "miner": "0x396343362be2a4da1ce0c1c210945346fb82aa49"},
    {"block": 26405114, "tx": 312, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405115, "tx": 214, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405116, "tx": 176, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405117, "tx": 337, "miner": "0x396343362be2a4da1ce0c1c210945346fb82aa49"},
    {"block": 26405118, "tx": 260, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405119, "tx": 326, "miner": "0xdadb0d80178819f2319190d340ce9a924f783711"},
    {"block": 26405120, "tx": 247, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405121, "tx": 231, "miner": "0xfb74767c1ce1aada0a0e114441173b57f8c1571b"},
    {"block": 26405122, "tx": 281, "miner": "0xdadb0d80178819f2319190d340ce9a924f783711"},
    {"block": 26405123, "tx": 332, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405124, "tx": 327, "miner": "0x396343362be2a4da1ce0c1c210945346fb82aa49"},
    {"block": 26405125, "tx": 342, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"},
    {"block": 26405126, "tx": 227, "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97"}
]

def analyze():
    tx_counts = [b["tx"] for b in BLOCK_DATA]
    total_blocks = len(BLOCK_DATA)
    total_tx = sum(tx_counts)
    mean_tx = statistics.mean(tx_counts)
    median_tx = statistics.median(tx_counts)
    stdev_tx = statistics.pstdev(tx_counts)
    
    min_block = min(BLOCK_DATA, key=lambda x: x["tx"])
    max_block = max(BLOCK_DATA, key=lambda x: x["tx"])
    
    min_span = BLOCK_DATA[0]["block"]
    max_span = BLOCK_DATA[-1]["block"]
    
    miners = {}
    for b in BLOCK_DATA:
        m = b["miner"]
        miners[m] = miners.get(m, 0) + 1
        
    sorted_miners = sorted(miners.items(), key=lambda x: x[1], reverse=True)
    
    report = {
        "span_blocks": f"#{min_span} to #{max_span}",
        "total_blocks": total_blocks,
        "total_transactions": total_tx,
        "metrics": {
            "mean_tx_per_block": round(mean_tx, 2),
            "median_tx_per_block": median_tx,
            "standard_deviation": round(stdev_tx, 2),
            "min_transactions": {"block": min_block["block"], "tx": min_block["tx"]},
            "max_transactions": {"block": max_block["block"], "tx": max_block["tx"]}
        },
        "miner_distribution": [{"miner": m, "blocks_won": count, "share_pct": round((count / total_blocks) * 100, 2)} for m, count in sorted_miners]
    }
    print(json.dumps(report))

if __name__ == "__main__":
    analyze()
