"""Removing the test table

Revision ID: 7c2bffdf1b46
Revises: 0f0e7842ed50
Create Date: 2023-03-29 15:26:58.965213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c2bffdf1b46'
down_revision = '0f0e7842ed50'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###