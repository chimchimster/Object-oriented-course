import re
from faker import Faker
class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            count = 0
            for i in range(len(email)):
                if email[i] == '@':
                    count += i
            if re.match(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email) and len(email[:count]) <= 100 and len(email[count:]) <= 50:
                return True
            return False

    @classmethod
    def get_random_email(cls):
        fa = Faker()
        email = fa.email()
        return email

    @staticmethod
    def __is_email_str(email):
        if type(email) == str:
            return True
        return False




em = EmailValidator()
res = EmailValidator.get_random_email()
print(res)