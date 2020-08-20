'''
    Author:
        * Muhammed Abdullah Al Ahad <ahad3112@yahoo.com, maaahad@gmail.com, maaahad@kth.se>


    Description:
        * ....

    Source:
        *
'''


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
