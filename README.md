Fitness Management System CLI

The Fitness Management System is a command-line interface (CLI) application designed to help users manage their fitness goals, workouts, nutrition logs, and overall health metrics. The application allows for easy interaction through prompts, providing a user-friendly experience.

Features

User Management

    Add User: Create a new user profile.

    View Goals: Retrieve and display fitness goals for a specified user.

Workout Management

    Add Workout: Add a workout plan for a specific user.

    Generate Workout Plan: Generate a customized workout plan based on the user's fitness level.

    Schedule Workout: Schedule a workout for a user on a specified date.

    Adjust Workout Plan: Modify the workout plan based on the user's fitness level.

Nutrition Management

    Log Nutrition: Log nutrition data including food items and calories consumed.

Fitness Tracking

    Log Fitness Metrics: Log fitness metrics such as weight and performance.

    Check Progress: Calculate progress toward fitness goals and provide motivational feedback.

Injury Prevention

    Injury Tips: Provide tips for injury prevention during workouts.

Schedule Recommendations

    Recommend Workout Schedule: Suggest a workout schedule based on the number of workouts per week.

Dependencies

This project requires the following Python packages:

    Click: For creating command-line interfaces.

    SQLAlchemy: For database interactions.

    SQLite: As the database backend (comes with Python).

    Alembic: For handling database migrations.

To install the dependencies, run:

bash

# pipenv install click sqlalchemy alembic

Getting Started
Clone the Repository

bash

# git clone https://github.com/Billy6483/fitness-management-systemm.git

# cd fitness-management-systemm 

# Activate the virtual environment

pipenv shell

 
Initialize the Database

To set up the SQLite database, run:

bash

# pipenv run python -m app.cli init

Run the CLI

You can access the CLI commands using:

bash

# python -m app.cli run
 
 
Choose an action:
1. Add User
2. Add Workout Plan
3. Log Nutrition
4. Add Fitness Goal
5. Log Fitness Metric
6. Check Progress
7. View Goals
8. Injury Tips
9. Generate Workout Plan
10. Recommend Workout Schedule
11. Schedule Workout
12. Adjust Workout Plan
13. View User Details
0. Exit
Enter your choice: 


Database Migration

Initial Migration Setup
To create the initial database migration, run:

bash
pipenv run python -m alembic revision --autogenerate -m "Initial migration"

Applying Migrations
To apply the migrations to your database, run:

bash

pipenv run python -m alembic upgrade head

Creating New Migrations
Whenever you make changes to your models, create a new migration with:

bash

 pipenv run python -m alembic revision --autogenerate -m "Description of changes"

 Rolling Back Migrations
If you need to roll back to a previous migration, you can use:

bash

 pipenv run python -m alembic downgrade <revision_id>

Viewing Migration History
To see the history of applied migrations, run:

bash

 pipenv run python -m alembic history

Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request to enhance the functionality of the application.

License
This project is licensed under the MIT License - see the LICENSE file for details.# fitness-management-systemm
