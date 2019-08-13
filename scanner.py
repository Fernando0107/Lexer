
alpha = ['0', 'x', '-', '1', '2', '3', '4', '5', '6', '7', '8',
         '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']


#Open File and split 
f = open('testxt.txt', "r")
lines = f.readlines()
for i in lines:
    spliter = i.split(" ")

print(spliter)

good = []
bad = []
hexa = []
dec = []

def scanner(s):
    print('test',s[0])
    try:
        if len(s)>1:
            if s[0] == alpha[0] and s[1] == alpha[1]:
                good.append(s)
                hexa.append(s)
                return '\nCorrecto!\n'
            else:
                pass
        else:
            pass
    except ValueError:
        pass
    try:
        float(s)
        good.append(s)
        dec.append(s)
        return '\nCorrecto!\n'
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        good.append(s)
        hexa.append(s)
        return '\nCorrecto!\n'
    except (TypeError, ValueError):
        bad.append(s)
        pass

    return '\nIncorrecto!\n'


tokens = []

for token in spliter:

    print(token)
    print(scanner(token))

print('Tokens validos:',good)
print('Tokens no validos:',bad, '\n')

print('Numeros enteros en Hexadecimal:', hexa)
print('Numeros enteros en Decimal', dec, '\n')