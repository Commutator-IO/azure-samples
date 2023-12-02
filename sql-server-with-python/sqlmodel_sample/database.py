from sqlmodel import SQLModel, create_engine

password = "yourStrong(!)Password"
path = f"mssql+pymssql://sa:{password}@localhost/master"
engine = create_engine(path, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
