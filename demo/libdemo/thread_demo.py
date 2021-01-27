from threading import Thread
import threading


class PrintThread(Thread):
    def run(self):
        for n in range(1, 11):
            print(n)

        print("Child1 is done!")


def print_numbers(start, end):
    for n in range(start, end):
        print(n)

    print("Child2 is done!")


print(threading.active_count())
pt = PrintThread()
pt.setName("Child1")
pt.start()
print("Count  :", threading.active_count())
for t in threading.enumerate():
    print(t.getName())

t = Thread(target=print_numbers, args=(10,15))
t.start()
