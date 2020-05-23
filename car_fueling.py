def compute_min_refills(distance, tank, n, stops):
    # write your code here
    num_refills, current_refills = 0, 0
    while(current_refills<= n):
        last_refills = current_refills 
        while(current_refills <= n and stops[current_refills+1]-stops[last_refills]<=tank):
            current_refills += 1
        if current_refills == last_refills:
            return -1
        if current_refills <= n:
            num_refills += 1 
    return num_refills

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, input().split()))
    stops.append(0)
    stops.append(d)
    stops.sort()    
    print(compute_min_refills(d, m, n, stops))