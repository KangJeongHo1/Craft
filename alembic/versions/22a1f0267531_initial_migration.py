"""initial migration

Revision ID: 22a1f0267531
Revises: 05b3beafe296
Create Date: 2024-08-31 16:00:43.686061

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22a1f0267531'
down_revision: Union[str, None] = '05b3beafe296'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
