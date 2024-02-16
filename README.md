# MP -2

## BI assignment

## Made by Pelle, Danyal, Nicolai og Carsten

### opg 1 Load wine data from the two source files winequality-red.xlsx and winequalitywhite.xslx

Is being done in the loadWines function.

### opg 2 Clean the data in both files.

We are checking for missing values in checkMissingData function. Considering that there isn't any missing values, and that our data sets contains the same columns, we consider the data clean.

### opg 3 Aggregate the two files in one still keeping the identity of each wine type - “red” or “white”.

We start by inserting a new column named 'type' in both dataframes, which contains the type of wine to be either 'red' or 'white' in the addTypeColumns function and then merge the two dataframes together using the concat method from pandas.

### opg 4 Explore the features of the original and the new files:

A: number of rows and columns \ [6497 rows x 13 columns]\
B: type of data in each column \
type object\
fixed acidity float64\
volatile acidity float64\
citric acid float64\
residual sugar float64\
chlorides float64\
free sulfur dioxide float64\
total sulfur dioxide float64\
density float64\
pH float64\
sulphates float64\
alcohol float64\
quality int64

### opg 5 Calculate the descriptive statistics of the numeric data. Is the data normally distributed?

on some points, it is normally distributed. Like Quality, pH value and Alcohol (for red wine table). But not on values like Sulphates (for red wine), sulfur dioxide (also red wine), where, it shows that how many of the value in question is present in the stock of red and white wine. So from these Histogram. It shows that there is a major representation of medium quality wine for both red and white wine. Its hard to spot if all the other values create a better or poorer wine if you turn up or down on some of the ingredienses.

<img src="Data\Graphs\HistogramOfDescriptiveStatisticRedAndWhite.png">
<img src="Data\Graphs\HistogramOfDescriptiveStatisticRed.png">
<img src="Data\Graphs\HistogramOfDescriptiveStatisticWhite.png">

### opg 6 Plot diagrams that visualize the differences in red and white wine samples. Use it as a support for answering the following questions:

<img src="Data\Graphs\RedAndWhiteComparisonHistogram.png">
<img src="Data\Graphs\Red_White_comparison_average.png">

a. What exactly is shown on the diagrams?\
The first diagram shows how the generel quality of wine is in the stock, in this case there is a big reprensentation of medium quality wine for both red and white
The second diagram shows how the volume of alcohol is distributed among the wine in stock. for red wine most wine have a alcohol % between 9 and 10 and for white its mainly
between 8.5 and 10 with a little spike at both 11 and 12%
The third diagram shows that for both red and white wine the residual sugar is mainly in the lower 1-3%, but where there is no red wine with over 3% RS, white still have a few all the way up to 20%
In the last diagram it is shown that both red and white wine have on average have a similar level of quality and amount of alcohol. There is however a big difference in the amount of residual sugar in the products.

b. After seeing it, can you tell which type of wine has higher average quality?\
From the first and fourth diagram we can deduct that there are many more white wine than red, but the generel quality of white wine is slightly better than red, since there are more quality
6 wine than any other. But in red wine there is a little overrepresentation of quality 5 wine over quality 6.

c. Which type of wine has higher average level of alcohol?\
This might be a little harder to answer out of visual comparison alone. Since the graph for both red and white wine follow each other quite similar. but there is a little spike
for white wine at both 11% and 12% which isn't quite as marked in the red wine. So the answer to this is most likely white.

d. Which one has higher average quantity of residual sugar?\
Clearly white wine. Since there is no residual sugar for red wine beyond 3-4% but for the white wine, even tho most are in the lower 1-4%, there are still some all the way up to 20%

### opg 7 Which other questions might be of interest for the wine consumers or distributers?

The acidity of the products, maybe in relation to how it relates to the quality.\
Price would also be an interesting comparison - although it is not represented in this dataset.

### opg 8 Split the aggregated data into five subsets by binning the attribute pH. Identify the subset with the highest density? What if you split the data in ten subsets?

Bin with most amount of entries is 2.978 - 3.236 when using 5 bins
<img src="Data\Graphs\pH_bins_5.png">

Bin with most amount of entries is 3.107 - 3.236 when using 10 bins
<img src="Data\Graphs\pH_bins_10.png">

### opg 9 Create a heat map or a correlation matrix of all data and investigate it. Can you tell which vine attribute has the biggest influence on the wine quality? Which has the lowest?

<img src="Data\Graphs\CorrelationMatrixOfAllAttributes.png">

The overall quality is depended mostly on the amount of alcohol, the correlation is under 0.50, so i would say there is no correlation. which might be the reason why it was difficult earlier to determend what the requirement for better quality wine would be.
The attribute with the lowest correlation is pH with 0.01

### Do you get the same results when you analyze the red and white wine data sets separately?

<img src="Data\Graphs\CorrelationOfAllAttributesRedWine.png">
<img src="Data\Graphs\CorrelationMatrixOfAllAttributesWhiteWine.png">
   
When we seperate the types of wine, the result for them are as following:\

Red: attribute with most correlation is - Alcohol with 0.47 and least is - Residual sugar with 0.01\
White attribute with most correlation is - Alcohol with 0.43 and least is - free sulfur dioxide with 0.008\
All in all the correlation between quality and the other features are quite similar for the individual wines when compared to the full collection of wine in our dataset.

### 10 Explore the feature ‘residual sugar’. Is there any outlier (a value much different from the rest)? On which row is it found? Remove that row.

<img src="Data\Graphs\boxplot_finding_outliers.png">
The boxplot shows that there is a collection of outliers, with some being relatively close to the center and 1 data entry being way off from the rest.\
We decided to use the IQR method to identify outliers and removed all of them, but considering that only 1 entry is so far from the rest, it would have been reasonable to remove that entry alone, in order to not lose to much data.

### 11 Identify the attribute with the lowest correlation to the wine quality and remove it.

The feature with the lowest correlation to quality is pH value. As also shown on our heatmap from earlier tasks.

### 12 Transform the categorical data into numeric.

The only non numeric feature in our dataset is the type category. We used labelencoder to convert the values, with red being 0, and white being 1.

### 13 Try to reduce the number of features of the aggregated data set by applying principal component analysis (PCA). What is the optimal number of components?

<img src="Data\Graphs\explained_variance_PCA_components.png">

We use the graph to determine how many components we require to represent 95% of our data. We can achieve that in our dataset using 9 components.\
We conclude that after standardisation we can use the PCA method to reduce our dataset from 12 to 9 columns.
But how many functional components do we need? Its not always a clear answer. We started by covering 50% of the data with 3 components,
but we upped it later to 9 components, to be able to cover 95 % of the data. If we wanted less components, we would have to trim the data even more.

### 14 Print out ten random rows from the final dataset as a prove of concept.

           PC1       PC2       PC3       PC4       PC5       PC6       PC7       PC8       PC9

4401 -0.955836 -1.345626 -0.429852 -0.921674 -0.397175 -1.705118 0.324397 0.201081 -0.056695
2406 -2.170322 1.903310 -0.760646 0.848182 -0.596678 0.210051 0.367429 -0.118659 0.046372
1891 -1.691728 3.827941 0.016511 0.035288 -0.775266 0.183304 0.400989 0.850571 0.599073
6431 -0.720332 -1.039373 -1.360439 -1.192416 0.814257 -0.321614 0.381251 0.260809 -0.192965
3917 -1.461114 3.191910 0.396328 -1.364064 0.631433 0.593017 -0.386883 0.572460 0.207807
3788 -1.059696 1.378547 0.257846 0.266660 -0.678386 -0.946984 -0.160922 -0.096449 0.340620
2800 -0.869127 -1.739620 0.868542 -0.309757 -0.372652 -0.689456 0.126811 -0.833956 -0.280719
2688 -1.154062 -1.123902 0.532419 -0.390238 -0.775522 -0.820636 0.438666 -0.686411 -0.437011
4391 -1.563515 1.733064 0.029487 -0.322923 0.763058 0.295985 -0.355212 0.083431 -0.142061
3867 -1.461872 1.038755 -0.574939 -0.351358 -0.223642 -0.942363 0.017488 -1.089523 -0.662107
