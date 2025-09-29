# Uncovering the Hidden Risks of Artificial Intelligence: Information Disorder

This repository accompanies the master’s thesis *Uncovering the Hidden Risks of Artificial Intelligence: Information Disorder*.  
It collects all experiment materials: prompts, raw outputs from large language models (LLMs), and predefined evaluation rubrics.

---

## Repository Contents

- **prompts/**  
  Exact input prompts, organized by test case and prompting strategy (baseline, chain-of-thought, role-based).

- **experiments/**  
  Raw outputs from the evaluated LLMs, structured by  
  `experiments/<test_case>/<strategy>/models/<model>/`.  
  Each output file is named to reflect its test case, strategy, model, and run number/date.

- **evaluation/**  
  - Global rubric: `rubric.csv` (dimensions: factual accuracy, timeliness, contextual relevance).  
  - Case-specific rubrics:  
    - `rubrics/test_case_1_rubric.md`  
    - `rubrics/test_case_2_rubric.md`  
    - `rubrics/test_case_3_rubric.md`  

- **metadata/**  
  JSON schema describing the structure for standardized experiment records.

- **scripts/**  
  Helper scripts used during data collection (not required for navigation).

- **data/**  
  Optional storage for raw or processed supplementary material (not central to this thesis).

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

---

## Navigation Guide

- To see **prompts used** → check `prompts/`.  
- To see **raw model answers** → check `experiments/`.  
- To see **evaluation criteria** → check `evaluation/rubrics/`.   

---

## License & Citation

- Licensed under MIT (see `LICENSE`).  
- If you use or adapt this material, please cite the master’s thesis (see `CITATION.cff`).  
