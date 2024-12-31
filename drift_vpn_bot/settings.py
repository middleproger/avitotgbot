import os
from dotenv import load_dotenv
import pathlib

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

# Access environment variables
TOKEN = os.getenv("TG_BOT_TOKEN")
BASE_URL = os.getenv("BASE_URL")
PUBLIC_IP = os.getenv("PUBLIC_IP")
CERTIFICATE_PATH = os.getenv("CERTIFICATE_PATH")
WEB_SERVER_HOST = "127.0.0.1"
WEB_SERVER_PORT = 8888
BOT_PATH = f"/webhook/bot/{TOKEN[:23]}"
BASE_DIR = pathlib.Path(__file__).parent
TEMPLATE_DIR = BASE_DIR / "templates"