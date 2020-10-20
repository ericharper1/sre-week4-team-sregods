import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

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
plt.show()

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
plt.show()

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
print(resources)

print("Done")
