from urllib import request
import re


response = request.urlopen('https://habr.com/')
headers: str = response.info()
content: str = response.read().decode('UTF-8')
print('Response: ', response)
print('URL: ', response.geturl())
print(headers)
for line in content.splitlines():
    if 'post__title_link' in line:
        print('Название статьи: ', re.search('>.*<', line).group(0)[1:-1])
        print("Ссылка на статью: {}\n".format(re.search('href=".*/"', line).group(0)[6:-1]))
