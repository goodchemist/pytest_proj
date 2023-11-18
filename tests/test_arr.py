import pytest

from utils import arrs


@pytest.mark.parametrize('array, index, default, expect', [
    ([1, 2, 3], 1, "test", 2),
    ([], 0, "test", "test")
])
def test_get(array, index, default, expect):
    assert arrs.get(array, index, default) == expect


def test_slice(array_fixture):
    assert arrs.my_slice(array_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(array_fixture, 1) == [2, 3, 4]
    assert arrs.my_slice(array_fixture, ) == [1, 2, 3, 4]


def test_slise__empty_array():
    assert arrs.my_slice([]) == []


def test_get_val(data_fixture):
    assert arrs.get_val(data_fixture, "apple") == "fruit"
    assert arrs.get_val(data_fixture, "apple", "404") == "fruit"
    assert arrs.get_val({}, "apple") == "not found"
    assert arrs.get_val({}, "apple", "404") == "404"
    assert arrs.get_val(data_fixture, "banana") == "not found"
    assert arrs.get_val(data_fixture, "banana", "404") == "404"
