# -*- coding: utf-8 -*-

from file_converter.column_types import ACCEPTED_TYPES


class MetadataReader:
    """
    Class with static methods to read and parse metadata from a metadata file
    """
    @staticmethod
    def read_metadata_file(metadata_file):
        """
        Read metadata file and parse its content to return a list of dict of columns metadata
        :param metadata_file: path to metadata file
        :return: list of dict (columns metadata)
        """
        with open(metadata_file, "r", encoding="utf8") as input_file:
            metadata = MetadataReader.parse_metadata(input_file.readlines())
        return metadata

    @staticmethod
    def parse_metadata(metadata_iterator):
        """
        Parse metadata line by line and returns a list of dict of columns metadata
        :param metadata_iterator: iterator to metadata line by line
        :return: list of dict (columns metadata)
        """
        col_list = []
        for line in metadata_iterator:
            col_metadata_list = line.strip().split(",")
            if len(col_metadata_list) != 3:
                raise(Exception("Wrong number of column metadata (3 fields expected) for line : {}".format(line)))
            col_name, col_size, col_type = col_metadata_list
            col_size = int(col_size)
            if col_type not in ACCEPTED_TYPES:
                raise(Exception("Column type not supported : {}".format(col_type)))
            col_list.append({
                "name": col_name,
                "size": col_size,
                "type": col_type
            })
        return col_list
