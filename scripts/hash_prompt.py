
import hashlib, sys, pathlib
p = pathlib.Path(sys.argv[1])
data = p.read_bytes()
print(hashlib.sha256(data).hexdigest())
