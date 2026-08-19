class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for i,n in enumerate(nums):
            complement = target - n
            if complement in Map:
                return [Map[complement], i]
            Map[n] = i