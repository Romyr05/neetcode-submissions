class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {"(":")", "{":"}", "[":"]"}

        for i in range(len(s)):
            if s[i] in pairs.values():
                if not stack or pairs[stack[-1]] != s[i]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])


        return not stack 
        
        
