"""Local testing configuration."""

# Third Party Imports
import boto3
import botocore.client
import classutilities

# Relative Imports
from .base_config import BaseConfig


class LocalTestingConfig(BaseConfig):
    """Configuration for local testing."""

    # Other Configuration
    PLATFORM_URL: str = "http://pbe"
    CONNECTION_TIMEOUT: int = 5
    FILE_DIRECTORY: str = "p2d/pointclouds"

    # S3 configuration
    AWS_BUCKET_NAME: str = "demo"
    AWS_REGION: str = "us-east-1"

    @classutilities.classproperty
    def S3_CLIENT(cls) -> botocore.client.BaseClient:
        """Create S3 client (connector)."""
        return boto3.client(service_name="s3", region_name=cls.AWS_REGION)