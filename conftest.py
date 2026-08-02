import pytest

@pytest.fixture(scope ="session")
def prework():
    print("Pre-work fixture")