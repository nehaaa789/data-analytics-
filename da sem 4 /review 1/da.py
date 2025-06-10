# data_preprocessing_project.py

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold

# Load dataset (use your dataset or an example like Titanic)
df = pd.read_csv('/Users/nehakumari/Desktop/da sem 4 /students_marks_dataset.csv')  # Replace with your actual CSV file

# 1. Initial Exploration
print("Dataset shape:", df.shape)
print(df.info())
print(df.describe())

# 2. Handling Missing Values
missing_values = df.isnull().sum()
print("Missing values:\n", missing_values)

# Impute numerical values with median
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
imputer = SimpleImputer(strategy='median')
df[num_cols] = imputer.fit_transform(df[num_cols])

# Impute categorical with most frequent
cat_cols = df.select_dtypes(include=['object']).columns
imputer_cat = SimpleImputer(strategy='most_frequent')
df[cat_cols] = imputer_cat.fit_transform(df[cat_cols])

# 3. Handling Outliers (Z-score)
from scipy.stats import zscore
z_scores = np.abs(zscore(df[num_cols]))
df = df[(z_scores < 3).all(axis=1)]

# 4. Feature Selection (Remove low variance features)
selector = VarianceThreshold(threshold=0.01)
df_selected = pd.DataFrame(selector.fit_transform(df[num_cols]), columns=num_cols[selector.get_support()])

# 5. Data Transformation (Standardization)
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df_selected), columns=df_selected.columns)

# 6. Summary Statistics
print("Summary Statistics:\n", df_scaled.describe())

# 7. Visualization
sns.heatmap(df_scaled.corr(), annot=True, fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# Pairplot for selected features
sns.pairplot(df_scaled.iloc[:, :4])  # Only first 4 for readability
plt.suptitle('Pairplot of Features', y=1.02)
plt.show()

# Distribution of target (if available)
# sns.countplot(x='TargetColumn', data=df)  # Uncomment and replace
