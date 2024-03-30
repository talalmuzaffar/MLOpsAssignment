import pytest
import json
from app import app  # Assuming your Flask app is in a file named app.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_predict_endpoint(client):
    # Define a sample request data with features
    data = {'features': [5.1, 3.5, 1.4, 0.2]}
    
    # Send a POST request to the /predict endpoint
    response = client.post('/predict', json=data)
    
    # Check if the response is successful (HTTP status code 200)
    assert response.status_code == 200
    
    # Parse the JSON response
    prediction = json.loads(response.data)
    
    # Check if the prediction is as expected (e.g., setosa)
    assert prediction['prediction'] == 'setosa'

def test_accuracy_endpoint(client):
    # Send a GET request to the /accuracy endpoint
    response = client.get('/accuracy')
    
    # Check if the response is successful (HTTP status code 200)
    assert response.status_code == 200
    
    # Parse the JSON response
    accuracy_data = json.loads(response.data)
    
    # Check if the accuracy is within the expected range (e.g., between 0 and 1)
    assert 0 <= accuracy_data['accuracy'] <= 1
