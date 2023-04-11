#Customer Conversion Prediction

This project is a classification problem that aims to predict whether a customer will subscribe for insurance or not. The data contains various features such as age, job, marital status, educational qualification, and call details like day, month, duration, number of calls, and call type. The target variable is a binary variable that indicates whether the customer will subscribe (Yes or No).

#Data Cleaning and Preprocessing

Before building the model, the data was cleaned and preprocessed using various techniques such as encoding and scaling. The missing values were handled, and the categorical variables were encoded using one-hot encoding. The numerical variables were scaled using StandardScaler. The data was also balanced using the SMOTE technique to handle class imbalance.

#Exploratory Data Analysis

The data was visualized using various types of plots such as histograms, box plots, and scatter plots. The relationships between the target variable and other features were explored using different visualizations such as count plots and heatmaps. This helped in understanding the distribution of data and identifying any outliers or anomalies.

#Model Building

Several algorithms were used to build the classification model, including Logistic Regression, Decision Tree, Random Forest, and XGBoost. The models were trained and evaluated using cross-validation techniques such as k-fold and stratified k-fold. The performance of the models was evaluated using various metrics such as accuracy, precision, recall, and F1-score.

#Results

The results of the model performance are summarized  below:

Logistic Regression - AUROC Score is 0.85

KNN - AUROC Score is 0.888

Decision Tree - AUROC Score is 0.893

XG Boost - AUROC Score is 0.899

Random Forest - AUROC Score is 0.903

Hence Random Forest is giving the good AUROC Score of 0.903
Based on the results, we can see that the Random Forest algorithm had the highest overall performance with an accuracy of 0.85 and an F1 score of 0.903

#Conclusion

In conclusion, this project demonstrated how a classification model can be built to predict customer conversion for insurance. The data was cleaned, preprocessed, and visualized to gain insights into the data. Different algorithms were used to build the model, and Random Forest performed the best. The feature importance analysis provided valuable insights into the important features in predicting customer conversion. This model can be used by insurance companies to target potential customers who are likely to subscribe to their services.

#Future Work

In the future, the model can be further improved by using more advanced techniques such as hyperparameter tuning and ensemble methods. Additionally, new features can be added to the data to improve the performance of the model. The model can also be deployed as a web application to make it easily accessible to users.






