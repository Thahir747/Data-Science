import matplotlib.pyplot as plt

x = [1, 6, 2, 18]
y = [3, 12, 10, 20]


plt.plot(x, y, color='red',linestyle="--",markerfacecolor="green",marker="o")


plt.title('Diagram')
plt.xlabel('X axis')
plt.ylabel('Y axis')


plt.show()

