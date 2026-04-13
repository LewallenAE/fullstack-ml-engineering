# Train and run a linear model
import matplotlib.pyplot as plt
import numpy as  np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor

# Download  and prepare data
data_root = "https://raw.githubusercontent.com/ageron/data/main/"
lifesat= pd.read_csv(data_root + "lifesat/lifesat_full.csv")
print(lifesat.columns.tolist())
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

# Visualize the data
lifesat.plot(kind='scatter', grid=True,
             x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()

# Select a linear model
model = KNeighborsRegressor(n_neighbors=3)


# Train the model
model.fit(X, y)

# Make a prediction for Puerto Rico
X_new = [[33_442.8]]  # Puerto Rico's GDP per capita in 2020
print(model.predict(X_new)) # print the outputs.
print(lifesat.columns.tolist())
