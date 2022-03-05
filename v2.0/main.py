from functii import *
from utils import *
from graphHandler import *

if __name__ == '__main__':

    # STAGE_1
    print('-->Start Stage 1:')
    candleSize = 3
    filter_candles_1 = 0.5
    filter_candles_2 = 0.3

    vector = readDataFromFile('../AAPL.csv', linesToRead=500000)

    print("Prelucrez prin candles...")
    graph = graphData()

    graph.setInputData(vector)
    # graph.printInputData()
    # graph.plotInputData('data')

    graph.inputToCandle(candleSize=candleSize)
    # graph.plotCandles('Candle Data')

    graph.filterCandles(filter_candles_1,
                        filter_candles_2)     # param_1, param_2 spun cat de atenta la detalii sa fie filtrarea (param mare => exclude delatiile fine)
    # graph.plotCandles('Candle Filtered Data')

    graph.candlesToFunctionWork(candleSize)
    # graph.plotCandlesToFunction('Without intern points')
    print("Adaug puncte intermediare...")
    graph.generateInternPoints()
    # graph.plotCandlesToFunction('data')
    # graph.printCandlesToFunction()

    print("DATA FINALA STAGE 1:")
    #TEMP code write to file:
    string_file = ''

    last_x = None
    for a in graph.candlesToFunction:
        if a[0] == last_x:
            print("balls")
            continue
        string_file +=f'{a[0]} {a[1]}\n'
        last_x = a[0]

    print("FINAL sttring:")
    f = open("Cdata.txt","w")
    f.write(string_file)
    f.close()


    print(string_file)
    # print("Stage 1 complet.")  # data finala in graph.candlesToFunction
    # print("-->Start Stage 2:")
    #
    # # COLLECT DATA FOR STAGE 2 & 3
    # size_seg_unic = 40
    # min_streching = 5  # relative to len(size_seg_unic)
    # max_streching = 5
    #
    # # STAGE_2 - toate combinatiile posibile pentru segmentul de baza
    #
    # print('Start generare segmente de baza...')
    # segmente_baza = segmentareArray(graph.candlesToFunction, size_seg_unic)
    #
    # print(f'Succes. S-au generat: {len(segmente_baza)} segmente baza de marime: {size_seg_unic}')
    # print("Start normalizare segmente de baza...")
    #
    # segmente_baza_normalizate = []
    # for a in segmente_baza:
    #     segmente_baza_normalizate.append(normzalieaza_segment(a))
    #
    # print('Succes. Size segmente normalizate:', len(segmente_baza_normalizate))
    #
    # # STAGE_3 - generare si prelucrare variatii
    # print('-->Start Stage 3:')
    # print(f'Date: min={min_streching}, max={max_streching}')
    #
    # variatii = determinaSizeVariatii(min_streching, max_streching, size_seg_unic)
    #
    # print('Test index variatii:', variatii)
    #
    # print('Populez variatii')
    # future_price_offset = 10
    # for a in variatii:
    #     variatii[a] = segmentareArrayFuturePrice(graph.candlesToFunction, int(a), future_price_offset)
    #
    # print('Succes populare segmente')
    #
    # # for a in variatii:
    # #     print(a)
    # #     for b in variatii[a]:
    # #         print(b)
    #
    # print('Start normalizare(orizontala) variatii...')
    # for a in variatii:
    #     variatii[a] = normalizareVariatii(variatii[a])
    # print('Succes normalizare variatii.')
    # # print('Variatii NE-interpolate------')
    # # for a in variatii:
    # #     print(a)
    # #     for b in variatii[a]:
    # #         print(b)
    #
    # print("Start interpolare variatii...")
    #
    # for index, a in enumerate(variatii):
    #     print(f'variatie noua[{index}]')
    #     variatii[a] = handlerComprimaInterpoleaza(variatii[a], size_seg_unic)
    #
    # # plt.show()
    #
    # # STAGE 4 - cross corelation for each
    # segmente_finale = []
    # abatere = 6000  # suma cross corelation
    # index_reset_scriere = 0
    # for index, a in enumerate(segmente_baza_normalizate):
    #
    #     index_reset_scriere += 1
    #     if index_reset_scriere == 50:
    #         print('scriu in fisier:')
    #         overwriteFile(segmente_finale, 'results.txt')
    #         index_reset_scriere = 0
    #
    #     print('seg baza nou:', index)
    #     obj_temp = {
    #         'segment_baza': a,
    #         'variatii': {}
    #     }
    #     for b in variatii:
    #         obj_temp['variatii'][b] = []
    #         for c in variatii[b]:
    #             if crossCorelation(c['values'], a) < abatere:
    #                 obj_temp['variatii'][b].append({
    #                     'values': c['values'],
    #                     'future_price': c['future_price']
    #                 })
    #
    #     segmente_finale.append(obj_temp)
    #
    # for index_1, a in enumerate(segmente_finale):
    #     # print('Segment final index',index)
    #     # print('Seg baza:',a['segment_baza'])
    #     total_asemanari = 0
    #     for b in a['variatii']:
    #         # print(b,len(a['variatii'][b]))
    #         total_asemanari += len(a['variatii'][b])
    #
    #         print('Total:', total_asemanari)

