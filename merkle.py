import hashlib, pathlib, sys

files = sorted((pathlib.Path(x) for x in sys.argv[1:]), key=lambda p: str(p))
if not files:
    sys.exit("Usage: python merkle.py FILE [FILE ...]")

nodes = []
for p in files:
    if not p.is_file():
        sys.exit(f"Not a file: {p}")
    h = hashlib.sha256()
    h.update(b"\x00" + p.name.encode() + b"\x00")
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    nodes.append(h.digest())

while len(nodes) > 1:
    if len(nodes) % 2:
        nodes.append(nodes[-1])
    nodes = [
        hashlib.sha256(b"\x01" + nodes[i] + nodes[i + 1]).digest()
        for i in range(0, len(nodes), 2)
    ]

print(nodes[0].hex())
