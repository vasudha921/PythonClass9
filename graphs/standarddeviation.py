import csv
import math 
with open ("data.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

    data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)

    mean = total/n
    return(mean)

#squaring and getting the values
squared_list = []
for x in data:
    a = int(x) - mean(data)
    a = a**2
    squared_list.append(a)

# getting the sum
sum = 0 
for x in squared_list:
    sum = sum + x

#dividing the sum by the total values
result = sum/ (len(data) - 1 )

# getting the deviation by taking the square root of the result
standard_deviation = math.sqrt(result)

print(standard_deviation)
