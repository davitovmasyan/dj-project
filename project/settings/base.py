import os

import environ

__all__ = (
    "PROJECT_DIR",
    "BASE_DIR",
    "ENV",
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Read configuration variables from .env file
ENV = environ.Env()
environ.Env.read_env(".env")
