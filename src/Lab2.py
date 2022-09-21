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
