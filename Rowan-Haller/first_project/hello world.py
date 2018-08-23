
nuv = 3153


a = 0
b = 1
count = 0


if nuv <= 0:
   print("Please enter a positive integer")
elif nuv == 1:
   print("Fibonacci sequence upto",nuv,":")
   print(a)
else:
   print("Fibonacci sequence upto",nuv,":")
   while count < nuv:
       print(a,end=' , ')
       c = a + b
       a = b
       b = c
       count += 1