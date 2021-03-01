from file_converter.value_formatter import NumericFormatter


def test_numeric_formatter_convert_01():
    """Test for numeric type"""
    input_tests = [
        "-3.2",
        "-3.2   ",
        "   -3.2"
    ]
    expected_result = "-3.2"
    for test in input_tests:
        assert NumericFormatter.convert(test) == expected_result


def test_numeric_formatter_validate_format_01():
    """Test for numeric type"""
    input_tests = [
        "-3.2",
        "-3.2   ",
        "   -3.2"
    ]
    for test in input_tests:
        assert NumericFormatter.validate_format(test)

    input_tests = [
        "-3.2A",
        "Test",
        "-3,2"
    ]
    for test in input_tests:
        assert not NumericFormatter.validate_format(test)
