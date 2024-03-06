### Introduction

The goal of this project is to create a machine learning model that can predict housing prices in Philadelphia. The dataset used can be gotten from https://www.phila.gov/property/data/. 

### Data Collection

Data was collected via the website above. The data is in the form a .csv file with 82 features and 582,933 columns. To visualize the data I used data wrangler which is an extension in Visual Studio Code that can read .csv files. I input the csv file into a pandas Data Frame which was used for the below preprocessing steps. I decided to stick with only residential houses because majority of the data was residential, and the industrial and commercial buildings would skew the data.

### Data Preprocessing

The bulk of the project was spent preprocessing data. Most columns had nan's, there were many outliers, and some row features needed to be changed. I found an article on Medium (https://medium.com/@GaussEuler/philadelphia-housing-data-part-i-data-analysis-fe45415554a9) that helped with weeding out some of the initial columns. I eliminated columns that were:
- Missing majority of their data
- Had columns with majority distinct rows
- Categories that didn't make sense to encode
- Columns with data that clearly had no correlation

After eliminating the first batch of columns, I went through one by one with the remaining to clean the data. First I displayed the unique values and summed the totals for each. This mainly helped with categorical data so that i could see the distributions and fill in the nan's. Depending on how many nan's were missing, I would either drop the missing rows, or fill in the missing data with the mean. Since the dataset has over 500,000 rows, i could safely remove rows without affecting the ability to train the model. 

As i was going through the data, there were columns that I could completely eliminate like fuel, number_of_rooms, utility, quality_grade, because there was either to much missing data, or the rows had to many extraneous features. Some columns like basements had categorical features like 1, 2, 3 that were not established housing codes, so I had to rename them to letters.

Once I finished cleaning the data, I could see all the outliers. This was mainly of concern for some of the numerical columns like number of rooms where the max was 45 and the mean was 3. For the columns with outliers, I used Interquartile Range to eliminate the lower and upper bounds.

### Feature Engineering

The next step was to select the features that had the highest correlation with the target data. I separated the categorical data from the numerical data so I could apply separate feature selection techniques. The categorical data was not ordinal, so I decided to use SelectKBest, which uses $chi^2$, to select the highest percentile features in correlation to the target feature. For the numerical data I used Pearson's correlation coefficient to find features with the highest correlation to the target data. I ended up using all of the numerical features because it didn't increase the dimensionality by much. I selected five of the categorical features. For the categories that had only a few unique features, I used one hot encoding so that I wouldn't introduce ordinal relationships. For zipcode and year built, I used frequency encoding to reduce the dimensionality and again, not introduce ordinal relationships. I ended up with 55 features.

After selecting all the features, I used PCA to pick out the signals in the data. 

### Model Development

 I decided to use a linear regression model because we're predicting price which is a continuous value. First I split the data into its x and y features. Then i standardized the data because I wanted to use PCA. Next I split the data into training and testing sets. First I trained the model without PCA and got results that did not make sense. The mean squared error was $10^{-16}$ and the $R^2$ was 1.0. I knew there was overfitting of the model because the mean squared error was so small. Also it is very unlikely for a linear regression model to have a perfect R^2 value. I switched to using PCA on the standardized data and started with 21 components. This fixed the overfitting of the data and resulted in an R^2 of 0.857. The PCA coverage was only 0.58, so I started to add increments of 2 to the component value. The best result was 49 components with a mean squared error of 242680740.4 and R^2 of 0.991.

### Construction of Test Dataset

To construct the test dataset, I simply used train_test_split from sklearn. After playing around with the test size, I settled on a 0.3 split which led to good model output. I made sure to standardize the data before splitting it so the standard deviation was calculated across the whole dataset. I also set a random state of 21 so the data was split randomly and so I can recreate the conditions. 

### Discussion of Project

The linear regression model performed exceptionally well on the unseen data. The limitation with this model is that it is only trained on residential housing. A separate model would need to be developed for industrial and commercial buildings. It would not be advised to create a combined model because the commercial housing would skew the data. There was also limited data on industrial and commercial buildings compared to residential.

One of the challenges faced on the project was being able to view the data easily. The discovery of data wrangler solved this issue and made it easy to sort the data, search for columns, view the max and min , and see trends. Without it, i would of had to use pyplot to navigate the data.

Another challenge was making sure to not overfit the model. I had to play around with the hyperparameters until the model had a good output. At times I would change the PCA components and the mean squared error would go toward 0. I also played around with different numbers of features to reduce dimensionality and still lead to good results.

Overall this was a great project to utilize machine learning techniques on a raw dataset. It was daunting at first dealing with such a large amount of data, but the more I worked with it, the more patterns I discovered in developing models. A future project could be to build a model for commercial and industrial buildings.

