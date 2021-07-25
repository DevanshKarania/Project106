import csv
import numpy as np


def getDataSource(data_path):
    daysPresent = []
    marks = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            daysPresent.append(float(row["Days Present"]))
            marks.append(float(row["Marks In Percentage"]))

    return {"x" : daysPresent, "y": marks}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and days present :-  \n--->",correlation[0,1])

def setup():
    data_path  = "class106/student.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()