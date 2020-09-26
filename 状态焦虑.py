import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='Songti.ttc', size=20)

# 皮质醇折线图
x1 = [1, 2, 3, 4, 5]
mean_1 = [38.7391, 37.1739, 37.6957, 41.0435, 36.5652]
std_1 = [8.08038, 7.32773, 6.92449, 8.61541, 5.98351]
std_1 = [i/5 for i in std_1]
mean_2 = [36.3043, 35.4348, 41.5652, 40.3043, 37.7826]
std_2 = [5.84213, 5.41736, 9.26786, 7.31396, 9.8947]
std_2 = [i/5 for i in std_2]



# 折线图
figsize = (7, 5)
fig, ax = plt.subplots(figsize=figsize)
# fig,ax = plt.figure(figsize = figsize)
# ax.plot(x, y_1, label = 'first_giant_component', color = 'blue')
# ax.errorbar( x1, mean_1, yerr = std_1, fillstyle = 'full',
#         fmt = 'o-',ecolor = 'C1',color = 'C0', elinewidth = 2, capsize = 5, ms = 5 )
# ax.errorbar( x1, mean_2, yerr = std_2, fillstyle = 'full',
#         fmt = 'o-',ecolor = 'C1',color = 'C0', elinewidth = 2, capsize = 5, ms = 5 )
ax.errorbar(x1, mean_1, label='控制组', yerr=std_1, fmt='-o', ecolor='lightseagreen', color='lightseagreen', elinewidth=2, capsize=4, marker='o')
ax.errorbar(x1, mean_2, label='应激组', yerr=std_2, fmt=':o', ecolor='crimson', color='crimson',elinewidth=2, capsize=4, marker='*')

ax.set_xticks([1, 2, 3, 4, 5])
# print(np.linspace(30,44,2))
# ax.set_yticks([30, 32, 34, 36, 38, 40, 42, 44])
# ax.set_yticks([4,  8, 12, 16])
plt.ylim(32,47)
plt.ylabel('状态焦虑分数（分）', fontproperties=my_font, fontsize=13)
ax.set_xticklabels(['Time1', 'Time2', 'Time3', 'Time4', 'Time5'], fontsize=10)
# ax.set_yticklabels([5,  7, 9, 11, 13, 15], fontsize = 16)
# ax.set_yticklabels([30, 32, 34, 36, 38, 40, 42, 44], fontsize=10)

# ax.set_title("状态焦虑分数", fontproperties=my_font, fontsize=20)
fig.legend(loc=1, prop=my_font, bbox_to_anchor=(1, 1), bbox_transform=ax.transAxes)
