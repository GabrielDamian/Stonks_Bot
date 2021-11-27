import matplotlib.pyplot as plt
import csv
from utils import *
from graphHandler import *

if __name__ == '__main__':

    vector = readDataFromFile('AAPL.csv')

    graph = graphData()

    graph.setInputData(vector)
    # graph.printInputData()

    # graph.plotInputData()
    # graph.plotCandles()
    graph.plotInputData('input data')
    ceva = graph.inputToCandle(candleSize=3)

    print(ceva)
    graph.plotCandles('simple candles')
    #factor mare => gaseste mai multe candeluri ce trebuiesc modificate
    graph.filterCandles(factor=2)
    graph.plotCandles('filtred candles')

    plt.show()


