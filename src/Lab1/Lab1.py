def Task1():
    print("Task 1")

    src = input()

    if src.isupper():
        print("YES")
    else:
        print("NO")


def Task2():
    print("Task 2")

    name = input()
    surname = input()

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
    i = int(num)
    if num.isnumeric():
        if (i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0):
            print("True")
        else:
            print("False")
    else:
        print("Enter number!!!")
        Task4()


def Task5():
    print("Task 5")
    list = []
    pos = 0
    neg = 0

    while 1:
        b = input()
        if b == '0':
            break

        list.append(int(b))

    for m in list:
        if m > 0:
            pos = pos + 1
        else:
            neg = neg + 1

    print(pos)
    print(neg)
