from random import *
import time
import threading

def merge_sort():
    arr = [randint(0, 100000) for i in range(1000000)]
    length = len(arr)

    start = 0
    end = length-1
    mid = (start+end)//2

    devide(arr, 0, mid)
    devide(arr, mid+1, end)
    merge(arr, 0, end)

    return True


def devide(arr, start, end):
    if start >= end: return

    mid = (start+end)//2

    devide(arr, start, mid)
    devide(arr, mid+1, end)
    merge(arr, start, end)

def merge(arr, start, end):
    mid = (start+end)//2
    i = start
    j = mid+1
    length = end-start+1

    new_arr = [0 for k in range(length)]
    
    for k in range(length):
        if i > mid: 
            new_arr[k] = arr[j]
            j += 1
        elif j > end:
            new_arr[k] = arr[i]
            i += 1
        elif arr[j] < arr[i]:
            new_arr[k] = arr[j]
            j += 1
        else:
            new_arr[k] = arr[i]
            i += 1

    for k in range(length):
        arr[k+start] = new_arr[k]


start = time.time()

t1 = threading.Thread(target=merge_sort)
t2 = threading.Thread(target=merge_sort)
t3 = threading.Thread(target=merge_sort)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = time.time()

print("thread time: ", end-start)


start = time.time()

for i in range(3):
    merge_sort()
    
end = time.time()

print("no thread time: ", end-start)


    
