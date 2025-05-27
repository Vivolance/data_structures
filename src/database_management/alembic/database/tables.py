"""
Define Schema odf your table here, and set metadata to allow alembic to know we are targeting this file
"""

from sqlalchemy import MetaData, Table, Column, FLOAT, TEXT, DateTime

metadata: MetaData = MetaData()


kucoin_table: Table = Table(
    "kucoin_result",
    metadata,
    Column("symbol", TEXT, primary_key=True),
    Column("price", FLOAT, nullable=False),
    Column("time", DateTime, nullable=False),
    Column("source", TEXT, nullable=False),
    Column("created_at", DateTime, nullable=False),
)
