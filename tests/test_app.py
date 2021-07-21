from app import index
export PYTHONPATH=src
def test_index():
    assert index() == "Hello World"