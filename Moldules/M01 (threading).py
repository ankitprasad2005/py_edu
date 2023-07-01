# multithreading , asyncronus 

import threading
import time

def lp1(x, y = 0.25):
    for i in range(x):
        print (i)
        time.sleep(y)

x = 10

# we can create multipe thread using same function
# args only take tuple as a parameter
a = threading.Thread(target=lp1, args=(x, 0.25))
b = threading.Thread(target=lp1, args=(x, 0.2))
a.start()
b.start()

print(threading.activeCount() * 10)

lp1(x, 0.15)

# waits for the thread to terminate
a.join()
b.join()

print ('THE END')