name=input("Your name is: ")
age=input("Your age is: ")

age100=2021+(100-int(age))
txt="Dear {}, You will be 100 years old on {}"
print(txt.format(name,age100))
