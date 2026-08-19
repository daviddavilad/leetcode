class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            current = numbers[l] + numbers[r]
            if current == target:
                return [l + 1, r + 1]
            elif current > target:
                r -= 1
                continue
            else:
                l += 1
        
        return 0 # If the solution can't be found