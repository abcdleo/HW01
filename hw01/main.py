# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061230.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
result = []
target_station = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
for target in target_station:
   count = 0
   target_data = list(filter(lambda item: item['station_id'] == target, data))
   for item in target_data:
      if float(item['WDSD']) == -99.000 or float(item['WDSD']) == -999.000 :
         del item['WDSD']
      else :
         count = count + 1
         Max_WDSD = item
         min_WDSD = item
   if count < 2 :
      result.append([target, 'None'])
   else :
      for curr_WDSD in target_data:
         if 'WDSD' in curr_WDSD.keys():
            if curr_WDSD['WDSD'] > Max_WDSD['WDSD']:
               Max_WDSD = curr_WDSD
            if curr_WDSD['WDSD'] < min_WDSD['WDSD']:
               min_WDSD = curr_WDSD
      result.append([target, float(Max_WDSD['WDSD']) - float(min_WDSD['WDSD'])])
# =======================================

# Part. 4
# =======================================
# Print result
print(result)
#========================================