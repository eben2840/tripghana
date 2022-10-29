"""empty message

Revision ID: 20436a436c5e
Revises: 57f71f1f0ee6
Create Date: 2022-10-21 18:46:07.011755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20436a436c5e'
down_revision = '57f71f1f0ee6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('central',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'course', ['email'])
    op.create_unique_constraint(None, 'course', ['name'])
    op.drop_column('item', 'des')
    op.drop_column('item', 'image_file')
    op.drop_column('item', 'incase')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('incase', sa.VARCHAR(), nullable=True))
    op.add_column('item', sa.Column('image_file', sa.VARCHAR(), nullable=True))
    op.add_column('item', sa.Column('des', sa.VARCHAR(), nullable=True))
    op.drop_constraint(None, 'course', type_='unique')
    op.drop_constraint(None, 'course', type_='unique')
    op.drop_table('central')
    # ### end Alembic commands ###