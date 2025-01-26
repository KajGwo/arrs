###
# The weather station report
#
temperatures = [
 3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
 4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
 -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

# number of mesaurements
mesaurements = len(temperatures)

# calculates average temperature
temp_total = 0
for temp in temperatures:
   temp_total = temp_total + temp
avg_temp = temp_total / len(temperatures)

# calculates min and max temperatures
min_temp = min(temperatures)
max_temp = max(temperatures)

# calculates number of days with negative temp
negative_temp = 0
i = 0
y = -1
while i < len(temperatures): 
   if (temperatures[y]) < 0:
      negative_temp = negative_temp + 1
   i = i + 1
   y = y + 1
   
# prints out month report
...
...
...

print("Temp report for march ")
print("num of days under 0 ",negative_temp)
print("min temp",min_temp)
print("max temp",max_temp)
print("avg temp",avg_temp)
print("num of days",mesaurements)
