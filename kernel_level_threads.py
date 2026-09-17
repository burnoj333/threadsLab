import time
import threading
#poo poo caca

def worker(t):
    #show when this kernel level thread begins running
    print(f'[{time.strftime('%X')}] start kernel thread {t+1}')

    #blocking user level threwad for 3 seconds to simulate thread execution
    time.sleep(3)

    #show when this user level thread STOPS running
    print(f'[{time.strftime('%X')}] end kernel thread {t+1}')

    # return control to user level shceduler
    #yield

# def scheduler(threads):
#     #run each user level thread
#     for i in threads:
#         try:
#             #run this user level thread until it yields or finished
#             next(i)
#         except StopIteration:
#             #remove thread when its finished
#             threads.remove(i)

#----------------------------main---------------------------------

#craeting 3 native threads, each should map to seperate OS/kernel thread
threads=[
    threading.Thread(target=worker,args=(i,))for i in range(3)
]

start_time = time.perf_counter()

#expecting OS scheduler to run in parallel
for t in threads:
    t.start()
#wait for all threads to finish
for t in threads:
    t.join()

#outputting total time taken to run all KERNEL threads
end_time= time.perf_counter()
print(f'Total execution time is {end_time-start_time:.4f} seconds')