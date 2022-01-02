
#ANY

def segmentareArray(array, size):
    #impare array aprx len(array) semegmente de len = size, obinute prin incrementarea indexului de inceput al celui anterior
    print('segmentare arr:', size)
    result = []

    for index, a in enumerate(array):
        if index < len(array) - size - 1:
            buffer = []
            index_buffer = index
            while len(buffer) < size:
                buffer.append(array[index_buffer])
                index_buffer += 1

            result.append(buffer)

        else:
            # nu mai pot incadra inca un segment
            pass

    return result

#STAGE 1
def normzalieaza_segment(segment):

    x_coords = []
    y_coords = []

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
        final.append([a, round(y_coords_normalizate[index],2)])

    return final

#STAGE 2

###

#STAGE 3
def determinaSizeVariatii(min_param, max_param,size_seg):

    print('Generez index variatii:')
    obj_result = {}

    sizes = []
    index = size_seg - min_param
    max = size_seg + max_param

    while index <= max:
        sizes.append(index)
        index += 1
    for x in sizes:
        obj_result[f'{x}'] = []

    return obj_result

def segmentareArrayFuturePrice(array, size, future_price_offset):
    #impare array aprx len(array) semegmente de len = size, obinute prin incrementarea indexului de inceput al celui anterior
    print('segmentare arr:', size)
    result = []

    for index, a in enumerate(array):
        if index < len(array) - size - 1:
            buffer = []
            index_buffer = index
            while len(buffer) < size:
                buffer.append(array[index_buffer])
                index_buffer += 1


            #find future price
            future_price_val = None
            if index + future_price_offset < len(array) - 1:
                future_price_val = array[index + future_price_offset]

            result.append({
                'values': buffer,
                'future_price': future_price_val
            })

        else:
            # nu mai pot incadra inca un segment
            pass

    return result

def normalizareVariatii(vector_variatie):

    #[{'values': [[0, 29270.54], [1, 29282.03], [2, 29293.51], [3, 29305.0], [4, 29286.67]], 'future_price': [10, 29176.68]}, {},{}]

    vector_variatie_reconstruct = []

    #min y pentru future_price final (normalizare manuala pentru future price)
    # min_value = vector_variatie[0]['values'][0][1]
    # for a in vector_variatie:
    #     for b in a['values']:
    #         if b[1] < min_value:
    #             min_value = b[1]

    for a in vector_variatie:
        min_value = a['values'][0][1]
        for b in a['values']:
            if b[1] < min_value:
                min_value = b[1]

        temp_future_price = None
        if a['future_price'] != None:
            temp_future_price = round(a['future_price'][1] - min_value,2)


        temp_obj = {
            'values': normzalieaza_segment(a['values']),
            'future_price': [0, temp_future_price]
        }
        vector_variatie_reconstruct.append(temp_obj)

    return vector_variatie_reconstruct




#Comprimare-Interpolare
def yEcuatieDreapta(point_a, point_b, x_value):
    x0 = point_a[0]
    y0 = point_a[1]

    x1 = point_b[0]
    y1 = point_b[1]

    x = x_value

    y = (y0*(x1-x) + y1*(x-x0))/(x1-x0)

    return y

def interpolareSegmente(segment_referinta, segment_factorizat):
    #cauta indicii x din segmentul referinta printre indicii (la propriu intre care se situeaza) in segmentul factorizat

    segment_rezultat = []
    x_segment_referinta = [a[0] for a in segment_referinta]
    x_segment_factorizat = [a[0] for a in segment_factorizat]

    # print('x_segment_referinta:', x_segment_referinta)
    # print('x_segment_factorizat:',x_segment_factorizat)

    for a in x_segment_referinta:
        x_current = a

        if x_current in x_segment_factorizat:
            #avem punct comun intre cele segmente
            x_y_factorizat_aferent = None
            for temp in segment_factorizat:
                if x_current == temp[0]:
                    x_y_factorizat_aferent = temp
                    break
            pereche_noua = [x_current, x_y_factorizat_aferent[1]]

            segment_rezultat.append(pereche_noua)

        else:
            #gaseste indicii intre care se situeaza
            prev_index =segment_factorizat[0]
            next_index = None
            index = 1
            while index < len(segment_factorizat):
                next_index = segment_factorizat[index]
                if prev_index[0] < x_current and x_current < next_index[0]:
                    pereche_noua =[x_current, round(yEcuatieDreapta(prev_index, next_index, x_current),2)]
                    segment_rezultat.append(pereche_noua)
                    break
                else:
                    index +=1
                    prev_index = next_index


    # print('Interpolare_final:', segment_rezultat)

    #adauga ultimul index manual

    if len(segment_rezultat) < len(segment_referinta):
        segment_rezultat.append([segment_referinta[-1][0], segment_factorizat[-1][1]])
    return segment_rezultat

def comprimaInterpoleazaSegmente(segment_mic, segment_mare):

    #[a, a, a, a, a]
    #[1, 5, 7, 9, 7, 4, 2]

    x_mic = []
    for a in segment_mic:
        x_mic.append(a[0])

    max_width_seg_mic = max(x_mic)


    x_mare = []
    y_mare = []
    for a in segment_mare:
        x_mare.append(a[0])
        y_mare.append(a[1])

    max_height_seg_mare = max(y_mare)
    max_width_seg_mare = max(x_mare)

    factor_height = 1
    factor_width = round(max_width_seg_mic / max_width_seg_mare,2)
    #factorizare inaltime din segment mare catre segment mic (fie ea subunitara sau supraunitara)

    y_mare_factorizat = [a*factor_height for a in y_mare]

    #factorizare width

    x_mare_facotirizat = [a*factor_width for a in x_mare]

    segment_mare_factorizat = []
    for index, a in enumerate(y_mare_factorizat):
        segment_mare_factorizat.append([x_mare_facotirizat[index],a])

    final_fact_interpolat = interpolareSegmente(segment_mic, segment_mare_factorizat)

    return final_fact_interpolat

def handlerComprimaInterpoleaza(variatii, size_ref):
    # [{'values': [[0, 29270.54], [1, 29282.03], [2, 29293.51], [3, 29305.0], [4, 29286.67]], 'future_price': [10, 29176.68]}, {},{}]
    #conteaza doar lungimea
    referinta_fake =[]
    index_fake = 0

    while index_fake< size_ref:
        referinta_fake.append([index_fake,0])
        index_fake +=1


    vector_variatii_reconstruct = []
    for a in variatii:
        temp_obj = {
            'values': comprimaInterpoleazaSegmente(referinta_fake, a['values']),
            'future_price': a['future_price']
        }

        vector_variatii_reconstruct.append(temp_obj)


    return vector_variatii_reconstruct


def crossCorelation(arr_1, arr_2):
    #len(arr_1) == len(arr_2)

    sum_dif = 0
    for index, a in enumerate(arr_1):
        val_1 = (arr_1[index][1])
        val_2 = (arr_2[index][1])

        if val_1 > val_2:
            sum_dif_temp =abs(val_1-val_2)
        else:
            sum_dif_temp =abs(val_2-val_1)


        sum_dif += sum_dif_temp*sum_dif_temp

    return sum_dif