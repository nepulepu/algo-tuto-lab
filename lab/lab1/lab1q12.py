def fibonacci(c):
    a=[1,1]
    i=1
    while i<c-1:
        a.append(a[len(a)-1]+a[len(a)-2])
        i+=1
    return a

numb=eval(input("input a number: "))

print(list(fibonacci(numb))) 