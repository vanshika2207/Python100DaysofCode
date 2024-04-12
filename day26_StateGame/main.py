# with open('weather_data.csv') as my_data:
#     data=my_data.readlines()
#     print(data)
# import csv
import numpy as np
# with open('weather_data.csv') as data_file:
#     data=csv.reader(data_file)
#     for row in data:
#         print(row)

# with open('weather_data.csv') as data_file:
#     temperature=csv.reader(data_file)
#     for row in temperature:
#         print(row[1])

import pandas

# data = pandas.read_csv('weather_data.csv')
# print(data)
# print(type(data))
# print(data['temp'])
# print(type(data['temp']))
# print(data.to_dict())
# print(data['temp'].to_list())
# print(sum(data['temp'])/len(data['temp']))

# print(data['temp'].mean())
# print(data['temp'].median())
# print(data['temp'].max())

# print(data.condition)
# print(data[data.day=='Monday'])
# print(data[data['day']=='Monday'])
# print(data[data.temp==data.temp.max()])

# data_dict={
#     'student':['Amy','Jckson','Michael']
#     ,'scores':[78,98,90]
# }
# data=pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')

# monday=data[data.day=='Monday']
#print(monday.condition)
# monday_temp=monday.temp[0]
# monday_temp_F=monday_temp+9/5+32
# print(monday_temp_F)

data=pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrels_count=len(data[data['Primary Fur Color']=='Gray'])
red_squirrels_count=len(data[data['Primary Fur Color']=='Cinnamon'])
black_squirrels_count=len(data[data['Primary Fur Color']=='Black'])
data_dict={'Fur Color':['Gray','Red','Black'],'Count':[gray_squirrels_count,red_squirrels_count,black_squirrels_count]}
data_new=pandas.DataFrame(data_dict)
print(data_new)
data_new.to_csv('data_new.csv')
