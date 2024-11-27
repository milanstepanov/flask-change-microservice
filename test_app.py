"""App testing ground."""

from app import change
from app import app as application


def test_change():
    """Test change method."""
    assert [{5: "quarters"}, {1: "nickels"}, {4: "pennies"}] == change(1.34)


def test_invoke():
    """Test change method via invoke."""
    client = application.test_client()
    response = client.get('/')
    assert response.status_code == 200, f"Got {response.status_code}"

    response = client.get('/change/1/10')
    assert response.get_json()[0] == {'4': 'quarters'}, {'1': 'dims'}
