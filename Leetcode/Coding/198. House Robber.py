class Solution:
    # Dp with memoization
    def robRec(self,nums,curr,dp):
        if curr >= len(nums) :
            return 0
        if dp[curr] != -1:
            return dp[curr]
        
        incl = self.robRec(nums,curr+2,dp) + nums[curr]
        excl = self.robRec(nums,curr+1,dp)
        dp[curr] = max(incl,excl)
        return dp[curr]
    #DP tabulation
    def rob(self, nums: List[int]) -> int:

        dp = [-1]*(len(nums)+2)
        curr = len(nums)
        dp[curr] = 0
        dp[curr+1] = 0
        #I am trying to build from bottom up
        #It is possible to do top-down,however since I have taken bottom up recursion, I implemented same for tabulation approach
        for i in range(curr-1,-1,-1):
            incl = dp[i+2]+nums[i]
            excl = dp[i+1]
            dp[i] = max(incl,excl)
        return dp[0]

        
