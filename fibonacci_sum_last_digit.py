
def fibonacci_sum(n):
    fib = [0, 1]
    for i in range(1, n):
        fib.append(fib[i-1]+fib[i])
    return sum(fib) % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))