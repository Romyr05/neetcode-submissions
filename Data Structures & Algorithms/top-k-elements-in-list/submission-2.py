
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_frequent = Counter(nums).most_common(k)

        keys = [key for key, freq in k_frequent]

        return keys
            
        

        