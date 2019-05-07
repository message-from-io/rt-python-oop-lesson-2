
'''
1. Получить количество учеников с сайта geekbrains.ru:
a) при помощи регулярных выражений,
b) при помощи библиотеки BeautifulSoup.
'''


# 1) При помощи регулярных выражений

import re

with open("index.html") as f:
    site_contents = f.read()

total_users = re.findall('<span class=\"total-users\">[А-я\s]+([\d\s]+)[А-я\s]+</span>', site_contents)

print('\n1:\n')
print('Количество учеников на сайте:', total_users[0].replace(' ', ''), '\n')


# 2) При помощи библиотеки BeautifulSoup

from bs4 import BeautifulSoup as BS

bs_obj = BS(site_contents, 'html.parser')

# Найти все элементы с тегом 'span'
span_tags = bs_obj.find_all('span')
print('\n2:\n')
print('span_tags:\n', span_tags, '\n')

for n in span_tags:
    # Если атрибут 'class' элемента равен 'total-users', то вывести содержимое элемента
    if 'total-users' in n.get("class", ""):
        print(n.contents)


# Результат:
#
# 1:
#
# Количество учеников на сайте: 3741756
#
# 2:
#
# span_tags:
#  [<span class="total-users">Нас уже 3 741 756 человек</span>, <span>Нажимая на кнопку, </span>, <span>вы</span>, <span>даете согласие на обработку своих персональных данных в соответствии с</span>, <span>Обучение</span>, <span>Курсы</span>, <span>Вебинары</span>, <span>Форум</span>, <span>Блог</span>, <span>Тесты</span>, <span>Карьера</span>, <span class="item">© GeekBrains</span>, <span class="item">Лицензия на образовательную деятельность № 038188 от 26 января 2017 г.</span>]
#
# ['Нас уже 3 741 756 человек']
