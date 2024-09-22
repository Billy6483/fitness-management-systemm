from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect

# revision identifiers, used by Alembic.
revision = '5d93b9430be7'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    conn = op.get_bind()
    inspector = inspect(conn)

    if 'users' not in inspector.get_table_names():
        op.create_table(
            'users',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String, nullable=False),
            sa.Column('fitness_level', sa.String, nullable=False)
        )

def downgrade():
    conn = op.get_bind()
    inspector = inspect(conn)

    if 'users' in inspector.get_table_names():
        op.drop_table('users')
