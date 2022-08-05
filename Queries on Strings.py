class Solution:
	def SolveQueris(self, str, Query):
	    ans = []
	    for element in Query:
	        temp = str[(element[0]-1):element[1]]
	        dicti = {}
	        count = 0
	        for i in temp:
	            if not i in dicti:
	                count += 1
	                dicti[i]=1
	        
	        ans.append(count) 
	        
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		q = int(input())
		Query = []
		for i in range(q):
			a = list(map(int, input().split()))
			Query.append(a)
		obj = Solution()
		ans = obj.SolveQueris(str, Query)
		for _ in ans:
		    print(_, end = " ")
		print()
	


# } Driver Code Ends
