def predict_size(height_cm: float, weight_kg: float, gender: str) -> tuple[str, list[str]]:
    score = 0
    reasons: list[str] = []

    if height_cm >= 175:
        score += 1
        reasons.append('height_over_or_eq_175')
    else:
        reasons.append('height_under_175')

    if weight_kg >= 75:
        score += 1
        reasons.append('weight_over_or_eq_75')
    else:
        reasons.append('weight_under_75')

    if gender.lower() == 'male':
        reasons.append('male_profile_baseline')
    else:
        reasons.append('non_male_profile_baseline')

    size = 'L' if score >= 1 else 'M'
    return size, reasons
