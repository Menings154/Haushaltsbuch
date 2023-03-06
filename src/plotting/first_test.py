#%%
import matplotlib.pyplot as plt
import sys
import numpy as np

sys.path.insert(1, r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\src")

from data_structure import *

Categories = Category.Categories
y = []
for member in Categories.members:
    y_temp = 0
    print(member)
    for trns in member.members:
        print(trns)
        y_temp += trns.value
    y.append(y_temp)
    print(y_temp)

fig, ax = plt.subplots()
x = np.linspace(0, len(Categories.members))
ax.plot( y)


# %%
