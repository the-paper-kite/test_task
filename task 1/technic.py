from dataclasses import dataclass
from decorators import my_decorator


@dataclass
class Technic:
    name: str
    price: int
    availability: bool

    @property
    def display_technic(self):
        print('Название: {}. Цена: {}. Наличие: {}'.format(self.name, self.price, self.availability))
        print('Категория: бюджетный') if self.price < 50000 else print('Категория: дорогой')

    @my_decorator
    def __ge__(arg1, arg2):
        return len(arg1) > len(arg2)

