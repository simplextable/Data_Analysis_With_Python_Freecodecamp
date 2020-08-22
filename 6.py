import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy import stats


df = pd.read_csv("epa-sea-level.csv")

df.head()

def draw_plot():
    # Read data from file
    
    
    # Create scatter plot
    slope, intercept, r_value, p_value, std_err = stats.linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    print("slope: %f    intercept: %f" % (slope, intercept))
    
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], )
    plt.plot(df["Year"], intercept + slope*df["Year"], 'r', label='fitted line')
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    

    # Create first line of best fit
    df1 = df["Year"].copy()
    temp = range(2014, 2051)

    df1 = df1.append(temp)
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], )
    plt.plot(df1, intercept + slope*df1, 'r', label='fitted line')
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    

    # Create second line of best fit
    df2 = df[df["Year"] >= 2000] 

    slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
    print("slope2: %f    intercept2: %f" % (slope2, intercept2))

    df3 = df1[df1>=2000]

    plt.scatter(df2["Year"], df2["CSIRO Adjusted Sea Level"], )
    plt.plot(df3, intercept2 + slope2*df3, 'r', label='fitted line')
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()