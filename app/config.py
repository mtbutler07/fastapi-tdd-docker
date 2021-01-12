#!/usr/bin/env python3

import logging
import os
from functools import lru_cache

from pydantic import BaseSettings, PostgresDsn

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", False)
    database_url: PostgresDsn = os.environ.get("DATABASE_URL")


@lru_cache
def get_settings() -> BaseSettings:
    log.info("Loading configuration settings from environment...")
    return Settings()
