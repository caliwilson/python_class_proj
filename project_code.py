#Final Project Python Class

import numpy

import pandas as pd

df = pd.read_csv('proj_data/merged_foraging_data.csv')
print(df)

##Explore the data

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
import matplotlib.pyplot as plt 

plt.hist(df["avg_count"])
plt.show()


df_bplt2 = df.boxplot(column = 'avg_count',by='foraging_type') #uses pandas boxplot method 
df_bplt2.plot()
plt.title('Distribution of birds within 1m of focal individual')
plt.show()

