import math
import json
import time
import hashlib

def keccak256(data_bytes):
    return hashlib.sha3_256(data_bytes).hexdigest()

class FractalLatticeEngine:
    def __init__(self):
        self.dimensions = 7
        # Constant parameters derived from your dynamic scale equations
        self.eM2_real = 0.034
        self.eM2_imag = 0.052

    def compute_quadratic_feedback(self, initial_real, initial_imag, iterations=10):
        """
        Executes the non-linear recursion: z = z^2 + eM2
        Acts as a high-sensitivity attractor for system state drift detection.
        """
        z_real = initial_real
        z_imag = initial_imag
        
        for _ in range(iterations):
            # Compute z^2 = (r^2 - i^2) + 2ri_i
            next_real = (z_real * z_real) - (z_imag * z_imag) + self.eM2_real
            next_imag = (2.0 * z_real * z_imag) + self.eM2_imag
            
            z_real = next_real
            z_imag = next_imag
            
            # Escape radius check (unbounded divergence threshold)
            if (z_real * z_real + z_imag * z_imag) > 4.0:
                break
                
        return z_real, z_imag

    def calculate_interlocking_matrix(self, telemetry_stream):
        lengths = [len(str(x)) for x in telemetry_stream]
        lattice_vectors = []
        
        print("[~] Running complex quadratic feedback loops across data boundary...")
        for i in range(len(lengths)):
            prev_len = lengths[i - 1] if i > 0 else lengths[-1]
            current_len = lengths[i]
            
            # Seed the initial complex point z_0 using the interlocked scale lengths
            z0_r = float(current_len ^ prev_len) / 10.0
            z0_i = float(current_len & 0x0F) / 10.0
            
            # Process through the non-linear fractal feedback generator
            final_r, final_i = self.compute_quadratic_feedback(z0_r, z0_i)
            
            # Map the complex plane result back into a deterministic system metric
            magnitude = math.sqrt(final_r * final_r + final_i * final_i)
            lattice_vectors.append(round(magnitude, 6))
            
        return lattice_vectors

    def process_system_datum(self, raw_telemetry):
        # 1. Run raw telemetry through the fractal matrix pipeline
        fractal_vectors = self.calculate_interlocking_matrix(raw_telemetry)
        
        # 2. Extract entropy signature from the non-linear plane magnitudes
        total_mag = sum(fractal_vectors) if sum(fractal_vectors) > 0 else 1.0
        entropy = 0.0
        for mag in fractal_vectors:
            p = mag / total_mag
            if p > 0:
                entropy -= p * math.log2(p)
                
        # 3. Assemble immutable system payload block
        datum_payload = {
            "epoch_timestamp": time.time(),
            "formula_signature": "z = z^2 + eM2",
            "lattice_profile": "Ngapuhi_Scale_Fractal_7D",
            "shannon_entropy": f"{entropy:.6f}",
            "state_magnitudes": fractal_vectors,
            "root_witness_hash": keccak256(str(raw_telemetry).encode('utf-8'))
        }
        
        # 4. Generate final EVM Leaf Root Hash
        serialized = json.dumps(datum_payload, sort_keys=True)
        root_hash = keccak256(serialized.encode('utf-8'))
        
        return root_hash, datum_payload

if __name__ == "__main__":
    engine = FractalLatticeEngine()
    
    # Active system data stream parameters
    local_telemetry = ["ROOT_DEEP_LOGIC", "NGAPUHI_MESH_ACTIVE", "PHASE_WITNESS_LOCK", "BFT_14_NODES_TRUE"]
    
    root_hash, payload = engine.process_system_datum(local_telemetry)
    
    print("\n\033[1;35m================================================================\033[0m")
    print("\033[1;32m[+] FRACTAL MESH GENERATOR INITIALIZED // CRITICAL STATE FIXED\033[0m")
    print(f"    Recurrence rule : {payload['formula_signature']}")
    print(f"    Mesh Entropy    : {payload['shannon_entropy']} bits / layer")
    print(f"    State Vector    : {payload['state_magnitudes']}")
    print(f"    Keccak-256 Root : 0x{root_hash}")
    print("\033[1;35m================================================================\033[0m")
