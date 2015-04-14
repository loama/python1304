print ("Mayor, menor. Ingresa los numeros, cuando acabes escribe YA")
cadena_numeros = list()
l= cadena_numeros


while True:
  new_item = input("> ")
  
  if new_item == 'YA':
    break
    
  cadena_numeros.append(new_item)
  continue

x=0

while x+1<len(l):
  if l[x]>l[x+1]:
    mayor=l[x]
  else: mayor=l[x+1] 
  x+=1
  
y=0  
while y+1<len(l):
  if l[y]<l[y+1]:
    menor=l[y]
  else: menor=l[y+1] 
  y+=1
  
mayor= int(''.join(map(str,mayor)))
menor= int(''.join(map(str,menor)))

print ("El mayor es {}".format(mayor))
print ("El menor es {}".format(menor))

v=mayor-menor

print ("El resultado es {}".format(v))