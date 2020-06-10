def count_sort(arr):
    count = [0 for i in range(max(arr)+1)]
    # counting the occurance of each element
    for i in arr:
        count[i]+=1
    # calculating positions
    for i in range(1, len(count)):
        count[i]+=count[i-1]
    #filling the output array in order
    op = [0 for i in range(len(arr))]
    for i in arr:
        op[count[i]-1] = i
        count[i]-=1
    return op

if __name__ == "__main__":
    A = list(map(int, input().split()))
    res = count_sort(A)
    for i in res:
        print(i, end=" ")