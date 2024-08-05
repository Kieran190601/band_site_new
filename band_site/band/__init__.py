# band/__init__.py

# Import specific components for convenience
from .admin import *
from .models import *
from .views import *
from .urls import *

# Example setup, such as logging
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.info("Band package initialized.")
