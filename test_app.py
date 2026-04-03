import pytest
import os
from app import app, init_db

TEST_DB = "test_aceest.db"

@pytest.fixture
def client():
    """Setup a temporary test database and Flask test client."""
    app.config['TESTING'] = True
    # Point the app to a temporary database for testing
    import app as my_app
    my_app.DB_NAME = TEST_DB
    
    init_db(TEST_DB)
    
    with app.test_client() as client:
        yield client
        
    # Teardown: Remove the test database after tests run
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

def test_home_endpoint(client):
    """Test if the UI loads successfully"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"ACEest Functional Fitness System" in rv.data

def test_add_client_valid(client):
    """Test accurate calorie calculation and DB insertion"""
    rv = client.post('/add_client', json={
        "name": "Test User",
        "age": 25,
        "weight": 70, 
        "program": "Fat Loss (FL)"
    })
    assert rv.status_code == 201
    json_data = rv.get_json()
    assert json_data["calories"] == 1540  # 70 * 22

def test_add_client_invalid_program(client):
    """Test error handling for an invalid program"""
    rv = client.post('/add_client', json={
        "name": "Bad User",
        "weight": 70, 
        "program": "CrossFit"
    })
    assert rv.status_code == 400
    assert b"Invalid program selected" in rv.data