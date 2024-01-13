from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

table_name = "items"
columns = (
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("name", sa.String, index=True),
    sa.Column("description", sa.String),
)

revision: str = '001'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_table(
        table_name,
        *columns
    )

def downgrade():
    op.drop_table(table_name)