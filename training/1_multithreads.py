import threading 
import time
def infinite_loop():
    while True:
        print("inf loop")
        time.sleep(1)
        pass
    
def myname():
    print("python")

t1 = threading.Thread(target=infinite_loop)
t2 = threading.Thread(target=myname)

#with nothreading the code is stuck in the loop
"""infinite_loop()
myname()
"""

#with threwading the code is not stuck in the loop

t1.start()
t2.start()