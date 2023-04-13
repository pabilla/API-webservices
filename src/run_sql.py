from sqlalchemy import create_engine
from sqlalchemy import text

db_string = "postgresql://root:root@localhost:5432/store"

engine = create_engine(db_string)
connection = engine.connect()

create_table_query = """
CREATE TABLE IF NOT EXISTS films (
    title text,
    director text,
    year text
);
"""
insert_data_query = """
INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scoot Derrickson', '2016')
"""

connection.execute(text(create_table_query))
connection.execute(text(insert_data_query))

connection.commit()

connection.close()


#Create
#connection.execute(text("CREATE TABLE IF NOT EXISTS film (title text, director text, year text"))
#connection.execute(text("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scoot Derrickson', '2016')"))