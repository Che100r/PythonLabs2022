import math


def Task1():
    print("Task 1")

    file = open("src/Files/input.txt")
    str1 = [int(a) for a in file.read().split()]
    file.close()

    file = open("src/Files/output.txt", "w")
    file.write(f"Max: {max(str1)}\nMin: {min(str1)}")
    file.close()


def Task2():
    print("Task 2")

    file = open("src/Files/input.txt")
    str1 = [int(a) for a in file.read().split()]
    file.close()

    file = open("src/Files/output.txt", "w")
    file.write(f"Multiplication: {math.prod(str1)}")
    file.close()


def Task3():
    print("Task 3")

    file = open("src/Files/input_1.txt")
    str1 = [a for a in file.read().split()]
    file.close()

    file = open("src/Files/input_2.txt")
    str2 = [a for a in file.read().split()]
    file.close()

    s = set(str1).intersection(set(str2))

    file = open("src/Files/output.txt", "w")
    file.write(f"{s}")
    file.close()


def Task4():
    print("Task 4")

    file = open("src/Files/inputt.txt")
    str1 = file.read()
    file.close()
    str1 = str1.translate({ord(i): None for i in '.,!? '}).lower()
    str2 = set(str1)
    dictionary = {}

    for c in str2:
        dictionary[c] = str1.count(c)

    sort = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

    file = open("src/Files/output.txt", "w")
    for k, i in sort.items():
        file.write(f"{k}: {i}\n")

    file.close()
