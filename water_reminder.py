
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

def run_app():
    try:
        kg = float(input("Please enter your weight (kg): "))
        user_age = int(input("Please enter your age: "))

        if kg <= 0 or user_age <= 0:
            raise ValueError("Both weight and age must be greater than zero.")

        required_liters = daily_water_amount(kg, user_age)
        reminder_gap = interval_based_on_age(user_age)
        suggested_temp = water_temp_suggestion(user_age)

        print("\n--- Hydration Plan ---")
        print(f"Water Intake: {required_liters} liters/day")
        print(f"Reminder: {reminder_gap}")
        print(f"Ideal Temperature: {suggested_temp}")

    except ValueError as ve:
        print(f"Input issue: {ve}")
    except Exception as error:
        print(f"Something went wrong: {error}")

if __name__ == "__main__":
    run_app()
