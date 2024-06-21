import os
from dotenv import load_dotenv, find_dotenv  # type: ignore
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.orm import sessionmaker, declarative_base  # type: ignore

load_dotenv()

# Utiliser une chaîne multi-lignes pour éviter les problèmes de formatage avec Prettier
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

# Créer l'engine SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
