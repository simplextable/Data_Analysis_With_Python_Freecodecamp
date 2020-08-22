import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from matplotlib.dates import DateFormatter
import datetime as dt
import matplotlib.dates as mdates


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")#, index_col= ["date"],  , parse_dates= ["date"] )



# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025))]
df = df[(df['value'] <= df['value'].quantile(0.975))]


df.date=pd.to_datetime(df.date)




def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots(figsize=(8, 5))
    fig = sns.lineplot(df["date"], df["value"] , data=df)
    fig.set(xlabel= "Date", ylabel= "Page Views", title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    
    plt.xlabel ('Years')
    plt.ylabel ('Avarage Page Views')
    #fig.savefig orjinaliydi. biz araya bir de figure ekledik. 
    # Save image and return fig (don't change this part)
    fig.figure.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot

    df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates= ["date"] )
    df_parse = df.groupby(df["date"].dt.strftime('%m-%Y'))[['value']].sum()
    df_parse.index = pd.to_datetime(df_parse.index)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.bar(df_parse.index.date, df_parse['value'], width=5, align='center')
    
    # Draw bar plot





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    #df_box = df.copy()
    #df_box.reset_index(inplace=True)
    #df_box['year'] = [d.year for d in df_box.date]
    #df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_parse = df.groupby(df["date"].dt.strftime('%m-%Y'))[['value']].sum()
    df_parse.index = pd.to_datetime(df_parse.index)

    df_parse.index = pd.to_datetime(df_parse.index, format = '%Y').strftime('%Y')
    sns.set(style="ticks", palette="pastel")

    # Draw a nested boxplot to show bills by day and time
    sns.boxplot(df_parse.index, y=df_parse["value"],
                
                data=df_parse)
    sns.despine(offset=10, trim=True)


    df1 = pd.read_csv("fcc-forum-pageviews.csv",parse_dates= ["date"] )
    df_parse = df.groupby(df1["date"].dt.strftime('%m-%Y'))[['value']].sum()
    df_parse.index = pd.to_datetime(df_parse.index)
    df_parse.index = pd.to_datetime(df_parse.index, format = '%b').strftime('%b')
    sns.set(style="ticks", palette="pastel")

    # Draw a nested boxplot to show bills by day and time
    sns.boxplot(df_parse.index, y=df_parse["value"],
                
                data=df_parse)
    sns.despine(offset=10, trim=True)

    fig = plt.show()




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
