import re

from file_converter.column_types import DATE_TYPE, NUMERIC_TYPE, STRING_TYPE


class ValueFormatter:
    """
    Factory to return a ValueFormatter class corresponding to each type of data
    """
    @staticmethod
    def validate_format(data_value):
        pass

    @staticmethod
    def convert(data_value):
        pass

    @staticmethod
    def factory(data_type):
        if data_type == DATE_TYPE:
            return DateFormatter
        elif data_type == NUMERIC_TYPE:
            return NumericFormatter
        elif data_type == STRING_TYPE:
            return StringFormatter
        raise Exception("Data type not supported : {}".format(data_type))


class DateFormatter(ValueFormatter):
    @staticmethod
    def validate_format(data_value):
        regex = re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}')
        return re.fullmatch(regex, data_value.strip())

    @staticmethod
    def convert(data_value):
        return "/".join(reversed(data_value.strip().split("-")))


class NumericFormatter(ValueFormatter):
    @staticmethod
    def validate_format(data_value):
        regex = re.compile(r'[-+]?\d*\.\d+|\d+')
        return re.fullmatch(regex, data_value.strip())

    @staticmethod
    def convert(data_value):
        return data_value.strip()


class StringFormatter(ValueFormatter):
    @staticmethod
    def validate_format(data_value):
        return True

    @staticmethod
    def convert(data_value):
        if ',' in data_value:
            return '"{}"'.format(data_value.strip())
        else:
            return data_value.strip()
