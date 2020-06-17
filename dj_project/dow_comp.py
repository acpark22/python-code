import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'dow_reports2.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, adj_closes, adj_closes1 = [], [], []
    for row in reader:
        current_date  = datetime.strptime(row[0], '%Y-%m-%d')
        adj_close = float(row[5])
        adj_close1 = float(row[11])
        dates.append(current_date)
        adj_closes.append(adj_close)
        adj_closes1.append(adj_close1)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, adj_closes, c = 'red', alpha = 0.5)
ax.plot(dates, adj_closes1, c = 'blue', alpha = 0.5)

ax.set_title("Daily Closing Index, 2019 in blue", fontsize = 18)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Dow Jones", fontsize = 19)
ax.tick_params(axis='both', which='major', labelsize=16)


plt.show()
