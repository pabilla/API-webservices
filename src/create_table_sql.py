from sqlalchemy import create_engine
from sqlalchemy import text

db_string = "postgresql://root:root@localhost:5432/store"

engine = create_engine(db_string)
connection = engine.connect()

create_user_table_query = """
CREATE TABLE IF NOT EXISTS Users (
    id SERIAL PRIMARY KEY,
    firstname text NOT NULL,
    lastname text NOT NULL,
    age INT,
    email CHAR(50),
    job CHAR(50)
);
"""
create_application_table_query = """
CREATE TABLE IF NOT EXISTS application (
    id SERIAL PRIMARY KEY,
    appname text,
    username text,
    lastconnection DATE,
    user_id INT references Users(id)
);
"""

connection.execute(text(create_user_table_query))
connection.execute(text(create_application_table_query))

connection.commit()
connection.close()