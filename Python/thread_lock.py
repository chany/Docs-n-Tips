import threading

#### 공유 변수들
shared_with_lock = 0
shared_with_no_lock = 0
COUNT = 100000
shared_lock = threading.Lock()  # Lock()

#### thread로 실행할 함수들

#### LOCK 사용 ##
def increment_with_lock():
    """Lock 걸고나서 1 증가 후 Lock 풀기"""
    global shared_with_lock
    for i in range(COUNT):
        shared_lock.acquire()  # Lock().acquire()
        shared_with_lock += 1
        shared_lock.release()  # Lock().release()

def decrement_with_lock():
    """Lock 걸고나서 1 감소 후 Lock 풀기"""
    global shared_with_lock
    for i in range(COUNT):
        shared_lock.acquire()
        shared_with_lock -= 1
        shared_lock.release()

#### NO LOCK ##
def increment_without_lock():
    """Lock 없이 1 증가"""
    global shared_with_no_lock
    for i in range(COUNT):
        shared_with_no_lock += 1

def decrement_without_lock():
    """Lock 없이 1 감소"""
    global shared_with_no_lock
    for i in range(COUNT):
        shared_with_no_lock -= 1

#### thread 4개 생성
t1 = threading.Thread(target=increment_with_lock)
t2 = threading.Thread(target=decrement_with_lock)
t3 = threading.Thread(target=increment_without_lock)
t4 = threading.Thread(target=decrement_without_lock)

#### thread 각각 시작
t1.start()
t2.start()
t3.start()
t4.start()

#### 각 thread 종료 기다림
t1.join()
t2.join()
t3.join()
t4.join()

print ("Lock 사용한 공유 변수의 값 = {}".format(shared_with_lock))
print ("Lock 사용하지 않은 변수의 값 = {}".format(shared_with_no_lock))
