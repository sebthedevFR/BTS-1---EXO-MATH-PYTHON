# Créé par Fenrir, le 26/04/2016 en Python 3.2
def compteCarac(car,test) :
    n = 0
    for x in test :
        if x.lower() == car.lower() :
            n = n + 1
    return n

print (compteCarac('A','Je mappelle SebAstien Toursel'))
