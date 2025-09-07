# Uncovering the Hidden Risks of Artificial Intelligence: Information Disorder

This repository accompanies the master’s thesis *Uncovering the Hidden Risks of Artificial Intelligence: Information Disorder*.  
It collects the materials used in the experimental study, including prompts, raw outputs from large language models (LLMs), and predefined evaluation rubrics.

---

## Repository Contents

- **prompts/**  
  Exact input prompts, organized by test case and prompting strategy (baseline, chain-of-thought, role-based).

- **experiments/**  
  Raw outputs from the evaluated LLMs, structured by test case → strategy → model (ChatGPT, DeepSeek, LLaMA).

- **evaluation/**  
  - Global rubric: `rubric.csv` (dimensions of factual accuracy, timeliness, and contextual relevance).  
  - Case-specific rubrics: `rubrics/test_case_1_rubric.md`, `test_case_2_rubric.md`, `test_case_3_rubric.md`.  
  - Example evaluations: `examples/`.

- **outputs/**  
  Processed or aggregated results, e.g. CSV or JSONL summaries.

- **metadata/**  
  JSON schema describing the structure for standardized experiment records.

- **scripts/**  
  Helper scripts used during data collection (not required for repository navigation).

- **data/**  
  Optional storage for raw or processed supplementary files (currently not central to this thesis).

---

## Experiment Design

- **Test Cases**
  1. **Retirement planning** (Austrian pension system context)  
  2. **Risk-based portfolio construction** (mid-career investor)  
  3. **Crisis-driven investment behavior**

- **Prompting Strategies**  
  - Baseline  
  - Chain-of-thought  
  - Role-based  

- **Models Evaluated**  
  - ChatGPT  
  - DeepSeek  
  - LLaMA  

Each LLM output file is named systematically to reflect its test case, strategy, model, and run number/date.

---

## Navigation Guide

- To see **what was asked** → check `prompts/`.  
- To see **raw answers** from the LLMs → check `experiments/`.  
- To see **how answers were evaluated** → check `evaluation/rubrics/` (criteria) and `evaluation/examples/` (scored examples).  
- To see **summarized results** → check `outputs/`.  

---

## License & Citation

- Licensed under MIT (see `LICENSE`).  
- If you use or adapt this material, please cite the master’s thesis (see `CITATION.cff`).  
