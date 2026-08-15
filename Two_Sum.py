class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index,num in enumerate(nums):
            x = target - num
            if x in d:
                return d[x],index
            d[num]=index
        return[]