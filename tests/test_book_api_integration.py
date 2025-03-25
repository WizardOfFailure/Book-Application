import pytest
from api.book_api import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add_book(client):
    response = client.post('/add_book', json={"title": "Python 101", "author": "John Doe"})
    assert response.status_code == 201
    assert response.json['message'] == "Book added successfully!"

def test_delete_book(client):
    client.post('/add_book', json={"title": "Python 101", "author": "John Doe"})
    response = client.delete('/delete_book', json={"title": "Python 101", "author": "John Doe"})
    assert response.status_code == 200