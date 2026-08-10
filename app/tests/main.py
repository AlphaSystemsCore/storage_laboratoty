from pathlib import Path

path = Path("test.bin")

with open(path, "w") as f:
    print(type(f))
    result = f.write("\nhello")
    print(result)