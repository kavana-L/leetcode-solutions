class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)


        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

        result = []

        for i in range(k):
            result.append(sorted_items[i][0])

        return result