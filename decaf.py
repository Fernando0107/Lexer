import itertools

#file 
'''
f = open("exp1.txt", "r")

print('\n-------------------- Opening file... ----------------------\n')
data = f.read().splitlines()
'''
#edges and alphabet
'''
edge = [[2, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [3, 4, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
'''

alpha = ['0','x', '-', '1', '2', '3', '4', '5', '6', '7', '8', '9' ,'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D' ,'E', 'F']

#lexer 

alm = []                                    #Almacenador de tokens
with open("testxt.txt") as f:
  syntax = True                             #Flag para verificar si el numero entero es valido
  dec = True                                #Flag para verificar si el numero entero es dcimal o hexadecimal

  while True:
    c = f.read(1)                           #Lee caracter por caracter
    
    if not c:                               #Cuando ya no hay mas caracteres en el archivo
        if alm[0] == alpha[0] and alm[1] == alpha[1]:               #Revisa si los primeros dos caracteres son 0x
        
            dec = False                                             #Si los primeros dos son 0x, entonces es hexa

        if syntax == True and dec == True:                          #Si el sitax esta correcto y la bandera de decimal es verdadera

            print('El numero entero decimal ingresado es correcto!\n')
            print("\n---------- End of file ----------\n")

        elif syntax == True and dec == False:                       #Si el sitax esta correcto y la bandera de decimal es falsa

            print('El numero entero hexadecimal ingresado es correcto!\n')
            print("\n---------- End of file ----------\n")

        if syntax == False:                                        #Si el sitax esta incorrecto 

            print('El numero entero ingresado es incorrecto!')
      
        break
    
    elif c in alpha:                                                #Revisa en el alphabeto si esta el caracter
        alm.append(c)
        print("Read a character:", c)
        print('\nCorrecto!\n')

    elif c not in alpha:                                            #Si no esta en el alphabeto, entonces activa el flag a False
        if c == ' ':
            syntax = True
            alm.append(c)
        else:
            print('La que no esta:',c)
            syntax = False

#Separar el array por espacios
space = ' '
spl = [list(y) for x, y in itertools.groupby(alm, lambda z: z == space) if not x]


print(spl)

