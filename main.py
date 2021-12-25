import matplotlib.pyplot as plt
import csv
from utils import *
from graphHandler import *
from generatorCombinatiiSegmente import *
from patternFinder import *

if __name__ == '__main__':

    #INPUT - FILTRARE ----------------------------
    candleSize = 3
    vector = readDataFromFile('AAPL.csv',linesToRead=1000)

    graph = graphData()

    graph.setInputData(vector)
    # graph.printInputData()
    # graph.plotInputData('Raw input data')

    graph.inputToCandle(candleSize=candleSize)
    # graph.plotCandles('Candle Data')

    graph.filterCandles(0.8,0.3) #param_1, param_2 spun cat de atenta la detalii sa fie filtrarea (param mare => exclude delatiile fine)
    # graph.plotCandles('Candle Filtered Data')


    graph.candlesToFunctionWork(candleSize)
    # graph.plotCandlesToFunction('Without intern points')
    graph.generateInternPoints()
    # graph.plotCandlesToFunction('Candle Data')


    #GENERATOR COMBINATII SEGMENTE----------------------------
    patternFinder = patternFinder(graph.candlesToFunction,30)
    # patternFinder.printInputData()
    # patternFinder.plotInputData('Input to Pattern Finder:')

    patternFinder.segmenteazaInputData()
    # patternFinder.printSegUnice()

    patternFinder.genereazaCombinatiiSegmente()
    # patternFinder.printCombinatiiPerSegUnic()

    #FINAL - FITRARE SEGMENTE REDUNDANTE (sum > abatere)

    patternFinder.filterWithCrossCorelation(abatere=1000)
    patternFinder.printFilteredData()

    #TEST PLOT MANUAL
    arr_1_temp = [[0, 115.02000000000044], [1, 107.34999999999854], [2, 99.68999999999869], [3, 92.02000000000044], [4, 84.34999999999854], [5, 76.68000000000029], [6, 69.0099999999984], [7, 61.349999999998545], [8, 53.68000000000029], [9, 46.0099999999984], [10, 38.340000000000146], [11, 30.669999999998254], [12, 23.0], [13, 15.340000000000146], [14, 7.669999999998254], [15, 0.0], [16, 8.529999999998836], [17, 17.06999999999971], [18, 25.599999999998545], [19, 34.13000000000102]]
    arr_2_temp =  [[0, 16.884], [1, 27.805000000000003], [2, 38.659000000000006], [3, 49.513000000000005], [4, 60.367], [5, 71.221], [6, 82.075], [7, 92.929], [8, 103.78300000000002], [9, 114.637], [10, 95.542], [11, 76.447], [12, 57.352], [13, 38.257000000000005], [14, 19.095000000000002], [15, 0.0], [16, 8.375], [17, 16.75], [18, 25.058], [19, 33.433]]

    # plotArraySingur(arr_1_temp, 'arr_1')
    # plotArraySingur(arr_2_temp, 'arr_2')


    #TESTARE CROSS CORELATION & ABATERE MANUAL
    arr_1 = [[0, 38.460000000002765], [1, 45.470000000001164], [2, 52.4900000000016], [3, 59.5], [4, 66.52000000000044], [5, 73.53000000000247], [6, 80.55000000000291], [7, 87.57000000000335], [8, 94.58000000000175], [9, 101.60000000000218], [10, 108.61000000000058], [11, 115.63000000000102], [12, 122.64000000000306], [13, 129.65999999999985], [14, 136.6700000000019], [15, 143.69000000000233], [16, 133.4300000000003], [17, 123.15999999999985], [18, 112.90000000000146], [19, 102.64000000000306], [20, 92.37000000000262], [21, 82.11000000000058], [22, 71.85000000000218], [23, 61.580000000001746], [24, 51.32000000000335], [25, 41.06000000000131], [26, 30.790000000000873], [27, 20.530000000002474], [28, 10.270000000000437], [29, 0.0]]

    arr_2 = [[0, 38.016000000000005], [1, 45.08], [2, 52.15], [3, 59.21], [4, 66.28], [5, 73.42], [6, 80.52], [7, 87.58], [8, 94.65], [9, 101.71], [10, 108.78], [11, 115.87], [12, 123.02], [13, 130.08], [14, 137.15], [15, 143.86], [16, 133.47], [17, 123.17], [18, 112.78], [19, 102.47], [20, 92.1], [21, 81.7], [22, 71.37], [23, 61.02], [24, 50.62], [25, 40.26], [26, 29.94], [27, 19.54], [28, 9.16], [29, 0.0]]
    plotArraySingur(arr_1,'arr_1')
    plotArraySingur(arr_2,'arr_2')

    # print('Test cross corelation manual:',crossCorelation(arr_1,arr_2))

    plt.show()


