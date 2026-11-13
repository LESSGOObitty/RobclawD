#!/usr/bin/env python3
import hashlib, time
print(hashlib.sha256(str(time.time()).encode()).hexdigest()[:16])
