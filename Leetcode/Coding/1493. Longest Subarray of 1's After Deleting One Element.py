class Solution:
  # Update freq and Zero counter
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        freq = [0]*(n+1)
        
        prefix_sum = 0
        zero_idx = []
        for i in range(n+1):
            if i == n or nums[i] == 0:
                freq[i] = prefix_sum
                zero_idx+=[i]

                prefix_sum = 0
            else:
                prefix_sum+=1
        res = 0
        n = len(zero_idx)
        for i in range(n):
            first = freq[zero_idx[i]] 
            if i+1 >= n:
                second = 0
            else:
                second = freq[zero_idx[i+1]]
            ans = first + second             
            if ans > res:
                res = ans
        if res == len(nums):
            res-=1
        return res
