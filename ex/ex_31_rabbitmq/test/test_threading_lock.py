import threading

thread_lock = threading.Lock()

threadList = []
global_data = 0

def mycallback(thread_num):
    global global_data
    # 1. ===================================
    # global thread_lock
    # with thread_lock:
    #     for i in range(1000000):        
    #         global_data = global_data + 1
    # 2. ===================================
    thread_lock.acquire()
    for i in range(1000000):        
        global_data = global_data + 1
    thread_lock.release()            

if __name__ == '__main__':
    for i in range(10):
        th = threading.Thread(target=mycallback, args=(i,))
        threadList.append(th)
        th.start()
    for i in range(10):
        threadList[i].join()

    print(global_data)
        

