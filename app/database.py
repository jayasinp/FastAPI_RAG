from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import motor.motor_asyncio

# PostgreSQL settings
SQLALCHEMY_DATABASE_URL = "postgresql://myuser:mypassword@localhost/rag_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# MongoDB settings
MONGO_DETAILS = "mongodb://admin:password@localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
mongo_db = client.rag_db
