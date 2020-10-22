import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import os

logfilename = 'nasa_access_log_500k.csv'

print(f"reading file: {logfilename}")
df = pd.read_csv(logfilename, low_memory=False, parse_dates=['timestamp'])

# Question 1. What is the date range for this access log?

print("\nQuestion 1:\n\tcalculate date range")
mindate = min(df['timestamp']).date()
maxdate = max(df['timestamp']).date()
print (f"\tdate range: {mindate} to {maxdate}")

# Question 2. Display a pie chart of in which each pie slice 
# represents a response code and the size of the pie piece is 
# proportionAL to the number of responses with that code.

print("\nQuestion 2: response code pie chart")
vc = df['rcode'].value_counts()
print(f"\nValue Counts for 'rcode':\n{vc}")
vc.plot.pie(figsize=(10,10))
#plt.show()

# Question 3. How many different, unique clients accessed 
# this service?

print("\nQuestion 3: How many different, unique clients accessed this service?")
cc = df['clientloc'].value_counts()
print(f"\nNumber of unique clients:\n{cc.count()}")

# 4. Which client accessed the service the most?
# How many times did that client access the service?
print("\nQuestion 4: Which client accessed the service the most?\n")
print("How many times did that client access the service?")
rows = df['clientloc'].value_counts(sort=True)
print(f"\nName of client and num of times accessed:\n{rows.iloc[[0]]}")

# 5. For the 5 clients with the most requests,
# show a bar chart of how many times each client accessed the service.
print("\nQuestion 5: For the 5 clients with the most requests,\n")
print("show a bar chart of how many times each client accessed the service.")
rows = df['clientloc'].value_counts(sort=True)
tf = rows.iloc[0:5]
tfLocs = [tf.index]
tfFreq = [tf[0:5]]
tf.plot.bar(tfLocs, tfFreq)
plt.ylim(0, 2500)
#plt.show()

# 6. Which resource (which path) was accessed the most?
print("\nQuestion 6: Which resource (which path) was accessed the most?")
rows = df['path'].value_counts(sort=True)
print(f"\nMost accessed path:\n{rows.drop_duplicates()}")

# 7. The first element in the path indicates a resource class. List all of the accessed resource classes.
print("\nQuestion 7: The first element in the path indicates a resource class.\n")
print("List all of the accessed resource classes")
rows = df['path']
resources = set()
for index in rows.items():
    split_path = index[1].split('/')
    resource = split_path[1]
    resources.add(resource)
print("\n".join(resources))

# 8. Display a histogram showing the frequency of access for each resource class.
print ("\nQuestion 8: Display a histogram showing the frequency of access for each resource class.")
rows = df['path']
resources = [] 
for index in rows.items():
    split_path = index[1].split('/')
    resource = split_path[1]
    resources.append(resource)

ser = pd.Series(resources)
rows = ser.value_counts(sort=True)
#print(rows)
#plt.hist(rows)
#plt.show()

# 9. Which day of the week typically had the most requests?
print ("Question 9: Which day of the week typically had the most requests?")
rows = df['timestamp']
days = [] 
for index in rows.items():
    temp = str(index[1])
    day = temp[8:10]
    days.append(day)
ser = pd.Series(days)
week = {"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0,"Monday":0}
rows = ser.value_counts(sort=True)

for index, item in rows.items():
    temp = int(index)
    day = temp % 7
    if (day == 1):
        week["Tuesday"] += item
    if (day == 2):
        week["Wednesday"] += item
    if (day == 3):
        week["Thursday"] += item
    if (day == 4):
        week["Friday"] += item
    if (day == 5):
        week["Saturday"] += item
    if (day == 6):
        week["Sunday"] += item
    if (day == 0):
        week["Monday"] += item
print(week)

# 10. During which hour of the day did the site typically serve the most data?
print('Question 10: During which hour of the day did the site typically serve the most data?')
rows = df['timestamp']
hours = [] 
for index in rows.items():
    temp = str(index[1])
    hour = temp[11:13]
    hours.append(hour)
ser = pd.Series(hours)
ser = ser.value_counts()
print(ser.iloc[[0]])

# 11. What was the availability of this site? 
print('Question 11: What was the availability of this site?')
rows = df['rcode'].value_counts()
total = 0
good_rcode = 0
for index, value in rows.items():
    if index < 400:
        good_rcode += value
    total += value

success_ratio = (good_rcode / total) * 100
print('Availability: ' + str(success_ratio) + '%')

# 12. How many different types of resources were served? 
print('How many different types of resources were served?')
resources = df['path']
extensions = set()
for item, value in resources.items():
    name, extension = os.path.splitext(value)
    extensions.add(extension)
print('Number of resources served: ' + str(len(extensions)))

print('Done')