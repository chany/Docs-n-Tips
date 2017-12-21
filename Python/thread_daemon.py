import threading
import time

def first_function():
    print (threading.currentThread().getName() + str(' 스레드 시작'))
    time.sleep(3)
    print (threading.currentThread().getName() + str( ' 스레드 종료'))

def second_function():
    print (threading.currentThread().getName() + str(' 스레드 시작'))
    # sleep 없음
    print (threading.currentThread().getName() + str( ' 스레드 종료'))

t_a = threading.Thread(name='first_function', target=first_function, daemon=True)
t_b = threading.Thread(name='second_function', target=second_function)

t_a.start(); t_b.start()
