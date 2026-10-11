"""Minimal deterministic ICAO 9303 TD3 MRZ integrity gate.

The model perceives; this gate verifies. Dependency-free.
It checks line shape, character set, document number, date of birth,
date of expiry, personal-number and final composite check digits.
It does not prove document authenticity or identity.
"""
WEIGHTS = (7, 3, 1)
CHAR_VAL = {str(d): d for d in range(10)}
CHAR_VAL.update({c: 10 + i for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")})
CHAR_VAL["<"] = 0
TD3_LINE_LEN = 44


def check_digit(value: str):
    values = []
    for char in value:
        if char not in CHAR_VAL:
            return None
        values.append(CHAR_VAL[char])
    return sum(v * WEIGHTS[i % 3] for i, v in enumerate(values)) % 10


def _digit_at(line: str, index: int, name: str, reasons: list[str]):
    char = line[index]
    if not char.isdigit():
        reasons.append(f"{name}:check_digit_not_numeric")
        return None
    return int(char)


def check(mrz_lines):
    """Return ``(passed, reasons)`` for two 44-character TD3 lines."""
    reasons = []
    if len(mrz_lines) != 2 or any(len(line) != TD3_LINE_LEN for line in mrz_lines):
        return False, ["length_or_shape"]
    if any(any(char not in CHAR_VAL for char in line) for line in mrz_lines):
        reasons.append("illegal_charset")

    line2 = mrz_lines[1]
    fields = [
        ("document_number", line2[0:9], 9),
        ("date_of_birth", line2[13:19], 19),
        ("date_of_expiry", line2[21:27], 27),
        ("personal_number", line2[28:42], 42),
    ]
    for name, value, digit_index in fields:
        expected = _digit_at(line2, digit_index, name, reasons)
        calculated = check_digit(value)
        if calculated is None:
            reasons.append(f"{name}:illegal_charset")
        elif expected is not None and calculated != expected:
            reasons.append(f"{name}:check_digit")

    composite_source = line2[0:10] + line2[13:20] + line2[21:43]
    composite_expected = _digit_at(line2, 43, "composite", reasons)
    composite_calculated = check_digit(composite_source)
    if composite_calculated is None:
        reasons.append("composite:illegal_charset")
    elif composite_expected is not None and composite_calculated != composite_expected:
        reasons.append("composite:check_digit")

    return not reasons, reasons
