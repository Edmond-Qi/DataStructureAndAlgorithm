import time


def select_sort(alist):
    """选择排序：不稳定"""
    n = len(alist)
    start_time = time.time()
    for i in range(n - 1):
        min_number = i
        for j in range(i + 1, n):
            if alist[j] < alist[min_number]:
                min_number = j
        alist[i], alist[min_number] = alist[min_number], alist[i]
    end_time = time.time()
    print("Time:%f" % (end_time - start_time))


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 45, 6, 7, 9, 12]
    select_sort(alist)
    print(alist)
