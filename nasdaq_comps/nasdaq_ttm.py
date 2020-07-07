import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename= 'nasdaq_perf_ttm.csv'
with open(filename) as f:
    reader= csv.reader(f)
    header_row= next(reader)

    dates, adj_closes, adj_closesa, adj_closesb, adj_closesc= [], [], [], [], []
    for row in reader:
        current_date= datetime.strptime(row[0], '%Y-%m-%d')
        adj_close= float(row[5])
        adj_closea= float(row[11])
        adj_closeb= float(row[17])
        adj_closec= float(row[23])
        dates.append(current_date)
        adj_closes.append(adj_close)
        adj_closesa.append(adj_closea)
        adj_closesb.append(adj_closeb)
        adj_closesc.append(adj_closec)

plt.style.use('seaborn')
fig, ax= plt.subplots()
ax.plot(dates, adj_closes, c= 'red', alpha= 0.5, label= 'APPLE')
ax.plot(dates, adj_closesa, c= 'blue', alpha= 0.5, label= 'NETFLIX')
ax.plot(dates, adj_closesb, c= 'green', alpha= 0.5, label= 'FACEBOOK')
ax.plot(dates, adj_closesc, c= 'gold', alpha= 0.5, label= 'TESLA')

ax.set_title("NASDAQ", fontsize= 18)
ax.set_xlabel("Trailing Twelve Months", fontsize= 13)
fig.autofmt_xdate()
ax.set_ylabel("Price", fontsize= 19)
ax.tick_params(axis= 'both', which= 'major', labelsize= 16)

plt.legend()
plt.show()












