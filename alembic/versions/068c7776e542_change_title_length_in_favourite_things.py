"""change title length in favourite things

Revision ID: 068c7776e542
Revises: 9025c35838f0
Create Date: 2019-06-18 16:40:46.439077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '068c7776e542'
down_revision = '9025c35838f0'
branch_labels = None
depends_on = None


def upgrade():
     op.alter_column('favorite_things', 'title', existing_type=sa.VARCHAR(100),
               nullable=False)


def downgrade():
     op.alter_column('favorite_things', 'title', existing_type=sa.VARCHAR(255),
               nullable=False)
