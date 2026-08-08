class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        answer = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix[i] = 1
            else:
                suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            answer[i] = suffix[i] * prefix[i]
        return answer
