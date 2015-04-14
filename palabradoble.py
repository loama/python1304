input_string = input ("¿Que palabra quieres hacer doble? ")
cadena = list()
s=input_string
x=0
while x<len(s):
  resultado=s[x]*2
  x=x+1
  cadena.append(resultado)
  
str=''.join(cadena)
print (str) 