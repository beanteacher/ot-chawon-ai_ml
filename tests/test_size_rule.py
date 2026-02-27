from app.services.size_rule import predict_size


def test_predict_size_m_profile():
    size, reasons = predict_size(170, 68, 'male')
    assert size == 'M'
    assert 'height_under_175' in reasons
    assert 'weight_under_75' in reasons


def test_predict_size_l_by_height():
    size, reasons = predict_size(176, 68, 'male')
    assert size == 'L'
    assert 'height_over_or_eq_175' in reasons


def test_predict_size_l_by_weight():
    size, reasons = predict_size(170, 80, 'female')
    assert size == 'L'
    assert 'weight_over_or_eq_75' in reasons
    assert 'non_male_profile_baseline' in reasons
