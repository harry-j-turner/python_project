"""Dispatch the appropriate CONFIG object based on the configuration required."""

# System Imports
import os

# Relative Imports
from .base_config import BaseConfig
from .local import LocalConfig
from .local_testing import LocalTestingConfig
from .production import ProductionConfig

environment = os.getenv("ENVIRONMENT", "LOCAL")

CONFIG: type[BaseConfig] = LocalConfig
if environment == "PRODUCTION" or environment == "STAGING":
    CONFIG = ProductionConfig
elif environment == "LOCAL_TESTING":
    CONFIG = LocalTestingConfig