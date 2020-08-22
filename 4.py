import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df["height_m"]   = df["height"] / 100
df["IBM"]        = df["weight"] /  ( df["height_m"] * df["height_m"] )
df["overweight"] = (df["IBM"] > 25) == 1 
df["overweight"] = df["overweight"].astype(int)

# cholesterol,gluc
df["cholesterol_bin"] = df["cholesterol"] > 1
df["cholesterol"]     =df["cholesterol_bin"].astype(int)

df["gluc_bin"] = df["gluc"] > 1
df["gluc"]     = df["gluc_bin"].astype(int)





# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    
    plot_melt = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol',   'gluc', 'smoke', 'alco', 'active','overweight'])
    plot_melt.head()


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    fig = sns.catplot(x="variable", y=None, col="cardio",                                       hue="value",
                             data=plot_melt, saturation=.5,
                             kind="count", ci=None, aspect=.6)
    #plt.show()
    # Draw the catplot with 'sns.catplot()'

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df = pd.read_csv("medical_examination.csv")
    
    df = df[df['ap_lo'] <= df['ap_hi']]
    

    df      = df[(df['height'] >= df['height'].quantile(0.025))]
    df      = df[(df['height'] <= df['height'].quantile(0.975))]
    df      = df[(df['height'] >= df['height'].quantile(0.025))]
    df_heat = df[(df['height'] <= df['height'].quantile(0.975))]


    

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=np.bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
    fig = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3,                 center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
    


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
