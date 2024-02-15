import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
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


# OPG 4
# Explore the data
# Number of rows, coloumns and type of data in each coloumn

def typeOfData (merged):
    print(merged.shape)
    print(merged.dtypes)


def describeMergedData(merged):
    mergedData = merged.describe()
    print(mergedData)
    return mergedData

typeOfData(mergedDF)
mergedData = describeMergedData(mergedDF)

# OPG 5
# Calculate the descriptive statistics of the numeric data

def analyzeNumericData(data, title='numeric data analysis'):
    numericData = data.select_dtypes(include=[np.number])
    descriptiveStatistics = numericData.describe()
    numericData.hist(bins=20, figsize=(15, 10))
    plt.suptitle(f'Histogram of Numeric Features - {title}')
    plt.show()

    print(descriptiveStatistics)

# Method for the merged data
analyzeNumericData(mergedDF, title='Red and White Wines')

# Method for red wine data
analyzeNumericData(redDF, title='Red Wine')

# Method for white wine data
analyzeNumericData(whiteDF, title='White Wine')

# OPG 6
# Compare red and white wine on Quality, Alcohol and Residual sugar
def compareWines(red, white):
    attributes = ['quality', 'alcohol', 'residual sugar']

    #Create subplots (let more diagrams be shown on the same page)
    fig, axes = plt.subplots(nrows=len(attributes), ncols=1, figsize=(10, 15))

    for i, attribute in enumerate(attributes):
        sb.histplot(data=red, x=attribute, color='red', label='Red Wine', kde=True, ax=axes[i])
        sb.histplot(data=white, x=attribute, color='Green', label='White Wine', kde=True, ax=axes[i])
        axes[i].set_title(f'Distribution of {attribute} in Red and White Wines')
        axes[i].legend()

    plt.subplots_adjust(hspace=0.5)
    plt.show()

compareWines(redDF, whiteDF)

# OPG 8
# Split aggregated data into 5 and 10 subsets and print out higest density
 
def splitAggregated(mergedDF):
    mergedDF['pHBins5'] = pd.cut(mergedDF['pH'], bins=5)

    # Higest density
    higestDensityOf5 = mergedDF['pHBins5'].value_counts().idxmax()

    print(f'The subset with the higest density (5 bins) is {higestDensityOf5}')

    mergedDF['pHBins10'] = pd.cut(mergedDF['pH'], bins=10)

    higestDensityOf10 = mergedDF['pHBins10'].value_counts().idxmax()
    print(f'The subset with the higest density (10 bins) is {higestDensityOf10}')


splitAggregated(mergedDF)

# OPG 9
# create a Correlation matrix of all the data
def plotCorrelationMatrix (data, title='Correlation Matrix'):
    
    numericData = data.select_dtypes(include=[np.number])

    correlationMatrix = numericData.corr()

    #plot the heatmap
    plt.figure(figsize=(12,8))
    sb.heatmap(correlationMatrix, annot=True, cmap='coolwarm', fmt='2f', linewidths=.5)
    plt.title(title)
    plt.show()

# Method for the merged data
plotCorrelationMatrix(mergedDF, title='Correlation Matrix of All Attributes (Red and White Wines)')

# Method for red wine data
plotCorrelationMatrix(redDF, title='Correlation Matrix of All Attributes (Red Wine)')

# Method for white wine data
plotCorrelationMatrix(whiteDF, title='Correlation Matrix of All Attributes (White Wine)')