"""users table

Revision ID: 9cd8ae4da42a
Revises: 
Create Date: 2021-02-14 18:40:43.603165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cd8ae4da42a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('dp', sa.String(length=20), nullable=False),
    sa.Column('dp2', sa.String(length=20), nullable=False),
    sa.Column('dp3', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('date_joined', sa.DateTime(), nullable=False),
    sa.Column('department', sa.String(length=20), nullable=False),
    sa.Column('student_number', sa.Integer(), nullable=True),
    sa.Column('age', sa.DateTime(), nullable=False),
    sa.Column('gender', sa.String(length=20), nullable=False),
    sa.Column('country', sa.String(length=20), nullable=True),
    sa.Column('bio', sa.String(length=120), nullable=True),
    sa.Column('private', sa.Boolean(), nullable=False),
    sa.Column('snapchat', sa.String(length=20), nullable=True),
    sa.Column('instagram', sa.String(length=20), nullable=True),
    sa.Column('last_message_read_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('student_number'),
    sa.UniqueConstraint('username')
    )
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('recipient_id', sa.Integer(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['recipient_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_message_timestamp'), 'message', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_message_timestamp'), table_name='message')
    op.drop_table('message')
    op.drop_table('followers')
    op.drop_table('user')
    # ### end Alembic commands ###
