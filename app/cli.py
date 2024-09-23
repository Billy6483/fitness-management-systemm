import click
from .database import init_db, SessionLocal
from .models import User, WorkoutPlan, FitnessGoal, NutritionLog, FitnessMetric
from datetime import datetime

@click.group()
def cli():
    """Fitness Management System CLI."""
    pass

@cli.command()
def init():
    """Initialize the database."""
    init_db()
    click.echo("Database initialized.")

@cli.command()
def run():
    """Run the interactive CLI."""
    while True:
        choice = prompt_user_choice()
        
        if choice == 1:
            click.echo(add_user())
        elif choice == 2:
            click.echo(add_workout())
        elif choice == 3:
            click.echo(log_nutrition())
        elif choice == 4:
            click.echo(add_goal())
        elif choice == 5:
            click.echo(log_fitness_metric())
        elif choice == 6:
            click.echo(check_progress())
        elif choice == 7:
            click.echo(view_goals())
        elif choice == 8:
            injury_tips()
        elif choice == 9:
            click.echo(generate_plan())
        elif choice == 10:
            click.echo(recommend_workout_schedule())
        elif choice == 11:
            click.echo(schedule_workout_command())
        elif choice == 12:
            click.echo(adjust_plan())
        elif choice == 0:
            click.echo("Exiting the program.")
            break
        else:
            click.echo("Invalid choice, please try again.")

def prompt_user_choice():
    """Prompt the user to choose an action."""
    click.echo("\nChoose an action:")
    click.echo("1. Add User")
    click.echo("2. Add Workout Plan")
    click.echo("3. Log Nutrition")
    click.echo("4. Add Fitness Goal")
    click.echo("5. Log Fitness Metric")
    click.echo("6. Check Progress")
    click.echo("7. View Goals")
    click.echo("8. Injury Tips")
    click.echo("9. Generate Workout Plan")
    click.echo("10. Recommend Workout Schedule")
    click.echo("11. Schedule Workout")
    click.echo("12. Adjust Workout Plan")
    click.echo("0. Exit")
    return click.prompt("Enter your choice", type=int)

def add_user():
    name = prompt_user_for_input("Enter user name: ")
    fitness_level = prompt_user_for_input("Enter fitness level: ")
    
    db = SessionLocal()
    new_user = User(name=name, fitness_level=fitness_level)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return f"Added user: {new_user.name}"

def add_workout():
    user_id = prompt_user_for_input("Enter user ID: ")
    description = prompt_user_for_input("Enter workout description: ")
    
    db = SessionLocal()
    workout_plan = WorkoutPlan(user_id=user_id, description=description)
    db.add(workout_plan)
    db.commit()
    return f"Added workout plan: {description}"

def log_nutrition():
    user_id = prompt_user_for_input("Enter user ID: ")
    date = prompt_user_for_input("Enter date (YYYY-MM-DD): ")
    food_item = prompt_user_for_input("Enter food item: ")
    calories = prompt_user_for_input("Enter calories: ")
    
    validated_date = validate_date(date)
    db = SessionLocal()
    nutrition_log = NutritionLog(user_id=user_id, date=validated_date, food_item=food_item, calories=int(calories))
    db.add(nutrition_log)
    db.commit()
    return format_nutrition_log(validated_date, food_item, int(calories))

def add_goal():
    user_id = prompt_user_for_input("Enter user ID: ")
    goal_description = prompt_user_for_input("Enter goal description: ")
    target_date = prompt_user_for_input("Enter target date (YYYY-MM-DD): ")
    
    validated_date = validate_date(target_date)
    db = SessionLocal()
    goal = FitnessGoal(user_id=user_id, goal_description=goal_description, target_date=validated_date)
    db.add(goal)
    db.commit()
    return f"Added goal: {goal_description} by {validated_date}"

def log_fitness_metric():
    user_id = prompt_user_for_input("Enter user ID: ")
    weight = prompt_user_for_input("Enter weight (kg): ")
    performance = prompt_user_for_input("Enter performance (units): ")
    
    db = SessionLocal()
    metric = FitnessMetric(user_id=user_id, weight=int(weight), performance=int(performance))
    db.add(metric)
    db.commit()
    return format_fitness_metric(int(weight), int(performance))

def check_progress():
    current_weight = prompt_user_for_input("Enter current weight (kg): ")
    target_weight = prompt_user_for_input("Enter target weight (kg): ")

    try:
        progress = calculate_progress(int(current_weight), int(target_weight))
        feedback = motivation_feedback(int(current_weight), int(target_weight))
        return f"Progress: {progress:.2f}%. {feedback}"
    except ValueError as e:
        return f"Error: {e}"

def view_goals():
    user_id = prompt_user_for_input("Enter user ID: ")
    session = SessionLocal()
    goals = session.query(FitnessGoal).filter(FitnessGoal.user_id == user_id).all()
    output = []
    if goals:
        output.append(f"Goals for user ID {user_id}:")
        for goal in goals:
            output.append(f"- Goal: {goal.goal_description} by {goal.target_date}")
    else:
        output.append(f"No goals found for user ID {user_id}.")
    session.close()
    return "\n".join(output)

def injury_tips():
    tips = [
        "Always warm up before workouts.",
        "Maintain proper form during exercises.",
        "Gradually increase workout intensity.",
        "Include rest days in your routine."
    ]
    click.echo("Injury Prevention Tips:")
    for tip in tips:
        click.echo(f"- {tip}")

def generate_plan():
    fitness_level = click.prompt("Enter your fitness level (beginner/intermediate/advanced)")
    plan = generate_workout_plan(fitness_level)
    if plan:
        output = [f"Workout Plan for {fitness_level}:"]
        output.extend(f"- {exercise}" for exercise in plan)
        return "\n".join(output)
    else:
        return "Invalid fitness level provided."

def recommend_workout_schedule():
    workouts_per_week = click.prompt("Enter the number of workouts per week", type=int)
    schedule = recommend_schedule(workouts_per_week)
    output = [
        f"Recommended Schedule: {schedule['workouts']} workouts per week, {schedule['rest_days']} rest days."
    ] + [day for day in schedule['schedule']]
    return "\n".join(output)

def schedule_workout_command():
    username = click.prompt("Enter your username")
    workout_date_str = click.prompt("Enter the workout date (YYYY-MM-DD)")
    validated_date = validate_date(workout_date_str)
    message = schedule_workout(username, validated_date)
    return message

def adjust_plan():
    username = click.prompt("Enter your username")
    fitness_level = click.prompt("Enter your fitness level (beginner/intermediate/advanced)")
    adjusted_plan = adjust_workout_plan(username, fitness_level)
    return f"Adjusted Workout Plan for {username}: {adjusted_plan}"

# Utility functions
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

def motivation_feedback(current_weight: int, target_weight: int) -> str:
    """Provide motivational feedback based on current and target weights."""
    if current_weight < target_weight:
        return "Keep pushing! You're getting closer to your goal!"
    elif current_weight == target_weight:
        return "Great job! You've reached your goal!"
    else:
        return "Don't get discouraged! Focus on your progress."

def generate_workout_plan(fitness_level: str) -> list:
    """Generate a workout plan based on fitness level."""
    plans = {
        'beginner': ['30 min walking', 'Bodyweight squats', 'Push-ups'],
        'intermediate': ['45 min cycling', 'Deadlifts', 'Bench press'],
        'advanced': ['1 hour HIIT', 'Weightlifting', 'CrossFit']
    }
    return plans.get(fitness_level.lower(), [])

def recommend_schedule(workouts_per_week: int) -> dict:
    """Recommend a workout schedule."""
    rest_days = 7 - workouts_per_week
    return {
        'workouts': workouts_per_week,
        'rest_days': rest_days,
        'schedule': [f"Workout on day {i + 1}" for i in range(workouts_per_week)]
    }

def schedule_workout(username: str, workout_date: datetime.date) -> str:
    """Schedule a workout for the user."""
    return f"Workout scheduled for {username} on {workout_date}"

def adjust_workout_plan(username: str, fitness_level: str) -> str:
    """Adjust the workout plan based on user preferences."""
    return f"Adjusted plan for {username} at {fitness_level} level."

if __name__ == "__main__":
    cli()
