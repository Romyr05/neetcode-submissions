class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for numbers in range(len(nums)):
            pointer_i = numbers
            for number in range(pointer_i + 1, len(nums)):
                pointer_j = number

                if nums[pointer_i] + nums[pointer_j] == target and pointer_i != pointer_j:
                    return [pointer_i, pointer_j]