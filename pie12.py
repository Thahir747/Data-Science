import matplotlib.pyplot as plt
languages = 'Java', 'Python', 'PHP','JavaScript', 'C#', 'C++' 
popularity = 22.2,17.6,8.8,8,7.7,6.7
colors="red","green","yellow","blue","black","pink"
plt.pie(popularity, labels=languages,colors=colors,autopct='%2.2f%%')
plt.axis('equal')


plt.show()
