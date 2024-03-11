# Задание 21.9.1 Создайте класс прямоугольника
#
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle : {self.x}, {self.y}, {self.width}, {self.height}"

# Пример использования:
rect = Rectangle(5, 10, 50, 100)
print(rect)  # Выведет: Rectangle : 5, 10, 50, 100

# Задание 21.9.2  Создайте класс «прямоугольник» с помощью метода init()

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle : {self.x}, {self.y}, {self.width}, {self.height}."

    def get_area(self):
        return self.width * self.height
# Пример использования:
rect = Rectangle(5, 10, 50, 100)
print(rect)  # Выведет: Rectangle : 5, 10, 50, 100
print(rect.get_area())  #5000

# Задание 21.9.3
# В проекте «Дом питомца» добавим новую услугу — электронный кошелек.
# Необходимо создать класс «Клиент», который будет содержать данные о клиентах и их финансовых операциях.
# О клиенте известна следующая информация: имя, фамилия, город, баланс.

class Client:
    def __init__(self, first_name, last_name, city, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"{self.first_name} {self.last_name}. {self.city}. Баланс: {self.balance} руб."

# Пример использования:
client = Client("Иван", "Петров", "Москва", 50)
print(client)  # Выведет: Иван Петров. Москва. Баланс: 50 руб.


# class Customers:
#     def __init__(self, first_name, second_name, city, balance):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.balance = balance
#         self.city = city
#
#     def __str__(self):
#         return f'''"{self.first_name} {self.second_name}". {self.city}. Баланс: {self.balance} руб.'''
#
#
# customer_1 = Customers('Иван', 'Петров', 'Москва', 50)
# print(customer_1)

# Задание 21.9.4
# Код позволит составить список гостей. В класс «Клиент» добавьте метод, который будет
# возвращать информацию только об имени, фамилии и городе клиента.#
# Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.

class Client:
    def __init__(self, first_name, last_name, city):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city

    def get_guest(self):
        return f"{self.first_name} {self.last_name}, г. {self.city}."

# Пример использования:
client_1 = Client("Иван", "Петров", "Москва")
client_2 = Client("Игорь", "Выборов", "Пермь")
client_3 = Client("Егор", "Куржон", "Омск")

guest_list=[client_1,client_2,client_3]

for guest in guest_list:
    print(guest.get_guest())    # Иван Петров, г. Москва.
                                # Игорь Выборов, г. Пермь.
                                # Егор Куржон, г. Омск.