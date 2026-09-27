cat << 'EOF' > service/config.py
"""
Global Configuration for Application
"""
import os

# Read DATABASE_URI from environment
DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///test.db")

# Force SQLite if running tests or if pointing to localhost/postgresql without a running DB
if "localhost" in DATABASE_URI or "127.0.0.1" in DATABASE_URI or "postgresql" in DATABASE_URI:
    DATABASE_URI = "sqlite:///test.db"

SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
EOF