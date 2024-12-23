"""Inisial Migrate 

Revision ID: adc4fdff019f
Revises: 
Create Date: 2024-11-29 23:08:35.632755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adc4fdff019f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=False),
    sa.Column('address_street', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=255), nullable=True),
    sa.Column('state', sa.String(length=255), nullable=True),
    sa.Column('zip_code', sa.String(length=255), nullable=True),
    sa.Column('role', sa.String(length=255), nullable=False),
    sa.Column('profile_image', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
