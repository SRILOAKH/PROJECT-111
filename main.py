import pandas as pd
import csv
import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
df=pd.read_csv("data.csv")
data=df["Math_score"].tolist()
mean1=statistics.mean(data)
std_deviation1=statistics.stdev(data)
fig=ff.create_distplot([data],["Math_score"],show_hist=True)
fig.show()
print(mean1)
print(std_deviation1)
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
     random_index=random.randint(0,len(data)-1)
     values=data[random_index]
     dataset.append(values)
    mean=statistics.mean(dataset)
    return mean
mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)
mean=statistics.mean(mean_list)
std_deviation=statistics.stdev(mean_list)
print(mean)
print(std_deviation)
first_stdev_start,first_stdev_end=mean-std_deviation,mean+std_deviation
second_stdev_start,second_stdev_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_stdev_start,third_stdev_end=mean-(3*std_deviation),mean+(3*std_deviation)

df=pd.read_csv("data1.csv")
data=df["Math_score"].tolist()
mean2=statistics.mean(data)
fig=ff.create_distplot([mean_list],["Math_score"],show_hist=True)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean2, mean2], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.17], mode="lines", name="first_stdev_end"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="second_stdev_end"))
fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.17], mode="lines", name="third_stdev_end"))
fig.show()

df=pd.read_csv("data2.csv")
data=df["Math_score"].tolist()
mean3=statistics.mean(data)
fig=ff.create_distplot([mean_list],["Math_score"],show_hist=True)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean3, mean3], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.17], mode="lines", name="first_stdev_end"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="second_stdev_end"))
fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.17], mode="lines", name="third_stdev_end"))
fig.show()

df=pd.read_csv("data3.csv")
data=df["Math_score"].tolist()
mean4=statistics.mean(data)
fig=ff.create_distplot([mean_list],["Math_score"],show_hist=True)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean4, mean4], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.17], mode="lines", name="first_stdev_end"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="second_stdev_end"))
fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.17], mode="lines", name="third_stdev_end"))
fig.show()