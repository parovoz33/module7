class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        """Считывает все продукты из файла и возвращает строку с их перечислением."""
        try:
            file = open(self.__file_name, 'r', encoding='utf-8')
            content = file.read().strip()
            file.close()
            return content
        except FileNotFoundError:
            return ''

    def add(self, *products):
        """Добавляет новые продукты в файл, если их там еще нет."""
        existing_products = self.get_products().splitlines()
        existing_names = [line.split(',')[0].strip() for line in existing_products]

        file = open(self.__file_name, 'a', encoding='utf-8')
        for product in products:
            if product.name in existing_names:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(str(product) + '\n')
                print(f'Продукт {product.name} добавлен в магазин')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # Spaghetti, 3.4, Groceries

s1.add(p1, p2, p3)

print(s1.get_products())
