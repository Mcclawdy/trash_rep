class Ingredient(object):
    def __init__(self, name, weight, cost):
        self.__name = name
        self.__weight = weight
        self.__cost = cost

    def get_name(self):
        return self.__name

    def get_weight(self):
        return self.__weight

    def get_cost(self):
        return self.__cost


class Pizza(object):
    def __init__(self, name):
        self.__name = name
    __ingredient = []


    def add_ingredient(self, ingredient):
        self.__ingredient.append(ingredient)


    def get_name(self):
        return self.__name


    def get_weight(self):
        weight = 0
        for i in self.__ingredient:
            weight += i.get_weight()
        return weight / 1000


    def get_cost(self):
        cost = 0
        for i in self.__ingredient:
            cost += i.get_cost()
        return cost

        



class Order(object):
    __pizza = list()
    def add_pizza(self, pizza):
        self.__pizza.append(pizza)


    def get_cost(self):
        cost = 0
        for i in self.__pizza:
            cost += i.get_cost()
        return cost 


    def print_receipt(self):
        for i in self.__pizza:
            print(f'{i.get_name()} ({"%.3f" % i.get_weight()}г) - {"%.2f" % i.get_cost()}руб')


# cream_sauce = Ingredient('Сливочный соус', 50, 50)
# blue_cheese = Ingredient('Сыр блю чиз', 100, 100)
# mozzarella = Ingredient('Моцарелла', 100, 100)
# cheddar = Ingredient('Чеддер', 100, 100)
# parmesan = Ingredient('Пармезан', 100, 100)

# pizza = Pizza('Четыре сыра')
# pizza.add_ingredient(cream_sauce)
# pizza.add_ingredient(blue_cheese)
# pizza.add_ingredient(mozzarella)
# pizza.add_ingredient(cheddar)
# pizza.add_ingredient(parmesan)

# order = Order()

# print(pizza.get_cost())
# print(pizza.get_weight())

# order.add_pizza(pizza)
# order.add_pizza(pizza)
# order.add_pizza(pizza)
# print(order.get_cost())
# print(order.print_receipt())

# # self.__pizza.append(f'{pizza.get_name()} ({"%.3f" % pizza.get_weight()}г) - {"%.2f" % pizza.get_cost()}руб')