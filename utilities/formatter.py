'''
    Author:
        * Muhammed Abdullah Al Ahad <ahad3112@yahoo.com, maaahad@gmail.com, maaahad@kth.se>


    Description:
        * ....

    Source:
        *
'''
# PYTHON Stdlib
import math


class Colors:
    Black = '\u001b[30m'
    Red = '\u001b[31m'
    Green = '\u001b[32m'
    Yellow = '\u001b[33m'
    Blue = '\u001b[34m'
    Magenta = '\u001b[35m'
    Cyan = '\u001b[36m'
    White = '\u001b[37m'

    Bright_Black = '\u001b[30;1m'
    Bright_Red = '\u001b[31;1m'
    Bright_Green = '\u001b[32;1m'
    Bright_Yellow = '\u001b[33;1m'
    Bright_Blue = '\u001b[34;1m'
    Bright_Magenta = '\u001b[35;1m'
    Bright_Cyan = '\u001b[36;1m'
    Bright_White = '\u001b[37;1m'

    # Some Predefined colors to be used in some specific context
    # HEADER = '\033[95m'
    # OKBLUE = '\033[94m'
    # OKGREEN = '\033[92m'
    # WARNING = '\033[93m'
    # FAIL = '\033[91m'
    # ENDC = '\033[0m'


class BackgroundColors:
    Black = '\u001b[40m'
    Red = '\u001b[41m'
    Green = '\u001b[42m'
    Yellow = '\u001b[43m'
    Blue = '\u001b[44m'
    Magenta = '\u001b[45m'
    Cyan = '\u001b[46m'
    White = '\u001b[47m'

    Bright_Black = '\u001b[40;1m'
    Bright_Red = '\u001b[41;1m'
    Bright_Green = '\u001b[42;1m'
    Bright_Yellow = '\u001b[43;1m'
    Bright_Blue = '\u001b[44;1m'
    Bright_Magenta = '\u001b[45;1m'
    Bright_Cyan = '\u001b[46;1m'
    Bright_White = '\u001b[47;1m'


class Decorators:
    Bold = '\u001b[1m'
    Underline = '\u001b[4m'
    Reversed = '\u001b[7m'


class Style:
    HEADER = Colors.Bright_White + Decorators.Bold + BackgroundColors.Bright_Green
    TITLE = Colors.Bright_White + Decorators.Bold + Decorators.Underline
    KEYWORD = Colors.Bright_Red + Decorators.Bold
    RESET = '\u001b[0m'


def justify(text, line_width, indent=0, left_separator='', right_separator=''):
    '''
    This function is responsible to justify alignment based on the line width
    '''
    # line_width = line_width - indent
    result = []
    text = text.strip()
    while text:
        try:
            if not text[line_width - 1].isspace() and not text[line_width].isspace():
                result.append('\r' + ' ' * indent + left_separator + text[:line_width - 1] + '-' + right_separator + '\n')
                text = text[line_width - 1:]
            else:
                result.append('\r' + ' ' * indent + left_separator + text[:line_width] + right_separator + '\n')
                text = text[line_width:]
        except IndexError:
            rest_text = text[:]
            result.append('\r' + ' ' * indent + left_separator + rest_text + ' ' * (line_width - len(rest_text)) + right_separator)
            text = ''

        text = text.lstrip()

    return ''.join(result)


def justify_backup(text, line_width, indent=0):
    '''
    This function is responsible to justify alignment based on the line width
    '''
    line_width = line_width - indent
    result = []
    text = text.strip()
    while text:
        try:
            if not text[line_width - 1].isspace() and not text[line_width].isspace():
                result.append(' ' * indent + text[:line_width - 1] + '-\n')
                text = text[line_width - 1:]
            else:
                result.append(' ' * indent + text[:line_width] + '\n')
                text = text[line_width:]
        except IndexError:
            result.append(' ' * indent + text[:])
            text = ''

        text = text.lstrip()

    return ''.join(result)


# Below is a test function for creating tables
def create_table(title, headers, rows, line_width=150, row_separator='-', column_separator='|'):
    # mock data for debugging
    # headers = [
    #     {'name': 'header1', 'percentage': 33},
    #     {'name': 'header2', 'percentage': 33},
    #     {'name': 'header3', 'percentage': 33},
    # ]
    # print(rows)
    # rows = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

    # create title
    title_length = len(title.strip())
    title_lr = f'{column_separator}'
    title_up = '+' + f'{row_separator}' * (title_length + 2) + '+' + '\n'
    formatted_title = title_up + title_lr + ' ' + Style.HEADER + title + Style.RESET + ' ' + title_lr

    # update line_width in case title is longer than the line_width
    if line_width < (title_length + 4):
        line_width = title_length + 4

    row_separator = '\n+' + f'{row_separator}' * (line_width - 2) + '+' + '\n'
    intermediate_row_separator = row_separator[:]

    # column width and column separator
    col_width = (line_width - len(headers) - 1) // len(headers)
    header_format = '{0[name]:^{1}}'
    formatted_headers = f'\r{column_separator}'

    for (index, header) in enumerate(headers):
        if index == len(headers) - 1:
            col_width = line_width - len(headers) - 1 - index * col_width
        if index > 0:
            intermediate_row_separator = intermediate_row_separator[:col_width + 1] + '+' + intermediate_row_separator[col_width + 2:]
        formatted_headers += Style.HEADER + header_format.format(header, col_width) + Style.RESET + f'{column_separator}'

    # adding rows
    formatted_rows = ''
    entry_format = '{0:<{1}}'
    for row in rows:
        occupied_line_width = 0
        entry_width = (line_width - len(headers) - 1) // len(headers)
        prev_entry_width = entry_width
        formatted_row = f'\r'
        left_separator = f'{column_separator}'
        right_separator = f'{column_separator}'

        max_lines = max([math.ceil(len(col) / entry_width) for col in row])

        print('Maxlines: '.upper(), max_lines)

        for (index, entry) in enumerate(row):
            if index == len(headers) - 1:
                entry_width = line_width - len(headers) - 1 - index * entry_width
            # formatted_row += Colors.Bright_White + Decorators.Bold + BackgroundColors.Bright_Blue + entry_format.format(entry, entry_width) + Style.RESET + f'{column_separator}'

            if index > 0:
                left_separator = ''

            justified_entry = justify(entry, entry_width, indent=occupied_line_width,
                                      right_separator=right_separator, left_separator=left_separator)

            occupied_line_width += entry_width + len(column_separator) * 2
            formatted_row = Decorators.Bold + justified_entry + Style.RESET + formatted_row

        formatted_rows += formatted_row + intermediate_row_separator

    return formatted_title + row_separator + formatted_headers + intermediate_row_separator + formatted_rows


# Below is a test function for creating tables
def create_table_backup(title, headers, rows, line_width=150, row_separator='-', column_separator='|'):
    # mock data for debugging
    # headers = [
    #     {'name': 'header1', 'percentage': 33},
    #     {'name': 'header2', 'percentage': 33},
    #     {'name': 'header3', 'percentage': 33},
    # ]
    # print(rows)
    # rows = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

    # create title
    title_length = len(title.strip())
    title_lr = f'{column_separator}'
    title_up = '+' + f'{row_separator}' * (title_length + 2) + '+' + '\n'
    formatted_title = title_up + title_lr + ' ' + Style.HEADER + title + Style.RESET + ' ' + title_lr

    # update line_width in case title is longer than the line_width
    if line_width < title_length:
        line_width = title_length

    row_separator = '\n+' + f'{row_separator}' * (line_width - 2) + '+' + '\n'
    intermediate_row_separator = row_separator[:]

    # column width and column separator
    col_width = (line_width - len(headers) - 1) // len(headers)
    header_format = '{0[name]:^{1}}'
    formatted_headers = f'\r{column_separator}'

    for (index, header) in enumerate(headers):
        if index == len(headers) - 1:
            col_width = line_width - len(headers) - 1 - index * col_width
        if index > 0:
            intermediate_row_separator = intermediate_row_separator[:col_width + 1] + '+' + intermediate_row_separator[col_width + 2:]
        formatted_headers += Style.HEADER + header_format.format(header, col_width) + Style.RESET + f'{column_separator}'

    # adding rows
    formatted_rows = ''
    entry_format = '{0:<{1}}'
    for row in rows:
        occupied_line_width = 0
        entry_width = (line_width - len(headers) - 1) // len(headers)
        prev_entry_width = entry_width
        formatted_row = f'\r'
        left_separator = f'{column_separator}'
        right_separator = f'{column_separator}'

        for (index, entry) in enumerate(row):
            if index == len(headers) - 1:
                entry_width = line_width - len(headers) - 1 - index * entry_width
            # formatted_row += Colors.Bright_White + Decorators.Bold + BackgroundColors.Bright_Blue + entry_format.format(entry, entry_width) + Style.RESET + f'{column_separator}'

            if index > 0:
                left_separator = ''

            justified_entry = justify(entry, entry_width, indent=occupied_line_width,
                                      right_separator=right_separator, left_separator=left_separator)

            occupied_line_width += entry_width + len(column_separator) * 2
            formatted_row = Decorators.Bold + justified_entry + Style.RESET + formatted_row

        formatted_rows += formatted_row + intermediate_row_separator

    return formatted_title + row_separator + formatted_headers + intermediate_row_separator + formatted_rows
