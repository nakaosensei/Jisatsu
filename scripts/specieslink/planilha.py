import pandas as pd
import csv

class Planilha:
    def open_xls(self):
        a = ""

    def writeCsv(self,file,titleArray,valuesArray):
        with open(file, mode='w') as csvFile:
            writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(titleArray)
            for value in valuesArray:
                writer.writerow(value)
