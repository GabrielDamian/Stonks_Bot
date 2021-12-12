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

    graph.plotInputData('Input Data')

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



    #GENERATOR COMBINATII SEGMENTE

    #constructorul primeste inputData si il seteaza pe variabila
    generatorCombinatii = generatorSegment(graph.candlesToFunction)

    #data temporara, patternFinder o sa incerc orice segment(shiftat la dreapta cu o unitate)
    segment_curent_fals = [[5,28609],[6,28620],[7,28631],[8,28643],[9,28654]]

    #seteaza parametrii obiectului (len(segment_curent_fals)),min_strech, max_strech, segment_curent)
    generatorCombinatii.setParams(5,2,7,segment_curent_fals)

    #forteaza segment_curent sa inceapa din 0 (atat x cat si y)
    generatorCombinatii.normalizeazaSegmentBaza()

    #insereaza cate o cheie in 'variatii' pentru fiecare unitate intre min_strech si max_strech
    generatorCombinatii.determinaSizeVariatii()

    #parcurge cheile variatiilor si segmenteaza toate segmentele posibile de acea dimensiune
    generatorCombinatii.genereazaVariatii()

    # generatorCombinatii.printData()

    #aduce toate variatiile in 0,0 ca punct de start (nu afecteaza marimea variatiei inca)
    generatorCombinatii.normalizeazaVariatii()

    # generatorCombinatii.printVariatii()

    #comprima segmentele mai mari decat segmentul de baza la marimea segmentului de baza (Atat pe ox si cat pe oy)
    # generatorCombinatii.comprimare_segmente_mari()

    # generatorCombinatii.comprimare_segmente_mici()

    segment_mic = [[0,6],[1,4],[2,9],[3,12],[4,5],[5,7],[5,11],[6,15],[8,12]]
    segment_mare = [[0,1], [1,5], [2,7],[3,9],[4,7],[5, 4],[6,2],[7,5],[8,5],[9,7],[10,5],[11,9],[12,5],[13,11],[14,20],[15,12]]
    comprimaSegment(segment_mic, segment_mare)

    plt.show()



