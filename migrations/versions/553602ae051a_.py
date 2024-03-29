"""empty message

Revision ID: 553602ae051a
Revises: 
Create Date: 2024-01-17 11:06:18.490652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '553602ae051a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('jcgstockdata', schema=None) as batch_op:
        batch_op.add_column(sa.Column('PRICE_dataprocess', sa.JSON(), nullable=True))
        batch_op.add_column(sa.Column('INCOME_dataprocess', sa.JSON(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('jcgstockdata', schema=None) as batch_op:
        batch_op.drop_column('INCOME_dataprocess')
        batch_op.drop_column('PRICE_dataprocess')

    # ### end Alembic commands ###
