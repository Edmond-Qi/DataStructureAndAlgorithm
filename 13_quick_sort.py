#quick sort
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

if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 45, 6, 7, 9, 12]
    n = len(alist)
    quickSort(alist,0,n-1)
    print(alist)
