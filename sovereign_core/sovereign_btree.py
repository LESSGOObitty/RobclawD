import os, json, hashlib

BASE_DIR = os.path.expanduser("~")
PROVMARK_DIR = os.path.join(BASE_DIR, ".provmark")
INDEX_PATH = os.path.join(PROVMARK_DIR, "btree_index.json")

class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []     # timestamps or block IDs
        self.values = []   # filenames / pointers
        self.children = [] # child nodes if not leaf

class SovereignBTree:
    def __init__(self, t=2):
        self.root = BTreeNode(leaf=True)
        self.t = t # Minimum degree

    def insert(self, key, value):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode(leaf=False)
            self.root = temp
            temp.children.append(root)
            self._split_child(temp, 0, root)
            self._insert_non_full(temp, key, value)
        else:
            self._insert_non_full(root, key, value)

    def _insert_non_full(self, node, key, value):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            node.values.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                node.values[i + 1] = node.values[i]
                i -= 1
            node.keys[i + 1] = key
            node.values[i + 1] = value
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i, node.children[i])
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key, value)

    def _split_child(self, parent, i, child):
        t = self.t
        z = BTreeNode(leaf=child.leaf)
        yb = child
        parent.children.insert(i + 1, z)
        parent.keys.insert(i, yb.keys[t - 1])
        
        z.keys = yb.keys[t: (2 * t) - 1]
        yb.keys = yb.keys[0: t - 1]
        
        if not yb.leaf:
            z.children = yb.children[t: 2 * t]
            yb.children = yb.children[0: t]
            
        z.values = yb.values[t: (2 * t) - 1]
        yb.values = yb.values[0: t - 1]

    def to_dict(self, node=None):
        if node is None:
            node = self.root
        return {
            "leaf": node.leaf,
            "keys": node.keys,
            "values": node.values,
            "children": [self.to_dict(c) for c in node.children]
        }

def build_and_save_btree():
    print("========================================================================")
    print(" [ROBDOE.COM] BUILDING PROVMARK B-TREE INDEX")
    print("========================================================================")
    
    if not os.path.exists(PROVMARK_DIR):
        print("[!] Provmark vault directory missing.")
        return

    btree = SovereignBTree(t=2)
    files = sorted([f for f in os.listdir(PROVMARK_DIR) if f.endswith('.json') and f != "btree_index.json"])
    
    for file in files:
        path = os.path.join(PROVMARK_DIR, file)
        with open(path, "r") as f:
            try:
                data = json.load(f)
                timestamp = data.get("timestamp", 0)
                btree.insert(timestamp, file)
            except Exception:
                pass
                
    index_data = {
        "engine": "robdoe_btree_v1",
        "indexed_records": len(files),
        "tree": btree.to_dict()
    }
    
    with open(INDEX_PATH, "w") as f:
        json.dump(index_data, f, indent=2)
        
    print(f"[✓] B-Tree index built successfully: {len(files)} records indexed.")
    print(f"[✓] Saved to: {INDEX_PATH}")
    print("========================================================================")

if __name__ == "__main__":
    build_and_save_btree()
