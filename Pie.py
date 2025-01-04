import pandas as pd
import matplotlib.pyplot as plt

# dark theme
plt.style.use('dark_background')
#import seaborn as sns

df = pd.read_csv('dataset/apple_quality.csv')
df.head()
print(df['Quality'].value_counts())

plt.figure(figsize=(6, 6))
plt.pie(df['Quality'].value_counts(), labels=['good', 'bad'], autopct='%1.1f%%', colors=['red', 'blue'])
plt.legend()
plt.title('Quality')
plt.tight_layout()
plt.show()