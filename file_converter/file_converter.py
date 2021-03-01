# -*- coding: utf-8 -*-

from file_converter.column_types import DATE_TYPE, NUMERIC_TYPE, STRING_TYPE


class FileConverter:
    """
    Class to convert a fixed file format to a csv file
    """
    def __init__(self, metadata, sep=","):
        self.metadata = metadata
        self.sep = sep

    @staticmethod
    def convert_value(data_value, column_type):
        if column_type == DATE_TYPE:
            # TODO : add control on date with bad format
            return "/".join(reversed(data_value.strip().split("-")))
        elif column_type == NUMERIC_TYPE:
            return data_value.strip()
        elif column_type == STRING_TYPE:
            return data_value.strip()

    def convert_line(self, data_line):
        # Verify line length
        if len(data_line) != sum([column["size"] for column in self.metadata]):
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
        return self.sep.join([col["name"] for col in self.metadata])

    def convert_data_generator(self, data_iterator):
        return (
            self.convert_line(data_line)
            for data_line in data_iterator
        )

    def convert_file_and_write(self, input_file, output_file):
        with open(output_file, "w", encoding="utf8") as output:
            output.write(self.get_header())
            with open(input_file, "r", encoding="utf8") as input_f:
                for converted_line in self.convert_data_generator(input_f.readlines()):
                    output.write(converted_line)
