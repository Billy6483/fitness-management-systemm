"""Initial migration

Revision ID: 7597c569aee5
Revises: a55523e6db42
Create Date: 2024-09-23 17:11:30.852489

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7597c569aee5'
down_revision: Union[str, None] = 'a55523e6db42'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
