import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np

# a single graph
squares = [i**2 for i in range(11)]
print(squares)
fig, ax = plt.subplots()
ax.plot(squares)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('a single plot')
ax.grid(linestyle='--')

# customize x and y ranges
# ax.set_xlim(0, 10)
# ax.set_ylim()

# add ticks
# ax.set_xticks(np.arange(0, 11, 2))
# ax.set_yticks(np.arange(0, 10, 1))


# add minor/major ticks
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(20))
ax.yaxis.set_minor_locator(MultipleLocator(5))


# to save your figure
plt.savefig("myPlot.png")

plt.show()

# two graphs plotted together
x = [i for i in range(6)]
squares5 = [i**2 for i in range(6)]
linear5 = [i for i in range(6)]
y = list(zip(squares5, linear5))
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
# ax.tick_prarams(labelsize=50)
ax.set_title('double plots')
ax.plot(x, squares5, label='squares') 
ax.plot(x, linear5, label='linear')
ax.legend(loc='upper left')
ax.grid(linestyle='--')
plt.show()

# check available styles
# options : ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
# scatter plot
print(plt.style.available)
a1 = [i for i in range(50)]
a2 = [i*2+5 for i in range(50)]
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots()
# ax.scatter(a1,a2,color='red')
ax.scatter(a1,a2,c=a2, cmap=plt.cm.twilight,s=5)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('scatter plot')
ax.grid(linestyle='-')
# options for the linestyle : '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

plt.show()




