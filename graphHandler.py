import matplotlib.pyplot as plt
import csv
'''
Comments section:
asdasd
'''

class graphData:
    inputData = None #y values, x is incremented by 1 min value in time
    candlesData = True #arr of arr [[x,height,bottom,direction],[],[]....]

    def __init__(self):
        pass
    def setInputData(self,data):
        self.inputData = data
    def printInputData(self):
        #print vector
        print(self.inputData)
    def plotInputData(self,code):
        plt.figure(code)
        # ceva = len(self.inputData)
        # arr = []
        # for x in range(0,ceva):
        #     arr.append(x)
        plt.plot(self.inputData)

    def inputToCandle(self,candleSize):
        if self.inputData == None:
            print('input data not generated yet (cannot use inputToCandle before that)')
        else:
            candles = []
            xIndex = 0
            triggerNewCandle = 0
            startPrice = self.inputData[0]
            stopPrice = None
            direction = None  # up or down

            for x in self.inputData:
                if triggerNewCandle == candleSize:
                    stopPrice = x
                    yValue = None
                    if startPrice < stopPrice:
                        direction='green'
                        yValue = startPrice
                    else:
                        direction = 'red'
                        yValue = stopPrice



                    newCandle = [xIndex, round(abs(startPrice-stopPrice),2),yValue,direction]
                    candles.append(newCandle)
                    #reseteaza contoare pt next candle
                    #????????????? not sure what to use for startPrice
                    # startPrice = self.inputData[xIndex + 1]

                    startPrice = stopPrice
                    stopPrice = None
                    triggerNewCandle = 0



                triggerNewCandle +=1
                xIndex +=1

                #conditie care previne eroare la startPrice = self.inputData[xIndex + 1]// index arr out of bounds
                if xIndex > len(self.inputData) - candleSize:
                    break

            self.candlesData = candles
            return candles

    def plotCandles(self,code):
        plt.figure(code)
        if self.candlesData == None:
            print("candlesData not generated yet")
        else:
            width =2
            for x in self.candlesData:
                plt.bar(x[0],x[1],width,x[2],color=x[3],align='center')
            # plt.bar(x=50,height=20, width=10, bottom=10,align='center')
            # plt.bar(x=30,height=100, width=5, bottom=40,align='center')


    def filterCandles(self,factor):


        temp_contor = 0
        if self.candlesData == None:
            print('input data not generated yet (cannot use filterCandles before that)')
        else:

            for index,x in enumerate(self.candlesData):
                print("X:",x)
                if index ==0 or index == len(self.candlesData)-1:
                    print("PASS")
                    continue

                leftCandle = self.candlesData[index-1]
                rightCandle = self.candlesData[index+1]

                #neightbours colors to be different
                if leftCandle[3] != x[3] and rightCandle[3] != x[3]:

                    #x[1] represents the height of the candle
                    leftValue = leftCandle[1]
                    rightValue = rightCandle[1]

                    print("left value:",leftValue)
                    compareTo = float(leftValue) + float(rightValue)
                    if x[1] < compareTo*factor:
                        newDirection = ''
                        if x[3] == 'green':
                            newDirection = 'red'
                        else:
                            newDirection = 'green'
                        temp_contor +=1
                        self.candlesData[index][3] =newDirection


            print("am modificat:",temp_contor,"culori")