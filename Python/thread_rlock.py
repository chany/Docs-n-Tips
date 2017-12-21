import threading
import time

class Box(object):
    lock = threading.RLock()   # RLock 사용

    def __init__(self):
        self.total_items = 0

    def execute(self, n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()

    def add(self):
        Box.lock.acquire()   # Lock 잠금
        self.execute(1)      # Lock()의 경우, 여기서 또 잠그려고하면 마냥 기다림
        Box.lock.release()

    def remove(self):
        Box.lock.acquire()   # Lock 잠금
        self.execute(-1)     # Lock()의 경우, 여기서 또 잠그려고하면 마냥 기다림
        Box.lock.release()


def adder(box, items):
    while items > 0:
        print ("box에 1 더하고, item 1 줄이기")
        box.add()
        time.sleep(1)
        items -= 1
        
def remover(box, items):
    while items > 0:
        print ("box에 1 빼고, item 1 줄이기")
        box.remove()
        time.sleep(1)
        items -= 1


items = 5
print ("box에 item {}개 넣기".format(items))

box = Box()

t1 = threading.Thread(target=adder, args=(box,items))
t2 = threading.Thread(target=remover, args=(box,items))

t1.start()
t2.start()

t1.join()
t2.join()

print ("box에 {}개 item 남아있음.".format(box.total_items))
