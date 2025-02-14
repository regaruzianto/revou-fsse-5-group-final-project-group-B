"""add discount,order,orderitem table

Revision ID: a83b67e30264
Revises: a9c83643fa62
Create Date: 2024-12-11 15:03:08.400826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a83b67e30264'
down_revision = 'a9c83643fa62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('order_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('total_amount', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('order_id')
    )
    op.create_table('discounts',
    sa.Column('discount_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('discount_name', sa.String(length=120), nullable=False),
    sa.Column('discount_type', sa.String(length=120), nullable=False),
    sa.Column('discount_value', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('end_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('discount_id'),
    sa.UniqueConstraint('discount_name')
    )
    op.create_table('orderitem',
    sa.Column('orderitem_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('unit_price', sa.Integer(), nullable=False),
    sa.Column('total_price', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.order_id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ),
    sa.PrimaryKeyConstraint('orderitem_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orderitem')
    op.drop_table('discounts')
    op.drop_table('orders')
    # ### end Alembic commands ###
