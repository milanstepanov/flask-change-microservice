"""App testing ground."""

from app import change


def test_change():
    """Test change method."""
    assert [{5: "quarters"}, {1: "nickels"}, {4: "pennies"}] == change(1.34)
