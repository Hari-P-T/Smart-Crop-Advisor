# Importing Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score

# Load Datasets
crop_data = pd.read_csv('crop_data.csv')
pesticides_data = pd.read_csv('pesticides.csv')

# Preprocessing Crop Data
X = crop_data[['year', 'state', 'district']]  # Feature Matrix
y = crop_data['crop_name']  # Target Variable

# Convert categorical data to numerical data
X = pd.get_dummies(X)

# Splitting Crop Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Building Random Forest Classifier Model
rfc = RandomForestClassifier(random_state=0)

# Hyperparameter Tuning
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30],
    'max_features': ['sqrt', 'log2']
}
grid_search = GridSearchCV(estimator=rfc, param_grid=param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Cross-validation
scores = cross_val_score(grid_search.best_estimator_, X_train, y_train, cv=5)
print("Cross-validation scores:", scores)
print("Mean cross-validation score:", scores.mean())

# Evaluating Model Performance
y_pred = grid_search.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of Random Forest Classifier: {:.2f}%".format(accuracy * 100))

# Predicting Top 3 Crops for User Input
area = 10.0  # Example input
crop_probs = grid_search.predict_proba(pd.DataFrame({'year': [2021], 'state': ['Maharashtra'], 'district': ['Pune'], 'area': [area]}))
top_3_crops = list(crop_probs.argsort()[0][::-1][:3])
print("Top 3 Crops Predicted:", top_3_crops)

# Finding Suitable Pesticides for Top 3 Crops
suitable_pesticides = []
for crop in top_3_crops:
    crop_name = y.unique()[crop]
    pesticides = pesticides_data[pesticides_data['Crop'] == crop_name]['Pesticide'].tolist()
    suitable_pesticides.append(pesticides)

# Flattening List of Suitable Pesticides
suitable_pesticides = [pesticide for sublist in suitable_pesticides for pesticide in sublist]
suitable_pesticides = list(set(suitable_pesticides))

# Printing Suitable Pesticides
print("Suitable Pesticides:")
for pesticide in suitable_pesticides:
    print(pesticide)

# Creating Bar Graph
plt.bar([1, 2, 3], crop_probs[0][top_3_crops], tick_label=top_3_crops)
plt.title("Top 3 Crops Predicted for {} hectares".format(area))
plt.xlabel("Crop Name")
plt.ylabel("Probability")
plt.savefig('images/bar_graph.png')
plt.close()
