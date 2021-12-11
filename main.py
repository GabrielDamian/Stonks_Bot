import matplotlib.pyplot as plt
import csv
from utils import *
from graphHandler import *

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


    graph.candlesToFunction(candleSize)
    graph.generateInternPoints()
    graph.plotCandlesToFunction('Points')

    plt.show()


