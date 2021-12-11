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
    graph.plotCandlesToFunction('Points')



    #GENERATOR COMBINATII SEGMENTE
    generatorCombinatii = generatorSegment(graph.candlesToFunction)
    generatorCombinatii.setParams(5,2,7)

    generatorCombinatii.determinaSizeVariatii()
    generatorCombinatii.genereazaVariatii()
    # generatorCombinatii.printData()


    generatorCombinatii.printVariatii()
    generatorCombinatii.comprimare_segmente_mari()






    # plt.show()



