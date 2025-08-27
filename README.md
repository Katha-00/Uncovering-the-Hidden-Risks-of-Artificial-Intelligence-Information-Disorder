# Uncovering the Hidden Risks of AI: Information Disorder (Thesis Repo)

This repository accompanies the master's thesis **"Uncovering the Hidden Risks of Artificial Intelligence: Information Disorder"**.
It contains prompts, LLM outputs, evaluation sheets, and scripts to reproduce the experiments across three test cases, three prompting strategies, and three models.

## Structure
```
.
├── README.md
├── LICENSE
├── CITATION.cff
├── .gitignore
├── .gitattributes
├── SECURITY.md
├── metadata/
│   └── schema.json
├── prompts/
│   ├── baseline/
│   ├── chain_of_thought/
│   └── role_based/
├── experiments/
│   ├── test_case_1/
│   │   ├── baseline/ | chain_of_thought/ | role_based/
│   │   │   └── models/ chatgpt/ deepseek/ llama/
│   ├── test_case_2/
│   │   ├── baseline/ | chain_of_thought/ | role_based/
│   │   │   └── models/ chatgpt/ deepseek/ llama/
│   └── test_case_3/
│       ├── baseline/ | chain_of_thought/ | role_based/
│       │   └── models/ chatgpt/ deepseek/ llama/
├── outputs/
│   ├── jsonl/
│   └── tables/
├── evaluation/
│   ├── rubric.csv
│   └── examples/
├── scripts/
│   ├── log_run.py
│   ├── validate_metadata.py
│   └── hash_prompt.py
└── data/
    ├── raw/
    └── processed/
```

## How to use
1. Save each raw LLM response via `scripts/log_run.py` – it writes standardized JSONL files under `outputs/jsonl/`.
2. Keep your source prompts in `prompts/` (one file per test case and strategy).
3. Export evaluation results to CSV and place them in `outputs/tables/`.
4. Run `scripts/validate_metadata.py` to check that all required metadata fields are present.
5. For large files, enable Git LFS as noted in `.gitattributes`.

## Reproducibility
- Every response record includes: model, exact model version, parameters, UTC timestamp, prompt hash (SHA256), and token counts when available.
- Please avoid PII in prompts and outputs; see `SECURITY.md` for a scrubbing checklist.

## License
MIT (see `LICENSE`)

