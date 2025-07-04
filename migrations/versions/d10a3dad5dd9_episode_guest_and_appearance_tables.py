"""Episode, Guest and Appearance tables

Revision ID: d10a3dad5dd9
Revises: 
Create Date: 2025-06-23 09:57:13.625138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd10a3dad5dd9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('episodes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('guests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('appearances',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('episode_id', sa.Integer(), nullable=True),
    sa.Column('guest_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['episode_id'], ['episodes.id'], ),
    sa.ForeignKeyConstraint(['guest_id'], ['guests.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appearances')
    op.drop_table('guests')
    op.drop_table('episodes')
    # ### end Alembic commands ###
