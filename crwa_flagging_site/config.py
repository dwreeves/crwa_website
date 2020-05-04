"""
Configurations for the website.
"""
import os
from dataclasses import dataclass

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
KEYS_FILE = os.path.join(ROOT_DIR, 'keys.yml')

@dataclass
class ConfigType:
    DEBUG: bool = False
    TESTING: bool = False
    CSRF_ENABLED: bool = True
    SECRET_KEY: str = 'this-really-needs-to-be-changed'
    DATABASE: str = None


class ProductionConfig(ConfigType):
    DEBUG: bool = False


class StagingConfig(ConfigType):
    DEVELOPMENT: bool = True
    DEBUG: bool = True


class DevelopmentConfig(ConfigType):
    DEVELOPMENT: bool = True
    DEBUG: bool = True


class TestingConfig(ConfigType):
    TESTING: bool = True
