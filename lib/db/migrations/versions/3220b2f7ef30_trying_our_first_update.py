"""Trying our first update

Revision ID: 3220b2f7ef30
Revises: 
Create Date: 2023-03-27 14:58:00.910629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3220b2f7ef30'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(), nullable=True),
    sa.Column('answer', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('difficulty', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('scores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('score', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('scores')
    op.drop_table('questions')
    # ### end Alembic commands ###
