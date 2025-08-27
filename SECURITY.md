
# Data Hygiene & Anonymization

- Remove personal identifiers from prompts and outputs.
- Replace names with synthetic placeholders (e.g., `Client_A`).
- Strip email addresses, phone numbers, account numbers, and addresses.
- If pasting model outputs that include fabricated references, mark them clearly as such.
- Store raw data in `data/raw/` and commit only de-identified excerpts to version control.
