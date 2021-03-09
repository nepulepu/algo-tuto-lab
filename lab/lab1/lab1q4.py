a=input("Write a number: ")
i=1
print("diviser for "+ a +" is: ", end="")
while i<=int(a):
    if int(a)%i==0:
        print(str(i)+",",end=" ")
    i+=1