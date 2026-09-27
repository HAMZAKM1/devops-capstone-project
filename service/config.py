"""
Global Configuration for Application
"""
import os

# Get configuration from environment
DATABASE_URI = os.getenv("DATABASE_URI")

# Build DATABASE_URI from environment variables if not directly set
if not DATABASE_URI:
    DATABASE_USER = os.getenv("DATABASE_USER", "postgres")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "postgres")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "postgres")
    DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")

    # If running locally without PostgreSQL host, fall back to SQLite
    if DATABASE_HOST == "localhost":
        DATABASE_URI = "sqlite:///test.db"
    else:
        DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# Configure SQLAlchemy
SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
