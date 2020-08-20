'''
    Author:
        * Muhammed Abdullah Al Ahad <ahad3112@yahoo.com, maaahad@gmail.com, maaahad@kth.se>


    Description:
        * ....

    Source:
        Ansi Colors : https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
'''


class Colors:
    # Core Colors
    Black = '\u001b[30m'
    Red = '\u001b[31m'
    Green = '\u001b[32m'
    Yellow = '\u001b[33m'
    Blue = '\u001b[34m'
    Magenta = '\u001b[35m'
    Cyan = '\u001b[36m'
    White = '\u001b[37m'
    Reset = '\u001b[0m'

    # Some Predefined colors to be used in some specific context
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    # def disable(self):
    #     self.HEADER = ''
    #     self.OKBLUE = ''
    #     self.OKGREEN = ''
    #     self.WARNING = ''
    #     self.FAIL = ''
    #     self.ENDC = ''
