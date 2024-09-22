"""Initial migration

Revision ID: 5d93b9430be7
Revises: 
Create Date: 2024-09-22 08:15:15.863121

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '5d93b9430be7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Create tables based on your models
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('fitness_level', sa.String(), nullable=False)
    )
    
    op.create_table(
        'workout_plans',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id')),
        sa.Column('description', sa.String(), nullable=False)
    )

    op.create_table(
        'fitness_goals',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id')),
        sa.Column('goal_description', sa.String(), nullable=False),
        sa.Column('target_date', sa.Date(), nullable=False)
    )

    op.create_table(
        'nutrition_logs',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id')),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('food_item', sa.String(), nullable=False),
        sa.Column('calories', sa.Integer(), nullable=False)
    )

    op.create_table(
        'fitness_metrics',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id')),
        sa.Column('weight', sa.Integer()),
        sa.Column('performance', sa.Integer())
    )

def downgrade() -> None:
    # Drop tables in reverse order of creation
    op.drop_table('fitness_metrics')
    op.drop_table('nutrition_logs')
    op.drop_table('fitness_goals')
    op.drop_table('workout_plans')
    op.drop_table('users')
