
import json, sys, jsonschema, pathlib

SCHEMA_PATH = pathlib.Path("metadata/schema.json")
schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

def validate_file(path):
    ok, n = True, 0
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line: 
                continue
            try:
                obj = json.loads(line)
                jsonschema.validate(obj, schema)
                n += 1
            except Exception as e:
                ok = False
                print(f"[ERROR] {path}:{i}: {e}")
    print(f"{'OK' if ok else 'FAILED'} — validated {n} records in {path}")

def main():
    files = sys.argv[1:] or list(pathlib.Path("outputs/jsonl").glob("*.jsonl"))
    if not files:
        print("No files to validate.")
        return
    for f in files:
        validate_file(str(f))

if __name__ == "__main__":
    main()
