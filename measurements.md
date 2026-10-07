# Raw measurement notes — Nemotron × FOL Evidence Gate

**Module 01 · Olares One · 06–07 September 2026.** Values as recorded in the lab log;
unedited. These measurements back the page at
[solodkiy.cv/Nemotron-FOL.html](https://www.solodkiy.cv/Nemotron-FOL.html).

```
Model tag:              nemotron3:33b-q4_K_M
Ollama version:         0.30.11 (Olares / Kubernetes)
API-reported size:      27,638,631,632 bytes (~27.6 GB)
Processor split:        18% CPU / 82% GPU
GPU after load:         23,819 MiB / 24,463 MiB
Cold text run:          48.759 s
Warm text run:          11.562 s
```

## T1 — clean synthetic passport
```
total_duration          19.653508780 s
load_duration           15.516499925 s
prompt_eval_duration     1.229832000 s
eval_duration            2.826628000 s
result                   9/9 human-readable fields; MRZ not exact; uncertain_fields: []
```

## T2 — degraded evidence (blur, rotation, JPEG, occlusion)
```
wall clock              12.17 s
finding                 confident reconstruction of unreadable fragments,
                         uncertain_fields still []
calibration             FAIL
role                    USEFUL as candidate extractor only
```

## T1b — formally valid control specimen (44-char MRZ, valid check digits)
```
wall clock              12.18 s
readable fields         9/9
mrz_line_1_structure    FAIL (model returned 42 chars)
date_of_birth_check     FAIL
expiry_date_check       FAIL
optional_data_check     FAIL
composite_check         FAIL
cross-field             CONFLICT (nationality / sex / DOB / expiry vs MRZ)
deterministic verdict   NEED_MORE_EVIDENCE
```

## Final FOL decision
```
decision = request_better_evidence
reasons  = [cross_field_conflict, deterministic_failure,
            identity_conflict, mrz_integrity_failed]
```

> Synthetic specimen data only. No real customer PII was used or exists in this repository.
