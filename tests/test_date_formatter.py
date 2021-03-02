from file_converter.value_formatter import DateFormatter


def test_date_formatter_convert_01():
    """Test for date type"""
    input_tests = [
        "2021-03-01",
        "   2021-03-01",
        "2021-03-01     "
    ]
    expected_result = "01/03/2021"
    for test in input_tests:
        assert DateFormatter.convert(test) == expected_result


def test_date_formatter_validate_format_01():
    """Test for date type"""
    input_tests = [
        "2021-03-01",
        "   2021-03-01",
        "2021-03-01     "
    ]
    for test in input_tests:
        assert DateFormatter.validate_format(test)

    input_tests = [
        "2021-01",
        "01-03-2021",
        "2021/03/01",
        "2021-0-000"
    ]
    for test in input_tests:
        assert not DateFormatter.validate_format(test)
