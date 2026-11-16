#!/usr/bin/env python3
import os
import json
import hashlib
from datetime import datetime, timezone

DOMAIN = "robdoe.com"
REPO_DIR = os.path.expanduser("~/atmospheric-truth-layer")
KDP_OUT = os.path.join(REPO_DIR, "KDP_Publishing_Packets")
os.makedirs(KDP_OUT, exist_ok=True)

def generate_kdp_coloring_book(niche_title="Cozy Hygge Room", page_count=40):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    slug = niche_title.lower().replace(" ", "_")
    book_dir = os.path.join(KDP_OUT, f"{slug}_kdp_pack")
    os.makedirs(book_dir, exist_ok=True)

    print(f"\033[35m========================================================================\033[0m")
    print(f"\033[32m   KDP SOVEREIGN PUBLISHING PIPELINE // NICHE: {niche_title}          \033[0m")
    print(f"\033[35m   ANCHOR: {DOMAIN} | FORMAT: 8.5x8.5 Square | PAGES: {page_count}    \033[0m")
    print(f"\033[35m========================================================================\033[0m")

    # 1. Generate Metadata & Interior Specification Packet
    manifest = {
        "timestamp": ts,
        "organization": "ROBDOE.Inc.Charity",
        "domain": DOMAIN,
        "book_metadata": {
            "title": f"{niche_title}: Bold & Easy Coloring Book for Stress Relief",
            "subtitle": "Cozy, Simple, and Relaxing Illustrations for Adults and Teens",
            "trim_size": "8.5 x 8.5 inches",
            "page_count": page_count,
            "interior_type": "Black & White with White Paper (Single-Sided Bleed Protection)",
            "pricing_strategy": "Optimized KDP Royalty Tier ($9.99+)"
        },
        "sovereign_liquidity_routing": {
            "treasury_pool": "Lymphatic QiDue Automated Flow",
            "intermediary_fees": 0.0,
            "domain_attestation": "Absolute Ownership: robdoe.com"
        }
    }

    # 2. Generate Sample SVG Coloring Page (Bold & Easy Vector Template)
    svg_sample_path = os.path.join(book_dir, "sample_interior_page.svg")
    svg_content = f'''<svg width="816" height="816" viewBox="0 0 816 816" xmlns="http://www.w3.org/2000/svg">
  <rect width="816" height="816" fill="#FFFFFF"/>
  <!-- Bold & Easy Thick Line Art Framework (Optimized for KDP & Markers) -->
  <rect x="100" y="100" width="616" height="616" rx="20" fill="none" stroke="#000000" stroke-width="6"/>
  <!-- Cozy Window Frame -->
  <path d="M 250 200 L 566 200 L 566 500 L 250 500 Z" fill="none" stroke="#000000" stroke-width="5"/>
  <line x1="408" y1="200" x2="408" y2="500" stroke="#000000" stroke-width="4"/>
  <line x1="250" y1="350" x2="566" y2="350" stroke="#000000" stroke-width="4"/>
  <!-- Text Watermark / Domain Anchor -->
  <text x="408" y="750" font-family="Arial" font-size="14" fill="#666666" text-anchor="middle">Published via robdoe.com sovereign pipeline</text>
</svg>'''
    with open(svg_sample_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    # 3. Double-Wrapped SHA-512 Lattice Sponge Seal for the Publishing Packet
    raw_packet = json.dumps(manifest, sort_keys=True).encode("utf-8")
    sponge_seal = hashlib.sha512(hashlib.sha512(raw_packet).digest()).hexdigest()
    manifest["lattice_sha512_sponge_seal"] = sponge_seal

    manifest_path = os.path.join(book_dir, "kdp_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(f"\n\033[32m[+] KDP Publishing Packet Assembled Successfully!\033[0m")
    print(f"\033[33m[+] Interior SVG Template : {svg_sample_path}\033[0m")
    print(f"\033[36m[+] Manifest & Seal       : {manifest_path}\033[0m")
    print(f"\033[32m[+] Lattice Sponge Seal   : {sponge_seal[:32]}...\033[0m")
    print(f"\033[35m========================================================================\033[0m")
    print(f"\033[36mBOOM. Upload interior PDF & cover to KDP, set price, and let liquidity flow.\033[0m")

if __name__ == "__main__":
    generate_kdp_coloring_book("Cozy Corner Aesthetic", 40)
