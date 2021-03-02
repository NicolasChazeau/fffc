# -*- coding: utf-8 -*-

import pytest

from file_converter.file_converter import FileConverter


SEP = ","
LINE_SEP = "\r\n"
ENCODING = "utf8"

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


def test_convert_line_01():
    input_line = '1970-01-01John           Smith           81.5'
    expected_result = '01/01/1970,John,Smith,81.5'
    my_file_converter = FileConverter(INPUT_METADATA, sep=SEP, line_sep=LINE_SEP, encoding=ENCODING)
    assert my_file_converter.convert_line(input_line) == expected_result


def test_convert_line_02():
    """Malformed line"""
    input_line = '1970-01-01JohnSmith81.5'
    my_file_converter = FileConverter(INPUT_METADATA, sep=SEP, line_sep=LINE_SEP, encoding=ENCODING)
    with pytest.raises(Exception):
        my_file_converter.convert_line(input_line)


def test_convert_line_03():
    """Bad line size"""
    input_line = '1970-01-01John           Smith           81.5AAA'
    my_file_converter = FileConverter(INPUT_METADATA, sep=SEP, line_sep=LINE_SEP, encoding=ENCODING)
    with pytest.raises(Exception):
        my_file_converter.convert_line(input_line)


def test_file_converter_01():
    """Basic tests for file converter"""
    input_data = ['1970-01-01John           Smith           81.5',
                  '1975-01-31Jane           Doe             61.1',
                  '1988-11-28Bob            Big            102.4']
    expected_result = ['Birth date,First name,Last name,Weight',
                       '01/01/1970,John,Smith,81.5',
                       '31/01/1975,Jane,Doe,61.1',
                       '28/11/1988,Bob,Big,102.4']
    my_file_converter = FileConverter(INPUT_METADATA, sep=SEP, line_sep=LINE_SEP, encoding=ENCODING)
    assert my_file_converter.get_header() == expected_result[0]
    converted_data = list(my_file_converter.convert_data_generator(input_data))
    assert converted_data == expected_result[1:]


def test_convert_and_write_csv_01():
    input_data_file = "./tests/input/test_convert_and_write_input_data.txt"
    output_file = "./tests/output/test_convert_and_write_output_data.csv"
    my_file_converter = FileConverter(INPUT_METADATA, sep=SEP, line_sep=LINE_SEP, encoding=ENCODING)
    my_file_converter.convert_file_and_write_to_csv(input_data_file, output_file)
    of1 = open(output_file)
    of2 = open("./tests/input/test_convert_and_write_expected_result.csv")
    for line1, line2 in zip(of1, of2):
        assert line1 == line2
    of1.close()
    of2.close()


def test_convert_and_write_csv_02():
    """Output file with bad extension"""
    input_data_file = "./tests/input/test_convert_and_write_input_data.txt"
    output_file = "./tests/output/test_convert_and_write_output_data.txt"
    my_file_converter = FileConverter(INPUT_METADATA, sep=SEP, line_sep=LINE_SEP, encoding=ENCODING)
    with pytest.raises(Exception):
        my_file_converter.convert_file_and_write_to_csv(input_data_file, output_file)


def test_convert_and_write_csv_03():
    """Input data file with bad path"""
    input_data_file = "UNKNOW_PATH"
    output_file = "./tests/output/test_convert_and_write_output_data.csv"
    my_file_converter = FileConverter(INPUT_METADATA, sep=SEP, line_sep=LINE_SEP, encoding=ENCODING)
    with pytest.raises(Exception):
        my_file_converter.convert_file_and_write_to_csv(input_data_file, output_file)
