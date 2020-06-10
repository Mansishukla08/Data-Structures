
def swap(a, b):
    return b, a

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = swap(arr[i], arr[min_index])
    return arr

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    res = selection_sort(arr)
    for i in res:
        print(i, end=" ")