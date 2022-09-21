def Task1():
    print("Task 1")

    file = open("src/Files/text.txt")
    str = [int(a) for a in file.read().split()]
    file.close()

    file = open("src/Files/newText.txt", "w")
    file.write(f"Max: {max(str)}\nMin: {min(str)}")
    file.close()


def Task2():
    print("Task 2")

