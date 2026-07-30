class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(char for char in s if char.isalnum()).lower()

        i = 0

        while (i < len(string)//2 ):
            start = string[i]
            end = string[-(i + 1)]
            if (start == end):
                i+=1
                continue
            else:
                return False
        return True
