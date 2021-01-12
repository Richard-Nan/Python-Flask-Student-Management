"""empty message

Revision ID: 16b6ed8fe2d2
Revises: 3df62c9a1faf
Create Date: 2019-12-09 20:35:05.312137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16b6ed8fe2d2'
down_revision = '3df62c9a1faf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Studata',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('stunumber', sa.String(length=10), nullable=False),
    sa.Column('stuname', sa.String(length=50), nullable=False),
    sa.Column('grede', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Studata')
    # ### end Alembic commands ###