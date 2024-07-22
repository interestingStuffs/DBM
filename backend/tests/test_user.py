import pytest
from pydantic import ValidationError
from app.models.user import UserCreate, UserUpdate, UserInDB

def test_user_create_valid():
    user = UserCreate(username="testuser", email="test@example.com", password="securepassword")
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.password == "securepassword"

def test_user_create_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(username="testuser", email="invalid-email", password="securepassword")

def test_user_update_valid():
    user_update = UserUpdate(username="testuser", email="test@example.com")
    assert user_update.username == "testuser"
    assert user_update.email == "test@example.com"
    assert user_update.password is None

def test_user_in_db():
    user_db = UserInDB(id="12345", username="testuser", email="test@example.com")
    assert user_db.id == "12345"
    assert user_db.username == "testuser"
    assert user_db.email == "test@example.com"
