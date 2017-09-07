import pytest
from datatyping import validate


def test_empty():
    assert validate((), ()) is None


def test_plain():
    assert validate((int, ), (1, 2, 3, 4, 5)) is None


def test_plain_typeerror():
    with pytest.raises(TypeError):
        validate((int, ), (1, 2, 3, 4.5))


def test_dict_empty():
    assert validate((dict, ), ({}, {}, {})) is None


def test_dict_strict():
    assert validate(({'a': int}, ), ({'a': 123}, {'a': 456})) is None


def test_dict_nested():
    assert validate(({'a': {'b': (dict,)}},),
        (
            {'a': {'b': ({}, {})}},
            {'a': {'b': ({'any': 'key'}, {'used': 'here'})}},
        )) is None


def test_list_error():
    with pytest.raises(AssertionError):
        validate([int], (1, 2, 3))
