import matplotlib
import matplotlib.pyplot as plt
import numpy as np

years= ['TTM', '2019', '2018', '2017', '2016']
revenues= [267.98, 260.17, 265.60, 229.23, 215.64]
earnings= [57.22, 55.26, 59.53, 48.35, 45.69]

x= np.arange(len(years))
width= 0.35

plt.style.use('seaborn')
fig, ax= plt.subplots()
rects1= ax.bar(x - width/2, revenues, width, label= 'Revenue')
rects2= ax.bar(x + width/2, earnings, width, label= 'Earnings')

ax.set_ylabel('USD in Billions')
ax.set_title("Apple's Annual Revenue and Earnings Report")
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()

fig.tight_layout()
plt.show()

