import time


def insert_sort(alist):
    """插入排序：稳定"""
    n = len(alist)
    start_time = time.time()
    for i in range(1, n):
        for j in range(i,0,-1):
            if alist[j-1] > alist[j]:
                alist[j-1], alist[j] = alist[j], alist[j-1]
    end_time = time.time()
    print("Time:%f" % (end_time - start_time))


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 45, 6, 7, 9, 12]
    insert_sort(alist)
    print(alist)
