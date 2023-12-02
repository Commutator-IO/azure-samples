import sqlalchemy
from .database import engine
from sqlalchemy import text
from sqlalchemy.orm import Session

def select_hello():
    with Session(engine) as session:
        result = session.execute(text("select 'hello world'"))
        print(result.all())

def insert_values():
    with Session(engine) as session:
        session.execute(text("CREATE TABLE some_table (x int, y int)"))
        session.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
        )
        session.commit()

if __name__ == "__main__":
    print(sqlalchemy.__version__)
    print(engine)
    select_hello()
    insert_values()
