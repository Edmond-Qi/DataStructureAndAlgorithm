def quickSort(L, low, high):
    """快速排序，不稳定"""
    i = low
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        # 左移
        while i < j and L[j] > key:
            j -= 1
        L[i] = L[j]
        while i < j and L[i] < key:
            i += 1
        L[j] = L[i]
    L[i] = key
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L


def binary_search(L, num):
    n = len(L)
    L = quickSort(L, 0, n-1)
    start_p = 0
    end_p = n-1
    while (end_p - start_p) > 0:
        if num == L[int((end_p + start_p)/2)]:
            return int((end_p + start_p)/2)
        elif num < L[int((end_p + start_p)/2)]:
            end_p = int((end_p + start_p)/2)
        elif num > L[int((end_p + start_p)/2)]:
            start_p = int((end_p + start_p)/2)
    else:
        print("这个数不存在！")


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 100, 44, 55, 20, 45, 6, 7, 9, 12]
    binary_search(alist,31)