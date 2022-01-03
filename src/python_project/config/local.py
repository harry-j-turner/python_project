"""Local configuration."""

# Relative Imports
from .base_config import BaseConfig


class LocalConfig(BaseConfig):
    """Configuration for local stack."""

    # Other Configuration
    PLATFORM_URL: str = "http://pbe"
    CONNECTION_TIMEOUT: int = 5
    FILE_DIRECTORY: str = "p2d/pointclouds"

    # S3 configuration
    AWS_ENDPOINT_URL: str = "http://p2d-localstack-service.p2d.svc.cluster.local:4566/"
    AWS_USE_SSL: bool = False
    AWS_ACCESS_KEY_ID: str = "xyz"
    AWS_SECRET_ACCESS_KEY: str = "123"
    AWS_BUCKET_NAME: str = "demo"
    AWS_REGION: str = "us-east-1"