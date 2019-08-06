def reverse(a):
    return a[::-1]
def ispalindrome(a):
    rev=reverse(a)
    if(a==rev):
     return true
    return false
a="malayalam"
ans=ispalindrome(a)
if ans==1:
    print("palindrome")
else:
    print("not a palindrome")
