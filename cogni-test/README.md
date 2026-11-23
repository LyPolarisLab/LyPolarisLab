# COGNI-TEST

Evaluation protocol for LLM cognitive capabilities — how do large language models express uncertainty, detect contradictions, and revise their responses?

**Status**: Protocol designed, implementation in progress.

---

## Research question

> How do LLMs express uncertainty, detect conflicting information, and revise their responses when prompted to re-examine?

## Hypotheses

- **H1**: LLMs detect explicit contradictions more reliably than implicit ones
- **H2**: Longer, more complex prompts reduce contradiction detection accuracy
- **H3**: LLMs express uncertainty through hedging language rather than explicit probability statements
- **H4**: Guided correction prompts yield better revision than neutral re-examination

## Experimental design

### Phase A — Scenario construction
30–50 test scenarios across 4 categories:
- Explicit contradictions
- Implicit contradictions
- Coherent controls (no contradiction)
- Insufficient information

### Phase B — 2×2 factorial design

|  | Short prompt | Long prompt |
|--|--|--|
| **With contradiction** | Condition A | Condition B |
| **Without contradiction** | Condition C | Condition D |

### Phase C — Evaluation conditions
Each scenario is tested under 3 conditions:
1. **Initial response** — baseline
2. **Neutral re-examination** — "Are you sure?"
3. **Guided correction** — pointing to the contradictory elements

## Metrics

- F1 score, precision, recall for contradiction detection
- Confusion matrices per condition
- Uncertainty expression categorization (hedging, explicit probability, refusal)
- Revision quality scoring

## Stack

Python · LLM API · Pandas · Matplotlib · scikit-learn

## Structure *(planned)*

```
cogni-test/
├── scenarios/          # Test scenario JSON files
├── evaluation/         # Evaluation scripts
├── analysis/           # Statistical analysis and visualization
└── results/            # Raw results and reports
```
