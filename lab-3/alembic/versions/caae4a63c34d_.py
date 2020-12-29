"""empty message

Revision ID: caae4a63c34d
Revises: ca10c31387d1
Create Date: 2020-12-02 01:42:50.129963

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'caae4a63c34d'
down_revision = 'ca10c31387d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.Integer(), nullable=True),
    sa.Column('create_data', sa.DATETIME(), nullable=True),
    sa.Column('last_edit_data', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('new_text', sa.String(length=16), nullable=True),
    sa.Column('article_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('DateTimeOfRequest', sa.DATETIME(), nullable=True),
    sa.Column('Status', sa.String(length=16), nullable=True),
    sa.Column('request_id', sa.String(length=16), nullable=True),
    sa.ForeignKeyConstraint(['article_id'], ['Article.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Request_Status'), 'Request', ['Status'], unique=False)
    op.create_index(op.f('ix_Request_new_text'), 'Request', ['new_text'], unique=False)
    op.create_index(op.f('ix_Request_request_id'), 'Request', ['request_id'], unique=False)
    op.drop_index('ix_Request_Status', table_name='request')
    op.drop_index('ix_Request_new_text', table_name='request')
    op.drop_index('ix_Request_request_id', table_name='request')
    op.drop_table('request')
    op.drop_table('article')
    op.add_column('user', sa.Column('untipassword', sa.String(length=16), nullable=True))
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)
    op.create_index(op.f('ix_user_firstName'), 'user', ['firstName'], unique=False)
    op.create_index(op.f('ix_user_lastName'), 'user', ['lastName'], unique=False)
    op.create_index(op.f('ix_user_password'), 'user', ['password'], unique=False)
    op.create_index(op.f('ix_user_phone'), 'user', ['phone'], unique=False)
    op.create_index(op.f('ix_user_untipassword'), 'user', ['untipassword'], unique=False)
    op.create_index(op.f('ix_user_userRole'), 'user', ['userRole'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    op.drop_index('ix_User_email', table_name='user')
    op.drop_index('ix_User_firstName', table_name='user')
    op.drop_index('ix_User_lastName', table_name='user')
    op.drop_index('ix_User_password', table_name='user')
    op.drop_index('ix_User_phone', table_name='user')
    op.drop_index('ix_User_userRole', table_name='user')
    op.drop_index('ix_User_username', table_name='user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_User_username', 'user', ['username'], unique=False)
    op.create_index('ix_User_userRole', 'user', ['userRole'], unique=False)
    op.create_index('ix_User_phone', 'user', ['phone'], unique=False)
    op.create_index('ix_User_password', 'user', ['password'], unique=False)
    op.create_index('ix_User_lastName', 'user', ['lastName'], unique=False)
    op.create_index('ix_User_firstName', 'user', ['firstName'], unique=False)
    op.create_index('ix_User_email', 'user', ['email'], unique=False)
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_userRole'), table_name='user')
    op.drop_index(op.f('ix_user_untipassword'), table_name='user')
    op.drop_index(op.f('ix_user_phone'), table_name='user')
    op.drop_index(op.f('ix_user_password'), table_name='user')
    op.drop_index(op.f('ix_user_lastName'), table_name='user')
    op.drop_index(op.f('ix_user_firstName'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_column('user', 'untipassword')
    op.create_table('article',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('author_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('text', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('create_data', mysql.DATETIME(), nullable=True),
    sa.Column('last_edit_data', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], name='article_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('request',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('new_text', mysql.VARCHAR(length=16), nullable=True),
    sa.Column('article_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('DateTimeOfRequest', mysql.DATETIME(), nullable=True),
    sa.Column('Status', mysql.VARCHAR(length=16), nullable=True),
    sa.Column('request_id', mysql.VARCHAR(length=16), nullable=True),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], name='request_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_Request_request_id', 'request', ['request_id'], unique=False)
    op.create_index('ix_Request_new_text', 'request', ['new_text'], unique=False)
    op.create_index('ix_Request_Status', 'request', ['Status'], unique=False)
    op.drop_index(op.f('ix_Request_request_id'), table_name='Request')
    op.drop_index(op.f('ix_Request_new_text'), table_name='Request')
    op.drop_index(op.f('ix_Request_Status'), table_name='Request')
    op.drop_table('Request')
    op.drop_table('Article')
    # ### end Alembic commands ###