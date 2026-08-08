class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        sorted_items = sorted(
            count.items(),
            key=lambda item: item[1],
            reverse=True
        )

        result = []
        for i in range(k):
            result.append(sorted_items[i][0])

        return result
