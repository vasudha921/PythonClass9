import pandas as pd
import csv
import plotly.express as px
df = pd.read_csv("class1.csv")
fig = px.scatter(df, x = "Student Number", y = "Marks", title = "Class 1 marks")

with open("class1.csv", newline= "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
newData = []
totalmarks = 0
for i in file_data:
     totalmarks += float(i[1])

n = len(file_data)
 

 
  

mean = totalmarks/n
print(mean)    

fig.update_layout(shapes= [
    dict(
        type = 'line', y0 = mean, y1 = mean, x0 = 0, x1 = n
    )
])
fig.update_yaxes(rangemode = "tozero")
fig.show()