from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[L, finalist[str]]:

        word_counter = []
        result = []

        for i in range(len(strs)):
            word_counter.append(Counter(strs[i]))

        for j in range(len(word_counter)):
            found_match = False

            #Checking each if has match, not checking any other if 
            for k in range(len(result)):
                if(word_counter[j] == word_counter[(strs.index(result[k][0]))]):
                    result[k].append(strs[j])
                    found_match = True
                    break


            # New group
            if not found_match:  #False
                result.append([strs[j]])
                


        return result
            