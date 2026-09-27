"""
Global Configuration for Application
"""
import os

# Read DATABASE_URI from environment
DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///test.db")

# Force SQLite if running tests or if DB is pointing to localhost/postgresql
is_local = "localhost" in DATABASE_URI or "127.0.0.1" in DATABASE_URI
is_postgres = "postgresql" in DATABASE_URI

if is_local or is_postgres:
    DATABASE_URI = "sqlite:///test.db"

SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
