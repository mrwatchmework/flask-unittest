import pytest
import sys
sys.path.append("/")

from main import create_app


@pytest.fixture
def app():
    app = create_app()
    yield app


@pytest.fixture
def client():
    return app.test_client()
