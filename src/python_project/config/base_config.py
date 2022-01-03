"""Base config that all configs must override."""

# Third Party Imports
import boto3
import botocore.client
import classutilities


class BaseConfig(classutilities.ConfigClassMixin):
    """Base class for app configuration."""

    # Other Configuration
    PLATFORM_URL: str
    CONNECTION_TIMEOUT: int
    FILE_DIRECTORY: str

    # S3 configuration
    AWS_ENDPOINT_URL: str
    AWS_USE_SSL: bool
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_BUCKET_NAME: str  # Name of S3 bucket
    AWS_REGION: str  # AWS region where bucket is located

    @classutilities.classproperty
    def S3_CLIENT(cls) -> botocore.client.BaseClient:
        """Create S3 client (connector)."""
        return boto3.client(
            service_name="s3",
            aws_access_key_id=cls.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=cls.AWS_SECRET_ACCESS_KEY,
            endpoint_url=cls.AWS_ENDPOINT_URL,
            use_ssl=cls.AWS_USE_SSL,
            region_name=cls.AWS_REGION,
            config=botocore.client.Config(signature_version="s3v4"),
        )