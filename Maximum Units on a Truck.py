class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        for f,s in boxTypes:
            if truckSize > f:
                truckSize -= f
                ans += f * s
            else:
                ans += truckSize * s
                return ans
        return ans
        
