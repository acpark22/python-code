import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects= ('APPLE', 'FACEBOOK', 'NETFLIX',  'TESLA')
y_pos= np.arange(len(objects))
performance= [12.73, 7.29, 4.94, -0.81]

plt.style.use('seaborn')
plt.barh(y_pos, performance, align= 'center', alpha= 0.5, color= ['red', 'green', 'blue', 'gold'])
plt.yticks(y_pos, objects)
plt.xlabel('EPS/ Trailing Twelve Months')
plt.title('Earnings Per Share Comparisons')

plt.show()

