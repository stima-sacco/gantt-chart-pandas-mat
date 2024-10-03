import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import date2num

# Load the Excel file
file_path = 'Book4.xlsx'
data = pd.read_excel(file_path)

# Display the data
# print(data.head())

# Convert Start Date to datetime
data['Start Date'] = pd.to_datetime(data['Start Date'])

# Ensure Duration is in numeric form (assuming it's given in days)
data['Duration'] = data['Duration'].apply(lambda x: int(x.split()[0]) if isinstance(x, str) else x)

# Calculate the End Date
data['End Date'] = data['Start Date'] + pd.to_timedelta(data['Duration'], unit='d')

print(data.head())  # Check the data


fig, ax = plt.subplots(figsize=(10, 6))

# Plot each task as a bar
for i, task in data.iterrows():
    ax.barh(task['Task'], date2num(task['End Date']) - date2num(task['Start Date']),
            left=date2num(task['Start Date']), color='skyblue')

# Format the chart
ax.set_xlabel('Dates')
ax.set_ylabel('Tasks')
ax.set_title('Monitoring & Evaluation')
ax.grid(True)

# Format x-axis to show dates
ax.xaxis_date()

# Rotate date labels
plt.xticks(rotation=45, ha='right')

plt.tight_layout()

plt.savefig('gantt_chart3.png')
plt.show(block=True)

