from xmlrpc.server import SimpleXMLRPCServer
from multiprocessing import Process, Manager
import time

address = ('localhost', 50000)
server = SimpleXMLRPCServer(address, logRequests=True, allow_none=True)

def sort(num, sorted_list):
    time.sleep(num/10)
    sorted_list.append(num)
    print(list(sorted_list))

def sort_array(arr):
	N = len(arr)
	print("Random list received from client")
	print("Sorting...")
	sorted_list = Manager().list()
	processes = []
	for i in range(N):
		p = Process(target=sort, args=(arr[i],sorted_list))
		p.start()
		processes.append(p)
	for p in processes:
		p.join()
	print("Completed!")
	return list(sorted_list)

server.register_function(sort_array)

if __name__ == '__main__':
    try:
        print("Server running on %s:%s" % address)
        print("Use Ctrl-C to Exit")
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("Exiting")