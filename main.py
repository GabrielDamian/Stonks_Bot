import matplotlib.pyplot as plt
import csv
from utils import *
from graphHandler import *
from generatorCombinatiiSegmente import *

if __name__ == '__main__':

    candleSize = 3
    vector = readDataFromFile('AAPL.csv',linesToRead=204)

    graph = graphData()

    graph.setInputData(vector)
    # graph.printInputData()

    # graph.plotInputData('Input Data')

    graph.inputToCandle(candleSize=candleSize)
    # graph.plotCandles('Candles data')

    graph.filterCandles(1,0.3)
    graph.filterCandles(1,0.3)
    # graph.filterCandles(1,0.3)
    # graph.plotCandles('Filtered candles')

    # print('Filtered candles',graph.candlesData);


    graph.candlesToFunctionWork(candleSize)
    graph.generateInternPoints()
    # graph.plotCandlesToFunction('Points')



    #GENERATOR COMBINATII SEGMENTE

    #constructorul primeste inputData si il seteaza pe variabila
    generatorCombinatii = generatorSegment(graph.candlesToFunction)

    #data temporara, patternFinder o sa incerc orice segment(shiftat la dreapta cu o unitate)
    segment_curent_fals = [[5,450],[6,800],[7,600],[8,100],[9,140],[10,250],[11,573],[12,400],[13,700],[14,790],[15,900],[16,1200],[17,1000],[18,1134],[19,1456],[20,1800]]

    #seteaza parametrii obiectului (len(segment_curent_fals)),min_strech, max_strech, segment_curent)
    generatorCombinatii.setParams(len(segment_curent_fals),10,20,segment_curent_fals)

    #forteaza segment_curent sa inceapa din 0 (atat x cat si y) (din x si y scade minimul de x si minimul de y)
    generatorCombinatii.normalizeazaSegmentBaza()

    #insereaza cate o cheie in 'variatii' pentru fiecare unitate intre min_strech si max_strech
    generatorCombinatii.determinaSizeVariatii()

    #parcurge cheile variatiilor si segmenteaza toate segmentele posibile de acea dimensiune
    generatorCombinatii.genereazaVariatii()

    # generatorCombinatii.printData()

    #aduce toate variatiile in 0,0 ca punct de start (nu afecteaza marimea variatiei inca) (la fel cu normalizarea de mai sus, din x si y scade minimul de x si minimul de y)
    generatorCombinatii.normalizeazaVariatii()


    #comprima segmentele mai mari decat segmentul de baza la marimea segmentului de baza (Atat pe ox si cat pe oy)
    generatorCombinatii.comprima_interpoleaza_variatii()


    segment_referinta = generatorSegment.data['segment']
    print('Referinta:', segment_referinta)

    print('Variatii:')
    variatii = generatorSegment.data['variatii']
    for a in variatii:
        print(a,variatii[a])

    print('Variatii inter:')
    variatii_inter = generatorSegment.data['variatii_interpolate']
    for a in variatii_inter:
        print(a,variatii_inter[a])


    #nu este definita functie de extindere a segmentului curent din iteratie la lungimea segmentului de referinta
    #putem vizualiza corect doar segmentele care au fost comprimate len(seg_referinta) < len(segment_curent)

    #referinta cu albastru
    test_0 = variatii_inter['16'][3]['values']
    test_0_before = variatii['16'][3]['values']
    plotArray_curent_interpolar_before(segment_referinta,test_0,test_0_before,'pleaseeee')

    # test_1 = variatii_inter['12'][10]['values']
    # plotArrayCombinat(segment_referinta, test_1,'test_1')
    # test_2 = variatii_inter['13'][4]['values']
    # plotArrayCombinat(segment_referinta, test_2,'test_2')



    plt.show()



