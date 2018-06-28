def check_prime(integer):
    y=""
    x=[]
    for i in range(2, integer):
        check = integer % i
        if check == 0:
            x.extend([i])
            y = x
        if x == []:
            return True
    return y, False
