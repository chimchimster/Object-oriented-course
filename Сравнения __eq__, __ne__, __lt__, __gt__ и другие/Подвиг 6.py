class Morph:
    def __init__(self, *args):
        self.args = [*args]

    def add_word(self, word):
        self.args.append(word)

    def get_words(self):
        return tuple(self.args)

    def __eq__(self, other):
        for i in self.args:
            if other.lower().strip() in i:
                return True

    def __ne__(self, other):
        for i in self.args:
            if other.lower().strip() != i:
                return True

dict_words = (Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'), Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'), Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'), Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'), Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'))

text = input().strip('.')
counter = 0
words = map(lambda x: x.strip("?!:;,.").lower(), text.split())
for i in words:
    for j in dict_words:
       if i in j.args:
           counter += 1

print(counter)



