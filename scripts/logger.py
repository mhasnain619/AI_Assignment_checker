import logging
import warnings
import os

# Ignore warnings
warnings.filterwarnings("ignore")

# Ensure log directory exists
os.makedirs("./log", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="./log/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def get_logger(name):
    """Return a logger instance."""
    return logging.getLogger(name)