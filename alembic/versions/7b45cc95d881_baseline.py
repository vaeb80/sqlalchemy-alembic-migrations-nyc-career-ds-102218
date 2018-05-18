"""baseline

Revision ID: 7b45cc95d881
Revises:
Create Date: 2018-05-18 12:14:43.957699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b45cc95d881'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'songs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String()),
        sa.Column('length', sa.Integer())
        )

def downgrade():
    op.drop_table('songs')
