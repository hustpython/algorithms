class solution():
   def __init__(self,inputstr):
        self.inputstr = inputstr 
        self.count = 0
        while not self.huaweijudge():
            self.getsamechar()
        self.getres()
   def getres(self):
       return self.count
   def getsamechar(self):
        flag = 0
        templen = 0
        tempstr = ""
        kk = 0
        for i in range(len(self.inputstr)):
            for j in range(len(self.inputstr)-1,i,-1):
                if self.inputstr[i] == self.inputstr[j]:  
                    #print(i,j,len(self.inputstr),self.inputstr)
                    if len(self.inputstr[i+1:j]) > templen:
                       kk = i + len(self.inputstr)- 1 - j
                       templen = len(self.inputstr[i+1:j])
                       tempstr =  self.inputstr[i+1:j] 
                    flag = 1  
        if flag:
            self.count += kk
            self.inputstr = tempstr 
        if not flag:
            self.count += len(self.inputstr)
            self.inputstr = []
            return              
   def  huaweijudge(self):
        return self.inputstr == self.inputstr[::-1]
huiwenclass = solution('abcdefedgggggggggggdddddggggggggggggggggggggggggdfffffffffffffffa')
print(huiwenclass.getres())
