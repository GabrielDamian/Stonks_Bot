import matplotlib.pyplot as plt
import csv

def readDataFromFile(fileName,linesToRead):
    vector = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                pass

                y = row[1].split()

                if len(y) >= 2:
                    z = y[1].split(':')
                    final_time = int(z[1])

                vector.append(row[3])
                line_count += 1
            linesToRead -= 1
            if linesToRead< 0:
                break
        print(f'Processed {line_count} lines.')

        #primul elem din arr este un header de tip string (trash de la citire)
        del vector[0]
        #inverseaza ordinea in vector
        # vector = vector[::-1]

        float_arr = []
        for x in vector:
            float_arr.append(float(x))
        return float_arr

