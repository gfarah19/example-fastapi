"""add content column to posts table

Revision ID: 4244cbedcd1c
Revises: 5adc6cc64dc6
Create Date: 2024-02-06 17:14:22.370280

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4244cbedcd1c'
down_revision: Union[str, None] = '5adc6cc64dc6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
