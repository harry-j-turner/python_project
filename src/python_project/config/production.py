"""Production configuration."""

# System Imports
import os

# Relative Imports
from .base_config import BaseConfig


class ProductionConfig(BaseConfig):
    """Configuration for production."""

    # Other Configuration
    PLATFORM_URL: str = str(os.getenv("PLATFORM_URL"))
    CONNECTION_TIMEOUT: int = int(os.getenv("CONNECTION_TIMEOUT", 5))
    FILE_DIRECTORY: str = "p2d/pointclouds"

    # S3 configuration
    AWS_ENDPOINT_URL: str = str(os.getenv("AWS_ENDPOINT_URL"))
    AWS_USE_SSL: bool = True
    AWS_ACCESS_KEY_ID: str = str(os.getenv("AWS_ACCESS_KEY_ID"))
    AWS_SECRET_ACCESS_KEY: str = str(os.getenv("AWS_SECRET_ACCESS_KEY"))
    AWS_BUCKET_NAME: str = str(os.getenv("AWS_BUCKET_NAME"))
    AWS_REGION: str = str(os.getenv("AWS_REGION"))
