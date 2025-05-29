from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

# Create database connection URL
DATABASE_URL = URL.create(
    drivername='postgresql+psycopg2',
    username='hello_fastapi',
    password='hello_fastapi',
    host='13.200.156.37',
    port=5432,
    database='hello_fastapi_dev'
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
