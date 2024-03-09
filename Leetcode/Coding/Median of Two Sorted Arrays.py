
class Solution:
    ''' 
        Step1 - Find how many elements to pick from arr1 and from arr2
        Step2 - Check if it forms a valid symmetry, by comparing adjacent elements (l1,l2,r1,r2)
        Step3 - Update the low,high accordingly. Depending on how many elements to pick from arr1
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if n < m: #The array nums1 should be smaller than nums2. 
            return self.findMedianSortedArrays(nums2,nums1)
        low = 0
        high = m
        while low<=high:
            #Mid1 tells how many elements to take from arr1
            #Mid2 tells how manyy elements to take from arr2
            mid1 = (low+high)//2
            mid2 = ((m+n)//2) - mid1

            
            l1 = l2 = -(1<<31)
            r1 = r2 = (1<<31)
            if mid1 < m : r1 = nums1[mid1]
            if mid2 < n: r2 = nums2[mid2]
            if mid1-1 >= 0 and mid1-1 < m: l1 = nums1[mid1-1]
            if mid2-1 >=0 and mid2-1 < n :l2 = nums2[mid2-1]

            #Check if valid symmetry
            if l1 <= r2 and l2 <= r1:
                if (m+n)%2 == 0:
                    return (max(l1,l2) + min(r1,r2))/2
                else:
                    return max(max(l1,l2),min(r1,r2))

            if l1 > r2:
                high = mid1-1
            else:
                low = mid1+1

        return 0.0
        
