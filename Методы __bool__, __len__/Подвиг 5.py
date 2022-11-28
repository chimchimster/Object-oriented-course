import sys
class CheckStr:
    class CheckStr:
        def __set_name__ (self, owner, name):
            self.name = '_' + name

        def __get__ (self, instance, owner):
            return getattr(instance, self.name)

        def __set__ (self, instance, value):
            if self.__check_type(value):
                setattr(instance, self.name, value)

        @classmethod
        def __check_type (cls, value):
            if type(value) == str:
                return True
            else:
                raise ValueError('not STR!')


class MailBox:
    def __init__(self):
        self.inbox_list = list()

    def recieve(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        lst_in = [MailItem(*x.split(';')) for x in lst_in]
        for i in lst_in:
            self.inbox_list.append(i)

class MailItem:
    mail_from, title, content = CheckStr(), CheckStr(), CheckStr()

    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read=True):
        self.is_read = fl_read


    def __bool__(self):
        if self.is_read == True:
            return True
        else:
            return False

mail = MailBox()
mail.recieve()
mail.inbox_list[0].set_read()
mail.inbox_list[-1].set_read()

inbox_list_filtered = list(filter(bool, mail.inbox_list))
print(inbox_list_filtered)
for i in inbox_list_filtered:
    print(i.mail_from)