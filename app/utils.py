from datetime import datetime

def validate_date(date_str):
    """Validate date format (YYYY-MM-DD) and return a datetime object."""
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")

def calculate_progress(current: int, target: int) -> int:
    """Calculate progress percentage."""
    if target <= 0:
        raise ValueError("Target must be greater than zero.")
    return (current / target) * 100

def format_nutrition_log(date, food_item, calories):
    """Format a nutrition log entry for display."""
    return f"{date}: {food_item} - {calories} calories"

def format_fitness_metric(weight, performance):
    """Format a fitness metric entry for display."""
    return f"Weight: {weight} kg, Performance: {performance} units"

def prompt_user_for_input(prompt: str) -> str:
    """Prompt the user for input with a message."""
    return input(prompt)

def motivation_feedback(current_weight, target_weight):
    if current_weight < target_weight:
        return "Great job! You're on track to reach your goal."
    elif current_weight > target_weight:
        return "Keep pushing! Remember your goal and stay focused."
    else:
        return "You've reached your goal! Maintain your progress."

def generate_workout_plan(fitness_level):
    plans = {
        'beginner': ['15 min walking', '20 min bodyweight exercises'],
        'intermediate': ['30 min jogging', '30 min strength training'],
        'advanced': ['45 min running', '1-hour HIIT'],
    }
    return plans.get(fitness_level, [])

def recommend_schedule(workouts_per_week):
    rest_days = workouts_per_week // 2
    return {
        'workouts': workouts_per_week,
        'rest_days': rest_days,
        'schedule': [f"Workout on Day {i+1}" if i % 2 == 0 else "Rest Day" for i in range(workouts_per_week + rest_days)]
    }

def schedule_workout(username, workout_date):
    """Schedule a workout for a user."""
    return f"Workout scheduled for {username} on {workout_date.strftime('%Y-%m-%d')}"

def adjust_workout_plan(username, fitness_level):
    plans = {
        'beginner': 'Basic bodyweight exercises',
        'intermediate': 'Incorporate weights and cardio',
        'advanced': 'High-intensity interval training (HIIT)',
    }
    return plans.get(fitness_level, 'Unknown fitness level')