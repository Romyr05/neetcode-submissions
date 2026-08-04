class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## Another solution easier... bruh

        result = {}

        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))
            
            if sorted_word in result:
                result[sorted_word].append(strs[i])
            else:
                result[sorted_word] = [strs[i]]

        return list(result.values())
