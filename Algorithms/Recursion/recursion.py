def factorial(n):
   if n == 0: #Base Case
       return 1
   else:
       return (n * (factorial(n - 1))) #Function Calling Itself
   

factorial(3)

def fibonacci (n):
  if n <= 1:
    return n
  else:
    return fibonacci (n - 1) + fibonacci (n - 2)
  

fibonacci(10)