def calc(num):
    minOP = [None for i in range(num+1)]
    minOP[0], minOP[1] = 0, 0
    # operations x*2 // x*3 // x+1
    # calculating the min number of operations
    for i in range(2, num+1):
        op1, op2, op3 = num, num, num 
        op1 = minOP[i-1] +1
        if i%2 == 0 :
            op2 = minOP[i//2] + 1
        if i%3 == 0 :
            op3 = minOP[i//3] + 1
        minOP[i] = min(op1, op2, op3)
    
    # storing the progression
    nums = [num]
    while num!=1:
        if num%3 ==0 and minOP[num]-1 == minOP[num//3]:
            nums += [num//3]
            num = num//3
        elif num%2 ==0 and minOP[num]-1 == minOP[num//2]:
            nums += [num//2]
            num = num//2
        else:
            nums += [num-1]
            num = num - 1

    progress = ' '.join([str(i) for i in nums][::-1])
    
    return minOP[number], progress

        
if __name__ == "__main__":
    number = int(input()) 
    res, seq = calc(number)
    print(res)
    print(seq)
