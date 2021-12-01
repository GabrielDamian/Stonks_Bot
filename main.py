import matplotlib.pyplot as plt
import csv
from utils import *
from graphHandler import *

if __name__ == '__main__':

    vector = readDataFromFile('AAPL.csv',linesToRead=50)

    graph = graphData()

    graph.setInputData(vector)
    # graph.printInputData()
    graph.plotInputData('Input Data')

    graph.inputToCandle(candleSize=3)
    # graph.plotCandles('Candles data')

    graph.filterCandles(1,0.3)
    # graph.filterCandles(1,0.3)
    graph.plotCandles('Filtered candles')

    # print('Filtered candles',graph.candlesData);

    # graph.groupCandles()
    # graph.plotCompressedCandles('Grouped candles')


    graph.filteredCandlesToFunction(3)
    graph.plotPoints('Points')

    graph.reduceInputData();

    plt.show()


