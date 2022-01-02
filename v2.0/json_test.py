import json

if __name__ == '__main__':
    file_object = open('results.txt', 'r')
    data_json = file_object.read()

    data_obj = json.loads(data_json)

    max_sum = 0
    max_sum_index = 0
    for index, a in enumerate(data_obj):
        print("--------")
        print('seg baza:', a['segment_baza'])
        print('variatii:')
        sum = 0
        for v in a['variatii']:
            print(v, f'len={len(a["variatii"][v])}',a['variatii'][v])
            sum += len(a["variatii"][v])
        print('total=',sum)
        if sum > max_sum:
            max_sum = sum
            max_sum_index = index

    print('sum max:', max_sum)
    print('la index:', max_sum_index)

    futures_pozitive = 0
    obj_max = data_obj[max_sum_index]
    print('seg baza:', data_obj[max_sum_index]['segment_baza'])
    for a in data_obj[max_sum_index]['variatii']:
        print(a, "-->")
        for b in data_obj[max_sum_index]['variatii'][a]:
            print(b)
            # if(b['future_price'])