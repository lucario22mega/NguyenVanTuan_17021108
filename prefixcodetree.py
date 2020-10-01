class PrefixCodeTree:
    def __init__(self,prefixDict):
        self.prefixDict = {}
    def insert(codeword, symbol):
         sum = 0
         for x in codeword:
                if codeword[x] == 0:
                    sum+=1
                else:
                    sum+=2
         self.prefixDic[sum] = symbol
    def decode(encodedData, datalen) :
            
              
