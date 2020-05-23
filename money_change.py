def get_change(money):
    coins = [10, 5, 1]
    num_of_coin = 0
    for i in coins:
        num_of_coin += money//i
        money = money%i
        if i == 1:
            break

    return num_of_coin
    

if __name__ == "__main__":
    amt = int(input())
    res = get_change(amt)
    print(res)