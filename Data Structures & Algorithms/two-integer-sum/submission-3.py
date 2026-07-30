class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for numbers in range(len(nums)):
            for number in range(numbers + 1, len(nums)):
                if nums[numbers] + nums[number] == target and numbers != number:
                    return [numbers, number]