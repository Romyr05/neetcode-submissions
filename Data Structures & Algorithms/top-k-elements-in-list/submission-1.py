class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #No using of Counter

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        #print(freq)

        result = []
        for i in range(k):
            best = None
            for j in freq:
                if best is None or freq[j] > freq[best]:
                    best = j

            #print(freq[best])
            result.append(best)
            del freq[best]

            
        #print(result)
        return result
    