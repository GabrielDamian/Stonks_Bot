import matplotlib.pyplot as plt
import csv
from utils import *
from graphHandler import *
from generatorCombinatiiSegmente import *
from patternFinder import *

if __name__ == '__main__':

    #INPUT - FILTRARE ----------------------------
    candleSize = 3
    vector = readDataFromFile('AAPL.csv',linesToRead=404)

    graph = graphData()

    graph.setInputData(vector)
    # graph.printInputData()
    # graph.plotInputData('Candle Data')

    graph.inputToCandle(candleSize=candleSize)
    # graph.plotCandles('Candle Data')

    graph.filterCandles(0.8,0.3) #param_1, param_2 spun cat de atenta la detalii sa fie filtrarea (param mare => exclude delatiile fine)
    # graph.plotCandles('Candle Filtered Data')


    graph.candlesToFunctionWork(candleSize)
    # graph.plotCandlesToFunction('Without intern points')
    graph.generateInternPoints()
    graph.plotCandlesToFunction('Candle Data')


    #GENERATOR COMBINATII SEGMENTE----------------------------
    #last 5 min handler
    patternFinder = patternFinder(graph.candlesToFunction,20)
    # patternFinder.printInputData()

    patternFinder.segmenteazaInputData()
    # patternFinder.printSegUnice()

    patternFinder.genereazaCombinatiiSegmente()
    # patternFinder.printCombinatiiPerSegUnic()

    print('TESTING FILTER:-------------------')
    patternFinder.filterWithCrossCorelation(abatere=20)

    # patternFinder.printFilteredData()


    #TEST PLOT MANUAL
    arr_1_temp = [[0, 115.02000000000044], [1, 107.34999999999854], [2, 99.68999999999869], [3, 92.02000000000044], [4, 84.34999999999854], [5, 76.68000000000029], [6, 69.0099999999984], [7, 61.349999999998545], [8, 53.68000000000029], [9, 46.0099999999984], [10, 38.340000000000146], [11, 30.669999999998254], [12, 23.0], [13, 15.340000000000146], [14, 7.669999999998254], [15, 0.0], [16, 8.529999999998836], [17, 17.06999999999971], [18, 25.599999999998545], [19, 34.13000000000102]]
    arr_2_temp =  [[0, 16.884], [1, 27.805000000000003], [2, 38.659000000000006], [3, 49.513000000000005], [4, 60.367], [5, 71.221], [6, 82.075], [7, 92.929], [8, 103.78300000000002], [9, 114.637], [10, 95.542], [11, 76.447], [12, 57.352], [13, 38.257000000000005], [14, 19.095000000000002], [15, 0.0], [16, 8.375], [17, 16.75], [18, 25.058], [19, 33.433]]

    # plotArraySingur(arr_1_temp, 'arr_1')
    # plotArraySingur(arr_2_temp, 'arr_2')

    plt.show()

