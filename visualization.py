import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.neighbors import LocalOutlierFactor
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import os

# takes in a filename and returns a dataframe


def readCSV(filename):
    '''
    Takes a string of a filename and reads the csv file into a dataframe
    Returns a dataframe
    '''
    df = pd.read_csv(filename)
    df.head(5)
    return df

# function used to analyz the dataframe


def analyze(df):
    '''
    Takes a dataframe and does some analysis on it
    Including: shape,description, and if any values are null
    Has no return value
    '''
    print(f'df shape: {df.shape}')
    data = df.sample(frac=0.2, random_state=1)
    print(f'df Descripe: {df.describe()}')
    print(f'data Shape: {data.shape}')
    print(f'Check If Null: {df.isnull().values.any()}')

# function to get a collection of the different types of a certain column


def getTypes(df, field):
    '''
    takes a dataframe and a field to focus on and
    returns all the different values in that field
    '''
    types = []
    for category in df[field]:
        # print(category)
        if category not in types:
            types.append(category)
    print(f'Type: {types}')
    return types


def createBarGraph(df, field, title, length, color):
    '''
    createBarGraph takes a dataframe, the field you want to measure, the title
    of the graph, and the length of items you want to display in the barGraph
    length must be either an integer or 'N'
    '''
    if length == 'N':   # check the value of length.
        # if 'N', set to integer equivalent to length of num_classes to see entire dataset
        length = len(fields)
    else:
        length = int(length)
    # get all different types of the specified field
    fields = getTypes(df, field)
    # get a list of the different options for the field
    num_classes = pd.value_counts(df[field], sort=True)
    # limit the size of the graph to 'length', default: length of num_classes

    num_classes = num_classes.take([0,length])
    # specify a bar graph
    num_classes.plot(kind='bar')
    # initialize the name of the graph
    plt.title(f"{field} Class Distribution")
    plt.xticks(range(length), fields[:length])
    plt.xlabel("Fields")
    plt.ylabel("Frequency")
    plt.show()
    return plt
def createLineGraph(df, field, title, length, color):
    '''
    # TODO:
    '''

def main():
    filename = input('Enter Filename: ')
    df = readCSV(filename)
    print('Analyzing...')
    analyze(df)
    field = input('What field are you looking for? ')
    title = input('What is the title of your graph? ')
    length = input('How Many Fields Would You Like To See? ')
    color = input('what color is this graph? ')
    plt = createBarGraph(
                        df=df,
                        field=field,
                        title=title,
                        length=length,
                        color=color
                        )
    plt.savefig(title+'.PNG')

if __name__ == '__main__':
    # df = pd.read_csv('hashed.rx.1.csv')
    # #getTypes(df, "Protocol")
    # createBarGraph(
    #     df=df,
    #     title='Frequency of Protocols in CryptoFortress',
    #     field='Protocol',
    #     length=5,
    #     color='Red'
    #     )
    main()
