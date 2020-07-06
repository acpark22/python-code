import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename= 'stock_perf_2020.csv'
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
ax.plot(dates, adj_closes, c= 'red', alpha= 0.5, label= 'TESLA')
ax.plot(dates, adj_closesa, c= 'blue', alpha= 0.5, label= 'AMAZON')
ax.plot(dates, adj_closesb, c= 'green', alpha= 0.5, label= 'SEABOARD')
ax.plot(dates, adj_closesc, c= 'orange', alpha= 0.5, label= 'BOOKING')

ax.set_title("2020 Year to Date Stock Performance", fontsize= 18)
ax.set_xlabel('', fontsize= 16)
fig.autofmt_xdate()
ax.set_ylabel("Stock Price", fontsize= 19)
ax.tick_params(axis= 'both', which= 'major', labelsize= 16)

plt.legend()
plt.show()












