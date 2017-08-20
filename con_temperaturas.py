def Fah_to_Cel(f): 
   return f, ' grados F equivale a ', round(5*(float(f)-32)/9,3), ' C'
def Cel_to_Fah(c):
   return c, ' grados C equivale a ', round(9*float(c)/5 + 32,3), ' F'
def Kel_to_Cel(k):
   return k, ' grados K equivale a ', round(k-273.15,3) ,' C'
def Cel_to_Kel(c):
   return c, ' grados C equivale a ', round(c+273.15,3) ,' K'
def Kel_to_Fah(k):
   return k, ' grados K equivale a ', round(9*(k-273.15)/5 + 32,3),' F'
def Fah_to_Kel(f):
   return f, ' grados F equivale a ', round(5*(f-32.0)/9 + 273.15,3),' K'

print '''---------------------------\n
CONVERSION ENTRE TEMPERATURAS       \n
---------------------------'''

tem = {1 : Fah_to_Cel,
       2 : Cel_to_Fah,
       3 : Kel_to_Cel,
       4 : Cel_to_Kel,
       5 : Kel_to_Fah,
       6 : Fah_to_Kel
}

print ''' Deseas convertir: \n
Fharenheit a Celsius ---- 1 \n
Celsius a Fahrenheit ---- 2 \n
Kelvin a Celsius -------- 3 \n
Celsius a Kelvin -------- 4 \n
Kelvin a Fahrenheit ----- 5 \n
Fahrenheit a Kelvin ----- 6 \n
TERMINAR ---------------- 7 \n '''

op = input('Opcion que deseas convertir:')

if(1 <= op and op <= 6):
   val = input('Introduce el valora convertir126666666666:')
   print tem[opt](val)
