"""create audit table

Revision ID: daa46fc1d31e
Revises: f150b9a54f8a
Create Date: 2019-06-17 14:54:33.689713

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func



# revision identifiers, used by Alembic.
revision = 'daa46fc1d31e'
down_revision = 'f150b9a54f8a'
branch_labels = None
depends_on = None



def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('log', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.TIMESTAMP(timezone=True), server_default=func.now(), nullable=False),
    sa.Column('modified_date', sa.TIMESTAMP(timezone=True), server_default=func.now(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id']),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    op.drop_table('audit')
