a="koceng"
def isPalindrome(b):
    return b==b[::-1]

ans=isPalindrome(a)
if ans:
    print(a+" is a palindrome")
else:
    print(a+" is not a palindrome")       