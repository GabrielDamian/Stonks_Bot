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
        self.size_seg = size_seg
        self.input_data = inputData

        self.seg_unice = []
        #final data
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


    def printData(self):
        print('Input data:', self.input_data)
        print('Size seg unic:', self.size_seg)
        for a in self.seg_unice:
            print(a)

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

    def printFinalData(self):
        for a in self.combinatiiPerSegUnic:
            print(f'Seg unic:{a["unic"]}')
            print('Obj comb data:', a['combinatii'])

    def returnFinalData(self):
        return self.combinatiiPerSegUnic

    def filtreazaCrossCorelation(self, marja_eroare):
        pass