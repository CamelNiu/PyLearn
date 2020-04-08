#py多进程


# from multiprocessing import Process
# import os


# def run_proc(name):
#   print('Run child process %s (%s)...'% (name,os.getpid()))

# if __name__=='__main__':
#   print('Parent process %s.'% os.getpid())
#   p = Process(target=run_proc, args=('test',))
#   print('Child process will start.')
#   p.start()
#   p.join()
#   print('Child process end.')




# from multiprocessing import Pool
# import os,time,random

# # def long_time_task(name):
# #   print('Run task %s (%s)...' % (name, os.getpid()))
# #   start = time.time()
# #   time.sleep(random.random() * 3)
# #   end = time.time()
# #   print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# # if __name__ == "__main__":
# #   print('Parent process %s' % os.getpid())
# #   p = Pool(6)
# #   for i in range(10):
# #     p.apply_async(long_time_task,args=(i,))
# #   print('waiting for all subprocess done...')
# #   p.close()
# #   p.join()
# #   print('all subprocess done.')


# print(time.time())
# print(random.random())


# import subprocess

# print ("$ nslookup www.python.org")
# r = subprocess.call(['nslookup','www.python.org'])
# print('exit code:',r)




# from multiprocessing import Process,Queue
# import os,time,random

# def write(q):
#   print('Process to write:%s' % os.getpid())
#   for value in ['A','B','C']:
#     print('Put %s to queue...' % value)
#     q.put(value)
#     time.sleep(random.random())

# def read(q):
#   print('Process to read %s' % os.getpid())
#   while True:
#     value = q.get(True)
#     print('Get %s from queue.' % value)

# if __name__ == '__main__':
#   q = Queue()
#   pw = Process(target=write,args=(q,))
#   pr = Process(target=read,args=(q,))
#   pw.start()
#   pr.start()
#   pw.join()
#   print('结束')
#   pr.terminate()


# import time,threading



# def loop():
#   print('thread %s is runing...' % threading.current_thread().name)
#   n = 0
#   while  n < 5:
#     n = n+1
#     print('thread %s >>> %s' % (threading.current_thread().name,n))
#     time.sleep(1)
#   print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is runing...' % threading.current_thread().name)
# t = threading.Thread(target=loop)
# t.start()
# t.join()
# print('thread %s ended' % threading.current_thread().name)


# import time,threading

# lock = threading.Lock()

# balance = 0

# def change_it(n):
#   global balance
#   balance = balance+n
#   balance = balance-n


# def run_thread(n):
#   for i in range(1000000):

#       change_it(n)


# t1 = threading.Thread(target=run_thread,args=(5,))
# t2 = threading.Thread(target=run_thread,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)


# import threading, multiprocessing

# def loop():
#   x = 0
#   while True:
#     x = x ^ 1

# for i in range(6):
#   t = threading.Thread(target=loop)
#   t.start()



# x = 0;
# x = x ^ 1;
# print(x)


from multiprocessing import Pool
import os

def loop():
  print('child process %s' % os.getpid())
  x = 0
  while True:
    x = x ^ 1


if __name__ == '__main__':
  print('Parent process %s' % os.getpid())
  p = Pool(6)
  for i in range(6):
    p.apply_async(loop)
  print('waiting for all subprocess Done...')
  p.close()
  p.join()