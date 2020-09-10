from urllib import request
import re

url = input('Введите ссылку на сайт hh.ru со списком резюме: ')
response = request.urlopen(url)
content = response.read().decode('UTF-8')


def get_structured_html(content):
    """This function takes not structured html, written each tag and his content on a new line and return this value.

    :param content: not structured html(I mean html tags are written in one line).
    :return: structured html. Each html tag and his content(<a>This is tag content</a>) will be written on a new line.
    """
    result = []
    for i in content:
        if i == '>':
            result.append('>\n')
        elif i == '<':
            result.append('\n<')
        else:
            result.append(i)
    return ''.join(result)


content_to_parse = get_structured_html(content).splitlines()
for line in content_to_parse:
    if 'resume-search-item__name' in line:
        print(content_to_parse[content_to_parse.index(line) + 1])
        print('https://hh.ru' + re.search('href=".*"', line).group(0)[6:-1])
