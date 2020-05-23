
def euclid_gcd(a, b):
    if b == 0:
        return a
    x = a%b
    return euclid_gcd(b, x)
    
if __name__ == "__main__":
    a, b = map(int, input().split())
    print(euclid_gcd(a, b))
