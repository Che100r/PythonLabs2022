def func(s):
    while True:
        try:
            return int(input(s))
        except ValueError:
            print("Error conversion")


def file(modi):
    try:
        return open('file.bin', modi)
    except IOError:
        print("Error open file")


class MyException(Exception):
    pass


class Book:
    def __init__(self, name, cost, page):
        self.__name = name
        self.__cost = cost
        self.__page = page

    @property
    def name(self):
        return self.__name

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        if cost < 0:
            print("Not correct")
        else:
            self.__cost = cost
            print("Cost updated")

    def costPage(self):
        return self.__cost / self.__page

    def costUp(self):
        if self.__name[:4] == "Prog":
            self.__cost = self.__cost * 2

    def save(self):
        f = file("wb")
        s = self.__name + "\n" + str(self.__cost) + "\n" + str(self.__page)
        f.write(s.encode())
        f.close()

    def open(self):
        f = file("rb")
        mass = []
        for _ in f:
            mass.append(_.decode()[:-1])
        f.close()

        self.__name = mass[0]
        self.__cost = mass[1]
        self.__page = mass[2]


class Child(Book):
    def __init__(self, name, cost, page, genre):
        super().__init__(name, cost, page)
        self.__genre = genre

    def info(self):
        print("Name: " + self.name + "\nGenre: " + self.__genre)


while True:
    try:
        name = input("Enter name: ")
        if len(name) < 4:
            raise MyException
        break
    except MyException:
        print("Error")

cost = func("Enter cost: ")
page = func("Enter page: ")

b = Book(name, cost, page)
# b.save()
b.open()
