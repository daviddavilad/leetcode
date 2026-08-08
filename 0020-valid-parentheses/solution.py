class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char not in pairs:
                # opening bracket
                stack.append(char)

            else:
                # closing bracket

                if len(stack) == 0:
                    return False

                if stack[-1] != pairs[char]:
                    return False
                
                stack.pop()

        return len(stack) == 0
