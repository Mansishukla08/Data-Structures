def fibonacci_partial_sum(from_, to):
    fib = [0, 1]
    res = 0
    from_ -= 2
    for i in range(1, to):
        fib.append(fib[i-1]+fib[i])
        if i == from_:
            res = sum(fib)
    return (sum(fib)-res)%10

if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum(from_, to))