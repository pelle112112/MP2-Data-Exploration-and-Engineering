# MP -2
## BI assignment
## Made by Pelle, Danyal, Nicolai og Carsten

### opg 1 Load wine data from the two source files winequality-red.xlsx and winequalitywhite.xslx

Is being done in the loadWines function.

### opg 2 Clean the data in both files. 

We are checking for missing values in checkMissingData function. Considering that there isn't any missing values, and that our data sets contains the same columns, we consider the data clean. 

### opg 3 Aggregate the two files in one still keeping the identity of each wine type - “red” or “white”. 

We start by inserting a new column named 'type' in both dataframes in the addTypeColumns function and then merge the two dataframes together using the concat method from pandas. 

### opg 4 Explore the features of the original and the new files: 

A: number of rows and columns \ [6497 rows x 13 columns]\
B: type of data in each column \
type                     object\
fixed acidity           float64\
volatile acidity        float64\
citric acid             float64\
residual sugar          float64\
chlorides               float64\
free sulfur dioxide     float64\
total sulfur dioxide    float64\
density                 float64\
pH                      float64\
sulphates               float64\
alcohol                 float64\
quality                   int64

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
   The acidity of the products, maybe in relation to how it relates to the quality. 
   Price would also be an interesting comparison - although it is not represented in this dataset. 


### opg 8 Split the aggregated data into five subsets by binning the attribute pH. Identify the subset with the highest density? What if you split the data in ten subsets?

Bin with most amount of entries is 2.978 - 3.236 when using 5 bins
<img src="Data\Graphs\pH_bins_5.png">

Bin with most amount of entries is 3.107 - 3.236 when using 10 bins
<img src="Data\Graphs\pH_bins_10.png">

### opg 9

   the overall quality is depended mostly on the amount of alcohol, the correlation is under 0.50, so i would say there is no correlation. which might be the reason why it was difficult earlier to determend what the requirement for better quality wine would be. the 
   attribute with the lowest correlation is pH with 0.01
   When we seperate the types of wine, the result for them are as following:

   Red: attribute with most correlation is - Alcohol with 0.47 and least is - Residual sugar with 0.01
   White attribute with most correlation is - Alcohol with 0.43 and least is - free sulfur dioxide with 0.008
