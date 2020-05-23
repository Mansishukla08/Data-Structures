def lastdigitfibo(n):
    a, b = 0, 1
    for _ in range(n-1):
        a = a + b
        a %= 10
        b, a = a, b
    print(b)

if __name__ == "__main__":
    n = int(input())
    if n<=1:
        print(n)
        quit()
    lastdigitfibo(n)