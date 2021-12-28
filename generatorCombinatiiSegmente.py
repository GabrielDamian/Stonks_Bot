from utils import *

class generatorSegment:

    #vectorul cu puncte pentru un an (ex.)


    def __init__(self,newData):
        self.inputData = None

        self.data = {
            'segment': None,
            'size_segment_principal': None,
            'min_stretching': None,
            'max_stretching': None,
            'variatii': {},
            'variatii_interpolate': {}
        }

        self.inputData = newData
        self.truncateInputData(1)

    def setParams(self,new_size, new_min, new_max,segment):
        self.data['segment'] = segment
        self.data['size_segment_principal'] = new_size
        self.data['min_stretching'] = new_min
        self.data['max_stretching'] = new_max

    def printData(self):
        print('Segment:',self.data['segment'])
        print('Input data:',self.inputData)
        print(f'Size segment principal:{self.data["size_segment_principal"]}')
        print(f'Min streching:{self.data["min_stretching"]}')
        print(f'Max streching:{self.data["max_stretching"]}')
        print(f'Variatii:{self.data["variatii"]})')
        print(f'Variatii_interpolate:{self.data["variatii_interpolate"]})')



    def truncateInputData(self,decimals):
        print('x->truncate input data')
        temp =[[round(a[0],decimals), round(a[1],decimals)] for a in self.inputData]
        self.inputData = temp

    def normalizeazaSegmentBaza(self):
        print('x->normalizeaza segment baza')
        #aduce x si y cu 0 ca punct de start

        if self.data['segment'] == None:
            raise 'Nu pot nromaliza, segment de baza nu a fost initializat (inca este None)!!!!'
        segment = self.data['segment']

        x_coords = []
        y_coords = []
        min_y_coords = segment[0][1] #primul y

        for x in segment:
            x_coords.append(x[0])
            y_coords.append(x[1])

        min_x = min(x_coords)
        min_y = min(y_coords)

        x_coords_normalizate = []
        y_coords_normalizate = []

        for x in x_coords:
            x_coords_normalizate.append(x - min_x)
        for x in y_coords:
            y_coords_normalizate.append(x - min_y)

        final = []
        for index, a in enumerate(x_coords_normalizate):
            final.append([a,y_coords_normalizate[index]])

        self.data['segment'] = final

    def determinaSizeVariatii(self):
        print('determina size variatii')
        #toate valorile dintre min si max si le pune drept key in 'variatii'

        min = self.data['min_stretching']
        max = self.data['max_stretching']

        sizes = []
        index= min
        while index <= max:
            sizes.append(index)
            index +=1
        for x in sizes:
            self.data['variatii'][f'{x}'] = []

    def genereazaVariatii(self):
        print('x->genereaza variatii')
        counter_varitii = 0
        counter_iteratii_input_data = 0

        offset_future_price = 4     #cat de departe sa fie future price

        for variatie in self.data["variatii"]:
            counter_varitii += 1
            size_segment = int(variatie)

            for index, el in enumerate(self.inputData):
                counter_iteratii_input_data +=1

                if index < len(self.inputData) - size_segment:
                    buffer = []
                    index_buffer = index
                    temp_obj = {}
                    while len(buffer) < size_segment:
                        buffer.append(self.inputData[index_buffer])
                        index_buffer += 1

                        temp_obj ={
                            'values': buffer,
                            'future_price': self.inputData[index_buffer + offset_future_price] if index_buffer + offset_future_price < len(self.inputData) else None,
                            'old_last_price': buffer[len(buffer)-1]
                        }

                    self.data['variatii'][variatie].append(temp_obj)

                else:
                    #nu mai pot incadra inca un segment de len size_segmetn in spatiul ramas
                    pass


    def printVariatii(self):
        print('segment baza:',self.data['segment'])
        variatii = self.data['variatii']

        for x in variatii:
            print('Segmente de:', x)
            for y in variatii[x]:
                print(y)

    def normalizeazaVariatii(self):
        print('x->normalizeaza variatii')
        variatii = self.data["variatii"]

        new_variatii = { }
        for x in variatii:
            new_variatii[x] =[]
            for index, y in enumerate(variatii[x]):

                values = y['values']
                future_price = y['future_price']
                old_last_price = y['old_last_price']


                #normalizez vectorul values
                x_coords = []
                y_coords = []

                for a in values:
                    x_coords.append(a[0])
                    y_coords.append(a[1])

                min_x = min(x_coords)
                min_y = min(y_coords)

                x_coords_normalized = []
                y_coords_normalized = []

                for a in x_coords:
                    x_coords_normalized.append(round(a - min_x,1))
                for a in y_coords:
                    y_coords_normalized.append(round(a - min_y,1))

                new_values =[]
                for index, a in enumerate(x_coords_normalized):
                    new_values.append([a,y_coords_normalized[index]])


                # new_future_price = []
                # if future_price != None:
                #     new_future_price.append(round(future_price[0] - min_x,1))
                #     new_future_price.append(round(future_price[1] - min_y,1))
                # else:
                #     new_future_price = future_price


                new_variatii[x].append({
                    'values': new_values,
                    'future_price': future_price,
                    'old_last_price': old_last_price
                })

        self.data['variatii'] = new_variatii

    def comprima_interpoleaza_variatii(self):
        print('x->comprima interpoleaza variatii')
        segment_referinta = self.data['segment']

        variatii_interpolare = {}
        variatii_sizes = []
        for index_size_variatie in self.data['variatii']:
            # print('x-aici:',index_size_variatie)
            variatii_interpolare[index_size_variatie] = []
            variatii_sizes.append(index_size_variatie)


        for index_size_variatie in variatii_sizes:
            vector_variatii_curente = self.data['variatii'][index_size_variatie]
            # print(f'vector variatii curente:{index_size_variatie}:')

            for obj_variatie in vector_variatii_curente:
                # print(obj_variatie)
                segment_curent = obj_variatie['values']
                copy_future_price = obj_variatie['future_price']
                old_last_price = obj_variatie['old_last_price']

                #segment_curent_interpolat = comprimaInterpoleazaSegment(segment_referinta, segment_curent)


                #bullshit code, trash de la ideea ca se interpoleaza in ordinea marimii segmentelor (nu este certa 100% solutia, ramane temporar structura else de alege a ordinii)
                if len(segment_curent) > len(segment_referinta):
                    segment_curent_interpolat = comprimaInterpoleazaSegment(segment_referinta,segment_curent)
                else:
                    #trebuie facuta alta functie care extinde un segment curent de lungime 2 la un segment referinta de lungime 5
                    #momentan, nu facem nicio prelucrare asupra segmentului curent aici
                    segment_curent_interpolat = comprimaInterpoleazaSegment(segment_referinta,segment_curent)


                obj_variatie_nou= {
                    'values': segment_curent_interpolat,
                    'future_price': copy_future_price,
                    'old_last_price': old_last_price
                }

                variatii_interpolare[index_size_variatie].append(obj_variatie_nou)

        self.data['variatii_interpolate'] = variatii_interpolare
    def returnData(self):
        return self.data

    def printVariatii(self):
        print('Variatii')
        for a in self.data['variatii']:
            print(self.data['variatii'][a])
    def printVariatiiInterPolate(self):
        print('Variatii interpolate:')
        for a in self.data['variatii_interpolate']:
            print(self.data['variatii_interpolate'][a])
