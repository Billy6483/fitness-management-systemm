from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    fitness_level = Column(String, nullable=False)

    workouts = relationship('WorkoutPlan', back_populates='user')
    goals = relationship('FitnessGoal', back_populates='user')
    nutrition_logs = relationship('NutritionLog', back_populates='user')
    fitness_metrics = relationship('FitnessMetric', back_populates='user')


class WorkoutPlan(Base):
    __tablename__ = 'workout_plans'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    description = Column(String, nullable=False)

    user = relationship('User', back_populates='workouts')


class FitnessGoal(Base):
    __tablename__ = 'fitness_goals'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    goal_description = Column(String, nullable=False)
    target_date = Column(Date, nullable=False)

    user = relationship('User', back_populates='goals')


class NutritionLog(Base):
    __tablename__ = 'nutrition_logs'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date, nullable=False)
    food_item = Column(String, nullable=False)
    calories = Column(Integer, nullable=False)

    user = relationship('User', back_populates='nutrition_logs')


class FitnessMetric(Base):
    __tablename__ = 'fitness_metrics'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    weight = Column(Integer)
    performance = Column(Integer)

    user = relationship('User', back_populates='fitness_metrics')
