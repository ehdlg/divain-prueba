import os
import sys

from dotenv import load_dotenv
from sqlmodel import create_engine

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "")

if not DATABASE_URL:
    print("Error: DATABASE_URL not set.")

    sys.exit(1)

try:
    engine = create_engine(DATABASE_URL, echo=True)
except Exception as e:
    print(f"Failed to create engine: {e}")

    sys.exit(1)
