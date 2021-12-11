
'''
Primeste un vector de input (modelat in prealabil pentru a scoate zgomotul).
Primeste size segment principal + max_stretching + min_stretching
Primeste future_distance (ce pret din viitor sa retina pentru fiecare generare).
Determina cati vectori trebuie de genereze intre min si max.
(Vectorii len() diferit. ex: daca min = x=> len() = len(input) / x)
Metoda care face streching segmentelor din vectorii de mai sus, pana la marimea
segmentului principal.
Acum avem:
{
    marime_segment_principal: 4 //4 puncte din graficul de input
    future_distance: x
    min_stretching = 2
    max_stretching = 7
    combinatii:{
    '2':[ {values:[a,a,a,a], future_price:x}, {values:[b,b,b,b], future_price:x}... ] //vectori de 2 puncte adusi la 4 puncte
    //4, deoarece atat are segmentul principal cu care facem mai departe cross-corelation, bla bla
    '3':[],
    '4':[],
    '5':[],
    '6':[],
    '7':[]
    }
}
'''
class generatorSegment:

    inputData = None

    def __init__(self):
        pass

