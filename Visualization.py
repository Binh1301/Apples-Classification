import pandas as pd
import matplotlib.pyplot as plt

#dark theme
plt.style.use('dark_background')
import seaborn as sns
df = pd.read_csv('dataset/apple_quality.csv')
df.head()
cols = df.columns[:-1]
colors = sns.color_palette('husl', len(cols))  # husl = hue saturation lightness

fig, axs = plt.subplots(nrows=4, ncols=2, figsize=(15, 15))  # 3 rows, 3 columns
axs = axs.flatten()  # flatten the 2D array to 1D array

for i, col in enumerate(cols):
    sns.kdeplot(df[col], ax=axs[i], color=colors[i])  # kdeplot = kernel density estimation plot
    sns.histplot(df[col], ax=axs[i], color=colors[i], stat='density')  # histplot = histogram plot
    sns.rugplot(df[col], ax=axs[i],
                color=colors[i])  # rugplot = draw a dash mark for every point on a univariate distribution

    axs[i].set_xlabel('')  # remove x label to avoid redundancy
    axs[i].set_title(col)
    plt.tight_layout()

fig.suptitle("Distribution of Variables", fontsize=14)
fig.delaxes(ax=axs[len(cols)])  # delete the last plot
fig.tight_layout()
df.describe().T