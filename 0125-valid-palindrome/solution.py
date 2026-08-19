class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = s.lower()
        clean = []

        for char in l:
            if char.isalnum():
                clean.append(char)

        clean = "".join(clean)

        for i in range(len(clean) // 2):
            if clean[i] != clean[len(clean) - 1 - i]:
                return False
        return True
