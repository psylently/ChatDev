'''
This module contains tests for the web application.
'''
import pytest
from main import app
from libretranslate import translate_text
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
def test_index(client):
    '''
    Test the index route of the web application.
    '''
    response = client.get('/')
    assert response.status_code == 200
    assert b'Translate Text' in response.data
def test_translate(client):
    '''
    Test the translation functionality of the web application.
    '''
    response = client.post('/translate', data={'text': 'Bonjour'})
    assert response.status_code == 200
    assert b'Hello' in response.data