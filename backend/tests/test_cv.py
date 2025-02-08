import pytest
from backend.services.cv_service import create_cv, get_cv_by_id, update_cv, delete_cv
from backend.db.connection import db

# Setup test collection
test_cvs_collection = db["test_cvs"]

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    """Clear test database before and after tests."""
    test_cvs_collection.delete_many({})
    yield
    test_cvs_collection.delete_many({})

def test_create_cv():
    """Test creating a CV."""
    cv_data = {
        "user_id": "123",
        "name": "Test User",
        "email": "test@example.com",
        "phone": "123-456-7890",
        "experience": ["Developer"],
        "education": ["BSc Computer Science"],
        "skills": ["Python"],
        "summary": "Test Summary"
    }
    cv_id = create_cv(cv_data)
    assert cv_id is not None

def test_get_cv_by_id():
    """Test retrieving a CV."""
    cv_data = {
        "user_id": "123",
        "name": "Test User",
        "email": "test@example.com"
    }
    cv_id = create_cv(cv_data)
    fetched_cv = get_cv_by_id(cv_id)
    assert fetched_cv["name"] == "Test User"

def test_update_cv():
    """Test updating a CV."""
    cv_data = {"name": "Old Name"}
    cv_id = create_cv(cv_data)
    
    update_cv(cv_id, {"name": "New Name"})
    updated_cv = get_cv_by_id(cv_id)

    assert updated_cv["name"] == "New Name"

def test_delete_cv():
    """Test deleting a CV."""
    cv_data = {"name": "Test Delete"}
    cv_id = create_cv(cv_data)

    delete_cv(cv_id)
    with pytest.raises(Exception):
        get_cv_by_id(cv_id)
