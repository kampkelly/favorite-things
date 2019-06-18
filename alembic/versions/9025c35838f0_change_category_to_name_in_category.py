"""change category to name in category

Revision ID: 9025c35838f0
Revises: daa46fc1d31e
Create Date: 2019-06-18 10:59:12.374195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9025c35838f0'
down_revision = 'daa46fc1d31e'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('categories', 'category', new_column_name="name",
               existing_type=sa.VARCHAR(255),
               nullable=False)


def downgrade():
    op.alter_column('categories', 'name', new_column_name="category",
               existing_type=sa.VARCHAR(255),
               nullable=False)
