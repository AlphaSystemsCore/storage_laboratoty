# from pathlib import Path

# path = Path("test.bin")

# with open(path, "w") as f:
#     print(type(f))
#     result = f.write("\nhello")
#     print(result)

import hashlib
sha512 = hashlib.sha3_512()
hash = sha512.update(b"I love Germany")
print(sha512.hexdigest())

