import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test if the home endpoint is running successfully"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Welcome to ACEest Fitness & Gym API" in rv.data

def test_calculate_calories_valid(client):
    """Test accurate calorie calculation for Fat Loss program"""
    rv = client.post('/calculate_calories', json={"weight": 70, "program": "Fat Loss (FL)"})
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data["target_calories"] == 1540  # 70 * 22

def test_calculate_calories_invalid_program(client):
    """Test error handling for an invalid program"""
    rv = client.post('/calculate_calories', json={"weight": 70, "program": "CrossFit"})
    assert rv.status_code == 400
    assert b"Invalid program selected" in rv.data