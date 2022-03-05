

if __name__ == '__main__':
    print("test file")
    arr =[29282, 29293.5, 29305, 29286.7, 29268.3, 29250, 29231.7, 29213.3, 29195, 29176.7,]
    min = arr[0]

    for a in arr:
        if(a < min):
            min =a

    print("min=",min)


    normalizat = []
    for a in arr:
        normalizat.append(a-min)

    print("normalizat:", normalizat)
