import xmlrpc.client
import random
import sys

def gen_random_array(N, R):
    arr = []
    while len(arr) < N:
        tmp = random.randint(1, R)
        if tmp not in arr:
            arr.append(tmp)
    return arr

if __name__ == '__main__':
    name_of_file = sys.argv[0]
    address = sys.argv[1]
    N = int(sys.argv[2])
    R = int(sys.argv[3])
    #address = 'localhost:50000'
    #N = 8
    #R = 20
    arr = gen_random_array(N, R)
    print(f"N value is: {N} for range {R}")
    print(f"list: {arr}")
    server = xmlrpc.client.ServerProxy('http://'+address)

    sorted_list = server.sort_array(arr)
    print(f"Sorted list from server : {sorted_list}")