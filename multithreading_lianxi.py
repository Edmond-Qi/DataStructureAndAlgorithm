"""1、描述进程与线程的区别
""""""
2、使用子线程计算0到100的数字和，主线程等待计算结束后输出计算结果
"""

"""Ex1"""
# 一个进程在内存中占用单独的空间，耗用的资源多，
# 不同的进程之间不会共享变量，通信需要通过队列等机制
# 一个进程可以包含多个线程，而线程却不能
# 线程间共享全局变量，为了保证线程安全需要加锁

"""Ex2"""
# import threading
# import time


# def compute_sum(start_num, end_number):
#     global sum_all
#     sum_all = sum((i for i in range(start_num, end_number + 1)))
#
#
# if __name__ == "__main__":
#     start_time = time.time()
#     sum_all = 0
#     th_sum = threading.Thread(target=compute_sum, args=(0, 100))
#     th_sum.start()
#     th_sum.join()
#     end_time = time.time()
#     print("sum = ", sum_all)
#     print("Time:%f" % (end_time-start_time))
"""1、使用子进程计算0到100的数字和，主进程输出计算结果
2、使用进程池实现单文件拷贝（3个进程拷贝即可）
"""
"""ex1"""
from multiprocessing import Pool, Process, Queue
import os

#
#
# def compute_sum(start_num, end_number, q):
#     global sum_all
#     sum_all = sum((i for i in range(start_num, end_number + 1)))
#     q.put(sum_all)
#
#
# if __name__ == "__main__":
#     q = Queue()
#     p = Process(target=compute_sum, args=(0, 100, q))
#     p.start()
#     p.join()
#     print("Sum = ", q.get())

"""ex2"""


def copy_movie(i, start, end):
    with open("Video_2018-01-19_091805.wmv","rb") as f:
        f.seek(start)
        content = f.read(end-start)
        with open("Video.wmv","ab+") as f1:
            f1.seek(start)
            f1.write(content)


if __name__ == "__main__":
    file_name = "Video_2018-01-19_091805.wmv"
    size = os.path.getsize(file_name)
    length = 4
    block = size//length
    pool = Pool(3)
    for i in range(3):
        if i != 2:
            pool.apply_async(copy_movie,args=(i, i*block,(i+1)*block))
        else:
            pool.apply_async(copy_movie,args=(i,i*block,size))
    pool.close()
    pool.join()