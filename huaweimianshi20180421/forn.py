#encoding:utf-8
#��Ŀ����,����[1,n]���ж��ٸ�"1"��
#����:[1,5]ֻ��һ��1:1��
#[1,11]����1,10,11����������һ����4��1��

#����1���������
def getn(n):
  count = 0
  for x in range(1,n+1):
      if str(x).count("1"):
         count += str(x).count("1")
  return count

print(getn(99))

#����2����λ��Ѱ�ҹ���
# ��nΪmλ��ʱ��
# �ֱ�����1,2,3...m��1ʱ�����
# ����
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