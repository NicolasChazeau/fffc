from file_converter.value_formatter import StringFormatter


def test_string_formatter_convert_01():
    """Test for string type"""
    input_tests = [
        "Un test",
        "Un test   ",
        "   Un test"
    ]
    expected_result = 'Un test'
    for test in input_tests:
        assert StringFormatter.convert(test) == expected_result

    input_tests = [
        "Un, test",
        "Un, test   ",
        "   Un, test"
    ]
    expected_result = '"Un, test"'
    for test in input_tests:
        assert StringFormatter.convert(test) == expected_result
