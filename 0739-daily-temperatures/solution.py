class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                old_index = stack[-1]
                stack.pop()
                answer[old_index] = i - old_index
            stack.append(i)

        return answer