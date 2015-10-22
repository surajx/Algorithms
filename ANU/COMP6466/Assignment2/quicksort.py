from random import random,randint

def quicksort(A, key=None):
    _quicksort(A, 0, len(A)-1, key)

def _quicksort(A, st_idx, sp_idx, key):
    if st_idx < sp_idx:
        p = partition(A, st_idx, sp_idx, key)
        _quicksort(A, st_idx, p-1, key)
        _quicksort(A, p+1, sp_idx, key)

def partition(A, st_idx, sp_idx, key):
    p_idx = randint(st_idx, sp_idx)
    pivot = A[p_idx]
    A[p_idx], A[sp_idx] = A[sp_idx], A[p_idx]
    i = st_idx
    for j in range(st_idx, sp_idx):
        if key:
            if key(A[j], pivot):
                A[i], A[j] = A[j], A[i]
                i += 1
        else:
            if A[j] <= pivot:
                A[i], A[j] = A[j], A[i]
                i += 1
    A[i], A[sp_idx] = A[sp_idx], A[i]
    return i

if __name__ == "__main__":
    class Vertex:
        pass
    def verMe(val):
        v = Vertex()
        v._value = val
        return v
    def getValue(self): return self._value
    Vertex.getValue = getValue 
    A = [verMe(randint(1,1000)) for i in range(1,1000)]
    B = [randint(1,1000) for i in range(1,1000)]
    def criterion(a,b): return a.getValue()<=b.getValue()
    quicksort(A, key=criterion)
    quicksort(B)
    for v in A:
        print v.getValue()
    print B
