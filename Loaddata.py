import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#dark theme
plt.style.use('dark_background')
import seaborn as sns
df = pd.read_csv('dataset/apple_quality.csv')
df.head()