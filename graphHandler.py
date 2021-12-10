import matplotlib.pyplot as plt
import csv
'''
Comments section:
asdasd
'''

class graphData:
    inputData = None #y values, x is incremented by 1 min value in time

    candlesData = None #arr of arr [[x,height,bottom,direction],[],[]....]

    compressCandles = None  #nu tine cont de offset x pe axa, doar de combinatiile dintre trenduri si marimea lor

    candlesToFunction = None
    # temp_points = None #

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
                    if startPrice <= stopPrice:
                        direction='green'
                        yValue = startPrice
                    else:
                        direction = 'red'
                        yValue = stopPrice

                    height = round(abs(startPrice-stopPrice),2)

                    #nu vr sa am candles cu height 0
                    if height  <= 1:
                        height = 1

                    newCandle = [xIndex, height ,yValue,direction]

                    candles.append(newCandle)
                    #reseteaza contoare pt next candle
                    startPrice = stopPrice
                    stopPrice = None
                    triggerNewCandle = 0
                triggerNewCandle +=1
                xIndex +=1

                #conditie care previne eroare la startPrice = self.inputData[xIndex + 1]// index arr out of bounds
                if xIndex > len(self.inputData) - candleSize:
                    break
            self.candlesData = candles

    def plotCandles(self,code):
        plt.figure(code)
        if self.candlesData == None:
            print("candlesData not generated yet")
        else:
            width =2
            for x in self.candlesData:
                plt.bar(x[0],x[1],width,x[2],color=x[3],align='center')

    def filterCandles(self,factor,factor_2):
        #rezultat tot in candlesData)

        #factor_1 = vecini stanga_dreapat
        #factor_2 = 2 vecini la stanga si dreapta (factor 2 << factor 1)


        candles_to_remove = []

        if self.candlesData == None:
            print('input data not generated yet (cannot use filterCandles before that)')
        else:

            for index,x in enumerate(self.candlesData):
                changeColor = False
                if index ==0 or index == 1 or index == len(self.candlesData)-1 or index == len(self.candlesData)-2:
                    continue

                leftCandle = self.candlesData[index-1]
                rightCandle = self.candlesData[index+1]

                #daca vecinii directi au culori diferite
                if leftCandle[3] != x[3] and rightCandle[3] != x[3]:

                    #x[1] represents the size of the candle
                    leftValue = leftCandle[1]
                    rightValue = rightCandle[1]

                    #factor raportat la vecini (1 vecin stanga dreapta)
                    suma_vecini= leftValue + rightValue
                    #factor = 0.5 => x[1] < jumatate din suma vecinilor
                    #factor = 1 => x[1] < suma vecinilor

                    if x[1] < suma_vecini*factor:
                        changeColor = True
                    else:
                        #daca vecinii imediati indica sa pastram aceeasi culoare, verifica 2 vecini la stanga si la dreapta

                        vecin_stanga_2 = self.candlesData[index-2]
                        vecin_stanga_1 = self.candlesData[index-1]
                        vecin_dreapta_1 = self.candlesData[index+1]
                        vecin_dreapta_2 = self.candlesData[index+2]

                        suma_vecini_aceeasi_culoare = 0
                        if x[3] != vecin_stanga_2[3]:
                            suma_vecini_aceeasi_culoare += vecin_stanga_2[1]
                        if x[3] != vecin_stanga_1[3]:
                            suma_vecini_aceeasi_culoare += vecin_stanga_1[1]
                        if x[3] != vecin_dreapta_1[3]:
                            suma_vecini_aceeasi_culoare += vecin_dreapta_1[1]
                        if x[3] != vecin_dreapta_2[3]:
                            suma_vecini_aceeasi_culoare += vecin_dreapta_2[1]

                        if x[1] < suma_vecini_aceeasi_culoare *factor_2:
                            changeColor = True

                    #suplimentar, factor vecin prea mare
                    factor_vecin_prea_mare = 4
                    # if x[1] * factor_vecin_prea_mare <= self.candlesData[index - 1][1] or x[1] * factor_vecin_prea_mare <= self.candlesData[index + 1][1]:
                    #     changeColor = False
                    #
                    filtru_candles_extrem_de_mici = 10
                    if x[1] < filtru_candles_extrem_de_mici:
                        pass
                    else:
                        if x[1] * factor_vecin_prea_mare <= self.candlesData[index - 1][1] or x[1] * factor_vecin_prea_mare <= self.candlesData[index + 1][1]:
                            changeColor = False

                    if changeColor == True:
                        candles_to_remove.append(index)
                        if x[3] == 'red':
                            self.candlesData[index][3] = 'green'
                        else :
                            self.candlesData[index][3] = 'red'

    def groupCandles(self):
        #rezultat in compressed candles

        size = len(self.candlesData)
        index = 0
        compressed_candles = []

        while index < size - 1:
            if self.candlesData[index][3] != self.candlesData[index+1][3]:
                compressed_candles.append(self.candlesData[index])
                index +=1
            else:
                temp_index = index +1
                while self.candlesData[temp_index][3] == self.candlesData[temp_index+1][3]  and temp_index < size - 2:
                    temp_index +=1
                # [x, height, bottom, direction]
                if self.candlesData[index][3] == 'red':
                    left_top_point = self.candlesData[index][2] + self.candlesData[index][1]
                    right_bottom_point = self.candlesData[temp_index][2]
                    newCandle = [0,left_top_point - right_bottom_point,self.candlesData[temp_index][2],'red']
                    compressed_candles.append(newCandle)
                else:
                    left_bottom_point = self.candlesData[index][2]
                    right_top_point = self.candlesData[temp_index][2] + self.candlesData[temp_index][1]
                    newCandle = [0,right_top_point - left_bottom_point,self.candlesData[index][2],'green']
                    compressed_candles.append(newCandle)


                index = temp_index +1

        final_candles = []
        for index,a in enumerate(compressed_candles):
            temp = compressed_candles[index]
            temp[0] = index
            final_candles.append(temp)

        self.compressCandles = final_candles

    def plotCompressedCandles(self,code):
        plt.figure(code)
        if self.compressCandles== None:
            print("groupedCandles not generated yet")
        else:
            width = 0.3
            for x in self.compressCandles:
                plt.bar(x[0],x[1],width,x[2],color=x[3],align='center')

    def candlesToFunction(self,candleSize):
        #foloseste data din candlesData
        #data din candlesData trebuie filtrata inainte  daca vr sa il folosim ca input in candles to function

        #metoda are ca output data din points
        size = len(self.candlesData)
        index = 0
        points = []


        while index < size - 1:
            if self.candlesData[index][3] != self.candlesData[index + 1][3]:
                print('caz 1, fara acumulare')

                if self.candlesData[index][3] == 'red':
                    print('caz 1.1, candle red')
                    # [x, height, bottom, direction]
                    x_B = self.candlesData[index][0]+candleSize
                    y_B = self.candlesData[index][2]

                    x_A = x_B - candleSize
                    y_A = self.candlesData[index][2] + self.candlesData[index][1]
                    points.append([x_A,y_A])
                    points.append([x_B,y_B])
                else:
                    print('cz 1.2, candles green')
                    x_B = self.candlesData[index][0]
                    y_B = self.candlesData[index][2] + self.candlesData[index][1]

                    x_A = x_B - candleSize
                    y_A = self.candlesData[index][2]

                    points.append([x_A, y_A])
                    points.append([x_B, y_B])

                index += 1
            else:
                print('caz 2, acumulez mai multe candles')
                temp_index = index + 1
                while self.candlesData[temp_index][3] == self.candlesData[temp_index + 1][3] and temp_index < size - 2:
                    temp_index += 1
                print(f'index:{index},temp_index:{temp_index}')

                # [x, height, bottom, direction]

                if self.candlesData[index][3] == 'red':
                    print("caz 2, red")
                    x_A = self.candlesData[index][0]
                    y_A = self.candlesData[index][2] + self.candlesData[index][1]

                    x_B = self.candlesData[temp_index][0]
                    y_B = self.candlesData[temp_index][2]

                    points.append([x_A, y_A])
                    points.append([x_B, y_B])

                else:
                    print("caz 2,green")
                    x_A = self.candlesData[index][0]
                    y_A = self.candlesData[index][2]

                    x_B = self.candlesData[temp_index][0]
                    y_B = self.candlesData[temp_index][2] + self.candlesData[temp_index][1]

                    points.append([x_A, y_A])
                    points.append([x_B, y_B])


                index = temp_index + 1


        self.candlesToFunction = points

    def candlesToFunction_2(self,candleSize):
        #input - candles data
        #output - a candles is transformed into a line
        print('candles data:',)
        for x in self.candlesData:
            print(x)

        points = []

        index = 0
        # [0, 1     , 2     , 3        ]
        # [x, height, bottom, direction]
        while index < len(self.candlesData)-1:
            if self.candlesData[index][3] != self.candlesData[index+1][3]:
                #caz 1, candles consecutive diferite

                #avem 2 puncte (max min candle stanga, cel din dreapta este de culoare(trend) diferit si o sa fie indexat in uratoare iteratie)
                #trebuie doar sa adaugam cele 2 puncte in point, fara sa le mai ordonam

                x = self.candlesData[index][0]
                height = self.candlesData[index][1]
                bottom = self.candlesData[index][2]
                direction = self.candlesData[index][3]

                x_a = None
                y_a = None
                x_b = None
                y_b = None
                if direction == 'green':
                    #caz candle crescator (A in stanga jos, B in dreapta sus)
                    x_a = x
                    y_a = bottom

                    x_b = x + candleSize
                    y_b = bottom + height

                else: #direction == 'green'
                    #caz candle descrescator (A in stanga sus, B in dreapta jos)
                    x_a = x
                    y_a =bottom + height

                    x_b = x+candleSize
                    y_b = bottom

                points.append([x_a,y_a])
                points.append([x_b, y_b])

                index +=1

            else:
                #caz 2, candles consecutive la fel
                #retinem primul candle (scoatem 2 puncte din el, max si min)
                #parcurgem pana la ultimul candle (scoatem la fel 2 puncte din el, max si min)
                #daugam cele 2 puncte A ,B la points

                #temp_index[color] != index[color] in mod sigur, deoarece nu se executa in else-ul aferent



                temp_index = index+1
                while self.candlesData[index][3] == self.candlesData[temp_index][3]  and temp_index < len(self.candlesData)-1:
                    temp_index +=1

                #stanga- index
                #drepta- temp_index
                x_a = None
                y_a = None
                x_b = None
                y_b = None

                # [0, 1     , 2     , 3        ]
                # [x, height, bottom, direction]

                if self.candlesData[index][3] == 'green':
                    #A - stanga jos (index), B - dreapta sus (temp_index)
                    x_a = self.candlesData[index][0]
                    y_a = self.candlesData[index][2]

                    x_b = self.candlesData[temp_index][0]
                    y_b = self.candlesData[temp_index][2] + self.candlesData[temp_index][1] #bottom + height

                else: #color = 'red'
                    #A - stanga sus (index), B -  dreapta jos (temp_index)
                    x_a = self.candlesData[index][0]
                    y_a = self.candlesData[index][2]

                    x_b = self.candlesData[temp_index][0]
                    y_b = self.candlesData[temp_index][2] + self.candlesData[temp_index][1] #bottom + height

                points.append([x_a, y_a])
                points.append([x_b, y_b])
                index = temp_index+1

        print('points cand to fct 2:', points)
        self.candlesToFunction = points

    def plotCandlesToFunction(self,code):
        plt.figure(code)
        arr_1 = []
        arr_2 = []
        for a in self.candlesToFunction:
            arr_1.append(a[0]-1.5)
            arr_2.append(a[1])

        plt.plot(arr_1,arr_2,'r')
        plt.plot(self.inputData,'b')


    def reduceInputData(self):
        #mediere a semnalului (media in jurul punctului pe baza vecinilor)

        new_points = []
        for index,a in enumerate(self.inputData):
            if index == 0 or index == len(self.inputData)-1:
                pass
            else:
                new_dot = (self.inputData[index-1] + self.inputData[index] + self.inputData[index+1])/3;
                new_points.append(new_dot)

        new_points_2 = []
        for index, a in enumerate(new_points):
            if index == 0 or index == len(new_points) -1:
                pass
            else:
                new_dot = (new_points[index-1] + new_points[index] + new_points[index+1])/3
                new_points_2.append(new_dot)

        plt.figure('Reduced points')
        plt.plot(new_points,'g')
        plt.plot(new_points_2,'b')
        plt.plot(self.inputData,'r')
