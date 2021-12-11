
'''
Primeste un vector de input (modelat in prealabil pentru a scoate zgomotul).
Primeste size segment principal + max_stretching + min_stretching
Primeste future_distance (ce pret din viitor sa retina pentru fiecare generare).
Determina cati vectori trebuie de genereze intre min si max.
(Vectorii len() diferit. ex: daca min = x=> len() = len(input) / x)
Metoda care face streching segmentelor din vectorii de mai sus, pana la marimea
segmentului principal.
Acum avem:
{
    marime_segment_principal: 4 //4 puncte din graficul de input
    future_distance: x
    min_stretching = 2
    max_stretching = 7
    variatii:{
    '2':[ {values:[a,a,a,a], future_price:x}, {values:[b,b,b,b], future_price:x}... ] //vectori de 2 puncte adusi la 4 puncte
    //4, deoarece atat are segmentul principal cu care facem mai departe cross-corelation, bla bla
    '3':[],
    '4':[],
    '5':[],
    '6':[],
    '7':[]
    }
}
'''

class generatorSegment:

    inputData = None

    data = {
        'segment': None,
        'size_segment_principal': None,
        'min_stretching': None,
        'max_stretching': None,
        'variatii':{

        }
    }

    def __init__(self,newData):
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

    def truncateInputData(self,decimals):
        temp =[[round(a[0],decimals), round(a[1],decimals)] for a in self.inputData]
        self.inputData = temp

    def normalizeazaSegmentBaza(self):
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

        for variatie in self.data["variatii"]:
            size_segment = int(variatie)

            index_global = 0 #parcurge tot graful pe un an
            counter = 0 #stie cand sa dea trigger la un nou segment
            buffer = [] #acumuleaza cate un segment pe rand

            for index, x in enumerate(self.inputData):

                if counter == size_segment:
                    #stocheaza segment din buffer + goleste buffer
                    temp_obj = {
                        'values': [a for a in buffer],
                        'future_price': self.inputData[index +4] if index + 4 < len(self.inputData) else None
                    }
                    self.data['variatii'][variatie].append(temp_obj)
                    buffer = []
                    counter = 0
                else:
                    counter +=1
                    buffer.append(x)

    def printVariatii(self):
        variatii = self.data['variatii']

        for x in variatii:
            print('Segmente de:', x)
            for y in variatii[x]:
                print(y)

    def normalizeazaVariatii(self):
        variatii = self.data["variatii"]

        new_variatii = { }
        for x in variatii:
            new_variatii[x] =[]
            print('Normalizez variatia:',x)
            for index, y in enumerate(variatii[x]):

                values = y['values']
                future_price = y['future_price']


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


                new_future_price = []
                if future_price != None:
                    new_future_price.append(round(future_price[0] - min_x,1))
                    new_future_price.append(round(future_price[1] - min_y,1))
                else:
                    new_future_price = future_price


                new_variatii[x].append({
                    'values': new_values,
                    'future_price': new_future_price
                })

        self.data['variatii'] = new_variatii



    def comprimare_segmente_mari(self):
        segmente = [x for x in self.data['variatii']]

        #lasa aici doar segmentele mari
        segmente_mari = [x for x in segmente if x > self.data['size_segment_principal']]

        for x in segmente_mari:
            for index,y in enumerate(self.data['variatii'][x]):

                from_size = x
                to_size = self.data['size_segment_principal']
                current_big_arr = y
                factor_sub_unitar = to_size / from_size

                #vr sa comprim current_big_arr de la from_size la to_size (in final o sa aiba to_size puncte)

    def comprimare_segmente_mici(self):
        pass