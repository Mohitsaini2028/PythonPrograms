class Solution:
    def minPartitions(self, n: str) -> int:
        maximum = 0;
        for i in n:
            maximum = max(maximum, ord(i)-ord('0'))
                             
        return maximum

  
