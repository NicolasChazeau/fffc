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


class DateFormatter(ValueFormatter):
    @staticmethod
    def validate_format(data_value):
        # TODO
        return True

    @staticmethod
    def convert(data_value):
        return "/".join(reversed(data_value.strip().split("-")))


class NumericFormatter(ValueFormatter):
    @staticmethod
    def validate_format(data_value):
        # TODO
        return True

    @staticmethod
    def convert(data_value):
        return data_value.strip()


class StringFormatter(ValueFormatter):
    @staticmethod
    def validate_format(data_value):
        # TODO
        return True

    @staticmethod
    def convert(data_value):
        return data_value.strip()
