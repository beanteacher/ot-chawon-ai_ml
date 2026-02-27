from app.services.size_rule import predict_size


def test_reason_contains_height_or_weight_keys():
    _, reasons = predict_size(180, 72, 'male')
    assert any(r.startswith('height_') for r in reasons)
    assert any(r.startswith('weight_') for r in reasons)


def test_reason_has_gender_profile_key():
    _, reasons = predict_size(168, 60, 'female')
    assert 'non_male_profile_baseline' in reasons


def test_boundary_height_175_is_l_path():
    size, reasons = predict_size(175, 60, 'male')
    assert size == 'L'
    assert 'height_over_or_eq_175' in reasons
