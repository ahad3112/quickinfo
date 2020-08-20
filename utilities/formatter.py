'''
    Author:
        * Muhammed Abdullah Al Ahad <ahad3112@yahoo.com, maaahad@gmail.com, maaahad@kth.se>


    Description:
        * ....

    Source:
        *
'''


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
    TITLE = Colors.Bright_White + Decorators.Underline
    KEYWORD = Colors.Bright_Red + Decorators.Bold
    RESET = '\u001b[0m'


def justify(text, line_width):
    '''
    This function is responsible to justify alignment based on the line width
    '''
    result = []
    text = text.strip()
    while text:
        try:
            if not text[line_width - 1].isspace() and not text[line_width].isspace():
                result.extend(text[:line_width - 1] + '-\n')
                text = text[line_width - 1:]
            else:
                result.extend(text[:line_width] + '\n')
                text = text[line_width:]
        except IndexError:
            result.extend(text[:])
            text = ''

        text = text.lstrip()

    return ''.join(result)
