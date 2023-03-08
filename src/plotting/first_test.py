#%%
import matplotlib.pyplot as plt
import sys
import numpy as np

sys.path.insert(1, r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\src")

from data_structure import *
# %%
Categories = Category.Categories
y = []
for member in Categories.members:
    y_temp = 0
    for trns in member.members:
        y_temp += trns.value
    y.append(y_temp)

fig, ax = plt.subplots()
x = np.linspace(0, len(Categories.members))
ax.plot( y)

fig2, ax2 = plt.subplots()
monthly_money = []
for member in SpecificMonth.SpecificMonths.members:
    monthly_money.append(member.final_balance)

x2 = np.linspace(0, len(SpecificMonth.SpecificMonths.members))
ax2.plot( monthly_money)

# %%
