<!-- ============================================================
     NEMOTRON × FOL EVIDENCE GATE · README
     Module 01 of the AuthorityClaw provenance chain
     ============================================================ -->

<div align="center">

<pre>
███╗   ███╗██████╗  ██████╗
████╗ ████║██╔══██╗██╔════╝
██╔████╔██║██║  ██║██║
██║╚██╔╝██║██║  ██║██║
██║ ╚═╝ ██║██████╔╝╚██████╗
╚═╝     ╚═╝╚═════╝  ╚═════╝  01 · EVIDENCE GATE
</pre>

# `NEMOTRON × FOL EVIDENCE GATE`

**The model perceives. Code verifies. Logic decides. The model only explains.**
A local multimodal model read the passport — then the deterministic layer refused to believe it.
**Module 01** of the chain that ends at <a href="https://www.solodkiy.cv/authorityclaw.html">AuthorityClaw</a> (First Place, NVIDIA Claw Agent Challenge: London).

<img src="https://img.shields.io/badge/MODEL-Nemotron%203%20Nano%20Omni-c8ff00?style=for-the-badge&labelColor=0b0d11" alt="model">
<img src="https://img.shields.io/badge/HARDWARE-Olares%20One%20%C2%B7%20RTX%205090%2024GB-35f2ff?style=for-the-badge&labelColor=0b0d11" alt="hw">
<img src="https://img.shields.io/badge/RUNTIME-Ollama%200.30.11-ff2d9a?style=for-the-badge&labelColor=0b0d11" alt="runtime">
<img src="https://img.shields.io/badge/FOL-SWI--Prolog-9b7bff?style=for-the-badge&labelColor=0b0d11" alt="fol">
<img src="https://img.shields.io/badge/DATA-SYNTHETIC%20ONLY-orange?style=for-the-badge&labelColor=0b0d11" alt="data">

</div>

---

## ▚ THE ONE-SENTENCE RESULT

On a deliberately degraded synthetic passport, Nemotron **confidently reconstructed** unreadable
MRZ fragments — and still reported `uncertain_fields: []`. The deterministic MRZ gate caught every
malformation; the Prolog policy layer returned `request_better_evidence`; the model explained the
decision without being allowed to change it.

## ▚ THE THREE NUMBERS

| READOUT | VALUE | MEANING |
|---|---|---|
| Human-readable fields, clean specimen | **9/9** | Local vision extraction works. |
| Uncertainty calibration on degraded evidence | **FAIL** | The model's self-reported confidence cannot be trusted. |
| Deterministic gate verdict | **NEED_MORE_EVIDENCE** | Formal logic refuses automated acceptance. |

## ▚ LAYERS

```
PASSPORT IMAGE ──► NEMOTRON (perception) ──► PYTHON / ICAO (verification)
      ──► SWI-PROLOG / FOL (decision) ──► NEMOTRON (explanation, no override)
```

## ▚ WHAT BELONGS IN THIS REPO

> This repository is the code-and-evidence home of Module 01. Drop these in to make it complete:

```
nemotron-fol-evidence-gate/
├── README.md                 ← this file
├── validator/                ← deterministic MRZ + cross-field checks (Python, dependency-free)
│   └── mrz_gate.py
├── policy/                   ← SWI-Prolog policy engine
│   └── evidence_gate.pl
├── synthetic/                ← synthetic passport generator + specimen images (NO real PII, ever)
├── runs/                     ← raw, unedited run artifacts
│   ├── t1_clean.json         ← extraction + timing (total 19.65s, load 15.52s, eval 2.83s)
│   ├── t2_degraded.json      ← the confident-reconstruction failure
│   └── t1b_control.json      ← formally valid specimen, model still fails MRZ
├── docs/
│   ├── measurements.md       ← 82% GPU split · 23,819/24,463 MiB VRAM · cold 48.8s · warm 11.6s
│   └── page.html             ← frozen snapshot of solodkiy.cv/Nemotron-FOL.html
└── tests/                    ← gate unit tests: PASS / FAIL / CONFLICT paths
```

## ▚ HONEST LIMITATIONS — READ BEFORE SHARING

> - Home-lab experiment, **not** a benchmark paper, **not** a compliance certification.
> - Synthetic passport data only. Deterministic checks validate properties of extracted data;
>   they do **not** prove a document is genuine or a person is who they claim to be.
> - Not proven: production OCR on real documents, uncertainty calibration, legal/regulatory
>   compliance, fraud/liveness/biometrics, that Prolog rules encode real law.

## ▚ THE CHAIN

| MODULE | REPO / PAGE |
|---|---|
| 01 · Nemotron × FOL (this repo) | `nemotron-fol-evidence-gate` |
| LC1 · Google Cloud witness | [`sovereign-decision-plane-live-case-01`](https://github.com/slavasolodkiy/sovereign-decision-plane-live-case-01) |
| 04 · AuthorityClaw — validated pilot | [`authorityclaw`](https://github.com/slavasolodkiy/authorityclaw) · [page](https://www.solodkiy.cv/authorityclaw.html) |
| 05 · Quantum double-check | [`quantum`](https://github.com/slavasolodkiy/quantum) |

<div align="center">

`▚ THE NVIDIA INNOVATOR'S DILEMMA — <a href="https://www.dram.gold/">dram.gold</a>` ·
`PAPER — <a href="https://doi.org/10.6084/m9.figshare.33427318">figshare 33427318</a>`

</div>
