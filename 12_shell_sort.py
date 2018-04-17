import time


def shell_sort(alist, gap):
    """希尔排序：不稳定"""
    n = len(alist)
    start_time = time.time()
    count = 0
    for k in gap:
        flag = 0
        for i in range(0, k):
            iter_list = list(range(i, n, k))
            m = len(iter_list)
            for p in range(1,m):
                for j in iter_list[:0:-1]:
                    if alist[j - k] < alist[j]:
                        alist[j - k], alist[j] = alist[j], alist[j - k]
                        flag += 1
                        count += 1
                iter_list.pop()
        if flag == 0:
            break
    print(flag,count)

    end_time = time.time()
    print("Time:%f" % (end_time - start_time))


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 45, 6, 7, 9, 12]
    gap = [7, 5, 3, 2, 1]
    shell_sort(alist, gap)
    print(alist)
