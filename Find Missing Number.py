class Solution:
    def MissingNumber(self,array,n):
        
        sum_no = 0
        mahaNumber = n*(n+1)//2
        for i in array:
            sum_no += i 

        return (mahaNumber - sum_no)
    
t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)

