"""
Simple parser to produce a markdown output for a text file with predeterminate format.

"""

from pathlib import Path

input_file = "data.txt"
predeterminate_format = "# {}\n\nAuthor: {}\n\n"


def get_file_content(filename):
    with open(filename, 'r') as reader:
        all_lines = reader.read().splitlines()
    return all_lines


def get_file_pure_content(filename):
    with open(filename, 'r') as reader:
        all_lines = reader.readlines()
    return all_lines


def store_file(filename, data):
    with open(filename, 'w') as writer:
        for line in data:
            writer.write(line)


def scan_directory(directory):
    files = Path(directory)
    all_files = [filename.name for filename in files.iterdir()]
    return all_files


def parse_file(filename, predeterminate_format):
    input_data = get_file_content(filename)
    input_prefix = Path(filename).stem
    input_suffix = Path(filename).suffix
    data_to_store = []
    for line in input_data:
        parsed_line = line.split(',')
        parsed_line = [entry.strip(' ') for entry in parsed_line]
        data_to_store.append(predeterminate_format.format(
            parsed_line[1], parsed_line[0]))
    store_file("{}_{}_output.md".format(
        input_prefix, input_suffix), data_to_store)


def get_complete_path_filename(base_path, filename):
    return "{}/{}".format(base_path, filename)


def get_all_formats(data_dir, format_dir):
    all_formats = []
    all_formats_files = scan_directory(
        get_complete_path_filename(data_dir, format_dir))
    for format_file in all_formats_files:
        content = get_file_pure_content(get_complete_path_filename(
            get_complete_path_filename(data_dir, format_dir), format_file))
        all_formats.append(content)
    return all_formats


def main(data_dir, input_dir, format_dir, opening_braquet, closing_braquet):
    try:
        pass

    except IOError:
        print("File Error")


if __name__ == "__main__":
    data_dir = "data"
    input_dir = "input"
    format_dir = "format"
    opening_braquet = "{"
    closing_braquet = "}"
    main(data_dir, input_dir, format_dir, opening_braquet, closing_braquet)
