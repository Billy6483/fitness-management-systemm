
import click
from .database import SessionLocal, init_db
from .models import User, WorkoutPlan, NutritionLog, FitnessGoal, FitnessMetric
from datetime import datetime
from .utils import (validate_date, format_nutrition_log, format_fitness_metric,
                    prompt_user_for_input, calculate_progress, motivation_feedback,
                    generate_workout_plan, recommend_schedule, schedule_workout, adjust_workout_plan)


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
def add_user():
    """Add a new user interactively."""
    name = prompt_user_for_input("Enter user name: ")
    fitness_level = prompt_user_for_input("Enter fitness level: ")
    
    db = SessionLocal()
    new_user = User(name=name, fitness_level=fitness_level)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    click.echo(f"Added user: {new_user.name}")

@cli.command()
def add_workout():
    """Add a workout plan for a user interactively."""
    user_id = prompt_user_for_input("Enter user ID: ")
    description = prompt_user_for_input("Enter workout description: ")
    
    db = SessionLocal()
    workout_plan = WorkoutPlan(user_id=user_id, description=description)
    db.add(workout_plan)
    db.commit()
    click.echo(f"Added workout plan: {description}")

@cli.command()
def log_nutrition():
    """Log nutrition data for a user interactively."""
    user_id = prompt_user_for_input("Enter user ID: ")
    date = prompt_user_for_input("Enter date (YYYY-MM-DD): ")
    food_item = prompt_user_for_input("Enter food item: ")
    calories = prompt_user_for_input("Enter calories: ")
    
    validated_date = validate_date(date)
    db = SessionLocal()
    nutrition_log = NutritionLog(user_id=user_id, date=validated_date, food_item=food_item, calories=int(calories))
    db.add(nutrition_log)
    db.commit()
    click.echo(format_nutrition_log(validated_date, food_item, int(calories)))

@cli.command()
def add_goal():
    """Add a fitness goal for a user interactively."""
    user_id = prompt_user_for_input("Enter user ID: ")
    goal_description = prompt_user_for_input("Enter goal description: ")
    target_date = prompt_user_for_input("Enter target date (YYYY-MM-DD): ")
    
    validated_date = validate_date(target_date)
    db = SessionLocal()
    goal = FitnessGoal(user_id=user_id, goal_description=goal_description, target_date=validated_date)
    db.add(goal)
    db.commit()
    click.echo(f"Added goal: {goal_description} by {validated_date}")

@cli.command()
def log_fitness_metric():
    """Log fitness metrics for a user interactively."""
    user_id = prompt_user_for_input("Enter user ID: ")
    weight = prompt_user_for_input("Enter weight (kg): ")
    performance = prompt_user_for_input("Enter performance (units): ")
    
    db = SessionLocal()
    metric = FitnessMetric(user_id=user_id, weight=int(weight), performance=int(performance))
    db.add(metric)
    db.commit()
    click.echo(format_fitness_metric(int(weight), int(performance)))

@cli.command()
def check_progress():
    """Check progress and provide motivation feedback."""
    current_weight = prompt_user_for_input("Enter current weight (kg): ")
    target_weight = prompt_user_for_input("Enter target weight (kg): ")

    # Calculate progress percentage
    try:
        progress = calculate_progress(int(current_weight), int(target_weight))
        click.echo(f"Progress: {progress:.2f}%")

        # Provide motivational feedback
        feedback = motivation_feedback(int(current_weight), int(target_weight))
        click.echo(feedback)

    except ValueError as e:
        click.echo(f"Error: {e}")

@cli.command()
def view_goals():
    """View goals for a user interactively."""
    user_id = prompt_user_for_input("Enter user ID: ")
    session = SessionLocal()
    goals = session.query(FitnessGoal).filter(FitnessGoal.user_id == user_id).all()
    if goals:
        click.echo(f"Goals for user ID {user_id}:")
        for goal in goals:
            click.echo(f"- Goal: {goal.goal_description} by {goal.target_date}")
    else:
        click.echo(f"No goals found for user ID {user_id}.")
    session.close()

@cli.command()
def injury_tips():
    """Provide injury prevention tips."""
    tips = [
        "Always warm up before workouts.",
        "Maintain proper form during exercises.",
        "Gradually increase workout intensity.",
        "Include rest days in your routine."
    ]
    click.echo("Injury Prevention Tips:")
    for tip in tips:
        click.echo(f"- {tip}")

@cli.command()
def generate_plan():
    """Generate a workout plan based on fitness level."""
    fitness_level = click.prompt("Enter your fitness level (beginner/intermediate/advanced)")
    plan = generate_workout_plan(fitness_level)
    if plan:
        click.echo(f"Workout Plan for {fitness_level}:")
        for exercise in plan:
            click.echo(f"- {exercise}")
    else:
        click.echo("Invalid fitness level provided.")

@cli.command()
def recommend_workout_schedule():
    """Recommend a workout schedule."""
    workouts_per_week = click.prompt("Enter the number of workouts per week", type=int)
    schedule = recommend_schedule(workouts_per_week)
    click.echo(f"Recommended Schedule: {schedule['workouts']} workouts per week, {schedule['rest_days']} rest days.")
    for day in schedule['schedule']:
        click.echo(day)

@cli.command()
def schedule_workout_command():
    """Schedule a workout for a user."""
    username = click.prompt("Enter your username")
    workout_date_str = click.prompt("Enter the workout date (YYYY-MM-DD)")
    validated_date = validate_date(workout_date_str)
    message = schedule_workout(username, validated_date)
    click.echo(message)

@cli.command()
def adjust_plan():
    """Adjust the workout plan based on fitness level."""
    username = click.prompt("Enter your username")
    fitness_level = click.prompt("Enter your fitness level (beginner/intermediate/advanced)")
    adjusted_plan = adjust_workout_plan(username, fitness_level)
    click.echo(f"Adjusted Workout Plan for {username}: {adjusted_plan}")




if __name__ == "__main__":
    cli()