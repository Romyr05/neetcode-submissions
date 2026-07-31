class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_letters = {}
        t_letters = {}


        for char in s:
            s_letters[char] = s_letters.get(char,0) + 1

        for char in t:
            t_letters[char] = t_letters.get(char,0) + 1

        return t_letters == s_letters