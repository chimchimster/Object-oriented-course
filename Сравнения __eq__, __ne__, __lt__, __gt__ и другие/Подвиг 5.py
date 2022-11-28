stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]
lst_text = []
stich = list(map(lambda x: x.strip('–?!,.;').split(), stich))

class StringText:
        def __init__(self, lst_words):
                self.lst_words = lst_words

        def __len__(self):
                count = 0
                for i in self.lst_words:
                        count += 1
                return count

        def __gt__(self, other):
                if len(self) > len(other):
                        return True

        def __ge__(self, other):
                if len(self) >= len(other):
                        return True

        def __lt__(self, other):
                if len(self) < len(other):
                        return True

        def __le__(self, other):
                if len(self) <= len(other):
                        return True

for i in stich:
        lst_text.append(StringText(i))

lst_text_sorted = sorted(lst_text[::-1], reverse=True)
lst_temp = list()
for i in lst_text_sorted:
        lst_temp.append(' '.join(i.lst_words))
lst_text_sorted = lst_temp

