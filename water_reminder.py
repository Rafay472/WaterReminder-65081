
def daily_water_amount(kg, user_age):
    """Estimate water intake (liters/day) based on weight."""
    return round(kg * 0.03, 2)  

def interval_based_on_age(user_age):
    """Suggest reminder frequency depending on age group."""
    if user_age < 18:
        return "Every 3 hours"
    elif user_age <= 50:
        return "Every 2 hours"
    else:
        return "Every 1.5 hours"

def water_temp_suggestion(user_age):
    """Recommend water temperature based on age bracket."""
    if user_age < 18:
        return "Cool"
    elif user_age <= 50:
        return "Room temperature"
    else:
        return "Lukewarm"
