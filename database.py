from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlPath = 'database.db'
sql_url = f"sqlite:///./{sqlPath}"
engine = create_engine(sql_url,connect_args={"check_same_thread": False})

sessionLocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)

base = declarative_base()