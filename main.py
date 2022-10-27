# 1.
# class Laptop:
#     """
#     Make the class with composition.
#     """
# class Battery:
#     """
#     Make the class with composition.
#     """
#
print("Task 1:\t Composition.\n")


class PC:
    manufacturer: str
    model: str
    price: float

    def __init__(self, manufacturer, model, price):
        self.manufacturer = manufacturer
        self.model = model
        self.price = price

    def print_info(self):
        print(f"Manufacturer: {self.manufacturer} \t Model: {self.model} \t Costs: {self.price}")


class Notebook(PC):
    screen_size: float
    battery_capacity: int

    def __init__(self, manufacturer, model, price, screen_size, battery_capacity):
        super().__init__(manufacturer=manufacturer, model=model, price=price)
        self.screen_size = screen_size
        self.battery_capacity = battery_capacity

    def print_info(self):
        print(
            f"Manufacturer: {self.manufacturer} \t Model: {self.model} \t Screen diagonal: {self.screen_size} \t "
            f"Battery capacity: {self.battery_capacity} \t Costs: {self.price}")


home_pc = PC("Dell", "A1", 2300.88)
notebook = Notebook("Asus", "571LH", 999.99, 15.6, 4500)

home_pc.print_info()
notebook.print_info()

# 2.
# class Guitar:
#     """
#     Make the class with aggregation
#     """
# class GuitarString:
#     """
#     Make the class with aggregation
#     """

print("\nTask 2:\t Aggregation.\n")


class GuitarString:
    material: str
    thickness: float

    def __init__(self, material, thickness):
        self.material = material
        self.thickness = thickness

    def info(self):
        return f"string is made of: {self.material} and is {self.thickness} inches thick."


class Guitar:
    material: str
    strings: list
    string_count: int

    def __init__(self, material, strings):
        self.material = material
        self.strings = strings
        self.string_count = self.strings.__len__()

    def print_info(self):
        print(f"The guitar is made of {self.material} and has {self.string_count} strings:")
        for i in range(self.string_count):
            print(f"\t {i} \t {self.strings[i].info()}")


string_1 = GuitarString("Metal", 0.12)
string_2 = GuitarString("Metal", 0.13)
string_3 = GuitarString("Metal", 0.14)
string_4 = GuitarString("Metal", 0.15)
string_5 = GuitarString("Metal", 0.16)
string_6 = GuitarString("Metal", 0.17)
g_1 = Guitar("Wood", [string_1, string_2, string_3, string_4, string_5, string_6])
g_1.print_info()

# 3
# class Calc:
#     """
#     Створіть клас з одним методом "add_nums" та 3 атрибутами, який повертає суму цих атрибутів.
#     """
#
print("\nTask 3:\t Calculator.\n")


class Calc:
    a: float
    b: float
    c: float

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # more convenient will be using a static method here
    @staticmethod
    def static_add_nums(a, b, c):
        print(f"The sum of {a}, {b} and {c} is {a + b + c}")

    def add_nums(self):
        return Calc.static_add_nums(self.a, self.b, self.c)


Calc.static_add_nums(2, 3, 9)
calculator = Calc(2, 18, 99)
calculator.add_nums()

# 4*.
# class Pasta:
#     """
#     Створіть клас, який приймає 1 атрибут при ініціалізації - ingredients і визначає інгридієнти атрибута екземпляра.
#     Він повинен мати 2 методи:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
#     """
#
# 5*.
# class Concert:
#     """
#     Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50
#     """
#
# 6.
# class AddressBookDataClass:
#     """
#     Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str),
#     birthday (str), age (int)
#     """
#
# 7. Create the same class (6) but using NamedTuple
# 8.
# class AddressBook:
#     """
#     Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for AddressBookDataClass defined above.
#     Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='',
#     email='', birthday= '', age='')
#     """
# 9.
# class Person:
#     """
#     Change the value of the age property of the person object
#     """
#     name = "John"
#     age = 36
#     country = "USA"
#
# 10.
# class Student:
#     """
#     Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
#     """
#     id = 0
#     name = ""
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
