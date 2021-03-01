from argparse import ArgumentParser

from file_converter.file_converter import FileConverter
from file_converter.metadata_reader import MetadataReader


def parse_arguments():
    parser = ArgumentParser(description='Script to read a data and a metadata file, and to convert them in a csv file')
    parser.add_argument("--input_data_file", required=True, type=str, help='Input data file in fixed format')
    parser.add_argument("--input_metadata_file", required=True, type=str, help='Input metadata file in csv format')
    parser.add_argument("--output_file", required=True, type=str, help='Output file in csv format')

    arguments = parser.parse_args()
    return arguments


def run(input_data_file, input_metadata_file, output_file):
    metadata_list = MetadataReader.read_metadata_file(input_metadata_file)
    file_converter = FileConverter(metadata_list)
    file_converter.convert_file_and_write_to_csv(input_data_file, output_file)


if __name__ == "__main__":
    args = parse_arguments()

    in_data_file = args.input_data_file
    in_metadata_file = args.input_metadata_file
    out_file = args.output_file

    print("Begin")
    run(in_data_file, in_metadata_file, out_file)
    print("End")
