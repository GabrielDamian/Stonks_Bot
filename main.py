import matplotlib.pyplot as plt
import csv
from utils import *
from graphHandler import *
from generatorCombinatiiSegmente import *
from patternFinder import *

if __name__ == '__main__':

    #INPUT - FILTRARE ----------------------------
    candleSize = 3
    vector = readDataFromFile('AAPL.csv',linesToRead=50)

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
    graph.plotCandlesToFunction('Points')



    #GENERATOR COMBINATII SEGMENTE----------------------------

    generatorCombinatii = generatorSegment(graph.candlesToFunction)

    #last 5 min from live chart
    len_referinta = 37
    min_ref = len_referinta - 5
    max_ref = len_referinta + 5
    segment_curent_fals =[]
    for index, a in enumerate(graph.candlesToFunction):
        if index < len_referinta:
            segment_curent_fals.append(a)
        else:
            break
    plotArraySingur(segment_curent_fals,'test referinta')

    #segment_curent_fals = [[5,450],[6,800],[7,600],[8,100],[9,140],[10,250],[11,573],[12,400],[13,700],[14,790],[15,900],[16,1200],[17,1000],[18,1134],[19,1456],[20,1800]]

    generatorCombinatii.setParams(len(segment_curent_fals), min_ref, max_ref, segment_curent_fals)

    #x,y from 0
    generatorCombinatii.normalizeazaSegmentBaza()
    # seg_baza_normalizat = generatorSegment.data['segment']
    # plotArraySingur(seg_baza_normalizat,'Seg baza normalizat')


    #declara range introdus la setParams
    generatorCombinatii.determinaSizeVariatii()

    generatorCombinatii.genereazaVariatii()

    # generatorCombinatii.printData()

    #x,y from 0
    generatorCombinatii.normalizeazaVariatii()

    #gaseste punctele din segmentul de baza in graficul functiei comprimate sau extinse
    generatorCombinatii.comprima_interpoleaza_variatii()


    #TEMP TESTING AREA----------------------------

    # segment_referinta = generatorSegment.data['segment']
    # print('Referinta:', segment_referinta)

    generatorCombinatii.printVariatii()
    generatorCombinatii.printVariatiiInterPolate()

    # /variatii = generatorSegment.data['variatii']
    # variatii_inter = generatorSegment.data['variatii_interpolate']
    #
    # test_0 = variatii_inter['42'][0]['values']
    # test_0_before = variatii['42'][0]['values']
    # plot_3_arrays(segment_referinta,test_0,test_0_before,'pleaseeee')


    #last 5 min handler
    patternFinder = patternFinder(graph.candlesToFunction,10)
    patternFinder.segmenteazaInputData()

    patternFinder.genereazaCombinatiiSegmente()
    print('Final data:-------------')
    # patternFinder.printFinalData()

    #mostra
    mostraPatterFinder = patternFinder.returnFinalData()
    for a in mostraPatterFinder:
        print("--------------------------------")
        printMostraPatterFinder(a)

    print("AICI TEST")
    print(mostraPatterFinder)

    # plt.show()



