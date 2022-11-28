from abc import ABC, abstractmethod

class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        """Абстрактное объект-свойство"""

    @property
    @abstractmethod
    def population(self):
        """Абстрактное объект-свойство"""

    @property
    @abstractmethod
    def square(self):
        """Абстрактное объект-свойство"""

    @abstractmethod
    def get_info(self):
        """Абстрактный метод"""

class Country(CountryInterface):
    def __init__(self, name, population, square):
        self._name = name
        self._population = population
        self._square = square

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, val):
        self._population = val

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, val):
        self._square = val

    def get_info(self):
        return f'{self.name}: {self.square}, {self.population}'

country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info()) # Россия: 354005483.0, 150000000