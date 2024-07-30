def shors_algo(num1,num2):
    #m^x = n*y + 1
    x=y=1
    n1 = n2 = 1
    while True:
        print(n1,n2)
        if n1 == n2-1:
            print(f"expo of {num1} should be: ", x)
            print(f'expo of {num2} should be: ', y)
            break
        elif n1 < n2-1:
            x += 1
            n1 *= num1
        else:
            y += 1
            n2 *= num2



shors_algo(5,7)