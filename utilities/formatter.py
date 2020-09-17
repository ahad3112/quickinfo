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
    # print('line_width', line_width)
    result = []
    text = text.strip()
    while text:
        try:
            if not text[line_width - 1].isspace() and not text[line_width].isspace():
                # TODO: will deal with addind '-'' later
                # result.append('\r' + ' ' * indent + left_separator + text[:line_width - 1] + '-' + right_separator + '\n')
                # text = text[line_width - 1:]
                result.append(' ' * indent + left_separator + text[:line_width] + right_separator + '\n')
                text = text[line_width:]
            else:
                result.append(' ' * indent + left_separator + text[:line_width] + right_separator + '\n')
                text = text[line_width:]
        except IndexError:
            rest_text = text[:]
            result.append(' ' * indent + left_separator + rest_text + ' ' * (line_width - len(rest_text)) + right_separator)
            text = ''

        text = text.lstrip()

    return ''.join(result)


# Below is a test function for creating column entry, row and table
def create_entry():
    '''
    Don't think we need this
    '''
    pass


def create_row(data, line_width, header=False):
    # we need place for cloumn separator and padding
    n_columns = len(data)
    total_columns_width = line_width - len(data) * 3 - 1
    columns_width = [
        (total_columns_width + n_columns - i - 1) // n_columns for i in range(n_columns)
    ]
    lines_in_row = max(
        [math.ceil(len(data[i]) / columns_width[i]) for i in range(n_columns)]
    )

    row = [' ' * (line_width - 2) + ' |\n'] * lines_in_row
    offset = 0

    for (index, col) in enumerate(data):
        justified_lines = justify(col, columns_width[index]).split('\n')

        assert lines_in_row >= len(justified_lines), 'Error in defining lines in a row'

        for i in range(lines_in_row):
            if i < len(justified_lines):
                row[i] = row[i][:offset] + '| ' + justified_lines[i] + ' ' + row[i][offset + len(justified_lines[i]) + 3:]
            else:
                row[i] = row[i][:offset] + '| ' + row[i][offset + 2:]

        offset += columns_width[index] + 3

    return ''.join(row)


def create_table(title, headers, rows, line_width=150, row_separator='-', column_separator='|'):
    # Adding the tile of the table
    table = Style.KEYWORD
    table += '+{0}+\n| {1} |\n+{0}+\n'.format('-'*(len(title) + 2), title)
    row_separator = '+' + f'{row_separator}' * (line_width - 2) + '+'
    table += row_separator
    table += '\n' + create_row(headers, line_width).strip() + '\n' + row_separator
    for row in rows:
        assert len(headers) == len(row), "Number of header and number of column in a row should be same."
        table += '\n' + create_row(row, line_width).strip() + '\n' + row_separator

    table += Style.RESET
    return table
