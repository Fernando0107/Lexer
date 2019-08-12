import itertools

alpha = ['0', 'x', '-', '1', '2', '3', '4', '5', '6', '7', '8',
         '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']

#Leer caracter por caracter
alm = []
with open("testxt.txt") as f:
  while True:
    c = f.read(1)
    if not c:
      print("End of file")
      break
    print("Read a character:", c)
    alm.append(c)

space = ' '
spl = [list(y) for x, y in itertools.groupby(alm, lambda z: z == space) if not x]

#print(spl)

good = []               
bad = []

def fun(array):
    temp = []
    for i in range(len(array)):
        #return(array[i])
        y = array[i]

        if y in alpha:
            
            temp.append(y)
            #print('Correcto!')
        elif y not in alpha:
            bad.append(y)
            #print('Incorrecto')
    
    if(len(temp) != 0):
        good.append(temp)



for i in range(len(spl)):
    x = spl[i]
    #print(x)
    #print('Resultado: \n ', fun(x))
    fun(x)


hexa = []           #En este arreglo, guardariamos los hexadecimales 
dec = []            #En este arreglo, guardariamos los decimales

print('\nEstos numeros ingresados son correctos!\n',good)
print('\nEstos numero ingresados son incorrectos!\n',bad)

















'''
def fun2(array):
    temp = []
    temp2 = []
    for i in range(len(array)):
        #return(array[i])
        y = array[i]
        ini = array[0]
        fin = array[1]

        if ini == alpha[0] and fin == alpha[1]:

            temp.append(y)
            #print('Correcto!')
        elif y not in alpha:

            temp2.append(y)
            #print('Incorrecto')

    if(len(temp) != 0):
        hexa.append(temp)
        dec.append(temp2)
        


for i in range(len(good)):
    w = good[i]
    #print(x)
    #print('Resultado: \n ', fun(x))
    fun2(w)

print('\Hexa!\n', hexa)
print('\nDec!\n', dec)
'''