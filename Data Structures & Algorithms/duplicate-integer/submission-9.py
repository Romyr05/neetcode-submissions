class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # For this we will use the set to remove all the duplicates 
        cleaned_nums = set(nums)

        num_length = len(nums)
        cleaned_nums_length = len(cleaned_nums)
    
        return not(num_length == cleaned_nums_length)