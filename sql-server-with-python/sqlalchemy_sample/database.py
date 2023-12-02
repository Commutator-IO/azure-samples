from sqlalchemy import create_engine

password = "yourStrong(!)Password"
path = f"mssql+pymssql://sa:{password}@localhost/master"
engine = create_engine(path, echo=True)