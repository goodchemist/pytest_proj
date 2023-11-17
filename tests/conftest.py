import pytest

ARRAY = [1, 2, 3, 4]


@pytest.fixture
def array_fixture():
    return ARRAY.copy()
