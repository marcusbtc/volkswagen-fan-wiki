import os

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")
ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "ALLOWED_ORIGINS",
        "http://localhost:3000,https://volkswagen-fan-wiki.com",
    ).split(",")
    if origin.strip()
]

os.makedirs(UPLOAD_DIR, exist_ok=True)
