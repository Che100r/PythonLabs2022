def Task1():
    print("Task 1")

    src = "HE FDFLLO342555*^F$%"

    if src.isupper():
        print("YES")
    else:
        print("NO")


def Task2():
    print("Task 2")

    name = "First"
    surname = "Second"

    print(name[0] + "." + surname[0] + ".")


def Task3():
    print("Task 3")

    a = input()
    if a.isnumeric():
        for i in a:
            if a.count(i) == 1:
                print(i)
    else:
        print("Enter number!!!")
        Task3()


def Task4():
    print("Task 4")

    num = input()
    if num.isnumeric():
        if int(num) % 4 == 0:
            print("True")
        else:
            print("False")
    else:
        print("Enter number!!!")
        Task4()


def Task5():
    print("Task 5")

    str = input()

    a = int(str)

    print(a)

Task5()
