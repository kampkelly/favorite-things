"""create categories table

Revision ID: e5549f71950d
Revises: 00854468ff70
Create Date: 2019-06-17 14:00:08.569604

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = 'e5549f71950d'
down_revision = '00854468ff70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    categories_table = op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=255), nullable=False),
    sa.Column('created_date', sa.TIMESTAMP(timezone=True), server_default=func.now(timezone="WAT"), nullable=False),
    sa.Column('modified_date', sa.TIMESTAMP(timezone=True), server_default=func.now(timezone="WAT"), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('category')
    )

    op.bulk_insert(categories_table,
        [
            {'id':1, 'category':'person'},
            {'id':2, 'category':'place'},
            {'id':3, 'category':'food'}
        ]
    )
    # ### end Alembic commands ###


def downgrade():
    op.drop_table('categories')
