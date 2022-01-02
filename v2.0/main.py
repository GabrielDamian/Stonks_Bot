from functii import *
from utils import *
from graphHandler import *


if __name__ == '__main__':

    #STAGE_1
    # RAW INPUT DATA -> CANDLE FORMAT + FILTER + BACK TO FUNCTION -> graph.candlesToFunction (500k points)
    print('-->Start Stage 1:')
    candleSize = 3
    filter_candles_1 = 0.5
    filter_candles_2 = 0.3

    # vector = readDataFromFile('AAPL.csv',linesToRead=500000)
    vector = readDataFromFile('../AAPL.csv', linesToRead=50000)

    print("Prelucrez prin candles...")
    graph = graphData()

    graph.setInputData(vector)
    # graph.printInputData()
    # graph.plotInputData('data')

    graph.inputToCandle(candleSize=candleSize)
    # graph.plotCandles('Candle Data')

    graph.filterCandles(filter_candles_1,filter_candles_2)  # param_1, param_2 spun cat de atenta la detalii sa fie filtrarea (param mare => exclude delatiile fine)
    # graph.plotCandles('Candle Filtered Data')

    graph.candlesToFunctionWork(candleSize)
    # graph.plotCandlesToFunction('Without intern points')
    print("Adaug puncte intermediare...")
    graph.generateInternPoints()
    # graph.plotCandlesToFunction('data')
    # graph.printCandlesToFunction()


    print("Stage 1 complet.") #data finala in graph.candlesToFunction
    print("-->Start Stage 2:")

    #COLLECT DATA FOR STAGE 2 & 3
    size_seg_unic = 40
    min_streching = 5 #relative to len(size_seg_unic)
    max_streching = 5

    #STAGE_2 - toate combinatiile posibile pentru segmentul de baza
    segmente_baza_normalizate = []


    print('Start generare segmente de baza...')
    segmente_baza = segmentareArray(graph.candlesToFunction, size_seg_unic)


    print(f'Succes. S-au generat: {len(segmente_baza)} segmente baza de marime: {size_seg_unic}')
    print("Start normalizare segmente de baza...")
    for a in segmente_baza:
        segmente_baza_normalizate.append(normzalieaza_segment(a))

    print('Succes. Size segmente normalizate:', len(segmente_baza_normalizate))


    #STAGE_3 - generare si prelucrare variatii
    print('-->Start Stage 3:')
    print(f'Date: min={min_streching}, max={max_streching}')


    variatii = determinaSizeVariatii(min_streching, max_streching, size_seg_unic)

    print('Test index variatii:', variatii)

    print('Populez variatii')
    future_price_offset = 10
    for a in variatii:
        variatii[a] = segmentareArrayFuturePrice(graph.candlesToFunction, int(a), future_price_offset)

    print('Succes populare segmente')


    # for a in variatii:
    #     print(a)
    #     for b in variatii[a]:
    #         print(b)

    print('Start normalizare(orizontala) variatii...')
    for a in variatii:
        variatii[a] = normalizareVariatii(variatii[a])
    print('Succes normalizare variatii.')

    # for a in variatii:
    #     print(a)
    #     for b in variatii[a]:
    #         print(b)
    #comprimare variatii pe orizontala in raport cu size_seg_baza

    #interpolare
    print("Start interpolare variatii...")
    # print('Variatii NE-interpolate------')
    # for a in variatii:
    #     print(a)
    #     for b in variatii[a]:
    #         print(b)
    #

    for index, a in enumerate(variatii):
        print('variatie nou:', index)
        variatii[a] = handlerComprimaInterpoleaza(variatii[a],size_seg_unic)


    # print('Variatii interpolate------')
    # for a in variatii:
    #     print(a)
    #     for b in variatii[a]:
    #         print(b)

    # arr_1 = [[0, 167.18], [1, 178.67], [2, 190.15], [3, 201.64], [4, 183.31], [5, 164.98], [6, 146.65], [7, 128.32], [8, 109.98], [9, 91.65], [10, 73.32], [11, 54.99], [12, 36.66], [13, 18.33], [14, 0.0]]
    # arr_2 = [[0, 167.18], [1, 175.63], [2, 184.07], [3, 192.52], [4, 200.96], [5, 189.24], [6, 175.76], [7, 162.28], [8, 148.81], [9, 135.33], [10, 121.85], [11, 108.36], [12, 94.88], [13, 81.41], [14, 67.93], [15, 54.45], [16, 40.97], [17, 27.49], [18, 14.02], [19, 0.54]]
    # plotArraySingur(arr_1,'arr-1')
    # plotArraySingur(arr_2,'arr-2')

    # print('Variatii finale interpolate')
    # for a in variatii:
    #     print(a)
    #     for b in variatii[a]:
    #         print(b)



    # plt.show()


    #STAGE 4 - cross corelation for each
    segmente_finale = []
    abatere = 4000 #suma cross corelation
    for index, a in enumerate(segmente_baza_normalizate):
        print('seg baza nou:', index)
        obj_temp = {
            'segment_baza':a,
            'variatii':{}
        }
        for b in variatii:
            obj_temp['variatii'][b] = []
            for c in variatii[b]:
                if crossCorelation(c['values'], a) < abatere:
                    obj_temp['variatii'][b].append({
                        'values': c['values'],
                        'future_price': c['future_price']
                    })

        segmente_finale.append(obj_temp)


        # print('Segmente finale:----')
    for index_1, a in enumerate(segmente_finale):
        # print('Segment final index',index)
        # print('Seg baza:',a['segment_baza'])
        total_asemanari = 0
        for b in a['variatii']:
            # print(b,len(a['variatii'][b]))
            total_asemanari +=len(a['variatii'][b])

            print('Total:', total_asemanari)
#crossCorelation



