import plotly.express as pe 
import csv 
import numpy as np 

def getDataSource(data_path):
    marksInPercent=[]
    daysPresent=[]

    with open(data_path) as CSVFile:
        csvreader=csv.DictReader(CSVFile)
        for row in csvreader:
            marksInPercent.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))
    return{'x':marksInPercent, 'y':daysPresent}

def findCorellation(data_source):
    corellation=np.corrcoef(data_source["x"], data_source["y"])
    print('Corellation b/w Marks Obtained & Days Present: ', corellation[0,1])


def plotFigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=pe.scatter(df, x='Marks In Percentage', y='Days Present')
        fig.show()

def setup():
    data_path="corel.csv"
    data_source=getDataSource(data_path)
    findCorellation(data_source)
    plotFigure(data_path)

setup()

