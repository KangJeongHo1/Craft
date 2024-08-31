"""initial migration

Revision ID: d27d248d069d
Revises: 22a1f0267531
Create Date: 2024-08-31 16:02:36.607970

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd27d248d069d'
down_revision: Union[str, None] = '22a1f0267531'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
