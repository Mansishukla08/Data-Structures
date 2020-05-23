def get_optimal_value(capacity, weights, values):
    value = 0
    value_by_weight = [v/w for v, w in zip(values, weights)]
    while(capacity>0 and len(value_by_weight)>0):
        x = value_by_weight.index(max(value_by_weight))
        a = min(weights[x], capacity)
        value += a*value_by_weight[x]
        weights[x] -= a
        capacity -= a
        value_by_weight.pop(x)
        weights.pop(x)
    return value


if __name__ == "__main__":
    n, capacity =  map(int, input().split())
    values = list()
    weights = list()
    for i in range(n):
        vi, wi = map(int, input().split())
        values.append(vi)
        weights.append(wi)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
