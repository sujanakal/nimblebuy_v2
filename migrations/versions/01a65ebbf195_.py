"""empty message

Revision ID: 01a65ebbf195
Revises: 65fc27dacbc8
Create Date: 2020-04-18 22:24:03.881814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01a65ebbf195'
down_revision = '65fc27dacbc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('customer_loc', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'customer_loc')
    # ### end Alembic commands ###