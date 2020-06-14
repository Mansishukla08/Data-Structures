def DPchange(money):
    coins = [1, 3, 4]
    minNumCoins = [None for i in range(money+1)]
    minNumCoins[0] = 0
    for m in range(1,money+1):
        minNumCoins[m] = money
        for i in coins:
            if m >= i:
                numCoins = minNumCoins[m - i] + 1
                if numCoins < minNumCoins[m]:
                    minNumCoins[m] = numCoins
    return minNumCoins[money]

if __name__ == "__main__":
    money = int(input())
    result = DPchange(money)
    print(result)