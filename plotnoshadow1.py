# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure(num=3,figsize=(8,5))
l1=plt.plot(x,y2)
l2=plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

plt.legend(labels=['up','down'],shadow=True,loc='best').get_frame().set_alpha(1)
#legend.get_frame().set_facecolor('white')
#plt.legend().get_frame().set_alpha(1) # 设置shadow内无阴影

plt.xlabel('x')
plt.ylabel('y')

plt.xlim((-1,2))
plt.ylim((-2,3))

new_ticks=np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],
          [r'$really\ bad$',r'$bad$',r'$normal$',r'$good$',r'$really\ good$'])

ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
plt.savefig("a.svg")
plt.show()

