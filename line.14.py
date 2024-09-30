import matplotlib.pyplot as plt
import numpy as np
temp=np.array([12,14,16,18,20,22,24])
sales=np.array([100,200,250,400,300,400,500])
plt.xlabel('Temperature')

plt.ylabel('Sales')

plt.title('Tempertaure and sales graph')

plt.plot(temp,sales)

plt.show()
