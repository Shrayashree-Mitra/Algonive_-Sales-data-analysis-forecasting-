import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r'C:\Users\User\OneDrive\Documents\task 2 dataset.csv')  


print(df.head())
print(df.info())
print(df.describe())

print("Missing values:\n", df.isnull().sum())


df = df.dropna()
df['date'] = pd.to_datetime(df['date'],format='%d-%m-%Y')


df_original = df.copy()
df.to_csv('cleaned_dataset.csv', index=False)
print("Cleaned dataset saved!")

print("Shape:", df.shape)
plt.figure(figsize=(12,4))
df.groupby('date')['sales'].sum().plot()
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('sales_over_time.png')
plt.show()


plt.figure(figsize=(10,4))
df.groupby('store_id')['sales'].mean().plot(kind='bar', color='steelblue')
plt.title('Average Sales by Store')
plt.tight_layout()
plt.savefig('sales_by_store.png')
plt.show()


plt.figure(figsize=(6,4))
df.groupby('promo')['sales'].mean().plot(kind='bar', color=['orange','green'])
plt.title('Average Sales: Promo vs No Promo')
plt.xticks([0,1], ['No Promo', 'Promo'], rotation=0)
plt.tight_layout()
plt.savefig('promo_effect.png')
plt.show()


plt.figure(figsize=(8,6))
sns.heatmap(df.select_dtypes(include=np.number).corr(), 
            annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('correlation.png')
plt.show()

df['day'] = df['date'].dt.day
df['quarter'] = df['date'].dt.quarter
df['is_weekend'] = df['weekday'].apply(lambda x: 1 if x >= 5 else 0)

 
df=df.sort_values('date')
df['lag_1'] = df['sales'].shift(1)
df['rolling_mean_7'] = df['sales'].shift(1).rolling(7).mean()


df = df.dropna()

print("New features added:", ['day','quarter','is_weekend','lag_1','rolling_mean_7'])

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


df_model = pd.get_dummies(df.drop('date', axis=1),columns=['store_id', 'item_id'],drop_first=True)

X = df_model.drop('sales', axis=1)
y = df_model['sales']

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)


mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")

test_indices = X_test.index
df_powerbi = df_original.loc[test_indices].copy()
df_powerbi['Predicted_Sales'] = predictions
df_powerbi['Actual_Sales'] = y_test.values
df_powerbi['Error'] = abs(df_powerbi['Actual_Sales'] - df_powerbi['Predicted_Sales'])

df_powerbi.to_excel('powerbi_output.xlsx', index=False)
print("Exported successfully!")
print(df_powerbi.head())