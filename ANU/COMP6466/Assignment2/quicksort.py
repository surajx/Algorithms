from random import random,randint

def quicksort(A, st_idx, sp_idx):
    if st_idx < sp_idx:
        p = partition(A, st_idx, sp_idx)
        quicksort(A, st_idx, p-1)
        quicksort(A, p+1, sp_idx)

def partition(A, st_idx, sp_idx):
    p_idx = randint(st_idx, sp_idx)
    pivot = A[p_idx]
    A[p_idx], A[sp_idx] = A[sp_idx], A[p_idx]
    i = st_idx
    for j in range(st_idx, sp_idx):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[sp_idx] = A[sp_idx], A[i]
    return i

if __name__ == "__main__":
    A = [randint(1,1000) for i in range(1,1000)]
    quicksort(A, 0, len(A)-1)
    print A
