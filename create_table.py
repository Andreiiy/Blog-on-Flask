from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String,Integer, MetaData



db_string = "postgresql://postgres:postgres@localhost/flask_blog"

db = create_engine(db_string)

meta = MetaData(db)
tablepost =  Table(
   'posts', meta,
   Column('id', Integer, primary_key = True),
   Column('title', String),
   Column('text', String),
   Column('author', String)
)

with db.connect() as conn:

    # Create
    tablepost.create()
    insert_statement = tablepost.insert().values(title="First", text="My first post", author="Andrei")
    conn.execute(insert_statement)

    # Read
    select_statement = tablepost.select()
    result_set = conn.execute(select_statement)
    for r in result_set:
        print(r)