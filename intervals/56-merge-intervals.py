# link: https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []
        i =0
        intervals.sort(key=lambda x:x[0])
        while i < len(intervals):
            inter = intervals[i]
            left = inter[0]
            right = inter[1]
            while i < len(intervals)-1 and intervals[i+1][0] <=right:
                i = i+1
                right = max(intervals[i][1], right)
            merged_intervals.append([left, right])
            i = i+1
        return merged_intervals
