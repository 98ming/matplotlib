import matplotlib.pyplot as plt

from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='Songti.ttc', size=16)
#皮质醇折线图
x1 = [1,2,3,4,5]
mean_1 = [5.4204,6.9252,7.0065,6.5674,5.0422]
std_1 = [2.53147,5.45226,5.47435,3.59677,2.48489]
std_1 = [i/5 for i in std_1]
mean_2 = [8.0643,9.7917,11.0552,15.12,10.663]
std_2 = [5.48248,6.5271,6.9393,9.20591,7.37169]
std_2 = [i/5 for i in std_2]

#折线图
figsize = (7, 5)
fig, ax = plt.subplots(figsize = figsize)
#fig,ax = plt.figure(figsize = figsize)
#ax.plot(x, y_1, label = 'first_giant_component', color = 'blue') 
# ax.errorbar( x1, mean_1, yerr = std_1, fillstyle = 'full',
#         fmt = 'o-',ecolor = 'C1',color = 'C0', elinewidth = 2, capsize = 5, ms = 5 )
# ax.errorbar( x1, mean_2, yerr = std_2, fillstyle = 'full',
#         fmt = 'o-',ecolor = 'C1',color = 'C0', elinewidth = 2, capsize = 5, ms = 5 )
# ax.plot(x1, mean_1, marker='o',label = '第一组')
# ax.plot(x1, mean_2,  marker='*',ms=10,label = '第二组')
ax.errorbar(x1, mean_1, label='控制组', yerr=std_1, fmt='-o', ecolor='lightseagreen', color='lightseagreen', elinewidth=2, capsize=4, marker='o')
ax.errorbar(x1, mean_2, label='应激组', yerr=std_2, fmt=':o', ecolor='crimson', color='crimson',elinewidth=2, capsize=4, marker='*')

ax.set_xticks([1, 2, 3, 4, 5])
ax.set_yticks([5,  7, 9, 11, 13, 15])
#ax.set_yticks([4,  8, 12, 16])
plt.ylabel('皮质醇浓度（L/lomn）', fontproperties=my_font, fontsize=13)

ax.set_xticklabels(['Time1', 'Time2', 'Time3', 'Time4', 'Time5'] , fontsize = 10)
ax.set_yticklabels([5,  7, 9, 11, 13, 15], fontsize = 10)
#ax.set_yticklabels([4,  8, 12, 16], fontsize = 20)

# ax.set_title("皮质醇变化情况",fontproperties = my_font,fontsize = 25)
plt.legend(loc='best', prop = my_font)
