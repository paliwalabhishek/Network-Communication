from multiprocessing import Process, Manager
import sys
import random
import time


def sort(num, sorted_list):
    time.sleep(num/10)
    sorted_list.append(num)

def gen_random_array(N, R):
    arr = []
    while len(arr) < N:
        tmp = random.randint(1, R)
        if tmp not in arr:
            arr.append(tmp)
    return arr

if __name__ == '__main__':
    name_of_file = sys.argv[0]
    N = int(sys.argv[1])
    R = int(sys.argv[2])
    #N = 8
    #R = 20
    arr = gen_random_array(N, R)
    sorted_list = Manager().list()
    processes = []
    for i in range(N):
        p = Process(target=sort, args=(arr[i],sorted_list))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    print(f"N value is: {N} for range {R}")
    print(f"list: {arr}")
    print(f"Sorted list : {sorted_list}")

