# -*- coding: utf-8 -*-

from file_converter.file_converter import FileConverter


def test_example():
    data = ['1970-01-01John           Smith           81.5',
            '1975-01-31Jane           Doe             61.1',
            '1988-11-28Bob            Big            102.4']
    metadata = ['Birth date,10,date',
                'First name,15,string',
                'Last name,15,string',
                'Weight,5,numeric']
    expected_result = ['Birth date,First name,Last name,Weight',
                       '01/01/1970,John,Smith,81.5',
                       '31/01/1975,Jane,Doe,61.1',
                       '28/11/1988,Bob,Big,102.4']
    my_file_converter = FileConverter()
    assert my_file_converter.convert(data, metadata) == expected_result
