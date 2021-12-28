import matplotlib.pyplot as plt
from generatorCombinatiiSegmente import *
import time

#segmenteaza graficul pe un an in segmente de marime size_seg(param_1 din constructor)
#pentru fiecare segment_unic, genereaza toate combinatiile posibile intre min, max, apoi filtreaza-le pe baza abaterii de la stdin
class patternFinder():

    def __init__(self, inputData, size_seg):

        #inputData = graficul pe 1 an (ex)
        self.size_seg = size_seg #size seg de baza (segmente mai exact)
        self.input_data = inputData

        self.seg_unice = [] #sau un singur segment unic cand se "hardcodeaza"
        #pentru fiecare segment unic, genereaza toate combinatiile posibile (interpolare + scalate folosing generatorCombinatii)
        self.combinatiiPerSegUnic = []
        self.combinatiiFiltrate = []

    def printInputData(self):

            print("Input data:")
            print('Size seg:', self.size_seg)
            print('len(input data):', len(self.input_data))

            print('Input data (nesegmentat inca):')
            for a in self.input_data:
                print(a)
            print('\n')

    def plotInputData(self, code):
        temp= []
        for a in self.input_data:
            temp.append(a[1])
        plt.figure(code)
        plt.plot(temp)

    #nu o sa fie folosita, se face setare segment curent in mod manual
    def segmenteazaInputData(self):
        seg_unic_temp = []
        counter_trigger = 0
        current_index = 0
        while current_index < len(self.input_data) - 1: #ultimul segment completat partial nu o sa mai fie adaugat in lista, deoarece conditia din while o sa il intrerupa intre timp
            seg_unic_temp.append(self.input_data[current_index])
            current_index +=1
            counter_trigger +=1
            if counter_trigger == self.size_seg:
                self.seg_unice.append(seg_unic_temp)
                seg_unic_temp = []
                counter_trigger =0

    def setSegmentareInputData(self, hardcodedInputData):
        #test purpose (1 segment for 10 * 500k combinations) (10 din comprimare +-5)
        self.seg_unice = [hardcodedInputData]
        # self.seg_unice.append()

    def printSegUnice(self):
        print('Seg unice (input data segmentat in functie de size_seg):')
        for a in self.seg_unice:
            print(a)
        print('\n')

    def genereazaCombinatiiSegmente(self):

        #pentru fiecare segment unic, genereaza toate variatiile de segmente intre min si max, apoi normalizeaza si interpoleaza variatiile, folosind generatorCombinatii
        for a in self.seg_unice:
            #for o sa se executa o singura data, deoarece este setat mereu un element in seg_unice
            generatorCombinatii = generatorSegment(self.input_data)
            generatorCombinatii.setParams(len(a), len(a)-0, len(a)+0, a)
            generatorCombinatii.normalizeazaSegmentBaza()

            generatorCombinatii.determinaSizeVariatii()
            generatorCombinatii.genereazaVariatii()
            # generatorCombinatii.printVariatii()
            generatorCombinatii.normalizeazaVariatii()
            generatorCombinatii.comprima_interpoleaza_variatii()


            self.combinatiiPerSegUnic.append({
                'unic':a,
                'combinatii': generatorCombinatii.returnData()
            })

    def printCombinatiiPerSegUnic(self):
        print('Print combinatii per seg unic: (before filtering)')
        for a in self.combinatiiPerSegUnic:
            print('-----New seg unic:----------------------')
            seg_unic = a['unic']
            combinatii = a['combinatii']

            print('Seg unic:', seg_unic)

            print('Combinatii: (return from generatorCombinatii)')
            segment_normalizat = combinatii['segment']
            print('     ->seg unic normalizat:', segment_normalizat)

            size_seg_unic_normalizat = combinatii['size_segment_principal']
            print('     ->size seg unic normalizat:', size_seg_unic_normalizat)

            min_streching_seg_unic_normalizat = combinatii['min_stretching']
            max_streching_seg_unic_normalizat = combinatii['max_stretching']

            print('     ->min streching:', min_streching_seg_unic_normalizat)
            print('     ->max streching:', max_streching_seg_unic_normalizat)


            #aici mai exista un obiect atasat cu 'variatii' care reprezinta trash dinaintea normalizarii
            variatii = combinatii['variatii_interpolate']
            print('     ->variatii interpolate:')
            # print('\nvariatii:')
            for a in variatii:
                print('          -->variatie:',a)
                # print(variatii[a])
                for b in variatii[a]:
                    print("               --->",b)
            # print('---------------')

    def filterWithCrossCorelation(self,abatere):
        for a in self.combinatiiPerSegUnic:
            #for o sa se executa o singura data, deoarece este setat cu append o singura daca un element (seg_unice) este de len = 1
            #fiecare obiect corespunde unui segment_unic
            obiect_nou_filtrat = {}


            unic = a['unic'] #ne-normalizat

            combinatie = a['combinatii']

            segment_normalizat = combinatie['segment']  # normalizat  atat x cat si y
            size_segment_principal = combinatie['size_segment_principal']  # acelasi cu len(segment_normalizat)
            min_stretching = combinatie['min_stretching']
            max_stretching = combinatie['max_stretching']
            variatii = combinatie['variatii_interpolate'] #exista si variatii neinterpolate

            #copy into new object
            obiect_nou_filtrat['unic'] = unic
            obiect_nou_filtrat['unic_normalizat'] = segment_normalizat
            obiect_nou_filtrat['min_stretching'] = min_stretching
            obiect_nou_filtrat['max_stretching'] = max_stretching
            obiect_nou_filtrat['variatii'] = {}



            # print('seg_normalizat', segment_normalizat)
            # print('size_seg_principal', size_segment_principal)
            # print('min_stretching', min_stretching)
            # print('max_streching', max_stretching)
            # print('->variatii:')
            for x in variatii:
                obiect_nou_filtrat['variatii'][x] = []

                # print(x, variatii[x])
                vector_variatii_x = variatii[x]
                for y in vector_variatii_x:
                    #fiecare obiect pe rand
                    values = y['values']
                    future_price= y['future_price']
                    old_last_price = y['old_last_price']

                #daca sum < abatere, adauga obiect in obj_nou
                    if crossCorelation(values, segment_normalizat) < abatere:
                        temp_variatie = {
                            'values': values,
                            'future_price': future_price,
                            'old_last_price': old_last_price,
                            'abatere': crossCorelation(values, segment_normalizat)
                        }
                        obiect_nou_filtrat['variatii'][x].append(temp_variatie)


            # for ceva in obiect_nou_filtrat:
            #     print(ceva, obiect_nou_filtrat[ceva])
            #     temp_variatii = obiect_nou_filtrat['variatii']
            #     for altceva in temp_variatii:
            #         print(altceva, temp_variatii[altceva])

            self.combinatiiFiltrate.append(obiect_nou_filtrat)

    def printFilteredData(self):
        for a in self.combinatiiFiltrate:
            print('Unic:', a['unic'])
            print('Unic normalizat:', a['unic_normalizat'])
            print('min:', a['min_stretching'])
            print('max:', a['max_stretching'])

            variatii = a['variatii']
            for b in variatii:
                print(b, variatii[b])

    def returnFilteredData(self):
        #stim sigur ca mereu o sa fie un singur element acolo

        return  self.combinatiiFiltrate[0]
