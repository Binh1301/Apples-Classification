import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import Perceptron
from sklearn.metrics import classification_report, accuracy_score


df = pd.read_csv('dataset/apple_quality.csv')

df = df.dropna()

label_encoder = LabelEncoder()
df['Quality'] = label_encoder.fit_transform(df['Quality'])

X = df.drop('Quality', axis=1)
y = df['Quality']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
perceptron = Perceptron(random_state=42)
perceptron.fit(X_train, y_train)
y_pred = perceptron.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=label_encoder.classes_)
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(report)