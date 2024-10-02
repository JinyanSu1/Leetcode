# link: https://leetcode.com/problems/summary-ranges/
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        range_list = []
        if len(nums)==0:
            return []
        left = 0
        while left < len(nums):
            cur = nums[left]
            right= left+1
            while right <len(nums) and nums[left]+1 == nums[right]:
                right+=1
                left+=1
            if nums[right-1] == cur:
                range_list.append(str(cur))
            else:
                range_list.append(str(cur)+'->'+str(nums[left]))
            left = right
        return range_list