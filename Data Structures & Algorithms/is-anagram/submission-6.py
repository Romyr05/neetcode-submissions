class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}

        for char in range(len(s)):
            char_count[s[char]] = char_count.get(s[char],0) + 1
            char_count[t[char]] = char_count.get(t[char],0) - 1

        return not any(char_count.values())