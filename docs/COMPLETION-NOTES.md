# Completion notes — runnable M1 core

Companion page: https://www.solodkiy.cv/Nemotron-FOL.html

This repository began as the public write-up and measurement record for a home-lab experiment. The runnable M1 core now adds:

- `validator/mrz_gate.py` — dependency-free ICAO 9303 TD3 check-digit integrity gate.
- `policy/evidence_gate.pl` — SWI-Prolog policy; `ai_authorised_to_override(false)`.
- `synthetic/` — generated valid and degraded MRZ fixtures; no real identity data.
- `runs/` — captured summaries of the clean and degraded model runs.
- `tests/` — deterministic regression tests.

Run:

```bash
python3 -m unittest discover -s tests -v
```

Honest boundary: this is the public reference core, not the full local Nemotron vision harness. The original inference is captured rather than re-executed in CI. Policy completeness and legal correctness are not claimed.
