import pytest
from fastapi.testclient import TestClient

from insult_generator.app import app
from insult_generator.entities import Insult


@pytest.fixture()
def fixed_insult():
    return "artless", "base-court", "apple-john"


@pytest.fixture()
def fake_insult_db(fixed_insult):
    class FakeInsultDB:
        @staticmethod
        def get_insult():
            return Insult(*fixed_insult)

    return FakeInsultDB()


@pytest.fixture()
def client():
    return TestClient(app)
