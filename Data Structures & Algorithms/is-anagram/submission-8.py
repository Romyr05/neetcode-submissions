"""
One faster way: thru dictionary 
    and checking whether or not that same letter in a dictionary based on count

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count_dict = {}

        for char in range(len(s)):

            count_dict[s[char]] = count_dict.get(s[char],0) + 1
            count_dict[t[char]] = count_dict.get(t[char],0) - 1


        return not any(count_dict.values())
