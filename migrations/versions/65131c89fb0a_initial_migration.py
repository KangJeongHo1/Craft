"""Initial migration

Revision ID: 65131c89fb0a
Revises: 
Create Date: 2024-09-01 16:01:55.637070

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65131c89fb0a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('derivative_trades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_category', sa.String(length=2), nullable=False),
    sa.Column('board_id', sa.String(length=2), nullable=False),
    sa.Column('session_id', sa.String(length=2), nullable=False),
    sa.Column('isin_code', sa.String(length=12), nullable=False),
    sa.Column('message_sequence_number', sa.Integer(), nullable=False),
    sa.Column('trading_price', sa.Float(), nullable=False),
    sa.Column('trading_volume', sa.Integer(), nullable=False),
    sa.Column('trading_date', sa.Date(), nullable=False),
    sa.Column('trading_time', sa.Time(), nullable=True),
    sa.Column('processing_time', sa.String(length=12), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_derivative_trades_id'), 'derivative_trades', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_derivative_trades_id'), table_name='derivative_trades')
    op.drop_table('derivative_trades')
    # ### end Alembic commands ###
