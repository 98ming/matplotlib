import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib notebook
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='Songti.ttc', size=20)
xing_wei_list = [[-4.53, 57.50], [43.54, -22.64], [51.67, -105.10]]
xing_wei_df = pd.DataFrame(xing_wei_list, columns=['应激组', '控制组'])
ying_ji = xing_wei_df['应激组']
kong_zhi = xing_wei_df['控制组']

ind = np.arange(3)  # the x locations for the groups
width = 0.25  # the width of the bars

figsize = (12, 7)
fig, ax = plt.subplots(figsize=figsize)
SD_yingji = [30.65, 40.37, 37.39]
SD_kongzhi = [40.51, 47.38, 36.96]
# print(ying_ji)
# SD_yingji.append(np.abs(ying_ji-mean_yingji))
rects1 = ax.bar(ind - width / 2, ying_ji, width, color='crimson', label='应激组', yerr=SD_yingji,
                error_kw={'ecolor': '0.2', 'capsize': 6}, )
rects2 = ax.bar(ind + width / 2, kong_zhi, width, color='lightseagreen', label='控制组', yerr=SD_kongzhi,
                error_kw={'ecolor': '0.2', 'capsize': 6}, )

plt.xticks(ind, ('Happy-Neutral', 'Disgust-Neutral', 'Sad-Neutral',), fontproperties=my_font, fontsize=16)
# ax.set_yticks([0, 200, 400, 600, 800])
plt.ylim((-150, 150))
plt.ylabel('总注视时间偏向分数（ms）', fontproperties=my_font, fontsize=13)

# ax.set_yticklabels([0, 200, 400, 600, 800], fontsize=20)
# ax.set_title("行为数据结果", fontproperties=my_font, fontsize=20)
# plt.errorbar( by_hour.index, by_hour['mean'], yerr = by_hour['std'], fillstyle = 'full',
#         fmt = 'o-',ecolor = 'C1',color = 'C0', elinewidth = 2, capsize = 5, ms = 5 )
plt.legend(loc='best', prop=my_font)
# ax.legend()
ax = plt.gca()
# 设置 上框架和 右框架为 空
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 设置 x轴 为 下框架
ax.xaxis.set_ticks_position('bottom')
# ax.axis["bottom"].label.set_pad(0)
# 设置 y轴 为 左框架
ax.yaxis.set_ticks_position('left')

# 设置 x 轴的位置为 y轴 0的位置
ax.spines['bottom'].set_position(('data', 0))  # outward,axes
# 设置 y 轴的位置为 x轴 0的位置
ax.spines['left'].set_position(('data', -0.38))
plt.show()
