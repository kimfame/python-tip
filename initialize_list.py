import time
import datetime


def init_for_loop(n):
    start = time.time()
    a = []
    for _ in range(n):
        a.append(0)
    end = time.time()
    print(datetime.timedelta(seconds=(end-start)))
    return a

def init_list_comp(n):
    start = time.time()
    a = [ 0 for _ in range(n)]
    end = time.time()
    print(datetime.timedelta(seconds=(end-start)))
    return a 

# fastest way
def init_mul(n):
    start = time.time()
    a = [0] * n
    end = time.time()
    print(datetime.timedelta(seconds=(end-start)))
    return a


num = 10
init_for_loop(num)
init_list_comp(num)
init_mul(num)