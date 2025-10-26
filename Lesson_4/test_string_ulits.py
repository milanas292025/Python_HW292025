import pytest
from string_ulits import StringUtils

string_ulits = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_ulits.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize(["input_data", "expected_data"], [
    ("1hello", "1hello"),
    ("", ""),
    (" ", " ")
])
def test_capitalize_negative(input_data, expected_data):
        assert string_ulits.capitalize(input_data) == expected_data


@pytest.mark.positive
@pytest.mark.parametrize(["input_data", "expected"], [
    ("hello", "e"),
    (" 123", " "),
    ("RER", "R")
])
def test_contains_positive(input_data, expected):
        assert string_ulits.contains(input_data, expected) == expected

@pytest.mark.negative
@pytest.mark.parametrize(["input_data", "expected"], [
    ("hello", "a"),
    (" 123", "R"),
    ("RER", "12")
])
def test_contains_negative(input_data, expected):
        assert not string_ulits.contains(input_data, expected) == expected


@pytest.mark.positive
@pytest.mark.parametrize(["input_data", "expected"], [
    (" hello", "hello"),
    (" 123", "123"),
    (" RER", "RER")
])
def test_trim_positive(input_data, expected):
    assert string_ulits.contains(input_data, expected) == expected

@pytest.mark.negative
@pytest.mark.parametrize(["input_data", "expected"], [
    ("hello", "hello"),
    ("123", "123"),
    ("RER", "RER")
])
def test_trim_negative(input_data, expected):
    assert string_ulits.contains(input_data, expected) == expected


@pytest.mark.positive
@pytest.mark.parametrize(["input_data", "expected"], [
    ("hello", "e"),
    ("Test", "T"),
    ("skip", "i")
])
def test_delete_simbol_positive(input_data, expected):
        assert string_ulits.delete_symbol(input_data, expected)

@pytest.mark.negative
@pytest.mark.parametrize(["input_data", "expected"], [
    ("hello", "r"),
    ("Test", "7"),
    ("skip", " ")
])
def test_delete_symbol_from_list_negative(input_data, expected):
        assert string_ulits.delete_symbol(input_data, expected)
