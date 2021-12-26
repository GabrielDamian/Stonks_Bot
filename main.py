import matplotlib.pyplot as plt
import csv
from utils import *
from graphHandler import *
from generatorCombinatiiSegmente import *
from patternFinder import *

if __name__ == '__main__':

    #INPUT - FILTRARE ----------------------------
    candleSize = 3
    # vector = readDataFromFile('AAPL.csv',linesToRead=500000)
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
    # graph.printCandlesToFunction()


    #GENERATOR COMBINATII SEGMENTE----------------------------
    patternFinder = patternFinder(graph.candlesToFunction,40)
    # patternFinder.printInputData()
    # patternFinder.plotInputData('Input to Pattern Finder:')

    # patternFinder.segmenteazaInputData()
    hardcodedInputData = [[0, 225.568], [1, 210.95], [2, 196.24], [3, 181.52], [4, 166.9], [5, 152.2], [6, 137.57], [7, 140.25], [8, 146.82], [9, 153.33], [10, 159.89], [11, 166.4], [12, 172.95], [13, 179.54], [14, 186.06], [15, 192.61], [16, 199.14], [17, 205.67], [18, 212.21], [19, 218.74], [20, 225.28], [21, 231.81], [22, 230.97], [23, 217.49], [24, 204.0], [25, 190.52], [26, 177.04], [27, 163.56], [28, 150.1], [29, 136.7], [30, 123.22], [31, 109.74], [32, 96.26], [33, 82.78], [34, 69.3], [35, 55.81], [36, 42.33], [37, 28.85], [38, 15.37], [39, 1.89]]

    patternFinder.setSegmentareInputData(hardcodedInputData)

    # patternFinder.printSegUnice()

    patternFinder.genereazaCombinatiiSegmente()
    # patternFinder.printCombinatiiPerSegUnic()

    #FINAL - FITRARE SEGMENTE REDUNDANTE (sum > abatere)

    patternFinder.filterWithCrossCorelation(abatere=5000)
    patternFinder.printFilteredData()

    #TEST PLOT MANUAL
    arr_1_temp = [[0, 115.02000000000044], [1, 107.34999999999854], [2, 99.68999999999869], [3, 92.02000000000044], [4, 84.34999999999854], [5, 76.68000000000029], [6, 69.0099999999984], [7, 61.349999999998545], [8, 53.68000000000029], [9, 46.0099999999984], [10, 38.340000000000146], [11, 30.669999999998254], [12, 23.0], [13, 15.340000000000146], [14, 7.669999999998254], [15, 0.0], [16, 8.529999999998836], [17, 17.06999999999971], [18, 25.599999999998545], [19, 34.13000000000102]]
    arr_2_temp =  [[0, 16.884], [1, 27.805000000000003], [2, 38.659000000000006], [3, 49.513000000000005], [4, 60.367], [5, 71.221], [6, 82.075], [7, 92.929], [8, 103.78300000000002], [9, 114.637], [10, 95.542], [11, 76.447], [12, 57.352], [13, 38.257000000000005], [14, 19.095000000000002], [15, 0.0], [16, 8.375], [17, 16.75], [18, 25.058], [19, 33.433]]

    # plotArraySingur(arr_1_temp, 'arr_1')
    # plotArraySingur(arr_2_temp, 'arr_2')


    #TESTARE CROSS CORELATION & ABATERE MANUAL
    arr_1 = [[0, 223.67800000000003], [1, 209.06], [2, 194.35000000000002], [3, 179.63000000000002], [4, 165.01000000000002], [5, 150.31], [6, 135.68], [7, 138.36], [8, 144.93], [9, 151.44000000000003], [10, 158.0], [11, 164.51000000000002], [12, 171.06], [13, 177.65], [14, 184.17000000000002], [15, 190.72000000000003], [16, 197.25], [17, 203.78], [18, 210.32000000000002], [19, 216.85000000000002], [20, 223.39000000000001], [21, 229.92000000000002], [22, 229.08], [23, 215.60000000000002], [24, 202.11], [25, 188.63000000000002], [26, 175.15], [27, 161.67000000000002], [28, 148.21], [29, 134.81], [30, 121.33], [31, 107.85], [32, 94.37], [33, 80.89], [34, 67.41], [35, 53.92], [36, 40.44], [37, 26.96], [38, 13.479999999999999], [39, 0.0]]

    arr_2 = [[0, 223.44500000000002], [1, 213.24], [2, 202.78], [3, 192.5], [4, 182.12], [5, 171.75], [6, 161.21], [7, 150.96], [8, 140.47], [9, 132.07], [10, 139.52], [11, 146.79], [12, 154.16], [13, 161.52], [14, 169.04], [15, 176.29], [16, 183.76], [17, 191.26], [18, 198.49], [19, 206.01], [20, 213.38], [21, 220.73], [22, 228.02], [23, 219.65], [24, 206.1], [25, 192.55], [26, 179.0], [27, 165.44], [28, 151.89], [29, 138.34], [30, 124.56], [31, 110.91], [32, 97.36], [33, 83.81], [34, 70.26], [35, 56.71], [36, 43.15], [37, 29.41], [38, 15.72], [39, 2.17]]
    plotArraySingur(arr_1,'baza')
    plotArraySingur(arr_2,'arr_2')

    # print('Test cross corelation manual:',crossCorelation(arr_1,arr_2))

    plt.show()


