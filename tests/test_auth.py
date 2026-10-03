import sqlite3

import pytest

from fitframe import app as app_module


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(app_module, "DB", str(tmp_path / "fitframe-test.db"))
    app_module.init_db()
    app_module.app.config.update(TESTING=True, SECRET_KEY="test-secret")
    with app_module.app.test_client() as test_client:
        yield test_client


def test_register_login_and_protected_pages(client):
    response = client.get("/history")
    assert response.status_code == 302
    assert "/login?next=/history" in response.headers["Location"]
    response = client.post("/analyze")
    assert response.status_code == 302
    assert "/login?next=/start" in response.headers["Location"]

    response = client.post("/register", data={
        "email": "Style@example.com",
        "password": "silk-and-linen",
        "confirm_password": "silk-and-linen",
    })
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/start")
    assert client.get("/history").status_code == 200

    with sqlite3.connect(app_module.DB) as connection:
        stored_hash = connection.execute("SELECT password_hash FROM users").fetchone()[0]
    assert stored_hash != "silk-and-linen"

    client.post("/logout")
    response = client.post("/login", data={"email": "style@example.com", "password": "silk-and-linen"})
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/start")


def test_register_rejects_mismatched_passwords(client):
    response = client.post("/register", data={
        "email": "style@example.com",
        "password": "silk-and-linen",
        "confirm_password": "linen-and-silk",
    })
    assert response.status_code == 400
    assert b"Those passwords do not match" in response.data


def test_homepage_prioritizes_signup_and_signin_has_no_lamp(client):
    homepage = client.get("/")
    assert b'href="/register">Sign up</a>' in homepage.data
    assert b'Already have an account?' in homepage.data
    assert b'href="/login?lamp=1">Sign in</a>' in homepage.data

    signup = client.get("/register")
    signin = client.get("/login")
    home_signin = client.get("/login?lamp=1")
    signup_signin = client.get("/login?lamp=0")
    assert b'id="lamp-toggle"' in signup.data
    assert b'id="lamp-toggle"' not in signin.data
    assert b'aria-hidden="true" inert' not in signin.data
    assert b'id="lamp-toggle"' in home_signin.data
    assert b'id="lamp-toggle"' not in signup_signin.data