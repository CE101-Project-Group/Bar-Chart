"""
A program that charts the
relationship between house price
and the size of the house
created by Connor W
date created 28/11/18
modified 29/11/18
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
house_price = ("1000","1250","1500","1750")
y_pos = np.arange(len(house_price))
house_size = [75000,100000,125000,50000]

fig, ax1 = plt.subplots()

plt.bar(y_pos, house_size, align='center', alpha=0.5, color='r')
plt.xticks(y_pos, house_price)
plt.ylabel('House Size')
plt.xlabel("House Price")
plt.title('House Price Against House Size')

fig.tight_layout()
plt.show()
