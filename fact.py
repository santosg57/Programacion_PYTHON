# calcula el factorial (3!) de dos maneras:

def fac_v1(n):
   fac = 1
   for i in range(1,n+1):
      fac = fac*i
   return fac

def fac_v2(n):
   fac = 1
   i = 1
   while (i <= n):
      fac = fac*i
      i = i+1
   return fac

def fac_v3(n):
  if (n == 1):
     fac = 1
  else:
     fac = n * fac_v3(n-1) 
  return fac

n = input('numero: ')

print fac_v1(n)
print fac_v2(n)
print fac_v3(n)


