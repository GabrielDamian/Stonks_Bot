import matplotlib.pyplot as plt
import csv
from utils import *
from graphHandler import *
from generatorCombinatiiSegmente import *
from patternFinder import *

if __name__ == '__main__':

    #INPUT - FILTRARE ----------------------------
    candleSize = 3
    vector = readDataFromFile('AAPL.csv',linesToRead=10000)

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
    patternFinder = patternFinder(graph.candlesToFunction,40)
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
    arr_1 = [[0, 225.87999999999738], [1, 211.61999999999898], [2, 197.36999999999898], [3, 183.10999999999694], [4, 168.84999999999854], [5, 154.59000000000015], [6, 140.3299999999981], [7, 146.6899999999987], [8, 153.03999999999724], [9, 159.39999999999782], [10, 165.75], [11, 172.10999999999694], [12, 178.45999999999913], [13, 184.8199999999997], [14, 191.16999999999825], [15, 197.52999999999884], [16, 203.87999999999738], [17, 210.23999999999796], [18, 216.59000000000015], [19, 222.9499999999971], [20, 229.29999999999927], [21, 235.65999999999985], [22, 222.5699999999997], [23, 209.47999999999956], [24, 196.37999999999738], [25, 183.28999999999724], [26, 170.1999999999971], [27, 157.10999999999694], [28, 144.0099999999984], [29, 130.91999999999825], [30, 117.82999999999811], [31, 104.73999999999796], [32, 91.64999999999782], [33, 78.54999999999927], [34, 65.45999999999913], [35, 52.36999999999898], [36, 39.279999999998836], [37, 26.179999999996653], [38, 13.090000000000146], [39, 0.0]]

    arr_2 = [[0, 225.568], [1, 210.95], [2, 196.24], [3, 181.52], [4, 166.9], [5, 152.2], [6, 137.57], [7, 140.25], [8, 146.82], [9, 153.33], [10, 159.89], [11, 166.4], [12, 172.95], [13, 179.54], [14, 186.06], [15, 192.61], [16, 199.14], [17, 205.67], [18, 212.21], [19, 218.74], [20, 225.28], [21, 231.81], [22, 230.97], [23, 217.49], [24, 204.0], [25, 190.52], [26, 177.04], [27, 163.56], [28, 150.1], [29, 136.7], [30, 123.22], [31, 109.74], [32, 96.26], [33, 82.78], [34, 69.3], [35, 55.81], [36, 42.33], [37, 28.85], [38, 15.37], [39, 1.89]]

    plotArraySingur(arr_1,'arr_1')
    plotArraySingur(arr_2,'arr_2')

    # print('Test cross corelation manual:',crossCorelation(arr_1,arr_2))

    plt.show()


