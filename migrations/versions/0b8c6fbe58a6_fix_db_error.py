"""fix db error

Revision ID: 0b8c6fbe58a6
Revises: 5fd728098b78
Create Date: 2024-12-03 22:27:31.484202

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0b8c6fbe58a6'
down_revision = '5fd728098b78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shop',
    sa.Column('shop_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('shop_name', sa.String(length=120), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('shop_image', sa.Text(), nullable=True),
    sa.Column('shop_address_street', sa.Text(), nullable=False),
    sa.Column('shop_address_province', sa.String(length=120), nullable=False),
    sa.Column('shop_address_city', sa.String(length=120), nullable=False),
    sa.Column('shop_address_district', sa.String(length=120), nullable=False),
    sa.Column('shop_address_subdistrict', sa.String(length=120), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('shop_id'),
    sa.UniqueConstraint('shop_name')
    )
    op.drop_table('shops')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('shop_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'shop', ['shop_id'], ['shop_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('shop_id')

    op.create_table('shops',
    sa.Column('shop_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('shop_name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('shop_image', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('shop_address_street', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('shop_address_province', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('shop_address_city', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('shop_address_district', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('shop_address_subdistrict', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('status', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name='shops_user_id_fkey'),
    sa.PrimaryKeyConstraint('shop_id', name='shops_pkey'),
    sa.UniqueConstraint('shop_name', name='shops_shop_name_key')
    )
    op.drop_table('shop')
    # ### end Alembic commands ###