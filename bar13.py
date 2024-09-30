import matplotlib.pyplot as plt;
import numpy as np
lanugages = ('Java','Python','PHP','JavaScript','C##','C++')
pop = np.arange(len(lanugages))
performance = [10,7,6,4,2,1]
plt.bar(pop, performance, align='center', alpha=0.5)
plt.xticks(pop,lanugages)
plt.ylabel('Usage')
plt.title('Programming language usage')
plt.show()
