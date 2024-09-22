"""Initial migration

Revision ID: a55523e6db42
Revises: 5d93b9430be7
Create Date: 2024-09-22 14:07:38.573509

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a55523e6db42'
down_revision: Union[str, None] = '5d93b9430be7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
