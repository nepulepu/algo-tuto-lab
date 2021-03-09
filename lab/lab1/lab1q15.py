import random,time,string
starttime=time.time()

def getPassword(number):
    password_char=string.ascii_letters+string.digits+string.punctuation
    password= ''.join(random.choice(password_char)for i in range(number))
    return password

leng=int(input("Please insert password length: "))
print("your password is: "+ getPassword(leng))