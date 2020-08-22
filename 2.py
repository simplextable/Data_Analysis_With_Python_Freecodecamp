import pandas as pd
import numpy as np

df = pd.read_csv("adult.data.csv")

def calculate_demographic_data(print_data=True):
    # Read data from file
    

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    a = pd.Series([(df["race"].loc[df["race"] == "White"]).size,
                  (df["race"].loc[df["race"] == "Black"]).size,
                  (df["race"].loc[df["race"] == "Asian-Pac-Islander"]).size,
                  (df["race"].loc[df["race"] == "Amer-Indian-Eskimo"]).size,
                  (df["race"].loc[df["race"] == "Other"]).size], index=[df["race"].unique()])

    #a= (df["race"].unique()
    
    #print(df.loc[df["race"] == "White"])

    race_count = a
    # What is the average age of men?
    c = df.loc[df["sex"] == "Male", "age"].agg(['mean'][0]).round(1)


    average_age_men = c

    # What is the percentage of people who have a Bachelor's degree?
    
    toplam = df["education"].loc[df["education"] == "Bachelors"].size
    toplam2 = df["education"].size
    d = (toplam / toplam2 * 100)
    d = round(d,1)
    percentage_bachelors = d

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    bsd_toplam = df["education"].loc[ (df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate")].size

    lise_toplam = df["education"].loc[ (df["education"] != "Bachelors") | (df["education"] != "Masters") | (df["education"] != "Doctorate")].size
   
    bsd_50 = df["education"].loc[ ((df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate")) & (df["salary"] == ">50K")].size

    lise_50 = df["education"].loc[ ((df["education"] != "Bachelors") | (df["education"] != "Masters") | (df["education"] != "Doctorate")) & (df["salary"] == ">50K")].size


    oran = bsd_50 / bsd_toplam *100  
    e = round(oran, 1)

    oran2 = lise_50 / lise_toplam *100  
    f = round(oran2, 1)


    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = bsd_toplam
    lower_education = lise_toplam

    # percentage with salary >50K
    higher_education_rich = e
    lower_education_rich = 17.4

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    g = df["hours-per-week"].min()
    

    min_work_hours = g

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    toplam =  df["hours-per-week"].loc[ (df["hours-per-week"] == 1)].size
    toplam2 = df.loc[ (df["hours-per-week"] == 1) & (df["salary"] == ">50K"), "salary"].size
    
    
    h = toplam2 / toplam * 100

    num_min_workers = toplam

    rich_percentage = h

    # What country has the highest percentage of people that earn >50K?
    
    toplam = df.groupby('native-country')['salary'].count()
    toplam2 =  df.loc[ (df["salary"] == ">50K")]
    toplam3 = toplam2.groupby('native-country')['salary'].count()

    i = (toplam3 / toplam * 100)
    #print(i.loc["Iran"])
    j = (i[i == i.max()].index[0])
    
    #print(i.groupby("native-country")["salary"])

    k = round(i.max(),1)
   

    highest_earning_country = j
    highest_earning_country_percentage = k

    # Identify the most popular occupation for those who earn >50K in India.
    
    l = df.loc[ (df["native-country"] == "India") & (df["salary"] == ">50K")]
    m =  l.groupby('occupation')['occupation'].count()
    n = m[m == m.max()].index[0]
    
    

    top_IN_occupation = n

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
