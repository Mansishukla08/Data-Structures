
def fibonacci_sum_squares_naive(n):
    fib = [0, 1]
    sq_fib = [0, 1]
    for i in range(1, n):
        fib.append(fib[i-1]+fib[i])
        sq_fib.append((fib[i-1]+fib[i])**2)
    return sum(sq_fib)%10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))