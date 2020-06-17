import matplotlib 
import matplotlib.pyplot as plt
import numpy as np

labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
means1 = [24158, 25606, 25747, 26410, 25757, 25468]
means2 = [28880, 28519, 22637, 23293, 24271, 26532]

x = np.arange(len(labels))
width = 0.49

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, means1, width, label='2019')
rects2 = ax.bar(x + width/2, means2, width, label='2020')

ax.set_ylabel('Dow Jones')
ax.set_title('Average Daily Closing Prices')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3), 
                textcoords="offset points",
                ha= 'center', va= 'bottom')

autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.show()


