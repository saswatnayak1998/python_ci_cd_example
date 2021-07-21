from src import app
from app import index
def test_index():
    assert index() == "Hello World"