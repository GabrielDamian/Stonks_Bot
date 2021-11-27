import matplotlib.pyplot as plt
import csv

def readDataFromFile(fileName):
    vector = []
    lines_to_plot = 1000
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
            lines_to_plot -= 1
            if lines_to_plot< 0:
                break
        print(f'Processed {line_count} lines.')
        del vector[0]
        #inverseaza ordinea in vector

        # vector = vector[::-1]
        return vector

