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

print(spl)

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



print('\nGood!\n',good)
print('\nBad!\n',bad)











'''
newarr =[]

for i in range(len(alm)):               #Revisa el primer array ->[[]]<-
    for j in range(len(alm[i])):        #Revisa el segundo array [->[]<-]
        print(alm[i][j], end=' ')
        if alm[i][j] in alpha:
            x = alm[i][j]
            newarr.append(x)
            print('test good!')
        else:
            print('Test fail')
            break
    print()    
'''
