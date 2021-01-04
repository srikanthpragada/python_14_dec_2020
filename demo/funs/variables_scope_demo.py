total = 0


def fun1():
    global total
    a = 1
    total = 10

    def fun2():
        nonlocal a
        a = a + 1
        print(a)

    fun2()
    print(a)


fun1()
