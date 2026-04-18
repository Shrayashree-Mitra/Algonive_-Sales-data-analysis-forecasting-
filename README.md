# Algonive_-Sales-data-analysis-forecasting-
Sales Data Analysis &amp; Forecasting System using Python —  Data Cleaning, EDA, Feature Engineering &amp; Predictive Modeling  to analyze past sales trends and predict future revenue
Overview
This project builds a complete Sales Forecasting pipeline using real-world retail data. It covers data cleaning, exploratory analysis,feature engineering, and predictive modeling to help businesses optimize inventory and marketing strategies.
Key Features
- ✅ Data Cleaning & Preprocessing
- ✅ Exploratory Data Analysis (EDA)
- ✅ Feature Engineering
- ✅ Sales Forecasting Model
- ✅ Dashboard & Visualization
Technologies Used
Python (Pandas , NumPy)
Scikit-learn — Machine learning
Visualization- PowerBi
Project Workflow:
Data collection
Data cleaning
Feature engineering
Model building
Evaluation
Visualization
Results:
The dataset contains 1,048,575 records with no missing values after preprocessing.
Feature engineering improved the dataset by adding:day, quarter, is_weekend, lag_1, and rolling_mean_7.
Model performance:
MAE (Mean Absolute Error): 4.70
RMSE (Root Mean Squared Error): 6.14
The model captures overall sales patterns reasonably well, with most prediction errors staying within a small range.
Sample predictions show close alignment between actual and predicted sales, though occasional higher deviations are observed.
The final dataset includes predicted values and error metrics, enabling further analysis and visualization in Power BI
The model achieved an MAE of 4.70, meaning predictions deviate
by only ~4.7 units on average across 1M+ records.
Conclusion:
This project successfully analyzed historical sales data and built a forecasting approach to predict future demand. Through data cleaning, feature engineering, and exploratory analysis, meaningful patterns such as seasonal trends and promotional impact were identified.
Overall, the project demonstrates how data-driven techniques can support better decision-making in inventory planning and sales strategy. Future enhancements can include advanced models and additional features to further improve accuracy.
