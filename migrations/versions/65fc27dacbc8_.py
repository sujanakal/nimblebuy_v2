"""empty message

Revision ID: 65fc27dacbc8
Revises: 24ad0beb4c27
Create Date: 2020-04-18 01:06:56.672639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65fc27dacbc8'
down_revision = '24ad0beb4c27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('enquiries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('locality', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('enquiries')
    # ### end Alembic commands ###