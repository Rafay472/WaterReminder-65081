import pytest
from water_reminder import daily_water_amount, interval_based_on_age, water_temp_suggestion

def test_daily_water_amount_for_various_weights():
    """Verify daily water consumption calculation for different body weights."""
    assert daily_water_amount(60, 20) == 1.8  # 60 kg → 1.8 L
    assert daily_water_amount(85, 30) == 2.55  # 85 kg → 2.55 L

def test_interval_based_on_age_categories():
    """Ensure reminder intervals vary appropriately for age groups."""
    assert interval_based_on_age(12) == "Every 3 hours"
    assert interval_based_on_age(40) == "Every 2 hours"
    assert interval_based_on_age(75) == "Every 1.5 hours"

    
