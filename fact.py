

def factorial(num):
 if num==1:
  return True
 else:
  return num*factorial(num-1)
num=int(input("input a number to compute the factorial:"))
print(factorial(num))
