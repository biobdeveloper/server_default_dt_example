"""add trigger

Revision ID: 72e251f4377c
Revises: e3eae0c0e578
Create Date: 2022-09-14 02:12:04.035481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72e251f4377c'
down_revision = 'e3eae0c0e578'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    CREATE OR REPLACE FUNCTION update_updated_at()   
    RETURNS TRIGGER AS $$
    BEGIN
        NEW.updated_at = now();
        RETURN NEW;   
    END;
    $$ language 'plpgsql';
    """)
    op.execute("""
    CREATE TRIGGER update_foo_updated_at
    BEFORE UPDATE ON foo FOR EACH ROW EXECUTE PROCEDURE update_updated_at();""")


def downgrade() -> None:
    pass
