import  sys

my_sam = open(sys.argv[1])

cero = open('d00.txt', 'w')
diez = open('d16.txt', 'w')

line = []

for i in my_sam:
   line = i.strip().split()
   print i
   print line[2]
   if (line[2] == '0'):
      print 'resultado 000000 : ', i
      cero.write(i)
      
   elif (line[2] == '16'):
      print 'resultado 161616161 : ', i
      diez.write(i)



