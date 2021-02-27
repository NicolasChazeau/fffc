from file_converter.metadata_reader import MetadataReader


def test_01():
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