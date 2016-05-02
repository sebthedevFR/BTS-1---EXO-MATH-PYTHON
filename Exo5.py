# Créé par Fenrir, le 26/04/2016 en Python 3.2
def indexMaximum(liste) :
    ind = 0
    for i in range(len(liste)) :
        if liste[i] > liste[ind] :
            ind = i
    return ind

serie = [5,25,9,7,1,58,5,48]
print (indexMaximum(serie))
