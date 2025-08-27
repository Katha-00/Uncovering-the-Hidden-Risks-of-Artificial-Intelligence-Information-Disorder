
import argparse, json, hashlib, pathlib, datetime, uuid, os

def sha256(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()

def main():
    ap = argparse.ArgumentParser(description="Standardize logging of LLM runs to JSONL.")
    ap.add_argument("--test-case", required=True, choices=["test_case_1","test_case_2","test_case_3"])
    ap.add_argument("--iteration", required=True, choices=["baseline","chain_of_thought","role_based"])
    ap.add_argument("--model", required=True, choices=["chatgpt","deepseek","llama"])
    ap.add_argument("--model-version", required=True)
    ap.add_argument("--prompt-path", required=True, help="Path to the exact prompt file used.")
    ap.add_argument("--temperature", type=float, default=None)
    ap.add_argument("--top-p", type=float, default=None)
    ap.add_argument("--max-tokens", type=int, default=None)
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--response-file", required=True, help="Text file containing the model's raw response.")
    ap.add_argument("--tokens", type=int, default=None)
    ap.add_argument("--latency-ms", type=int, default=None)
    ap.add_argument("--annotator", default="")
    ap.add_argument("--notes", default="")
    args = ap.parse_args()

    record = {
        "id": str(uuid.uuid4()),
        "test_case": args.test_case,
        "iteration": args.iteration,
        "model": args.model,
        "model_version": args.model_version,
        "timestamp_utc": datetime.datetime.utcnow().isoformat() + "Z",
        "prompt_hash_sha256": sha256(args.prompt_path),
        "prompt_path": str(pathlib.Path(args.prompt_path)),
        "params": {
            "temperature": args.temperature,
            "top_p": args.top_p,
            "max_tokens": args.max_tokens,
            "seed": args.seed
        },
        "response": {
            "text": pathlib.Path(args.response_file).read_text(encoding="utf-8"),
            "tokens": args.tokens,
            "latency_ms": args.latency_ms
        },
        "provenance": {
            "interface": "web",
            "annotator": args.annotator,
            "notes": args.notes
        }
    }

    out_dir = pathlib.Path("outputs/jsonl")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.test_case}-{args.iteration}-{args.model}.jsonl"
    with out_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"Wrote: {out_path}")

if __name__ == "__main__":
    main()
