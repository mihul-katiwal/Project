# Import Libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset URL
url = "https://raw.githubusercontent.com/suraj-tiwary18/Data-Science-Journey/refs/heads/main/moviesTMBD.csv"

# Load Dataset
df = pd.read_csv(url)

# Display First 5 Records
print("=" * 50)
print("First 5 Records")
print("=" * 50)
print(df.head())

# Dataset Information
print("\nDataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

# Drop Unnecessary Columns
df.drop(
    ['overview', 'adult', 'title', 'original_language',
     'release_date', 'Unnamed', 'id'],
    axis=1,
    inplace=True,
    errors='ignore'
)

# Remove Missing Values
df.dropna(inplace=True)

# Display Cleaned Data
print("\nCleaned Dataset:")
print(df.head())

# Feature Scaling
scaler = StandardScaler()

df[['popularity', 'vote_average']] = scaler.fit_transform(
    df[['popularity', 'vote_average']]
)

# Features and Target
X = df[['popularity', 'vote_average']]
y = df['vote_count']

# Train-Test Split
x_train, x_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Model Training
model = LinearRegression()
model.fit(x_train, y_train)

# Model Accuracy
score = model.score(x_test, y_test)
print(f"\nModel Accuracy (R² Score): {score:.2f}")

# Prediction
new_data = pd.DataFrame({
    "popularity": [577],
    "vote_average": [4574]
})

# Scale Input Data
new_data[['popularity', 'vote_average']] = scaler.transform(
    new_data[['popularity', 'vote_average']]
)

# Predict
prediction = model.predict(new_data)

print(f"\nPredicted Vote Count: {prediction[0]:.2f}")



fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Heatmap
sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm",
    ax=axes[0, 0]
)
axes[0, 0].set_title("Correlation Heatmap")

# Scatter Plot 1
sns.scatterplot(
    x=df["vote_average"],
    y=df["vote_count"],
    ax=axes[0, 1]
)
axes[0, 1].set_title("Vote Average vs Vote Count")

# Scatter Plot 2
sns.scatterplot(
    x=df["popularity"],
    y=df["vote_count"],
    ax=axes[1, 0]
)
axes[1, 0].set_title("Popularity vs Vote Count")

# Histogram
sns.histplot(
    df["vote_count"],
    kde=True,
    ax=axes[1, 1]
)
axes[1, 1].set_title("Vote Count Distribution")

# Adjust Layout
plt.tight_layout()

# Show All Graphs
plt.show()