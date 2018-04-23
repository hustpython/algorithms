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

#print(getn(99))

#方法2：按位数寻找规律
# 分别考虑每一位为1的情况，然后加强来
# 当当前位为m时，要考虑m-1位和m+1位上的数字
# 还要根据m此时的数字，分=0，=1和>1应用不同的公式
# 公式中有一个factor就是不同位的权重
def getnweishu(n):
    count = 0
    factor = 1
    while n//factor != 0:
        LowerNum = n - (n//factor) * factor
        CurrNum = (n//factor) % 10  
        HigherNum = n // (factor*10)
        if CurrNum == 0:
            count += HigherNum * factor
        elif CurrNum == 1:
            count += HigherNum * factor + LowerNum +1
        else:
            count += (HigherNum +1)*factor
        factor *= 10
    return count
print(getnweishu(123))