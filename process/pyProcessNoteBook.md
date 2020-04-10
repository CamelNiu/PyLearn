#### Python多进程

*1,认识fock函数*

    1,unix/linux操作系统提供，所以只能在linux/unix系统运行
    2,fork()调用过程中,操作系统会把当前进程复制一份出来，返回的时候两个进程均返回
    3,fork()返回两次,分别在父进程/子进程中返回。
        父进程返回子进程的进程id
        子进程返回0               (获取进程id：父进程getppid(),当前进程getpid())
    4,win下不能使用此函数
    
*2，multiprocessing模块*(跨平台版本的多进程模块)
    
1,简介
      
    multiprocessing模块，可以跨平台使用，提供了常用的Process,Queue,Pipe,Lock等组件
    
 2,Process类多进程实例  
 
    1，基础实例
    from multiprocessing import Process,Lock
    import os,time,random
    
    def child_process_func(name):
      #os.getpid() 获取当前进程id
      #os.getppid() 获取父进程id
      msg = "child process,My Name is "+str(name)+",processId is "+str(os.getpid())+" my father ProcessId is "+str(os.getppid())
      time.sleep(random.random()*5)
      print(msg)
    
    if __name__ == "__main__":
      print('parent process %s' % os.getpid() )
      # 这里表示Process类实例化了一个子进程对象,但是并未执行。target参数，表示子进程要执行的具体对象，args参数，表示子进程执行对象的参数
      p = Process(target=child_process_func,args=('a',))
      #p.start(),start()方法用于子进程对象的启动，即子进程开始执行
      p.start()
      #is_alive()方法，查看当前进程是否存在
      print(p.is_alive())#进程存在
      #p.join(),join()方法用于子进程结束。如果没有join，父进程子进程互不相干各自执行,如果有了join，则父进程等待子进程结束后才往下执行(可注释下面的p.join()语句尝试输出的不同结果)
      p.join()
      print(p.is_alive())#进程不存在
      print('parent end')
    
    #以上是一个最简单的Process类多进程实例。
    #知识点:os.getPid(),os.getppid(),time.sleep(),random.random()
    #Process类常用方法
    # Process(target,args),最常用的两个参数
    # start(),is_alive(),join(),常用方法
  
 3,Pool类进程池批量创建子进程 
    
    def child_process_func(name):
      #os.getpid() 获取当前进程id
      #os.getppid() 获取父进程id
      msg = "child process,My Name is "+str(name)+",processId is "+str(os.getpid())+" my father ProcessId is "+str(os.getppid())
      time.sleep(random.random()*5)
      #print(time.time())
      print(msg)
    
    if __name__ == '__main__':
      print('parent process %s' % os.getpid())
      #进程池指定最多进程，并且创建对象
      p = Pool(6)
      defParName = ['a','b','c','d','e','f']
      for name in defParName:
        #apply_async(defName,args=(param,))，创建进程，非阻塞的且支持结果返回后进行回调
        p.apply_async(child_process_func,args=(name,))
      #关闭进程池
      p.close()
      #p.terminal()#强制关闭进程
      #等待进程结束
      p.join()
      print('end')
    
      #知识点
      #以上是一个最简单的Pool进程池类多进程实例
      #p=Pool(num)
      #for i in range(num):
      #   p.apply_async(defName,args(param,))
      #p.close()
      #p.join()