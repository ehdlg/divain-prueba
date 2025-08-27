import os
from pathlib import Path

from dotenv import load_dotenv

app_env = os.getenv("ENV", "dev").lower()
app_dir = Path.cwd() / "app"

env_files = [".env", f".env.{app_env}"]

for env_file in env_files:
    env_path = app_dir / env_file
    if not os.path.exists(env_path):
        continue

    load_dotenv(dotenv_path=env_path, override=True)


DATABASE_URL = os.getenv("DATABASE_URL")
