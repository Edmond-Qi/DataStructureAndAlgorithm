# coding:utf-8


def merge_part(group1, group2):
    """归并排序，稳定，最优时间复杂度和最坏时间复杂度一致"""
    n1 = len(group1)
    n2 = len(group2)
    i = 0
    j = 0
    li = []
    while i < n1 or j < n2:
        if i < n1 and j < n2:
            if group1[i] < group2[j]:
                li.append(group1[i])
                i += 1
            elif group1[i] > group2[j]:
                li.append(group2[j])
                j += 1
        elif i >= n1:
            li.append(group2[j])
            j += 1
        elif j >= n2:
            li.append(group1[i])
            i += 1
    return li


def merge_sort(L):
    n = len(L)
    if len(L[0:int(n / 2)]) > 1:
        L1 = merge_sort(L[0:int(n / 2)])
    else:
        L1 = L[0:int(n / 2)]
    if len(L[int(n / 2):]) > 1:
        L2 = merge_sort(L[int(n / 2):])
    else:
        L2 = L[int(n / 2):]
    L = merge_part(L1, L2)
    return L


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 100, 44, 55, 20, 45, 6, 7, 9, 12]
    print(merge_sort(alist))
