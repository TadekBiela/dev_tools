import sys


class LogFilter(object):
    def __init__(self):
        self.filtered_file_content = []

    def filter_file(self, input_file_path, filter_string, output_file_path):
        input_file_content = self._get_input_file_content(input_file_path)
        self._filter_input_file_content(input_file_content, filter_string)
        self._save_filtered_content_to_file(output_file_path)

    def _get_input_file_content(self, input_file_path):
        input_file = self._open_file(input_file_path, "r")
        input_file_lines = input_file.readlines()
        input_file.close()

        return input_file_lines

    def _open_file(self, file_path, mode):
        try:
            return open(file_path, mode)
        except IOError as e:
            print("Unable to open the file", file_path, "Exit!\n", e)
            sys.exit()

    def _filter_input_file_content(self, input_file_lines, filter_string):
        for line in input_file_lines:
            if filter_string in line:
                self.filtered_file_content.append(line)

    def _save_filtered_content_to_file(self, output_file_path):
        output_file = self._open_file(output_file_path, "w")
        output_file.writelines(self.filtered_file_content)
        output_file.close()


def main(input_args):
    filter_string, input_file_path, output_file_path = get_input_params(input_args)

    log_filter = LogFilter()
    log_filter.filter_file(input_file_path, filter_string, output_file_path)


def get_input_params(input_args):
    if valid_input_arguments(input_args):
        input_file_path = input_args[0]
        filter_string = input_args[1]
        output_file_path = input_args[2]
        return filter_string, input_file_path, output_file_path
    exit()


def valid_input_arguments(input_args):
    return valid_if_help_info_not_printed(input_args) and valid_number_of_input_args(input_args)


def valid_if_help_info_not_printed(input_args):
    if input_args[0] == "-h" or input_args[0] == "--help":
        print("""
        valid input arguments:
        <input_file_path> <filter_string> <output_file_path>
        
        <input_file_path>   : file which one you want filter
        <filter_string>     : this string will be checked in each line in input file,
                              if line contain this string it will be saved in output_file
        <output_file_path>  : file where only filtered lines from input file will be saved,
                              if this file don't exist, log_filter will create it
        example:
        
        file.txt "abc" file_out.txt
        
        options:
        -h, --help          : print this HELP message
        """)
        return False
    return True


def valid_number_of_input_args(input_args):
    if len(input_args) != 3:
        print("Wrong input arguments!\n")
        return False
    return True


main(sys.argv[1:])
