import pytest

ARRAY = [1, 2, 3, 4]
DATA_DICTIONARY = {"apple": "fruit"}


@pytest.fixture
def array_fixture():
    return ARRAY.copy()


@pytest.fixture()
def data_fixture():
    return DATA_DICTIONARY
