class PhoneBook:
    def __init__(self):
        self.list_phones = list()

    def add_phone(self, phone):
        self.list_phones.append(phone)

    def remove_phone(self, indx):
        self.list_phones.pop(indx)

    def get_phone_list(self):
        return self.list_phones

class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(p.__dict__)

k = PhoneNumber(12345678901, "Сергей Балакирев")
print(k.__dict__)