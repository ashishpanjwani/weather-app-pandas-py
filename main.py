# with open('weather_data.csv') as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv('weather_data.csv')
# # print(data)
# # print(data['temp'])
# data_dict = data.to_dict(orient='list')
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# # sum_var = sum(temp_list)
# # avg = sum_var / len(temp_list)
# # print(f"Average: {avg}")
# # or
#
# print(data['temp'].mean())
# print(f"Max {data['temp'].max()}")
#
# # Get Data in Columns
# print(data['condition'])
# print(data.condition)
#
# # Get Data in Row
# print(data[data.day == 'Monday'])
#
# # Get the row having maximum temperature
# print(data[data.temp == data.temp.max()])
#
# Get specific data based on a certain data from another column in the same row
monday = data[data.day == 'Monday']
print(monday)
print(monday.condition)
print((monday.temp * 9 / 5) + 32)

# Create DataFrame from Scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# # print(data1)
# data.to_csv("new_data.csv")
# Without Index
# data.to_csv("new_data.csv", index=False)
