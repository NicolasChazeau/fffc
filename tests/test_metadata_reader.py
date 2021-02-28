# -*- coding: utf-8 -*-

import pytest

from file_converter.metadata_reader import MetadataReader


def test_parse_metadata_01():
    metadata = ['Birth date,10,date',
                'First name,15,string',
                'Last name,15,string',
                'Weight,5,numeric']
    expected_result = [
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
    assert MetadataReader.parse_metadata(metadata)


def test_read_metadata_file_01():
    METADATA_FILE = "./tests/input/test_read_metadata_file_01.csv"
    expected_result = [
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
    assert MetadataReader.read_metadata_file(METADATA_FILE) == expected_result


def test_read_metadata_file_02():
    METADATA_FILE = "./tests/input/test_read_metadata_file_02.csv"
    with pytest.raises(Exception):
        MetadataReader.read_metadata_file(METADATA_FILE)


def test_read_metadata_file_03():
    METADATA_FILE = "./tests/input/test_read_metadata_file_03.csv"
    with pytest.raises(Exception):
        MetadataReader.read_metadata_file(METADATA_FILE)
