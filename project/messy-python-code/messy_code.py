def calc(a,b):
 s=0
 for i in range(a,b+1):
  if i%2==0:s=s+i
 return s
print(calc(1,10))