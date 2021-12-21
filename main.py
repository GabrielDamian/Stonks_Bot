import matplotlib.pyplot as plt
import csv
from utils import *
from graphHandler import *
from generatorCombinatiiSegmente import *
from patternFinder import *

if __name__ == '__main__':

    #INPUT - FILTRARE ----------------------------
    candleSize = 3
    vector = readDataFromFile('AAPL.csv',linesToRead=150)

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

    #last 5 min handler
    patternFinder = patternFinder(graph.candlesToFunction,10)
    patternFinder.printInputData()

    patternFinder.segmenteazaInputData()
    patternFinder.printSegUnice()

    patternFinder.genereazaCombinatiiSegmente()
    patternFinder.printCombinatiiPerSegUnic()

    print('TESTING FILTER:-------------------')
    patternFinder.filterWithCrossCorelation(abatere=50)

    # plt.show()



