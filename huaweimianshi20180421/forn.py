#encoding:utf-8
#题目描述,计算[1,n]中有多少个"1"；
#举例:[1,5]只有一个1:1；
#[1,11]中有1,10,11，三个数中一共有4个1；

#方法1：整体遍历
def getn(n):
  count = 0
  for x in range(1,n+1):
      if str(x).count("1"):
         count += str(x).count("1")
  return count

print(getn(99))

#方法2：按位数寻找规律
# 当n为m位数时，
# 分别考虑有1,2,3...m个1时的情况
# 对于
from itertools import combinations
def getnweishu(n):
    count = 0
    lenn = len(str(n))
    for i in range(1,lenn):
        for j in range(1,i+1):
            combins = len(list(combinations(range(i),j)))
            #print(j*combins*9**(i-j),combins,j)
            count += j*combins*9**(i-j)
    return count
print(getnweishu(1000))