import json

from insult_generator.app import app, get_db


def test_heartbeat(client):
    response = client.get("/")
    assert response.status_code == 200
    assert json.loads(response.json()) == {"message": "I'm alive! Are you ready to be insulted?"}


def test_bad_route(client):
    response = client.get("/bad_route")
    assert response.status_code == 404


def test_get_insult(client, fake_insult_db, fixed_insult):
    app.dependency_overrides[get_db] = lambda: fake_insult_db
    response = client.get("/insult")
    assert response.status_code == 200
    assert json.loads(response.json()) == {"message": f"Thou {' '.join(fixed_insult)}"}


def test_get_insult_for_name(client, fake_insult_db, fixed_insult):
    name = "Paul"
    app.dependency_overrides[get_db] = lambda: fake_insult_db
    response = client.get(f"/insult?name={name}")
    assert response.status_code == 200
    assert json.loads(response.json()) == {"message": f"Paul, thou {' '.join(fixed_insult)}"}


def test_get_insult_for_lower_case_name(client, fake_insult_db, fixed_insult):
    name = "paul"
    app.dependency_overrides[get_db] = lambda: fake_insult_db
    response = client.get(f"/insult?name={name}")
    assert response.status_code == 200
    assert json.loads(response.json()) == {"message": f"Paul, thou {' '.join(fixed_insult)}"}


def test_get_insult_for_two_word_name(client, fake_insult_db, fixed_insult):
    name = "paul harrison"
    app.dependency_overrides[get_db] = lambda: fake_insult_db
    response = client.get(f"/insult?name={name}")
    assert response.status_code == 200
    assert json.loads(response.json()) == {"message": f"Paul Harrison, thou {' '.join(fixed_insult)}"}
