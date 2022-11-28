from string import ascii_lowercase, digits
import re

class CardCheck:
    @staticmethod
    def check_card_number(number):
        if re.match(r'\d{4}-\d{4}-\d{4}-\d{4}\Z', number):
            return True
        return False

    @staticmethod
    def check_name(name):
        if re.match(r'[A-Z]+\s[A-Z]+\Z', name):
            return True
        return False

is_number = CardCheck.check_card_number("1334-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(is_number)
print(is_name)