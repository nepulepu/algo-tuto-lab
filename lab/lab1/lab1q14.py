
ayat=input("Enter a sentence : ")

x =ayat.split()
result =""

for i in x :
    result= i+" "+result
print(result)