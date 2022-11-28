class Recipe:
    def __init__(self, *args):
        self.recipe_list = [] + [*args]

    def add_ingredient(self, ing):
        self.recipe_list.append(ing)

    def remove_ingredient(self, ing):
        if ing in self.recipe_list:
            self.recipe_list.remove(ing)

    def get_ingredients(self):
        return tuple(self.recipe_list)

    def __len__(self):
        return len(self.recipe_list)


class Ingredient:
    def __init__(self, name, volume, measure):
        if isinstance(name, str):
            self.name = name
            self.measure = measure
        else:
            raise TypeError('Type must be STR')
        if isinstance(volume, (float, int)):
            self.volume = volume
        else:
            raise TypeError('Type must be INT/FLOAT')

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


i1 = Ingredient("Соль", 1, "столовая ложка")
i2 = Ingredient("Мука", 1, "кг")
i3 = Ingredient("Мясо баранины", 10, "кг")
i4 = Ingredient("Масло", 100, "гр")
recipe = Recipe(i1, i2, i3)
recipe.add_ingredient(i4)
recipe.remove_ingredient(i3)
print(recipe.__dict__)