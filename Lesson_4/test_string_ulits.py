import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize(["imput_data", "expected_data"], [("1hello", "1hello"), ("", ""), ("R", "R")])
def test_capitalize_negativ(self, imput_data: str, expected_data: str):
        res = string_funcs.capitalize(string=imput_data)
        assert result == expected_data

@pytest.mark.parametrize(["imput_data", "simbol" "expected"], [("hello", "e" True), (" 123", " " True), ("RER", "R" True)])
def test_contains_positiv(self, imput_data: str, simbol: str, expected: bool):
        res = string_funcs.contains(string=imput_data, symbol=simbol)
        assert res == expected

@pytest.mark.parametrize(["imput_data", "simbol" "expected"], [("hello", "e" True), ("Flai", "F" True), ("Test", "T" True)])
def test_delete_simbol_positiv(self, imput_data: str, simbol: str, expected: bool):
        res = string_funcs.delete_simbol(string=imput_data, symbol=simbol)
        assert res == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


def test_delete_symbol_from_list_positive(utils, input_list, symbol, expected_output_list):
    result = [utils.delete_symbol(string, symbol) for string in input_list]
    assert result == expected_output_list


