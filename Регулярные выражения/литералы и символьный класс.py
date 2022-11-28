import re

string = 'Еда, беду,-3м44 победа'

match = re.findall(r'[а-яА-Я0-9]', string)
print(match)
