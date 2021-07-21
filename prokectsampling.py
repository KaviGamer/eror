import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as fg
import statistics
import csv
import random

df = pd.read_csv('medium_data.csv')
data = df["id"].tolist()

population_mean = statistics.mean(data)
stdev = statistics.stdev(data)

def random_set_of_mean(counter):
    sampledata = []
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        sampledata.append(data[random_index])
    mean1 = statistics.mean(sampledata)
    stdev1 = statistics.stdev(sampledata)
    return mean1

def setup():
    mean_list = []
    for i in range(0,30):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
        print(set_of_means)

    mean = statistics.mean(mean_list)
    print(mean)
    df = mean_list
    fig = ff.create_distplot([df],["id"]),show_hist=False)
    fig.show()

setup()