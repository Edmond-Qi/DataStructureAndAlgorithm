import time


def bubble_sort1(alist):
    """冒泡排序1"""
    n = len(alist)
    start_time = time.time()
    for j in range(n - 1):
        for i in range(0, n - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    end_time = time.time()
    print("Time:%f" % (end_time - start_time))


def bubble_sort2(alist):
    """冒泡排序2:优化"""
    n = len(alist)
    start_time = time.time()
    for j in range(n - 1):
        flag = 0
        for i in range(0, n - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                flag = 1
        if flag == 0:
            break
    end_time = time.time()
    print("Time:%f" % (end_time - start_time))


if __name__ == "__main__":
    alist1 = [54, 26, 93, 17, 77, 31, 44, 55, 20, 45, 6, 7, 9, 12]
    alist2 = [54, 26, 93, 17, 77, 31, 44, 55, 20, 45, 6, 7, 9, 12]
    bubble_sort1(alist1)
    bubble_sort2(alist2)
    print(alist1)
    print(alist2)
