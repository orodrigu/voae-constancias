import re

string = "123AAAMississippiZZZ123"

try:
    found = re.search('AAA(.+?)ZZZ', string).group(1)
    print(found)
except AttributeError:
    pass