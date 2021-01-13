#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import pytest
from fastapi.testclient import TestClient
from tortoise.contrib.fastapi import register_tortoise

from app.config import Settings, get_settings
from app.main import create_application


def get_settings_override():
    return Settings(testing=True, database_url=os.getenv("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app():

    app = create_application()

    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(app) as test_client:

        yield test_client


@pytest.fixture(scope="module")
def test_app_with_db():
    app = create_application()

    app.dependency_overrides[get_settings] = get_settings_override

    register_tortoise(
        app,
        db_url=os.getenv("DATABASE_TEST_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

    with TestClient(app) as test_client:

        yield test_client
