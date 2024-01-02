"""empty message

Revision ID: aa8a0fad3f34
Revises: 
Create Date: 2023-12-13 11:54:33.668141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa8a0fad3f34'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('CommerceCSVModel', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Name', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('CommerceCSVModel', schema=None) as batch_op:
        batch_op.drop_column('Name')

    # ### end Alembic commands ###
