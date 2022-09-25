from re import T
from time import daylight
import plotly.express as px
import pandas as pd
import statistics as st
import csv
import plotly.graph_objects as pg

with open('data.csv',newline='') as f:
    r = csv.reader(f)
    savingsData = list(r)

savingsData.pop(0)    

tEntries = len(savingsData)
tReminder = 0

for i in savingsData:
    if int(i[3]) == 1:
        tReminder = tReminder+1

data = pd.read_csv('data.csv')

fig = px.scatter(data, y= "quant_saved" ,color="rem_any")
fig.show()

graph = pg.Figure(pg.Bar(x=['reminded', 'notReminded'], y=[tReminder,(tEntries-tReminder)]))

graph.show()

allSavings = []
for i in savingsData:
    allSavings.append(float(i[0]))
mean = st.mean(allSavings)
median = st.median(allSavings)
mode = st.mode(allSavings)
ST = st.stdev(allSavings)
print(mean)
print(median)
print(mode)
print(ST)

R = []
r = []
for i in savingsData:
    if int(i[3]) == 1:
        R.append(float(i[0]))
    else:
        r.append(float(i[0]))    

Rmean = st.mean(R)
Rmode = st.mode(R)
Rmedian = st.median(R)
rmean = st.mean(r)
rmedian = st.median(r)
rmode = st.mode(r)
RsT = st.stdev(R)
rSt = st.stdev(r)
print(Rmean)
print(Rmode)
print(Rmedian)
print(RsT)
print(rmean)
print(rmedian)
print(rmode)
print(rSt)


