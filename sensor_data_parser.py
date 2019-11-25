import csv
import math
import sys

Sense_1_Avg = 0.0
Sense_1_Min = 50
Sense_1_Max = 0
Sense_2_Avg = 0.0
Sense_2_Min = 50
Sense_2_Max = 0
Sense_3_Avg = 0.0
Sense_3_Min = 50
Sense_3_Max = 0
Sense_4_Avg = 0.0
Sense_4_Min = 50 
Sense_4_Max = 0
Sense_5_Avg = 0.0
Sense_5_Min = 50
Sense_5_Max = 0


with open('raw_data.csv') as file_csv:
    read_csv = csv.reader(file_csv, delimiter = ',')
    #lines_csv = csv_file.readinglines()
    #length_csv = len(lines_csv)
    #print length_csv 
    cur_line = 0

    for row in read_csv:
        if cur_line == 0:   #if first line
            print('\t\t\tSummary of Raw Data from Sensors') #print title of table 
            cur_line += 1   # next line 
        elif cur_line == 1: #if second line 
            print('\t\tAverage\t\tMinimum Reading\t\tMaximum Reading') #next set of titles 
            cur_line += 1   #next line 
        else: #steps through and computes all values as it goes 
            Sense_1_Avg = Sense_1_Avg + float(row[0])   #Sensor 1 
            #Sense_1_Avg = round(Sense_1_Avg/6000,1)
            if int(row[0]) < Sense_1_Min:
                Sense_1_Min = int(row[0])
            if int(row[0]) > Sense_1_Max:
                Sense_1_Max = int(row[0])
            
            Sense_2_Avg = Sense_2_Avg + float(row[1])   #Sensor 2
            #Sense_2_Avg = round(Sense_2_Avg/6000,1)
            if int(row[1]) < Sense_2_Min:
                Sense_2_Min = int(row[1])
            if int(row[1]) > Sense_2_Max:
                Sense_2_Max = int(row[1])

            Sense_3_Avg = Sense_3_Avg + float(row[2])   #Sensor 3
            #Sense_3_Avg = round(Sense_3_Avg/6000 , 1)
            if int(row[2]) < Sense_3_Min:
                Sense_3_Min = int(row[2])
            if int(row[2]) > Sense_3_Max:
                Sense_3_Max = int(row[2])

            Sense_4_Avg = Sense_4_Avg + float(row[3])   #Sensor 4
            #Sense_4_Avg = round(Sense_4_Avg/6000 , 1)
            if int(row[3]) < Sense_4_Min:
                Sense_4_Min = int(row[3])
            if int(row[3]) > Sense_4_Max:
                Sense_4_Max = int(row[3])

            Sense_5_Avg = Sense_5_Avg + float(row[4])   #Sensor 5
            #Sense_5_Avg = round(Sense_5_Avg/6000 , 1)
            if int(row[4]) < Sense_5_Min:
                Sense_5_Min = int(row[4])
            if int(row[4]) > Sense_5_Max:
                Sense_5_Max = int(row[4])

            cur_line += 1

    Sense_1_Avg = round(Sense_1_Avg/6000 , 1)   #divide by the number of elements 
    Sense_2_Avg = round(Sense_2_Avg/6000 , 1)
    Sense_3_Avg = round(Sense_3_Avg/6000 , 1)
    Sense_4_Avg = round(Sense_4_Avg/6000 , 1)
    Sense_5_Avg = round(Sense_5_Avg/6000 , 1)

    print 'Sensor 1\t', Sense_1_Avg, '\t\t', Sense_1_Min, '\t\t\t', Sense_1_Max
    print 'Sensor 2\t', Sense_2_Avg, '\t\t', Sense_2_Min, '\t\t\t', Sense_2_Max
    print 'Sensor 3\t', Sense_3_Avg, '\t\t', Sense_3_Min, '\t\t\t', Sense_3_Max
    print 'Sensor 4\t', Sense_4_Avg, '\t\t', Sense_4_Min, '\t\t\t', Sense_4_Max
    print 'Sensor 5\t', Sense_5_Avg, '\t\t', Sense_5_Min, '\t\t\t', Sense_5_Max
