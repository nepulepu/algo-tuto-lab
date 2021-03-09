num=eval(input("Enter a number: "))

if num>1:
    for i in range(2,num-1):
        if num%i==0:
            print(str(num)+ " is not prime number")
            print(str(num)+" can be divided by ",i)
            break
    print(str(num)+ " is a prime number")

else:
    print(str(num)+ " is not prime number")
