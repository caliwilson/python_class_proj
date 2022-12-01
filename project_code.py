#Final Project Python Class
import numpy as np
import pandas as pd


df = pd.read_csv('class_proj/proj_data/merged_foraging_data.csv')
print(df)

##Explore the data
df.groupby('foraging_type').describe()

#What's the average bird density for each group (provisioned vs non_provisioned?)
df.groupby('foraging_type').mean()

#What about avergae bird density for each site? 
df.groupby('site').mean()

#What if we group by site and foraging type?
df.groupby(['site', 'foraging_type']).mean()

#How many observations are there in each group? 
obs_ft = df.groupby("foraging_type")
obs_ft.count()

obs_site = df.groupby("site")
obs_site.count()

obs_ft_site = df.groupby(["site", "foraging_type"])
obs_ft_site.count()

#Make a boxplot of data
#import matplotlib as mpl
import matplotlib.pyplot as plt 

#Histogram of all data (not grouped)
plt.hist(df["avg_count"])
plt.grid(False) #remove gridlines 
plt.title("Histogram of Ibis Densities")
plt.xlabel("Average 1m Density (birds / $\mathregular{m^2}$)")
plt.ylabel("Frequency")
plt.show()

#2 separate histograms by group
df['avg_count'].hist(by=df['foraging_type'], edgecolor='black')
plt.title("Histogram of Ibis Densities")
plt.xlabel("Average 1m Density (birds / $\mathregular{m^2}$)")
plt.ylabel("Frequency")

#Plot histograms by group using one plot
#define avg_count values by group
A = df.loc[df['foraging_type'] == 'not provisioned', 'avg_count']
B = df.loc[df['foraging_type'] == 'provisioned', 'avg_count']

#add 2 histograms to one plot
plt.hist(A, alpha=0.5, label='Not Provisioned')
plt.hist(B, alpha=0.5, label='Provisioned')

#add plot title and axis labels
plt.title("Histogram of Ibis Densities")
plt.xlabel("Average 1m Density (birds / $\mathregular{m^2}$)")
plt.ylabel("Frequency")

plt.legend(title='Foraging Type')#add legend
plt.show()#display plot

#Boxplot grouped by foraging type
df_bplt2 = df.boxplot(column = 'avg_count',by='foraging_type') #uses pandas boxplot method 
df_bplt2.plot()
plt.grid(False)#remove gridlines 
plt.title('Distribution of birds within 1m of focal individual')
plt.xlabel("Foraging Type")
plt.ylabel("Average 1m Density (birds / $\mathregular{m^2}$)")
plt.show()

#Dot-boxplot grouped by foraging type 


numBoxes = len(pd.unique(df.foraging_type))
df.boxplot(column = 'avg_count',by='foraging_type') 
for i in range[numBoxes]:
    y = data[i]
    x = np.random.normal(1+i, 0.04, size=len(y))
    plt.plot(x, y, 'r.', alpha=0.2)

numBoxes = len(pd.unique(df.foraging_type))
df.boxplot(column = 'avg_count',by='foraging_type') 
for i in numBoxes:
    y = data[i]
    x = np.random.normal(1+i, 0.04, size=len(y))
    plt.plot(x, y, 'r.', alpha=0.2)

numBoxes = len(pd.unique(df.foraging_type))
df.boxplot(column = 'avg_count',by='foraging_type') 
for i in numBoxes:
    y = data[i]
    x = np.random.normal(1+i, 0.04, size=len(y))
    plt.plot(x, y, 'r.', alpha=0.2)