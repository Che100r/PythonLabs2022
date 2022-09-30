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


class Child(Book):
    def __init__(self, name, cost, page, genre):
        super().__init__(name, cost, page)
        self.__genre = genre

    def info(self):
        print("Name: " + self.name + "\nGenre: " + self.__genre)


b = Book("Prog book", 1000, 300)
b.cost = -1
b.cost = 1500
print(b.costPage())
b.costUp()
print(b.costPage())

c = Child("book2", 2000, 300, "genre")
c.costPage()
print(c.info())
print("")
