import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

APP_PATH = Path(__file__).parent.parent
APP_ENV = os.getenv("APP_ENV")
LOG_LEVEL = os.getenv("LOG_LEVEL")
APP_PORT = int(os.getenv("PORT"))
