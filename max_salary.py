def maxDigit(n):
    ans = ""
    while len(n) > 0:
        md=str(max(n))
        for i in n:
            if isGreaterOrEqual(i,md):
                md = str(i)
        ans += md
        n.remove(int(md))
    return ans

def isGreaterOrEqual(x,y):
    if int(str(x)+y) > int(y+str(x)):
        return True
    return False

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    res = maxDigit(numbers)
    print(res)
    