def fun(**kwargs):
    print(kwargs)


def fun2(*args, **kwargs):
    print(args)
    print(kwargs)


fun(a=10, b=20)
fun(name='Python', version=3.9)
fun2(10, 20, 30, a=1, b=100)
