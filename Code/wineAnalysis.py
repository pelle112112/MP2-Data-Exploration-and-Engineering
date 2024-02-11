import pandas as pd
import numpy as np
import matplotlib as plt
import xlrd

# Function for loading in the files
def loadWines():
    redWine = pd.read_excel('../Data/winequality-red.xlsx', skiprows=1)
    whiteWine = pd.read_excel('../Data/winequality-white.xlsx', skiprows=1)
    return redWine, whiteWine

redDF, whiteDF = loadWines()

# Checking for missing data
def checkMissingData(red, white):
    print(red.isnull().sum())
    print(white.isnull().sum())

checkMissingData(redDF, whiteDF)

# No missing data to report
# The two files have the same columns, so at this point theres no reason to remove any of them.

# Adding a type column with 'red' and 'white'
def addTypeColumns (red, white):
    red.insert(0, 'type', 'red')
    white.insert(0, 'type', 'white')

# Checking if we got the new columns:
addTypeColumns(redDF, whiteDF)

# Concatenating the two dataframes
def aggregateData(red, white):
    combined_df = pd.concat([red, white], ignore_index=True)
    return combined_df

mergedDF = aggregateData(redDF, whiteDF)
print(mergedDF, mergedDF.count)