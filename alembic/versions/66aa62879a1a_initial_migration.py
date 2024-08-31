"""initial migration

Revision ID: 66aa62879a1a
Revises: d27d248d069d
Create Date: 2024-08-31 16:02:55.057622

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66aa62879a1a'
down_revision: Union[str, None] = 'd27d248d069d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
