# -*- coding: utf-8 -*-

import os

from file_converter.value_formatter import ValueFormatter


class FileConverter:
    """
    Class to convert a fixed file format to a csv file according to associated metadata
    :param metadata: list of dict with data describing each column
                     Example :
                     [{"size":3, "type": "numeric", "name": "height"},...]
    """
    def __init__(self, metadata, sep=",", line_sep="\r\n", encoding="utf8"):
        self.metadata = metadata
        self.sep = sep
        self.line_sep = line_sep
        self.encoding = encoding

    @staticmethod
    def convert_value(data_value, column_type):
        """
        Verify and convert a value according to its type
        :param data_value: value as a string
        :param column_type: value type
        :return: converted value as string
        """
        value_formatter = ValueFormatter.factory(column_type)
        if value_formatter.validate_format(data_value):
            return value_formatter.convert(data_value)
        else:
            raise Exception("Value does not respect format : {} with type {}".format(data_value, column_type))

    def convert_line(self, data_line):
        """
        Convert a line according to metadata
        """
        # Verify line length
        data_line = data_line.rstrip()
        if len(data_line) > sum([column["size"] for column in self.metadata]):
            raise Exception(
                "Can not convert line, line length different from expected : {} found, {} expected".format(
                    len(data_line),
                    sum([column["size"] for column in self.metadata])
                )
            )

        converted_values = []
        current_index = 0
        for column in self.metadata:
            current_elem = data_line[current_index:current_index + column["size"]]
            converted_values.append(FileConverter.convert_value(current_elem, column["type"]))
            current_index += column["size"]
        return self.sep.join(converted_values)

    def get_header(self):
        """
        Return metadata as a csv header
        """
        return self.sep.join([col["name"] for col in self.metadata])

    def convert_data_generator(self, data_iterator):
        """
        Return a generator to convert data line by line
        :param data_iterator: data to convert
        :return: generator of converted data
        """
        return (
            self.convert_line(data_line)
            for data_line in data_iterator
        )

    def convert_file_and_write_to_csv(self, input_file, output_file):
        """
        Read an input file, convert it to csv and write it to output file
        """
        if not os.path.isfile(input_file):
            raise Exception("Input data file does not exists")
        out_path, out_filename = os.path.split(output_file)
        if not os.path.exists(out_path):
            raise Exception("Output path does not exists")
        if not os.path.splitext(out_filename)[-1] == ".csv":
            raise Exception("Bad file extension for output file, .csv expected")
        with open(output_file, "w", encoding=self.encoding, newline=self.line_sep) as output:
            output.write(self.get_header() + "\n")
            with open(input_file, "r", encoding=self.encoding) as input_f:
                for converted_line in self.convert_data_generator(input_f.readlines()):
                    output.write(converted_line + "\n")
