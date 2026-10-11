# Nemotron × FOL Evidence Gate

> **The model perceives. Code verifies. Logic decides. The model only explains.**

**Role in the Lab:** Evidence Gate — model perception separated from deterministic verification.

- [Canonical project page](https://www.solodkiy.cv/Nemotron-FOL.html)
- [Full research trail — Sovereign Agent Lab](https://www.solodkiy.cv/sovereign-agent-lab.html)

On a deliberately degraded synthetic passport specimen, a local Nemotron model confidently reconstructed an invalid MRZ while reporting no uncertain fields. The deterministic ICAO-shaped integrity gate rejected the candidate; the Prolog policy maps that failure to `need_better_evidence`; the model is not allowed to change the decision.

## Status

**Runnable M1 reference core.** This repository reproduces the deterministic gate and policy boundary from committed synthetic fixtures and captured run summaries. It does **not** reproduce the original multimodal inference in CI.

## Quick start

```bash
python3 -m unittest discover -s tests -v
```

SWI-Prolog is optional locally; when installed, the suite also executes the policy assertion that AI override is false.

## Layers

```text
SYNTHETIC PASSPORT IMAGE / MRZ
        ↓
NVIDIA NEMOTRON — perception candidate
        ↓
PYTHON / ICAO-SHAPED INTEGRITY GATE — verification
        ↓
SWI-PROLOG / FOL — policy decision
        ↓
NEMOTRON — explanation only, no override
```

## Result

| Readout | Value | Meaning |
|---|---|---|
| Human-readable fields, clean specimen | 9/9 in the recorded experiment | Local vision extraction can work. |
| Uncertainty calibration on degraded evidence | **FAIL** | Self-reported model confidence is not authority. |
| Deterministic gate verdict | `NEED_MORE_EVIDENCE` | Invalid evidence does not earn automated acceptance. |

## Repository map

- `validator/mrz_gate.py` — complete TD3 field and composite check-digit integrity gate
- `policy/evidence_gate.pl` — Prolog policy; `ai_authorised_to_override(false)`
- `synthetic/` — generated text MRZ fixtures; no real PII
- `runs/` — captured, sanitised result summaries
- `tests/` — deterministic regression tests
- `measurements.md` and `page.html` — original experiment documentation already present in the repository

## Honest limitations

- Home-lab experiment, not a benchmark paper or compliance certification.
- Synthetic data only.
- Check digits verify internal MRZ integrity. They do **not** prove a document is genuine or identify a person.
- The original model inference is captured, not reproduced by public CI.
- Not proven: production OCR, uncertainty calibration, fraud/liveness/biometrics, legal correctness or regulatory compliance.
- FOL is useful after evidence and semantics are made trustworthy; formal validity is not institutional authority.

MIT licence.
