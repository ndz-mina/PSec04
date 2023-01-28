#Inicio del problema A
word1 = input ('Ingrese frase (o palabra) a comparar: ')
word2 = input ('Ingrese frase (o palabra) a verificar: ')
word1 = word1.lower()
word2 = word2.lower()
cmf1_1 = word1.isnumeric()
cmf2_1 = word2.isnumeric()

if (not cmf1_1) and (not cmf2_1):
    l1 = []
    n = 0
    m = len(word1)
    while n < m:                #Creando lista 1
        t1 = word1[n]
        e1 = '{}'.format(t1)
        if e1 != ' ':
            l1.append(e1)
            n += 1
        else:
            n += 1
    l2 = []
    p = 0
    q = len(word2)
    while p < q:                #Creando lista 2
        t2 = word2[p]
        e2 = '{}'.format(t2)
        if e2 != ' ':
            l2.append(e2)
            p += 1
        else:
            p += 1
    length1 = len(l1)
    length2 = len(l2)
    u = 0
    while u < length1:          #Comparación
        if (length1 == length2) and (l1[u] in l2) and (l2[u] in l1):
            u += 1
            if u == length1 - 1:
                print('Son anagramas.')
        else:
            print('No son anagramas.')
            u = length1
else:
    print('Error. El dato ingresado tiene algún elemento que no es alfabético.')

#Inicio del problema B
text = input('Ingrese una oración para verificar si es un tautograma: ')
text = text.lower()
vldt1 = text.isnumeric()
vldt2 = text.isalnum()

if (not vldt1) and (not vldt2):
    z = ' '
    if z in text:
        t = text[0]
        x = 0
        y = len(text)
        while x < y:
            k = text[x]
            w = text[x - 1]
            e3 = '{}'.format(w)
            if x > 0 and e3 == z and k == t:
                x += 1
                if x == (y - 1):
                    print('True.')
            elif x > 0 and e3 == z and k != t:
                x == y
                print('False.')
        else:
            x += 1
    else:
        print('Error. El dato ingresado no es una oración.')
else:
    print('Error. El dato ingresado tiene algún elemento que no es alfabético.')
