#User function Template for python3

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,text1,text2):
        dp = [[0 for j in range(y + 1)] for i in range (x+1)] # assigning all 0
        # 1 extra column and 1 extra row
        
        for i in range(len(text1)-1, -1, -1): # traversing in reverse order from bottom
            for j in range(len(text2)-1, -1, -1):
                if text1[i]==text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                    
        return dp[0][0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends
