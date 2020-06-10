def merge_sort(A):
    if len(A) == 1:
        return A
    m = len(A)//2
    B = merge_sort(A[:m])
    C = merge_sort(A[m:])
    RA = merge(B, C)
    return RA
    
def merge(B, C):
    D = []
    while len(B)>0 and len(C)>0 :
        if B[0]>C[0]:
            D.append(C[0])
            C.remove(C[0])
        else:
            D.append(B[0])
            B.remove(B[0])
    if len(B)>0:
        for i in B:
            D.append(i)
    if len(C)>0:
        for i in C:
            D.append(i)
    return D
    
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    res = merge_sort(arr)
    for i in res:
        print(i, end=" ")