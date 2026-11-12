#!/usr/bin/env python3
import json
import hashlib

def keccak256(data: bytes) -> bytes:
    return hashlib.sha3_256(data).digest()

# Australian NEM Regional Fuel & Capacity State (MW Baseline)
NEM_BUSES = {
    "NSW1": {"region": "New South Wales", "v_nom": 330, "lat": -33.8688, "lon": 151.2093},
    "VIC1": {"region": "Victoria", "v_nom": 500, "lat": -37.8136, "lon": 144.9631},
    "QLD1": {"region": "Queensland", "v_nom": 330, "lat": -27.4705, "lon": 153.0260},
    "SA1":  {"region": "South Australia", "v_nom": 275, "lat": -34.9285, "lon": 138.6007},
    "TAS1": {"region": "Tasmania", "v_nom": 220, "lat": -42.8821, "lon": 147.3272}
}

GENERATOR_UNITS = [
    {"name": "Bayswater_Coal", "bus": "NSW1", "p_nom": 2640, "carrier": "coal"},
    {"name": "Snowy_Hydro", "bus": "NSW1", "p_nom": 4100, "carrier": "hydro"},
    {"name": "Darlington_Point_Solar", "bus": "NSW1", "p_nom": 333, "carrier": "solar"},
    {"name": "Loy_Yang_Coal", "bus": "VIC1", "p_nom": 2210, "carrier": "coal"},
    {"name": "MacIntyre_Wind", "bus": "QLD1", "p_nom": 1026, "carrier": "wind"},
    {"name": "Hornsdale_Power_Reserve", "bus": "SA1", "p_nom": 150, "carrier": "battery"}
]

TRANSMISSION_INTERCONNECTORS = [
    {"name": "VNI_NSW_VIC", "bus0": "NSW1", "bus1": "VIC1", "s_nom": 1600},
    {"name": "QNI_NSW_QLD", "bus0": "NSW1", "bus1": "QLD1", "s_nom": 1200},
    {"name": "Heywood_VIC_SA", "bus0": "VIC1", "bus1": "SA1", "s_nom": 850},
    {"name": "Basslink_VIC_TAS", "bus0": "VIC1", "bus1": "TAS1", "s_nom": 500}
]

def build_nem_state_hashes():
    leaves = []
    # Hash network topology components into B-Tree leaves
    for b_id, b_data in NEM_BUSES.items():
        leaves.append(keccak256(f"BUS_{b_id}_{b_data['v_nom']}".encode()))
    for gen in GENERATOR_UNITS:
        leaves.append(keccak256(f"GEN_{gen['name']}_{gen['bus']}_{gen['p_nom']}".encode()))
    for line in TRANSMISSION_INTERCONNECTORS:
        leaves.append(keccak256(f"LINE_{line['name']}_{line['s_nom']}".encode()))
    return leaves

def build_merkle_root(leaves):
    if len(leaves) % 2 != 0:
        leaves.append(leaves[-1])
    current = leaves
    while len(current) > 1:
        next_layer = []
        for i in range(0, len(current), 2):
            l, r = current[i], current[i+1]
            pair = keccak256(l + r) if l < r else keccak256(r + l)
            next_layer.append(pair)
        current = next_layer
    return current[0]

if __name__ == "__main__":
    nem_leaves = build_nem_state_hashes()
    nem_root = build_merkle_root(nem_leaves)
    
    sealed_tag = "SHA1296000ARC"
    
    grid_manifest = {
        "tag": sealed_tag,
        "aus_nem_state_root": f"0x{nem_root.hex()}",
        "buses_count": len(NEM_BUSES),
        "generators_count": len(GENERATOR_UNITS),
        "interconnectors_count": len(TRANSMISSION_INTERCONNECTORS),
        "primary_bus": "NSW1 (Sydney Grid Zone)"
    }
    
    print("==================================================")
    print("       AUSTRALIAN NEM POWER GRID MERKLE BINDING   ")
    print("==================================================")
    print(json.dumps(grid_manifest, indent=2))

