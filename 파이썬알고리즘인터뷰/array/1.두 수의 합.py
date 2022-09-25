class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 1. bruteforce
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [nums[i], nums[j]]

        # 2. target - num 찾기
        for i in range(len(nums)):
            if target - nums[i] in nums:
                return [i, nums[i+1:].index(target - nums[i]) + (i+1)]

        # 3. dictionary 추가
        nums_dict = dict()
        for idx, n in enumerate(nums):
            if target - n in nums_dict:
                return [idx, nums_dict[target - n]]
            nums_dict[n] = i