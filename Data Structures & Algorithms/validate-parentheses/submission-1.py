class Solution:
    def isValid(self, s: str) -> bool:
        hash_table = {
            ")": "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for i in range(len(s)):
            if s[i] in hash_table:
                if not stack or stack[-1] != hash_table[s[i]]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])


        return not stack 
