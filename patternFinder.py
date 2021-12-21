import matplotlib.pyplot as plt
from generatorCombinatiiSegmente import *
'''
Defineste segment_principal size;
Primeste combinatiile de la generatorCombinatiiSegmente.(obiectul cu totul)

La obiectul primit, adauga un camp de difenta pentru fiecare combinatie + values pentru segment curent:

Parcuge input data si creeaza un vector de obiecte:

{
    marime_segment_principal: 4
    values_segment_principal = [a,a,a,a]
    min_stretching = 2
    max_stretching = 7

    combinatii:{
        '2':[{
                values:[a,a,a,a],
                future_price:x,
                diferenta: 2334 //cross correlation or matrix correlation
            },{}...],
        .
        .
        '7':[{},{}...]
    }

}

[obj_seg_1, obj_seg_2 ... ]
Acum stim pentru fiecare segment de marime stabilita de noi, cat de mult seama cu
toate variatiile intre min si max de alte segmente.

Final:
Metoda de sortat segmentele:
-primeste ca param o marja de eroare = diferanta de la cross correlation
-????????? pain, help
------------
[
{
unic:[[],[],[]...]
combinatii: {
		segment: [[],[],[]..],
		size_segment_principal: 10,
		min_streching: 5,
		max_streching: 10,
		variatii:{
			'5':[{
				'values':[[],[],[]],
				'future_price': 100
				},
				{
				'values':[[],[],[]],
				'future_price': 100
				}
			   ],
			'6':......
			
			}
		}
    }
]

'''

class patternFinder():
    def __init__(self, inputData, size_seg):
        #inputData = graficul pe 1 an (ex)
        self.size_seg = size_seg #size seg de baza (segmente mai exact)
        self.input_data = inputData

        self.seg_unice = []
        #pentru fiecare segment unic, genereaza toate combinatiile posibile (interpolare + scalate folosing generatorCombinatii)
        self.combinatiiPerSegUnic = []

    def segmenteazaInputData(self):
        seg_unic_temp = []
        counter_trigger = 0
        current_index = 0
        while current_index < len(self.input_data) - self.size_seg-1:
            seg_unic_temp.append(self.input_data[current_index])
            current_index +=1
            counter_trigger +=1
            if counter_trigger == self.size_seg:
                self.seg_unice.append(seg_unic_temp)
                seg_unic_temp = []
                counter_trigger =0

    def genereazaCombinatiiSegmente(self):

        for a in self.seg_unice:
            generatorCombinatii = generatorSegment(self.input_data)
            generatorCombinatii.setParams(len(a), len(a)-5, len(a)+5, a)
            generatorCombinatii.normalizeazaSegmentBaza()

            generatorCombinatii.determinaSizeVariatii()
            generatorCombinatii.genereazaVariatii()
            generatorCombinatii.normalizeazaVariatii()
            generatorCombinatii.comprima_interpoleaza_variatii()


            self.combinatiiPerSegUnic.append({
                'unic':a,
                'combinatii': generatorCombinatii.returnData()
            })

    def printInputData(self):
            print("Input data:")
            print('Size seg:', self.size_seg)
            print('Input data (nesegmentat inca):')
            for a in self.input_data:
                print(a)
            print('\n')

    def printSegUnice(self):
        print('Seg unice (input data segmentat in functie de size_seg):')
        for a in self.seg_unice:
            print(a)
        print('\n')
    def printCombinatiiPerSegUnic(self):
        print('Combinatii per seg unic (pr fiecare seg unic, genereaza toate combinatiile folosind generatorCombinatii:')
        for a in self.combinatiiPerSegUnic:
            seg_unic = a['unic']
            combinatii = a['combinatii']
            print('seg unic:', seg_unic)

            segment_normalizat = combinatii['segment']
            print('seg unic normalizat:', segment_normalizat)

            size_seg_unic_normalizat = combinatii['size_segment_principal']
            print('size seg unic normalizat:', size_seg_unic_normalizat)

            min_streching_seg_unic_normalizat = combinatii['min_stretching']
            max_streching_seg_unic_normalizat = combinatii['max_stretching']
            print('min streching:', min_streching_seg_unic_normalizat)
            print('max streching:', max_streching_seg_unic_normalizat)
            #aici mai exista un obiect atasat cu 'variatii' care reprezinta trash dinaintea normalizarii
            variatii = combinatii['variatii_interpolate']
            print('\nvariatii:')
            for a in variatii:
                print('--variatie:',a)
                # print(variatii[a])
                for b in variatii[a]:
                    print(b)
            print('---------------')

    def filterWithCrossCorelation(self,abatere):
        for a in self.combinatiiPerSegUnic:
            segment_unic_normalizat_curent = a['combinatii']['segment']
            print('seg unic curent:', segment_unic_normalizat_curent)

            variatii = a['combinatii']['variatii_interpolate']
            for index, b in enumerate(a['combinatii']['variatii_interpolate']):
                values_curente = a['combinatii']['variatii_interpolate'][b]
                #print(values_curente)



