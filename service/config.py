"""
Global Configuration for Application
"""
import os

# Read DATABASE_URI from environment
DATABASE_URI = os.getenv("DATABASE_URI")

# If DATABASE_URI is not set, or if it points to a local PostgreSQL instance that isn't running,
# default to SQLite for unit testing.
if not DATABASE_URI or "localhost" in DATABASE_URI or "127.0.0.1" in DATABASE_URI:
    DATABASE_URI = "sqlite:///test.db"

# Configure SQLAlchemy
SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
