from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter_nums = []
        result = []

        counter_nums.append(Counter(nums))

        listing = Counter(nums).most_common(k)

        for i in range(len(listing)):
            result.append(listing[i][0])


        return result

        
