import matplotlib.pyplot as plt
import csv
from utils import *
from graphHandler import *

if __name__ == '__main__':

    vector = readDataFromFile('AAPL.csv',linesToRead=100)

    graph = graphData()

    graph.setInputData(vector)
    # graph.printInputData()
    graph.plotInputData('Input Data')


    graph.inputToCandle(candleSize=3)
    graph.plotCandles('Candles data')


    plt.show()


