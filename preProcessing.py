import csv
import pandas as pd
from hashlib import sha256



'''read in the csv of netflow data'''
def read_csv(filename):
    dataframe = pd.read_csv(filename)
    return dataframe



'''Hashes the Destination and Source fields'''
def hash(dataframe):
    hashedSourceList = []
    hashedDestList = []
    for line in dataframe['Source']:
        #hash the line with a sha256 hash
        hashedLine = sha256(line.encode()).hexdigest()
        hashedSourceList.append(hashedLine)# add this hashed line to the global list

    #replace the dataframe column with the hashed column
    dataframe['Source'] = hashedSourceList
    print(dataframe['Source'])


    for line in dataframe['Destination']:
        #hash line with a sha256 hash
        hashedLine = sha256(line.encode()).hexdigest()
        hashedDestList.append(hashedLine) # add the hashed line to the global list
    # replace the normal column with the hashed column
    dataframe['Destination'] = hashedDestList
    print(dataframe['Destination'])
    return dataframe



dataframe = read_csv('csvfile.csv')
print(dataframe)
hashedData = hash(dataframe)
hashedData.to_csv('hashed.csv')
print(dataframe)
