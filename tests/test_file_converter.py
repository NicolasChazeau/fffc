# -*- coding: utf-8 -*-

import pytest

from file_converter.file_converter import FileConverter
from file_converter.column_types import DATE_TYPE, NUMERIC_TYPE, STRING_TYPE


INPUT_METADATA = [
    {
        "name": "Birth date",
        "size": 10,
        "type": "date",
    },
    {
        "name": "First name",
        "size": 15,
        "type": "string",
    },
    {
        "name": "Last name",
        "size": 15,
        "type": "string",
    },
    {
        "name": "Weight",
        "size": 5,
        "type": "numeric",
    },
]


def test_convert_value_01():
    """Test for date type"""
    value_type = DATE_TYPE
    input_tests = [
        "2021-03-01",
        "   2021-03-01",
        "2021-03-01     "
    ]
    expected_result = "01/03/2021"
    for test in input_tests:
        assert FileConverter.convert_value(test, value_type) == expected_result


def test_convert_value_02():
    """Test for numeric type"""
    value_type = NUMERIC_TYPE
    input_tests = [
        "-3.2",
        "-3.2   ",
        "   -3.2"
    ]
    expected_result = "-3.2"
    for test in input_tests:
        assert FileConverter.convert_value(test, value_type) == expected_result


def test_convert_value_03():
    """Test for string type"""
    value_type = STRING_TYPE
    input_tests = [
        "Un, test",
        "Un, test   ",
        "   Un, test"
    ]
    expected_result = "Un, test"
    for test in input_tests:
        assert FileConverter.convert_value(test, value_type) == expected_result


def test_convert_line_01():
    input_line = '1970-01-01John           Smith           81.5'
    expected_result = '01/01/1970,John,Smith,81.5'
    my_file_converter = FileConverter(INPUT_METADATA)
    assert my_file_converter.convert_line(input_line) == expected_result


def test_convert_line_02():
    input_line = '1970-01-01JohnSmith81.5'
    my_file_converter = FileConverter(INPUT_METADATA)
    with pytest.raises(Exception):
        my_file_converter.convert_line(input_line)


def test_file_converter_01():
    """Test basic example for file converter"""
    input_data = ['1970-01-01John           Smith           81.5',
                  '1975-01-31Jane           Doe             61.1',
                  '1988-11-28Bob            Big            102.4']
    expected_result = ['Birth date,First name,Last name,Weight',
                       '01/01/1970,John,Smith,81.5',
                       '31/01/1975,Jane,Doe,61.1',
                       '28/11/1988,Bob,Big,102.4']
    my_file_converter = FileConverter(INPUT_METADATA)
    assert my_file_converter.get_header() == expected_result[0]
    converted_data = list(my_file_converter.convert_data_generator(input_data))
    assert converted_data == expected_result[1:]
